import random as rnd
import time

#Definição da classe Rainha e suas funções
class Rainha:

#Função da posição das rainhas nas linhas e colunas do tabuleiro 
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Posição da rainha x --> Linha ; y-->Coluna
    def __getPosicao__(self):
        return [self.x, self.y]

#Pega a posição na coluna
    def __getY__(self):
        return self.y

#Define a posição em y
    def __setY__(self, y):
        self.y = y
    

#Classe do Algoritmo Hill Climbing
class Hill:

#Chamar a função self no init 
    def __init__(self):
        pass

#Avaliação se é o estado objetivo
    def avaliacao(self, lista_rainhas, gabarito):
        pontuacao = 8
        for i in range(8):
            if lista_rainhas[i].__getY__() != gabarito[i]:
                pontuacao -= 1
        return pontuacao

#Mudar os valores das posições das rainhas 
    def mutacao(self, lista_rainhas):
        posicao1 = rnd.randint(0,7)
        posicao2 = rnd.randint(0,7)
        while posicao2 == posicao1:
            posicao2 = rnd.randint(0, 7)
        aux = lista_rainhas[posicao1].__getY__()
        lista_rainhas[posicao1].__setY__(lista_rainhas[posicao2].__getY__())
        lista_rainhas[posicao2].__setY__(aux)
        return lista_rainhas

#Definir a Heurística do algoritmo
def heuristica(linhas):
    #É verificado a posição de cada Rainha, e então varremos cada diagonal
    #em busca de quantos ataques essa rainha faz, e no final teremos o total de quantos ataques occorem no estado
    x = 0
    y = 0
    xx = 0
    yy = 0
    ataques = 0 
    teste = []
    for i in range(8):
      x = i
      y = linhas[i]
      xx = x
      yy = y
      while(True):
        xx += 1
        yy -= 1
        if(xx > 7 or yy < 0):
          break
        if (yy == linhas[xx]):
         teste.append([y, xx,yy])
         ataques += 1     
      xx = x
      yy = y
      while(True):
        xx -= 1
        yy -= 1
        if(xx < 0 or yy < 0):
          break
        if(yy == linhas[xx]):
          teste.append([y, xx,yy])
          ataques += 1
      xx = x
      yy = y
      while(True):
        xx += 1
        yy += 1
        if(xx > 7 or yy > 7):
          break
        if(yy == linhas[xx]):
          teste.append([y, xx,yy])
          ataques += 1
      xx = x
      yy = y
      while(True):
        xx -= 1
        yy += 1
        if(xx < 0 or yy > 0):
          break
        if(yy == linhas[xx]):
          teste.append([y, xx,yy])
          ataques += 1
    return ataques
    teste.append([y, xx,yy])
    ataques += 1
    return ataques

#Função que cria as rainhas em posições aleatórias e as adicionam a uma lista, 
# chamada lista_rainhas
def criaRainha(a,b):
  lista_rainhas = []
  for i in range(8):
    rainha = Rainha(a[i], b[i])
    lista_rainhas.append(rainha)
  return lista_rainhas

#Retorna a lista das posições Y das Rainhas da Lista de Rainhas
def rainhaY(lista_rainhas):
  rainhas = []
  for rainha in lista_rainhas:
    rainhas.append(rainha.__getY__())
  return rainhas

#Função que retorna a solução do problema com auxilio da heurística
def solucao(lista):
  if (heuristica(lista) == 0):
    return True
  else:
    return False

iteracoes = 0
#Criação das Duas listas de posições
a = list(range(0, 8))
b = list(range(0, 8))
print("Colunas")
print(a)
rnd.shuffle(b)
print("Linhas")
print(b)
  

#Criação das listas das rainhas
lista_rainhas = criaRainha(a,b)
rainhas = []
#Exibição do Estado Inicial
print("\nEstado Inicial")
for rainha in lista_rainhas:
    rainhas.append(rainha.__getY__())
print(rainhas)

inicio = time.time()#Variavel pra calcular o tempo de execução do programa
#Aplicação da Classe do Algoritmo
hill = Hill()
pontuacao = heuristica(rainhas)#Aplicação da Heuristica
pontuacao_antiga = pontuacao

#Enquanto não for a solução com Heuristica 0 ele executará a mudança
while pontuacao != 0:
    lista_rainhas = hill.mutacao(lista_rainhas)
    iteracoes += 1 
    rainhas = rainhaY(lista_rainhas)
    pontuacao = heuristica(rainhas)
    while pontuacao_antiga <= pontuacao: #Enquanto o novo estado criado não for melhor que o antigo ele executará a mudança
        lista_rainhas = hill.mutacao(lista_rainhas)
        iteracoes += 1
        pontuacao_antiga = pontuacao
        rainhas = rainhaY(lista_rainhas)
        pontuacao = heuristica(rainhas)

#Variaveis para calcular o tempo
fim = time.time()
tempo = fim-inicio
#Exibição das Informações
print("\nEstado Final")
print(rainhas)
print("Iterações:",iteracoes)
print(f'Tempo:{tempo}')
