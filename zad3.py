def krzyzyk(n):
    for x in range(n):
          print (n * ' ' + n * '*')
    for y in range(n):
          print (3 * n * '*')
    for z in range(n):
          print (n * ' ' + n * '*')
    print()
      

a=input("Podaj bok kwadratu: ")
krzyzyk(int(a))