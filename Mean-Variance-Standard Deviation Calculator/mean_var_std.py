import numpy as np

num = []

def calculadora():
    print("Digite 9 números (um de cada vez). Para sair antes, pressione Enter sem digitar nada.")

    while len(num) < 9:
        entrada = input(f"Digite o {len(num)+1}º número para compor a matriz: ")

        if entrada == "":
            print(f"Entrada invalida... Você digitou apenas {len(num)} números, faltaram {9 - len(num)}.")
            break

        if entrada.isdigit():
            num.append(int(entrada))
        else:
            print("Entrada inválida! Digite apenas números.")

    if len(num) == 9:
        print("Lista completa:", num)

calculadora()

matriz = np.array(num).reshape(3, 3)
print(matriz)
print("mean: ", np.mean(matriz, axis=0) , np.mean(matriz, axis=1) , np.mean(matriz))
print("variance: ", np.var(matriz, axis=0), np.var(matriz, axis=1), np.var(matriz))        
print("standard deviation: ", np.std(matriz, axis=0), np.std(matriz, axis=1), np.std(matriz))        
print("max: ", np.max(matriz, axis=0), np.max(matriz, axis=1), np.max(matriz))        
print("min: ", np.min(matriz, axis=0), np.min(matriz, axis=1), np.min(matriz))        
print("sum: ", np.sum(matriz, axis=0), np.sum(matriz, axis=1), np.sum(matriz))        
