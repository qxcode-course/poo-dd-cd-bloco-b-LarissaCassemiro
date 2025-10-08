class Camisa():
    def __init__(self):
        self.__tamanho = ""

    def set_tamanho(self, tamanho:str)-> bool:
        opcoes = ['PP', 'P', 'M', 'G', 'GG', 'XG']
        if tamanho in opcoes:
            self.__tamanho = tamanho 
            print(f"O tamanho do sua camisa é: {tamanho}")
            return True
        else:
            print("Tamanho inválido! Os tamanhos permitidos são: PP, P, M, G, GG, XG.") 
            return False

def main ():
    camisa = Camisa()
    while True:
        roupa: str = input("Qual o tamanho de roupa você escolhe?").upper()

        if camisa.set_tamanho(roupa) == True:
            break

main()
        