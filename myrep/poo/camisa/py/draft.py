class Camisa:
    def __init__(self, tamanho:str):
        self.__tamanho = ""

    def set_tamanho(self, tamanho:str)-> bool:
        opcoes = ['PP', 'P', 'M', 'G', 'GG', 'XG']
        if tamanho in opcoes:
            self.__tamanho = tamanho 
            print(f"O tamanho do sua camisa é: {tamanho}")
        return False 

def main ():
    camisa = Camisa()
    while True:
        