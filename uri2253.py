while True:
    try:
        senha = input()
    except EOFError:
        break
    if len(senha) not in range(6, 33):  
        print("Senha invalida.")
    else:
        maiuscula = 0
        minuscula = 0
        numeral = 0
        for i in senha:  
            if i.isupper(): 
                maiuscula += 1
            elif i.islower(): 
                minuscula += 1
            elif i.isdecimal():  
                numeral += 1
            else:  
                print("Senha invalida.")
                break
        else:  
            if minuscula == 0 or maiuscula == 0 or numeral == 0: 
                print("Senha invalida.")
            else:  
                print("Senha valida.")