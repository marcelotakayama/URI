t = int(input())  
case = 1  
for i in range(t):  
    numeros = input().split() 
    numero = numeros[0]  
    tipo = numeros[1] 
    print("Case " + str(case) + ":") 
    if tipo == "dec":  
        print("{:x} hex".format(int(numero))) 
        print("{:b} bin".format(int(numero))) 
        case += 1  
        print()  
    elif tipo == "bin": 
        dec = int(numero, 2) 
        print(dec, "dec")  
        print("{:x} hex".format(dec))
        case += 1  
        print() 
    else: 
        dec = int(numero, 16) 
        print(dec, "dec")  
        print("{:b} bin".format(dec))  
        case += 1  
        print()  

        #Comentário apenas para testar os commit