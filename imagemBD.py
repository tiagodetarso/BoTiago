from PIL import Image

def imagemBD(dados):
    result = 'result'
    with open(result, 'wb') as file_handler:
        file_handler.write(dados)
    imagem = Image.open(result).save(result+'.jpg')