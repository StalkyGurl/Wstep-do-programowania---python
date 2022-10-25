def szachownica(n,k):
    for o in range(2*n):
        for _ in range(k):
                if o%2==0:
                    print(n*(k*' '+k*'*'))
                else:
                    print(n*(k*'*'+k*' '))

szachownica(4,3)