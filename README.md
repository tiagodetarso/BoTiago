# BoTiago
Bot para Discord feito em Python com a biblioteca discor.py

Envia mensagens em chat do discord, com imagens.

As imagens vêm de um banco de dados, portanto há uma classe BD (banco de dados) para fazer a conexão com o banco.

As imagens vêm do banco de dados em formato binário, portanto há tb uma função para poder mostrá-la no chat do discord, ao invés de somente enviar os dados binários.

Abaixo, colo a mensagem que o bot envia quando algum novo usuário entra no servidor ou quando qualquer usuário, a qualquer tempo, digita ?info; pois ela e bem
explicativa com relação às ações do bot.

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
        
        As "escolhas" das imagens ou respostas a serem mostradas é feita com a função random.choice da biblioteca random do python.
