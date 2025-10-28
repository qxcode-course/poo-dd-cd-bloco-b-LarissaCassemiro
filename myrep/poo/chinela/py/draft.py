class Chinela: 
    def __init__(self):
        self.__tamanho = 0

    def set_tamanho(self,tamanho:int)-> bool:
        if tamanho < 20 or tamanho > 50:
            print ("Este tamanho é inválido, deve está entre 20 e 50")
            return False
        if tamanho % 2 != 0:
            print("Número inválido, deve ser um número par")
            return False
        self.__tamanho = tamanho
        print(f"O tamanho do sua camisa é: {tamanho}")
        return True

    def get_tamanho(self)-> int:
        return self.__tamanho

def main():
    chinela = Chinela()
    while True:
        numero: int = int(input("Digite o tamanho da sua chinela"))

        if chinela.set_tamanho(numero) == True:
            break 
main()
        
