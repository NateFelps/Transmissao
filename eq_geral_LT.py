#Esse programa calcula as tensões e correntes para múltiplos pontos de uma linha de transmissão
#considerando que essa linha está operando a vazio

#A última seção de plot aumenta de forma exagerada o tamanho do gráfico para que 
#a figura possa ser salva em formato vetorial para inserção em relatório impresso

import math as m
import cmath as c
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Entrada de dados do modelo:
f = 60              # hz
r = 0.0852          # ohm/km
g = 0               # ohm^-1
l = 345             # km
L =  0.9187 * 10**-3  # H/km
C =  0.01339 * 10**-6 # F/km
U =  120      # V Fase-neutro

#Pontos da linha (km)
x = [0, 69, 138, 207, 276, 345]

#Cálculo da impedância e admitância da LT em parâmetros distribuídos
z = r + 1j*(2*m.pi*L)
y = g + 1j*(2*m.pi*C)

#Cálculo das impedâncias e potências naturais e características da LT
Z0 = m.sqrt(L/C)
P0 = (U**2)/Z0

ZC = c.sqrt(z/y)
PC = ((U**2)/(abs(ZC)))*m.cos(c.phase(ZC))

#Cálculo da constante de propagação
gamma = c.sqrt(z*y)

#Cálculo das tensões 
Ux = []
Ix = []
for d in x:
    result_tensao = (U/2)*(c.exp(gamma*d)+c.exp(-gamma*d))
    result_corrente = (U/(2*ZC))*(c.exp(gamma*d)-c.exp(-gamma*d))
    Ux.append(abs(result_tensao))
    Ix.append(abs(result_corrente)*1000)

#Exibição dos resultados
print(f"z = {z} ohms")
print(f"y = {y} ohms^-1")
print(f"Zo = {Z0} ohms")
print(f"Po = {P0} watts")
print(f"Zc = {ZC} ohms")
print(f"Pc = {PC} watts")
print(f"gamma = {abs(gamma)} <{m.degrees(c.phase(gamma))} km^-1")

#Tensões e correntes em função de x
print(f"\nx (km)  \t Ux (V) \t I (mA)")
for i in range(len(x)):
    print(f"{x[i]} \t {Ux[i]} \t {Ix[i]} ")

#Plotando os gráficos

#Criando figura e eixo 1
fig, ax1 = plt.subplots()

#Label do eixo x
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)

#Plotando tensão no eixo y da esquerda
ax1.plot(x, Ux, label='Tensão Ux (V)')
ax1.plot(x, Ux, 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)

#Criando eixo 2 como mesmo eixo horizontal x
ax2 = ax1.twinx()

#Plotando corrente no eixo y da direita
ax2.plot(x, Ix, color='red', label='Corrente Ix (mA)')
ax2.plot(x, Ix, 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)

#Colocando legendas e título
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de Tensão e Corrente', fontsize=20)

#Ajustes nos tamanhos dos eixos e nos valores da tensão
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.5f'))

plt.show()
