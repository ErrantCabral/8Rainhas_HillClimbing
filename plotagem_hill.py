import csv
import statistics
import matplotlib.pyplot as plt

#Função de plotagem do Tempo de Execução
def plotTp(y):
    plt.plot(y, marker='.',color = 'Blue')
    plt.title("Gráfico do Tempo de Execução")
    plt.xlabel("Nº de Execuções")
    plt.grid()
    plt.ylabel("Tempo de Execução(Em segundos)")
    plt.ylim(0,0.12)
    plt.show()
#Função de plotagem do número de iterações
def plotIt(y):
    plt.plot(y, marker='.',color = 'Red')
    plt.title("Gráfico das Iterações")
    plt.xlabel("Nº de Execuções")
    plt.grid()
    plt.ylabel("Nº de Iterações")
    plt.ylim(0,1000)
    plt.show()    

#Listas das váriaveis
iteracoes, tempo = [],[]

#Abrindo o arquivo CSV com as informações das 50 Execuções
with open('informações_hill.csv') as stream:
    reader = csv.reader(stream, delimiter=',')
    next(reader)  # Descarta o cabeçalho
    for line in reader: 
        iteracoes.append(int(line[0]))#Adicionando a lista de iterações
        tempo.append(float(line[1]))#Adicionando a lista de tempo

        
#Medias utilizando a biblioteca statistics
mediaIt = statistics.mean(iteracoes)
mediaTp = statistics.mean(tempo)
#Desvios Padrão utilizando a biblioteca statistics
desvioIt = statistics.pstdev(iteracoes)
desvioTp = statistics.pstdev(tempo)
#Exibição das Informações
print(f'Média de Iterações: {mediaIt}\nMédia de Tempo: {mediaTp:.5f}s')
print(f'Desvio Padrão de Iterações: {desvioIt:.2f}\nDesvio Padrão de Tempo de Execução: {desvioTp:.5f}')
#Plotagem dos Gráficos
plotTp(tempo)
plotIt(iteracoes)