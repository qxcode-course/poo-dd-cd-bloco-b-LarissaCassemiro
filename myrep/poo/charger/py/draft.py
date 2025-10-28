class Bateria:
    def __init__(self, carga: int):
        self.__carga = carga 
        self.__capacidade = carga 
        
    
    def descarregar(self, tempo: int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0


    def carregar(self, potencia: int, tempo: int):
        self.__carga += potencia * tempo 
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade


    def get_carga(self):
        return self.__carga
    
    def get_capacidade(self):
        return self.__capacidade
    
    def __str__(self):
        return f"Bateria {self.__carga}/{self.__capacidade}"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def get_potencia(self):
        return self.__potencia

    def __str__(self):
        return f"Carregador {self.__potencia}W"


class Notebook:
    def __init__(self):
        self.__carregador = None
        self.__bateria = None
        self.__ligado = False
        self.__tempo = 0

    def set_charger(self, potencia: int):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return
        self.__carregador = Carregador(potencia)

    def rm_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.__carregador.get_potencia()}W")
        self.__carregador = None
        if self.__bateria is None:
            self.__ligado = False

    def set_battery(self, carga: int):
        self.__bateria = Bateria(carga)

    def rm_battery(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__bateria.get_carga()}/{self.__bateria.get_capacidade()}")
        self.__bateria = None
        if self.__carregador is None:
            self.__ligado = False

    def turn_on(self):
        if self.__ligado:
            return
        if self.__bateria and self.__bateria.get_carga() > 0:
            self.__ligado = True
        elif self.__carregador:
            self.__ligado = True
        else:
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.__ligado = False

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return

        self.__tempo += tempo

        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.get_potencia(), tempo)
            return

        if self.__carregador and not self.__bateria:
            return

        if self.__bateria and not self.__carregador:
            carga_inicial = self.__bateria.get_carga()
            self.__bateria.descarregar(tempo)
            if self.__bateria.get_carga() == 0 and carga_inicial > 0:
                print("fail: descarregou")
                self.__ligado = False

    def __str__(self):
        if not self.__ligado:
            base = "Notebook: desligado"
        else:
            base = f"Notebook: ligado por {self.__tempo} min"

        partes = []
        if self.__carregador:
            partes.append(str(self.__carregador))
        if self.__bateria:
            partes.append(str(self.__bateria))
        if partes:
            base += ", " + ", ".join(partes)
        return base


def main():
    notebook = Notebook()

    while True:
        line = input()
        args = line.split()
        print(f"${line}")

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(notebook)

        elif args[0] == "set_charger":
            potencia = int(args[1])
            notebook.set_charger(potencia)

        elif args[0] == "rm_charger":
            notebook.rm_charger()

        elif args[0] == "set_battery":
            carga = int(args[1])
            notebook.set_battery(carga)

        elif args[0] == "rm_battery":
            notebook.rm_battery()

        elif args[0] == "turn_on":
            notebook.turn_on()

        elif args[0] == "turn_off":
            notebook.turn_off()

        elif args[0] == "use":
            tempo = int(args[1])
            notebook.use(tempo)


main()
