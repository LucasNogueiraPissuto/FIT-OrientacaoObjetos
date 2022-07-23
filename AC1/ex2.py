def substituir(lista, old, new):
  newList = lista

  for index, item in enumerate(newList):
    if item == old:
      newList[index] = new

  return newList

# Debug Function (Delete to send)
lista = [4, 3, 4, 8, 7]
retorno = substituir(lista, 4, 6)
print(retorno)