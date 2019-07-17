num = int(input())

x1 = num//3600
x2 = num % 3600 // 60
x3 = num % 3600 % 60 

print("%i:%i:%i" %(x1,x2,x3))