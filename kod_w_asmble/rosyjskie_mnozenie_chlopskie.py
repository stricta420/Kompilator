def mnozenie(a, b):
    wynik = 0
    while a != 0:
        if a % 2 == 1:
            wynik += b
        b += b
        a = a // 2
    return wynik

print(mnozenie(-20, -58))
#print(-1//2)