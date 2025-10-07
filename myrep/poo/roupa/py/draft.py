# - Vamos implementar uma classe que controla os possíveis valores de tamanho para uma roupa.
# - Os tamanhos serão identificados como uma variável tipo texto, e os valores válidos são "PP", "P", "M" e "G", "GG" e "XG".
# - Faça o objeto roupa iniciar o tamanho como uma string vazia, para expressar que nenhum tamanho foi atribuído.
# - Crie o método setTamanho que apenas aceita os valores válidos de tamanho.
# - Caso o valor seja inválido, avise e dê uma mensagem de erro informando quais os valores permitidos.
# - Faça um código de teste iniciando uma roupa com tamanho vazio e pedindo para o usuário informar o tamanho da roupa.
# - Mantenha o usuário preso no loop até que ele insira um valor válido.

class Roupa:
    def __init__(self):
        self.tamanho = ''
        self.tamanhoValidos = ["PP", "P", "M", "G", "GG", "XG"]

    def set_tamanho(self, tamanho: str) -> bool:
        tamanho = tamanho.upper()  # garante letras maiúsculas
        if tamanho != self.tamanhoValidos:
            print(f"Tamanho inválido! Os tamanhos permitidos são: {self.tamanhoValidos}.")
            return False
        self.tamanho = tamanho
        print(f"Tamanho '{self.tamanho}' definido com sucesso!")
        return True

    def get_tamanho(self) -> str:
        return self.tamanho

    def __str__(self) -> str:
        if self.tamanho == '':
            return "Roupa sem tamanho definido."
        return f"Roupa tamanho {self.tamanho}"


def main():
    roupa = Roupa()

    while True:
        tamanho = input("Digite o tamanho da roupa (PP, P, M, G, GG, XG): ").strip()
        if roupa.set_tamanho(tamanho):
            break  

    print(roupa)


main()
