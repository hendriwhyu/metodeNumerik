import math

def FX(x):
    return x + math.exp(x)

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
N = int(input("Masukkan nilai pembagi N: "))

x = [0] * (N+1)
y = [0] * (N+1)

h = (b - a) / N

for i in range(N+1):
    x[i] = a + i * h
    y[i] = FX(x[i])
    print(i, "|", format(x[i], '.5f'), "|", format(y[i], '.5f'))

for j in range(N):
    if y[j] * y[j+1] < 0.0:
        print("Akar terletak antara", x[j], "dan", x[j+1])
        if y[j] < y[j+1]:
            print("Akar lebih dekat ke", x[j])
        else:
            print("Akar lebih dekat ke", x[j+1])
