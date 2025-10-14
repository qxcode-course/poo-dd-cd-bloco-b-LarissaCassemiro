# Seu objetivo é construtir uma Classe Relógio `Watch` que garanta que a hora, minuto e segundo sejam válidos.

# - Construtor
#   - O construtor deve receber 3 parâmetros, hora, minuto e segundo.
#   - Para fazer a inicialização dos 3 parâmetros, utilize os métodos set.
# - Crie os métodos getters e setters para cada atributo.
#   - Os métodos set devem garantir que os valor atribuído sempre seja válido, ou não realize nenhuma mudança.
# - `toString`
#   - Crie um método que imprime a hora no formato HH:MM:SS.
#   - Você precisará pesquisar como formatar números menores que 10 com 2 dígitos (ex: 01, 02, 03).
# - Nos métodos set, realize a validação dos valores.
#   - Hora deve ser entre 0 e 23.
#   - Minuto e segundo devem ser entre 0 e 59.
# - Próximo Segundo `nextSecond`
#   - Crie um método nextSecond que incrementa o segundo em 1.
#   - Se o segundo for 59, ele deve ser zerado e o minuto incrementado.
#   - Se o minuto for 59, ele deve ser zerado e a hora incrementada.
#   - Se a hora for 23, ela deve ser zerada.

class Relogio:
    def __init__(self, hora: int, minuto: int, segundo: int):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0

        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, hora: int):
        if 0 <= hora <= 23:
            self.__hora = hora
        else:
            print("fail: Hora inválida! Deve estar entre 0 e 23")

    def set_minuto(self, minuto: int):
        if 0 <= minuto <= 59:
            self.__minuto = minuto
        else:
            print("fail: Minuto inválido! Deve estar entre 0 e 59")

    def set_segundo(self, segundo: int):
        if 0 <= segundo <= 59:
            self.__segundo = segundo
        else:
            print("fail: Segundo inválido! Deve estar entre 0 e 59")

    def get_hora(self):
        return self.__hora

    def get_minuto(self):
        return self.__minuto

    def get_segundo(self):
        return self.__segundo

    def toString(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

    def __str__(self):
        return self.toString()

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto > 59:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0


def main():
    relogio = Relogio(0, 0, 0)

    while True:
        line = input().strip()
        args = line.split()
        print(f"${line}")

        if args[0] == "end":
            break

        elif args[0] == "init":
            h, m, s = int(args[1]), int(args[2]), int(args[3])
            relogio = Relogio(h, m, s)

        elif args[0] == "show":
            print(relogio)

        elif args[0] == "set":
            h = int(args[1])
            m = int(args[2])
            s = int(args[3])
            relogio.set_hora(h)
            relogio.set_minuto(m)
            relogio.set_segundo(s)


        elif args[0] == "next":
            relogio.nextSecond()


main()


