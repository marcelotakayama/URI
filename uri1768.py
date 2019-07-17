while True:
    try:
        base_arvore = int(input())
        espacamento = base_arvore // 2
        original_espacamento = espacamento
        for i in range(0, base_arvore, 2):
            print(espacamento * " " + "*" * (i+1))
            espacamento -= 1
        print(original_espacamento * " " + "*\n" + (original_espacamento-1) * " " + "***\n")
    except EOFError:
        break