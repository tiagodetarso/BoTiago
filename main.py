import discord
import random
from classBD import BD
import os
from imagemBD import imagemBD


class MyClient (discord.Client):
    """"""

    # lista de opções para cara ou coroa
    caraCoroa = ['CARA', 'COROA']

    # lista de opções para o jogo de dado
    dado = [1,2,3,4,5,6]

    # lista de números de 1 até 52 (inclusive), na qual cada número representa a opção de uma carta do baralho
    carta = [n for n in range(1,53,1)]

    # lista de respostas do oraculo
    resp_orac = ["SIM", "NÃO", "COM ABSOLUTA CERTEZA", "AS CHANCES SÃO BOAS", 
                "NÃO ME PARECE MUITO PROMISSOR", "NÃO EXISTE QUALQUER CHANCE",
                "VOCÊ ESTÁ LOUCO", "EU TENHO UM BOM PRESSENTIMENTO", "TALVEZ",
                "MELHOR REZAR", "OPA", "YEP", "NÃO TENHO RESPOSTA PRA ESSA"]

    # string das regras do chat, que o bot poderá fornecer aos participantes por um comando
    regras = f""", as regras e princípios deste chat são:
        REGRAS e PRINCÍPIOS:
        1- Esse chat é laico, assim como o Estado, mas você pode ter religião, sem problemas;
        2- Não apoiar a liberação de armas (aquelas de verdade; nos games pode);
        3- Você deve estar ciente da esfericidade do planeta Terra;
        4- Você deve estar em dia com suas vacinas;
        5- Nunca fale do que não sabe. Se não sabe, pergunte humildemente. Se não tem certeza, responda dizendo que não tem certeza;
        6- Nunca chame a dor do(a) coleguinha de 'mimimi'. Respeite, e se puder ajude-o(a);
        7- Se tem algo a dizer a alguém, diga na cara (diretamente). Por favor!;

        Sempre que quiser receber novamente essas regras, digite no chat:
        ?regras
    """

    # String de apresentação do Bot aos usuários. Sempre que um usuário entrar, essa mensagem.
    info = f"""
        Olá, eu sou o BoTiago.

        Eu conheço todas as regras desse chat.
        Para recebê-las, digite:
        ?regras

        Eu ainda tenho as seguintes utilidades:

        1 - Sou oráculo (indico meus sentimentos e previsões para suas perguntas):
            Para requisitar uma previsão, digite no chat:
            ?oraculo (e em seguida coloque sua pergunta)
        2 - Tenho, em meu bolso, uma moeda de R$ 1,00.
            Para tirar CARA OU COROA, digite no chat:
            ?caraoucoroa
        3 - Sempre levo comigo um DADO;
            Para JOGAR DADOS, digite no chat:
            ?joguedados
        4 - Nunca saio de casa sem meu baralho:
            Para tirar uma carta dentre as 52 cartas do baralho, digite no chat:
            ?tireumacarta

        Sempre que quiser receber estas informnações novamente, digite no chat:
        ?info
    """


    async def on_ready(self):
        """Método que imprime no console quando o bot está on-ne"""

        print('Logged on as {0}!'.format(self.user))
    

    async def on_message (self, message):
        """Método que reage às mensagens recebidas dos usuários"""

        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.lower() == '?regras':
            await message.author.send(f"{message.author.name}{self.regras}") 
        
        elif message.content.lower() == '?info':
            await message.author.send(f'{message.author.name}{self.info}')

        elif message.content.lower() == '?caraoucoroa':
            resultado = random.choice(self.caraCoroa)
            await message.channel.send(f'{message.author.name} jogou cara ou coroa e obteve ...')

            if resultado == 'CARA':
                binario = BD.selecionar("SELECT imagem FROM CaraCoroa WHERE nome='Cara'")
                img = binario[0][0]
                imagemBD(img)
                await message.channel.send(file=discord.File('result.jpg'))

            elif resultado == 'COROA':
                binario = BD.selecionar("SELECT imagem FROM CaraCoroa WHERE nome='Coroa'")
                img = binario[0][0]
                imagemBD(img)
                await message.channel.send(file=discord.File('result.jpg'))

            os.remove("result")
            os.remove("result.jpg")

        elif message.content.lower() == '?joguedados':
            resultado = random.choice(self.dado)
            await message.channel.send(f'{message.author.name} jogou os dados e obteve o resultado ...')

            binario = BD.selecionar(f"SELECT imagem FROM dados WHERE id={resultado}")
            img = binario[0][0]
            imagemBD(img)
            await message.channel.send(file=discord.File('result.jpg'))
            
            os.remove("result")
            os.remove("result.jpg")
        
        elif message.content.lower() == '?tireumacarta':
            resultado = random.choice(self.carta)
            await message.channel.send(f'{message.author.name} pediu uma carta e recebeu ...')

            binario = BD.selecionar(f"SELECT imagem FROM cartas WHERE id={resultado}")
            img = binario[0][0]
            imagemBD(img)
            await message.channel.send(file=discord.File('result.jpg'))

            os.remove("result")
            os.remove("result.jpg")

        elif message.content.lower()[0:8] == '?oraculo':
            resultado = random.choice(self.resp_orac)
            await message.channel.send(f'Sua resposta é: {resultado}')

    async def on_member_join(self, member):
        """Método que reage à entrada de um novo membro"""

        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f"{member.name} acabou de entrar no {guild.name}"
            # envia 'mensagem' acima na parte pública do chat
            await guild.system_channel.send(mensagem)
            # envia a string 'info' diretamente ao novo membro
            await member.send (self.info)
    

    async def on_member_remove(self, member):
        """Método que reage à remoção de um usuário"""

        guild = member.Guild
        if guild.system_channel is not None:
            mensagem = f"{member.name} acabou de ser removido de {guild.name}"
            await guild.system_channel.send(mensagem)


#Cria o objeto client
client = MyClient(intents=discord.Intents.all())

#Roda o objeto (bot)
client.run('MTAyNDMxMDEyNzk0NTMyMjU3Nw.Gt_O9R.sR-2UlY7bxR86aTZMZTIZLiOosEbWCukgnq6TY')