def pertence(lista, item1, item2):
  hasItem1 = False
  hasItem2 = False

  for i in lista:
    if item1 == i:
      hasItem1 = True

    if item2 == i:
      hasItem2 = True

  if hasItem1 and hasItem2:
    return True

  return False

# Debug Function (Delete to send)
lista = [2, 3, 4, 8, 7]
retorno = pertence(lista, 4, 3)
print(retorno)