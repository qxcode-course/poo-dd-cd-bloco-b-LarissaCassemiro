# - Vamos implementar uma classe que controla os possíveis valores de tamanho para uma roupa.
# - Os tamanhos serão identificados como uma variável tipo texto, e os valores válidos são "PP", "P", "M" e "G", "GG" e "XG".
# - Faça o objeto roupa iniciar o tamanho como uma string vazia, para expressar que nenhum tamanho foi atribuído.
# - Crie o método setTamanho que apenas aceita os valores válidos de tamanho.
# - Caso o valor seja inválido, avise e dê uma mensagem de erro informando quais os valores permitidos.
# - Faça um código de teste iniciando uma roupa com tamanho vazio e pedindo para o usuário informar o tamanho da roupa.
# - Mantenha o usuário preso no loop até que ele insira um valor válido.

class Camisa():
    def __init__(self):
        self.__tamanho = ""

    def set_tamanho(self, tamanho:str)-> bool:
        opcoes = ['PP', 'P', 'M', 'G', 'GG', 'XG']
        if tamanho in opcoes:
            self.__tamanho = tamanho 
            print(f"{self.__tamanho}")
            return True
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG") 
            return False

    def __str__(self):
            return f"size: ({self.__tamanho})"


def main ():
    camisa = Camisa()
    while True:
        line = input()
        args = line.split()
        print(f"${line}")

        if args[0] == "end":
            break 
        elif args[0] == "init":
            camisa = Camisa()
        elif args[0] == "show":
            print(camisa)
        elif args[0] == "size":
            camisa.set_tamanho(args[1])


main()