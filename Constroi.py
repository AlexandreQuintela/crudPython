class Constroi():


    def titulo(titulo):
        print("*" * 80)
        tamanho = int((78 - len(titulo))/2)
        branco = " " * tamanho
        print("*" + branco + titulo + branco + "*")
        print("*" * 80)


    def linhabranca():
        print("*" + " " * 78 + "*")


    def linhaopcoes(texto):
        tamanho = len(texto)
        branco = int((75 - tamanho))
        print("*   " + texto + " " * branco + "*")



    def rodape(info01, info02):
        Constroi.linhabranca()
        print("*" * 80)
        tamanho = int((75 - len(info01) + len(info02)) /2)
        branco = " " * tamanho
        print("* " + info01 + " " * tamanho + "-" + " " * tamanho + info02 + " *")
        print("*" * 80)
