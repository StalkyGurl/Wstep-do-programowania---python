from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    haslo = ""
    while len(haslo)<n:
        frag=losuj_fragment()
        if len(haslo) + len(frag) < n-1 or len(haslo) + len(frag) == n:
            haslo = haslo + frag
    return haslo
for i in range(10):
    print("n=8 ", losuj_haslo(8))
for j in range(10):
    print("n=12 ", losuj_haslo(12))
