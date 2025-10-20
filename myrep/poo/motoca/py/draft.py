# Este é um projeto de modelagem e implementação de uma motoca motorizada em um parque. A ideia é simular o funcionamento dessa motoca através de classes em um programa. Para isso, serão implementadas duas classes principais: `Pessoa` e `Moto`.

# - Descrição
#   - A classe `Moto` representa a motoca em si. Ela possui atributos como potência, tempo e a pessoa que está atualmente utilizando-a.
#   - A motoca inicia com potência 1, sem minutos e sem ninguém.
#   - Apenas uma pessoa pode estar na motoca por vez.
#   - As funcionalidades principais da motoca incluem subir uma pessoa, descer uma pessoa, comprar tempo, dirigir por um tempo determinado e buzinar.
#   - A classe `Pessoa` representa os usuários da motoca. Ela possui os atributos nome e idade.
# - Comandos
#   - Todos os comandos seguem o modelo `$comando arg1 arg2 ...`. Em caso de erro, uma mensagem adequada deve ser impressa.
#   - `$show` - Mostra o estado atual da motoca, incluindo potência, tempo e pessoa atualmente na motoca.
#     - `f"power:{this.power}, time:{this.time}, person:{this.person}"`
#     - power:1, time:0, person:(marcos:4)
#   - `$init` - Reinicia a motoca para o estado inicial, com potência 1, sem minutos e sem ninguém.
#   - `$enter` - Permite uma pessoa subir na motoca. Deve ser seguido pelos argumentos `nome` e `idade` da pessoa.
#   - `$leave` - Faz a pessoa atualmente na motoca descer.
#   - `$buy` - Permite comprar tempo em minutos para utilizar a motoca. O tempo recebido é incrementado ao tempo atual.
#   - `$drive` - Permite dirigir a motoca por um tempo determinado.
#   - `$honk` - Permite buzinar a motoca.

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def __str__(self):
        return f"({self.__nome}:{self.__idade})"

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade


class Moto:
    def __init__(self, potencia: int = 1):
        self.power = potencia
        self.time = 0
        self.person: Pessoa | None = None
    

    def __str__(self):
        return f"power:{self.power}, time:{self.time}, person:{self.person}"

    def inserir(self, pessoa: Pessoa):
        if self.person is not None:
            print("fail: moto ocupada")
            return
        self.person = pessoa

    def remover(self):
        if self.person is None:
            print("fail: moto vazia")
            return
        print(self.person)
        self.person = None

    def comprarTempo(self, value: int):
        self.time += value

    def dirigir(self, tempo: int):
        if self.pessoa == None:
            print("fail: moto vazia")
            return
        if self.tempo == 0:
            print("fail: tempo zerado")
            return
        if tempo > self.tempo:
            print(f"fail: andou {self.tempo} min e acabou o tempo")
            self.tempo = 0
        else:
            self.tempo -= tempo
        
    def buzinar(self):
        print("P" + "e" * self.potencia + "m")


def main():
    moto = Moto()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            moto = Moto(int(args[1]))
        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            moto.inserir(Pessoa(nome, idade))
        elif args[0] == "leave":
            moto.remover()
        elif args[0] == "buy":
            moto.comprarTempo(int(args[1]))
        elif args[0] == "drive":
            moto.dirigir(int(args[1]))
        elif args[0] == "honk":
            moto.buzinar()


main()
