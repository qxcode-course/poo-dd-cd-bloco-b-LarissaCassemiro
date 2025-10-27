# Seu sistema deverá:

# - Classe `Tamagochi`
#   - É responsável por armazenar os dados relativos ao bichinho, controlar os limites permitidos para os atributos e registrar a morte.
#   - Construtor
#     - Recebe energia máxima`energyMax` e limpeza máxima `cleanMax` do pet que representam os valores máximo de energia e limpeza.
#     - Energia `energy` e limpeza `clean` devem ser iniciados no máximo.
#     - Idade `age` inicia em zero e aumenta a cada turno.
#     - Vivo `alive` inicia como `true` porque o bichinho inicia vivo.
#   - Os métodos `set` alteram os valores dentro dos limites de 0 até o máximo permitido e se o valor em algum momento for 0, muda o valor de vivo para false.
# - Classe `Game`
#   - É responsável por armazenar o bichinho.
#   - É onde estão localizadas as lógicas sobre as ações de brincar `play`, dar banho `shower` e dormir `sleep`.
#   - Cada operação causa aumento e reduções nos atributos utilizando-se os métodos `set` e `get` do `Tamagotchi`.
#   - Antes de qualquer ação, é necessário verificar se o bicho está vivo. Pois brincar com bichos mortos não é recomendado.


class Tamagochi:
    def __init__(self, idade: int, energia:int, limpeza: int):
        self.__energiaMaxima = energia
        self.__limpezaMaxima = limpeza
        self.__idade = idade 
        self.__vivo = True 



class Game: 
    def __init__(self):
        pass
