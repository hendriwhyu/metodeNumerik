x = float(input("Mencari Nilai : "))
x1 = float(input("Nilai x(1) : "))
x2 = float(input("Nilai x(2) : "))

y1 = float(input("Nilai y(1) : "))
y2 = float(input("Nilai y(2) : "))


def nilaiY():

    a = (y2 - y1) / (x2 - x1)
    b = (x - x1)
    return y1 + a * b


hasil = str(float(nilaiY()))
print("Hasil nilai Y : " + hasil)
