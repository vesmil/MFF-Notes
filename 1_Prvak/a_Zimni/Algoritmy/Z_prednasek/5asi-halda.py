def Zkontroluj(otec, posledni):
    global a

    while 2*otec+1 <= posledni:
        syn = 2 * otec+1
        if syn+1 <= posledni and a[syn+1]<a[syn]:
            syn+=1

        if a[syn] < a[otec]:
            a[otec], a[syn] = a[syn], a[otec]
            a = []

        otec = syn

a = [22, 1, 67, 3, 5, 19, 4, 7, 6, 11]
n = len(a)

print(a)

k = n//2 + 1
while k>=0:
    Zkontroluj(k, n-1)
    k -= 1

while n > 0:
    print(a[0])
    a[0] = a[n-1]
    n -= 1
    Zkontroluj(0, n-1)