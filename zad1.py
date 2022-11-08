def prime(i):
    prime = True
    if i > 1:
        for x in range(2, i):
            if (i % x) == 0:
                prime = False
                break
    return prime


def lucky(s):
    lucky = False
    for i in range(len(s) - 2):
        if s[i] == '7' and s[i + 1] == '7' and s[i + 2] == '7':
            lucky = True
            break
    return lucky

amount = 0
for m in range(1, 100000):
    n = str(m)
    if prime(m) and lucky(n):
        print (m)
        amount = amount + 1

print("Tych liczb jest",amount)