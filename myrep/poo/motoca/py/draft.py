class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_nome(self, value: str):
        self.__nome = value
    def __str__(self):
        return self.__nome
    
    def __str__)(self):
        return f"nome: {self.cliente}"

class Moto:
    def __init__(self): # type union
        self.cliente: Pessoa | None = None

    def inserir(self, cliente: Pessoa) -> bool:
        if self.cliente != None:
            print("moto ocupada")
            return False
        self.cliente = cliente
        return True
    
    def remover(self) -> Pessoa | None:
        if self.cliente == None:
            print("moto vazia")
            return None
        aux: Pessoa = self.cliente
        self.cliente = None
        return aux
        
    def __str__(self):
        return f"moto: {self.cliente}"
    
moto = Moto()
jose = Pessoa("jose") # 500
moto.inserir(jose)
saiu = moto.remover() # 500
print(saiu == jose) # True
def main():
    moto = Moto()
    while True: 
        line = input()
        args = line.split()
        print(f"${line}")

        if args[0] == "end":
            break 

        elif args[0] == "power":

