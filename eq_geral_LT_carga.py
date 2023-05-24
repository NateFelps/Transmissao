#Esse programa calcula as tensões e correntes para múltiplos pontos de uma linha de transmissão
#considerando que essa linha está operando com carga

#A última seção de plot aumenta de forma exagerada o tamanho do gráfico para que 
#a figura possa ser salva em formato vetorial para inserção em relatório impresso

import math as m
import cmath as c
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

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
z = r + 1j*(2*m.pi*60*L)
y = g + 1j*(2*m.pi*60*C)

#Cálculo das impedâncias e potências naturais e características da LT
Z0 = m.sqrt(L/C)
P0 = (U**2)/Z0

ZC = c.sqrt(z/y)
PC = ((U**2)/(abs(ZC)))*m.cos(c.phase(ZC))

#Criando lista para três cenários de potência na carga
P2 = [0.5*P0, P0, 1.5*P0]
fp2 = 1 #Fator de potência unitário

I2 = []
for potencia in P2:
    I2.append(potencia/(U*fp2))

#Cálculo da constante de propagação
gamma = c.sqrt(z*y)

#Cálculo das tensões 
Ux = np.zeros((len(P2),len(x)))
Ix = np.zeros((len(P2),len(x)))
for linha in range(len(P2)):
    for coluna in range(len(x)):
        result_tensao = ((U + I2[linha]*ZC)/2)*(c.exp(gamma*x[coluna])) + ((U - I2[linha]*ZC)/2)*(c.exp(-gamma*x[coluna]))
        result_corrente = ((U + I2[linha]*ZC)/(2*ZC))*(c.exp(gamma*x[coluna])) - ((U - I2[linha]*ZC)/(2*ZC))*(c.exp(-gamma*x[coluna]))
        Ux[linha,coluna] = (abs(result_tensao))
        Ix[linha,coluna] = (abs(result_corrente)*1000)

#Exibição dos resultados
print(f"z = {z} ohms")
print(f"y = {y} ohms^-1")
print(f"Zo = {Z0} ohms")
print(f"Po = {P0} watts")
print(f"Zc = {ZC} ohms")
print(f"Pc = {PC} watts")
print(f"gamma = {abs(gamma)} <{m.degrees(c.phase(gamma))} km^-1")

#Tensões e correntes em função de x para cada carga
for aux in range(len(P2)):
    print(f"-------------------")
    print(f"Tensões e correntes em função de x para P2 = {P2[aux]} W")
    print(f"\nx (km)  \t Ux (V) \t I (mA)")
    for i in range(len(x)):
        print(f"{x[i]} \t {Ux[aux,i]} \t {Ix[aux,i]} ")

#Plotando os gráficos
# X representa os dados colhidos via teórica
# Y representa os dados colhidos via empírica
Uy = [[117.4,121.2,121.6,121.4,121,119.8],[118.2,122.9,126.4,128.9,132.9,137.5],[118.3,124.8,131.4,139.6,147,157.2]]
Iy = [[240,241,245,260,275,300],[580,585,585,580,580,580],[718,710,710,680,660,680]]


# Analítico P2 = 0,5 P0
fig, ax1 = plt.subplots()
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)
ax1.plot(x, Ux[0], label='Tensão Ux (V)')
ax1.plot(x, Ux[0], 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(x, Ix[0], color='red', label='Corrente Ix (mA)')
ax2.plot(x, Ix[0], 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de tensão e corrente analíticas para P2 = 0,5.P0', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)

# Analítico P2 = P0
fig, ax1 = plt.subplots()
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)
ax1.plot(x, Ux[1], label='Tensão Ux (V)')
ax1.plot(x, Ux[1], 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(x, Ix[1], color='red', label='Corrente Ix (mA)')
ax2.plot(x, Ix[1], 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de tensão e corrente analíticas para P2 = P0', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)

# Analítico P2 = 1,5 P0
fig, ax1 = plt.subplots()
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)
ax1.plot(x, Ux[2], label='Tensão Ux (V)')
ax1.plot(x, Ux[2], 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(x, Ix[2], color='red', label='Corrente Ix (mA)')
ax2.plot(x, Ix[2], 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de tensão e corrente analíticas para P2 = 1,5.P0', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)

# Empírico P2 = 0,5 P0
fig, ax1 = plt.subplots()
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)
ax1.plot(x, Uy[0], label='Tensão Ux (V)')
ax1.plot(x, Uy[0], 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(x, Iy[0], color='red', label='Corrente Ix (mA)')
ax2.plot(x, Iy[0], 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de tensão e corrente empíricas para P2 = 0,5.P0', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)

# Empírico P2 = P0
fig, ax1 = plt.subplots()
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)
ax1.plot(x, Uy[1], label='Tensão Ux (V)')
ax1.plot(x, Uy[1], 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(x, Iy[1], color='red', label='Corrente Ix (mA)')
ax2.plot(x, Iy[1], 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de tensão e corrente empíricas para P2 = P0', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)

# Empírico P2 = 1,5 P0
fig, ax1 = plt.subplots()
ax1.set_xlabel('Distância do receptor (km)', fontsize=20)
ax1.plot(x, Uy[2], label='Tensão Ux (V)')
ax1.plot(x, Uy[2], 'o',color= "C0")
ax1.set_ylabel('Tensão Ux (V)', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(x, Iy[2], color='red', label='Corrente Ix (mA)')
ax2.plot(x, Iy[2], 'o',color='red')
ax2.set_ylabel('Corrente Ix (mA)', fontsize=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico de tensão e corrente empíricas para P2 = 1,5.P0', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)

plt.show()