
liczba = int(input('Podaj liczbe: '))

def check_pierwsza(liczba):
    if liczba > 1:

        for i in range(2, liczba):
            if liczba % i == 0:
                print('nie jest')
                break
            elif i == liczba -1:
                print ('jest zajebiscie')
                break



    else:
        return False

print(check_pierwsza(liczba))
