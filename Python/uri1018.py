num= int (input ())
n1= num // 100
x= num % 100
n2= x // 50
x2= x % 50
n3= x2 // 20
x3= x2 % 20
n4= x3 // 10
x4= x3 % 10
n5= x4 // 5
x5= x4 % 5
n6= x5 // 2
x6= x5 % 2
n7= x6 // 1
x7= x6 % 1
print(num)
print (n1, "nota(s) de R$ 100,00")
print (n2, "nota(s) de R$ 50,00")
print (n3, "nota(s) de R$ 20,00")
print (n4, "nota(s) de R$ 10,00")
print (n5, "nota(s) de R$ 5,00")
print (n6, "nota(s) de R$ 2,00")
print (n7, "nota(s) de R$ 1,00")