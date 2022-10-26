from duze_cyfry import daj_cyfre

def duza_liczba(n):
    text = ''
    for i in range(5):
        for cyfra in str(n):
            text = text + daj_cyfre(int(cyfra))[i] + '  '
        print(text)
        text = ''

duza_liczba(1234567890)

