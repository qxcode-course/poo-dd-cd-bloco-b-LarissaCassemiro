#  Descrição
#   - A lapiseira é capaz de iniciar, inserir e remover grafite, além de escrever em uma folha.
#   - Para inserir um grafite, é necessário especificar o calibre (float), a dureza (string) e o tamanho em mm (int).
#   - A remoção do grafite só é possível se houver algum na lapiseira.
#   - A escrita na folha só é possível se houver grafite suficiente e se o tamanho do grafite for superior a 10mm.
#   - A quantidade de grafite gasto varia de acordo com a dureza do grafite. Quanto mais macio, mais ele se desgasta.
#   - Quando o tamanho do grafite atinge 10mm, não é mais possível escrever.
#   - Se não houver grafite suficiente para terminar a escrita na folha, é emitido um aviso de texto incompleto.

# - Responsabilidades
#   - A classe Grafite `Lead` é responsável por armazenar as informações do grafite.
#     - `thickness` é a espessura e terá valores como 0.3, 0.5, 0.7.
#     - `hardness` é a dureza e poderá ter os seguintes valores: `HB, 2B, 4B, 6B`.
#     - O método `usagePerSheet` retorna a quantidade de grafite gasto por folha.
#       - Um grafite `HB` gasta `1mm` por folha.
#       - Um grafite `2B` gasta `2mm` por folha.
#       - Um grafite `4B` gasta `4mm` por folha.
#       - Um grafite `6B` gasta `6mm` por folha.
#     - `size` representa o tamanho do grafite em `milímetros`.
#   - A classe `Pencil` é responsável por gerenciar as operações de inserção, remoção de grafite e escrita na folha.
#     - Ela referencia um único objeto lapiseira como atributo.
#     - E também possui um indicador de espessura `thickness`.
# - Comandos
#   - Todos os comandos seguem o modelo `$comando arg1 arg2 ...`.
#   - `$iniciar calibre` - Inicializa a lapiseira com um determinado calibre.
#   - `$inserir calibre dureza tamanho` - Insere um grafite com o calibre, dureza e tamanho especificados.
#     - erros:
#       - `fail: calibre incompativel` - Se o calibre do grafite for diferente do calibre da lapiseira.
#       - `fail: ja existe grafite` - Se já houver um grafite na lapiseira.
#   - `$remover` - Remove o grafite da lapiseira, se houver.
#     - erros:
#       - `fail: nao existe grafite` - Se não houver grafite na lapiseira.
#   - `$escrever` - Escreve na folha, considerando o grafite presente na lapiseira.
#     - O grafite é gasto de acordo com a dureza.
#     - erros:
#       - `fail: nao existe grafite` - Se não houver grafite na lapiseira.
#       - `fail: tamanho insuficiente` - Se o tamanho do grafite for insuficiente para começar a escrita.
#       - `fail: folha incompleta` - Se o grafite não for suficiente para terminar a escrita.

# - Parte 1: Inserir
#   - Crie a classe Grafite `Lead` com o atributo tamanho `size`.
#   - Crie a classe Lapiseira `Pencil` com o atributo ponta `tip` inicializado como `null`.
#   - Implemente o método tem grafite `hasGrafite` que retorna `true` se houver grafite na lapiseira.
#   - Implemente o método inserir `insert` que insere um grafite na lapiseira, se não houver grafite.
#   - Implemente o método `toString` que mostra a lapiseira e o grafite presente.

# - Parte 2: Remover Grafite
#   - Implemente o método `remove` que retira o grafite da lapiseira, se houver.
#   - Verifique se o método `remove` retorna o grafite removido ou `null` se não havia grafite.

# - Parte 3: Escrever na Folha
#   - Implemente o método `writePage` que escreve na folha.
#   - Implemente o método `usagePerSheet` que retorna a quantidade de grafite gasto por folha.
#   - Verifique se a lapiseira consegue escrever na folha.
#   - Faça as verificações antes de escrever na folha.
#   - Para ver se o grafite será suficiente para escrever na folha, verifique qual o tamanho final que ele teria se fizesse a folha completa.
#     - Se esse tamanho for menor que 10mm, ele deve gastar o que for possível e parar a folha pela metade.


class Lapiseira: 
    def __init__(self, calibre:int, dureza:int, tamanho:int):

    def inserir(self,)


    