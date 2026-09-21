from PIL import Image

LARGURA_NOVA = 100
ASCII_CHARS = ["@", "#", "$", "%", "*", "+", "=", "-", ":", ".", " "]

def redimensionar_imagem(imagem, nova_largura=LARGURA_NOVA):
    largura_original, altura_original = imagem.size
    proporcao = altura_original / largura_original
    nova_altura = int(nova_largura * proporcao * 0.55)
    return imagem.resize((nova_largura, nova_altura))

def converter_para_ascii(caminho_imagem):
    try:
        imagem = Image.open(caminho_imagem)
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return

    imagem_redimensionada = redimensionar_imagem(imagem)
    imagem_cinzenta = imagem_redimensionada.convert("L")
    
    pixels = imagem_cinzenta.getdata()
    carateres = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    
    largura_pixel = imagem_redimensionada.width
    linhas_ascii = [carateres[i:i + largura_pixel] for i in range(0, len(carateres), largura_pixel)]
    arte_ascii = "\n".join(linhas_ascii)

    with open("ascii-art.txt", "w", encoding="utf-8") as f:
        f.write(arte_ascii)
        
    print("Arte ASCII gerada com sucesso em 'ascii-art.txt'!")

if __name__ == "__main__":
    converter_para_ascii("foto.jpg")