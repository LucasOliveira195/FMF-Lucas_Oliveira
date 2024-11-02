#autor: Pedro Lucas Oliveira dos Santos
#Data: 01/11/2024
#Código: Baskara a, b, c

import math
#Importando biblioteca matemática.


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
#a, b e c são varáveis dinâmicas, significa que o usuário vai determinar o valor delas.
#o "input" é usado pra capturar os valores digtados pelo teclado.

delta = b**2 - 4*a*c
#É o cálculo do delta, delta é uma  variável  que vai receber o valor da operação que vem depois do sinal de "="

if delta == 0:
#Aqui ele vai verificar se o valor de delta é 0.
    raiz1 = (-b+math.sqrt(delta))/(2*a)
#"Math.sqrt" tira a raiz quadrada de um número, nesse caso, o delta.
    print(" Essa equação tem a as mesmas raízes: ", raiz1)
#Se for 0, calcula a primeira raiz e usa "print" pra mostrar que as duas raízes são iguais.
#Se não, o programa continua.

else:
    if delta < 0:
#Aqui ele verifica se o delta é menor que 0.
        print("A equação não tem raízes reais")
#Se o delta for inferior a 0, será imprimido que a equação nõ tem raízes reais.
    else:
#se não, o programa continua.

        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b-math.sqrt(delta))/(2*a)
#Aqui ele calcula as duas raízes.
        print("A primeira raiz da equação é: ", raiz1)
        print("A segunda raiz da equação é: ", raiz2)
#Aqui elas são impressas.
