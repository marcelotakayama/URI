a, b = input().split()
a = int(a)
b = int(b)
while a != b:
    if a < b:
        print("Crescente")
    elif a > b:
        print("Decrescente")
    a, b = input().split()
    a = int(a)
    b = int(b)