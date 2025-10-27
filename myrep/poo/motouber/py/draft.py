class Pessoa: 
    def __init__(self, nome: str, dinheiro: float):
        self.__nome = nome 
        self.__dinheiro = dinheiro 
    
    def get_nome(self):
        return self.__nome
    
    def get_dinheiro(self):
        return self.__dinheiro
    
    def adicionar_Saldo(self, valor: float):
        self.__dinheiro += valor 

    def remover_Saldo(self, valor: float):
        if valor > self.__dinheiro:
            pago = self.__dinheiro
            self.__dinheiro = 0
            return pago
        else:
            self.__dinheiro -= valor
            return valor
        
    def __str__(self):
        return f"{self.__nome}:{int(self.__dinheiro)}"
    

class Moto:
    def __init__(self, custo = 0, motorista = None, passageiro = None):
        self.__custo = custo
        self.__motorista = motorista
        self.__passageiro = passageiro

    def embarcar_Motorista(self, motorista: Pessoa):
        self.__motorista = motorista

    def embarcar_Passageiro(self, passageiro: Pessoa):
        if self.__motorista is None:
            print("fail: no driver")
            return 
        self.__passageiro = passageiro
    
    def dirigir(self, km: float):
        if self.__motorista is None:
            print("fail: no driver")
            return
        if self.__passageiro is None:
            print("fail: no passenger")
            return
        self.__custo += km

    def desembarcar_Passageiro(self):
        if self.__passageiro is None:
            print("fail: no passenger")
            return 
        
        pago = self.__passageiro.remover_Saldo(self.__custo)
        if pago < self.__custo:
            print("fail: Passenger does not have enough money")
        self.__motorista.adicionar_Saldo(self.__custo)
        print(f"{self.__passageiro.get_nome()}:{int(self.__passageiro.get_dinheiro())} left")
        
        self.__passageiro = None
        self.__custo = 0

    def __str__(self):
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"


def main():
    moto = Moto()
    while True:
        line = input()
        args = line.split()
        print(f"${line}")

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(moto)

        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = float(args[2])
            moto.embarcar_Motorista(Pessoa(nome, dinheiro))

        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = float(args[2])
            moto.embarcar_Passageiro(Pessoa(nome, dinheiro))

        elif args[0] == "drive":
            km = int(args[1])
            moto.dirigir(km)

        elif args[0] == "leavePass":
            moto.desembarcar_Passageiro()


main()












    






        