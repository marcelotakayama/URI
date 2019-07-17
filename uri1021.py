num=  float(input())

if (0<= num <= 1000000.00):

    n1= int (num / 100)
    x = num % 100
    n2 = int (x / 50)
    x2 = x % 50
    n3 = int (x2 / 20)
    x3 = x2 % 20
    n4 = int (x3 / 10)
    x4 = x3 % 10
    n5 = int (x4 / 5)
    x5 = x4 % 5
    n6 = int (x5 / 2)
    x6 = x5 % 2

    n7 = int (x6/1)
    x7 = x6%1
    n8 = int (x7/0.50)
    x8 = x7%0.50
    n9 = int (x8/0.25)
    x9 = x8%0.25
    n10 = int (x9/0.10)
    x10 = x9%0.10
    n11 = int (x10/0.05)
    x11 = x10%0.05
    n12 = round (x11/0.01)
    x12 = (x11%0.01)

    print ("NOTAS:")
    print (n1, "nota(s) de R$ 100.00")
    print (n2, "nota(s) de R$ 50.00")
    print (n3, "nota(s) de R$ 20.00")
    print (n4, "nota(s) de R$ 10.00")
    print (n5, "nota(s) de R$ 5.00")
    print (n6, "nota(s) de R$ 2.00")
    print ("MOEDAS:")
    print(n7, "moeda(s) de R$ 1.00")
    print(n8, "moeda(s) de R$ 0.50")
    print(n9, "moeda(s) de R$ 0.25")
    print(n10, "moeda(s) de R$ 0.10")
    print(n11, "moeda(s) de R$ 0.05")
    print(n12, "moeda(s) de R$ 0.01")