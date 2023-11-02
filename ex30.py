import random

n = []
p = 0
inp = 0

for i in range(1, 20):
    valor = random.randint(0, 100) 
    n.append(valor)
    print(valor)

    if valor % 2 == 0:
        p = p + valor
    else:
        inp = inp + valor

print("A soma dos pares é", p)
print("A soma dos ímpares é", inp)
