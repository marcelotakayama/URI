n1, n2 = input().split()

n1 = int(n1)
n2 = int(n2)

if n1 == 1:
    res = (4.00*n2)
    print("Total: R$", format (res,".2f"))

elif n1 == 2:
    res = (4.50*n2)
    print("Total: R$", format (res,".2f"))

elif n1 == 3:
    res = (5.00*n2)
    print("Total: R$", format (res,".2f"))

elif n1 == 4:
    res = (2.00*n2)
    print("Total: R$", format (res,".2f"))

elif n1 == 5:
    res = (1.50*n2)
    print("Total: R$", format (res,".2f"))