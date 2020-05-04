
liczba = int(input('Podaj liczbe: '))

def check_pierwsza(liczba):
    if liczba > 1:

        for i in range(2, liczba):
            if liczba % i == 0:
                return False
            else:
                return True

    else:
        return False

print(check_pierwsza(liczba))
