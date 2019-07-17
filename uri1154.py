lista = []
while(True):
  x = int(input())
  if(x < 0):
    break
  else:
    lista.append(x)
cal = sum(lista) / len(lista)
print('%.2f' %cal)