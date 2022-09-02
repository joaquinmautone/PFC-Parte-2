def buscar_palabra_en_linea(linea_de_texto, palabra_buscada): 
  count = 0

  for text in linea_de_texto:
    count += text.count(palabra_buscada)
  
  exist = 0
  
  if count > 0:
    exist = 1

  return [exist, count]
     
def leer_archivo(lista, elemento):
  if elemento in lista:
    return "El elemento está en la lista"
  
  return 'El elemento no está en la lista'
  