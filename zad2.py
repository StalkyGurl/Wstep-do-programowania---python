def koperta(n):
    wielkosc = 2*n+1
    for y in range(1, wielkosc + 1):
        for x in range(1, wielkosc + 1):
            if (y == 1 or y == wielkosc or x == 1 or x == wielkosc or x == y or x == (wielkosc - y + 1)):
                print ('*', end='')
            else:
                print (' ', end='')
        print()

koperta(10)