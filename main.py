def lab2_a(names):
    for i in names:
       print(i)

przykladowe_imiona = ['Mateusz', 'Marcin', 'Fryderyk', 'Krzysztof', 'Piotr']
lab2_a(przykladowe_imiona)

def lab2_b(numbers):
    lista_liczb = []
    for i in numbers:
        lista_liczb.append(2 * i)
    return lista_liczb

przykladowe_liczby = [2, 16, 21, 23, 31]
print(lab2_b(przykladowe_liczby))

def lab2_b2(numbers):
    lista_liczb = [2 * i for i in numbers]
    return lista_liczb

print(lab2_b2(przykladowe_liczby))

def lab2_c(list):
    for i in range(10):
        if list[i] % 2 == 0:
            print(list[i])

liczby10 = [2, 16, 21, 23, 31, 33, 53, 55, 15, 18]
lab2_c(liczby10)


def lab2_d(list):
    for i in range(10):
        if i % 2 == 0:
            print(list[i])

lab2_d(liczby10)