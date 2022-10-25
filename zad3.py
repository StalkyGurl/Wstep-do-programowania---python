def kolko1(n):
    r = (n / 2)-0.5
    for i in range(n):
        for j in range(n):
            x = i - r
            y = j - r
            if (x ** 2 + y ** 2 <= r ** 2 + 1):
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()

def kolko2(n, max_n):
    r = (n / 2) - 0.5
    for i in range(n):
        for j in range(max_n):
            x = i - r
            y = j - (max_n + 1)/ 2 + 1
            if (x ** 2 + y ** 2 <= r ** 2 + 1):
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()

kolko2(7,15)
kolko2(9,15)
kolko2(15,15)