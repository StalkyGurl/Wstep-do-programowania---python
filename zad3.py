def delete_text_in_brackets(s):
    text = ''
    beggining=False
    ignore=False
    for a in s:
        if a == '(' and not beggining:
            ignore = True
            beggining = True
        if a == ')' and beggining:
            beggining = False
            ignore = False
        if not ignore and not beggining and a != ')':
            text = text + a

    print(text)

text1 = 'Ala ma kota (perskiego)!'
text2 = 'Dzisiaj jest slonecznie (a jest listopad!) i wyjatkowo nie pada (a mialo padac)'
text3 = '(Maj 2022) Drogi pamietniku...'
text4 = 'Zeszyt (rozowy(taki z kwiatkami)) lezal na stole (ale juz go nie ma) i ona (moja mama) go szuka'
text5 = '(Nie lubie poniedzialkow...)'

delete_text_in_brackets(text1)
delete_text_in_brackets(text2)
delete_text_in_brackets(text3)
delete_text_in_brackets(text4)
delete_text_in_brackets(text5)

