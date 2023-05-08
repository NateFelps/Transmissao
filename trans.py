import numpy as np

# Entrada dos valores do exercício

U = 800.0
z0 = 400.0
i0 = U/z0
z1 = 0.0
z2 = 1600.0 # 100 400 1600

kru2 = (z2-z0)/(z2+z0)
kru1 = (z1-z0)/(z1+z0)

kri1 = - kru1
kri2 = - kru2

U_transmitido = U
U1_antigo = U
U2_antigo = 0
U1_atual = U
U2_atual = 0

print(f"Ponto 0: ")
print(f"U1 = {U1_atual} .... U2 = {U2_atual}")
print(f"Transmitido para ponto {1}: {U_transmitido}")

for i in range(1,4):
    if i%2 == 0:
        U1_atual = U1_antigo + U_transmitido + kru1*U_transmitido
        U_transmitido = kru1*U_transmitido
        U1_antigo = U1_atual
        U2_atual = U2_antigo
    else: 
        U2_atual = U2_antigo + U_transmitido + (kru2*U_transmitido)
        U_transmitido = kru2*U_transmitido
        U2_antigo = U2_atual
        U1_atual = U1_antigo
    print(f"Ponto {i}l/v: ")
    print(f"U1 = {U1_atual} .... U2 = {U2_atual}")
    print(f"Transmitido para ponto {i+1}: {U_transmitido}")

   
        





