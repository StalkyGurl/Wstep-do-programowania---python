def usun_w_nawiasach(s):
    napis = ''
    poczatek=False
    ignoruj=False
    for a in s:
        if a == '(' and not poczatek:
            ignoruj = True
            poczatek = True
        if a == ')' and poczatek:
            poczatek = False
            ignoruj = False
        if not ignoruj and not poczatek and a != ')':
            napis = napis + a

    print(napis)

text1 = 'Ala ma kota (perskiego)!'
text2 = 'Dzisiaj jest slonecznie (a jest listopad!) i wyjatkowo nie pada (a mialo padac)'
text3 = '(Maj 2022) Drogi pamietniku...'
text4 = 'Zeszyt (rozowy(taki z kwiatkami)) lezal na stole (ale juz go nie ma) i ona (moja mama) go szuka'
text5 = '(Nie lubie poniedzialkow...)'

usun_w_nawiasach(text1)
usun_w_nawiasach(text2)
usun_w_nawiasach(text3)
usun_w_nawiasach(text4)
usun_w_nawiasach(text5)

