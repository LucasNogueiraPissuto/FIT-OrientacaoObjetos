def posicoes(tupla, item):
  indexes = []

  for index, itemSingle in enumerate(tupla):
    if itemSingle == item:
      indexes.append(index)
      
  return indexes

# Debug Function (Delete to send)
tupla = (2, 1, 2, 2, 3, 2)
resultado = posicoes(tupla, 5)
print(resultado)
