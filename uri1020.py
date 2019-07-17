num = int(input())

x1 = num // 365
x2 = num % 365 // 30
x3 = (num % 365) % 30

print(x1, "ano(s)")
print(x2, "mes(es)")
print(x3, "dia(s)")