def pierwsza(i):
    pierwsza = True
    if i > 1:
        for x in range(2, i):
            if (i % x) == 0:
                pierwsza = False
                break
    return pierwsza


def szczesliwa(s):
    szczesliwa = False
    for i in range(len(s) - 2):
        if s[i] == '7' and s[i + 1] == '7' and s[i + 2] == '7':
            szczesliwa = True
            break
    return szczesliwa

ilosc = 0
for m in range(1, 100000):
    n = str(m)
    if pierwsza(m) and szczesliwa(n):
        print (m)
        ilosc = ilosc + 1

print("Tych liczb jest",ilosc)