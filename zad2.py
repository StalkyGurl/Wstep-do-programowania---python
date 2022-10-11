from math import log

def silnia(n):
    wynik=1
    for i in range(2,n+1):
        wynik=wynik*i
    return wynik

def dlugosc(m):
    return(len(str(m)))

for j in range(4,101):
    if dlugosc(silnia(j)) == 1:
        print(j,"! ma ",dlugosc(silnia(j)),"cyfrę")
    elif dlugosc(silnia(j)) >= 2 and dlugosc(silnia(j)) <= 4:
        print(j,"! ma ",dlugosc(silnia(j)),"cyfry")
    else:
        print(j,"! ma ",dlugosc(silnia(j)),"cyfr")
    
