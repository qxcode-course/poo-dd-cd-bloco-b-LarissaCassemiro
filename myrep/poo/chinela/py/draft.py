#- Vamos implementar uma classe que controla os possíveis valores de calçados para uma chinela.
#- As regras de validação de valores são as seguintes.
#- Uma chinela tem um valor tamanho que é um número par entre 20 e 50, incluindo 20 e 50.
#- Faça o objeto chinela iniciar com tamanho 0 e controle através do método setTamanho que apenas valores válidos de tamanho sejam atribuídos.
#- Por fim, crie um loop no qual um objeto chinela é criado e é perguntado ao usuário qual seu tamanho de chinela.
#- Mantenha o usuário preso no loop até que ele insira um valor válido.
#- Caso ele digite um valor inválido, avise e dê uma mensagem de erro adequada.

# código do Tempo
# usar o __ no começo pra definir private
# criar um get_algo para leitura e retornar o valor
# criar um set_algo que recebe um valor
# parametros default utilizados quando o valor não vem
# parametros nomeados quando quero um valor especifico
# class Tempo:
#     def init(self, hora: int = 0, min: int = 0):
#         self.h = 0
#         self.set_hora(hora)
#         self.m = min
#         self.s = 0

#     def set_hora(self, valor: int) -> None: # escrita
#         if valor > 11 or valor < 0:
#             print("hora errada")
#             return
#         self.h = valor

#     def get_hora(self) -> int: # leitura
#         return self.h

#     def str(self):
#         return f"{self.h}:{self.m}:{self.s}"

# agora = Tempo(min=55, hora=9)
# print(agora)


class Chinela: 
    def __init__(self, tamanho: int):
        self.set_tamanho(tamanho)

    def set_tamanho(self, tamanho: int) -> None:
        if tamanho < 20 or tamanho > 50:
            print("Este tamanho é inválido, deve estar entre 20 e 50")
            return
        self.tamanho = tamanho
        if tamanho % 2 != 0:
            print("número inválido, deve ser par")
            return
        self.tamanho = tamanho 

    def get_tamanho(self) -> int:
        return self.tamanho
    
    def __str__(self)->str:
        return f"Chinela tamanho {self.tamanho}"
    

def main():
    chinela = Chinela
    while True:
        line = input()
        args = line.split()
        print("$" + line)

        if args [0] == "oi":
            print(line)
main()