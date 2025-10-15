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
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, h): print("fail: hora invalida") if not 0 <= h <= 23 else setattr(self, "_Relogio__hora", h)
    def set_minuto(self, m): print("fail: minuto invalido") if not 0 <= m <= 59 else setattr(self, "_Relogio__minuto", m)
    def set_segundo(self, s): print("fail: segundo invalido") if not 0 <= s <= 59 else setattr(self, "_Relogio__segundo", s)

    def __str__(self): return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo, self.__minuto = 0, self.__minuto + 1
            if self.__minuto == 60:
                self.__minuto, self.__hora = 0, (self.__hora + 1) % 24


def main():
    relogio = Relogio(0, 0, 0)
    while True:
        args = input().split()
        print(f"${' '.join(args)}")
        if args[0] == "end": break
        if args[0] == "init": relogio = Relogio(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "show": print(relogio)
        elif args[0] == "set": relogio.set_hora(int(args[1])); relogio.set_minuto(int(args[2])); relogio.set_segundo(int(args[3]))
        elif args[0] == "next": relogio.nextSecond()

main()
