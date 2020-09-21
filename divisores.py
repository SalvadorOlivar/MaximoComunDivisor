numero1 = int(input("a que numero le quieres encontrar sus divisores? \n"))
numero2 = int(input("otro numero? \n"))

def divisores(num):
  i = 1
  lista_divisores = []
  while i <= num:
    if num/i == int(num/i):
      lista_divisores.append(i)
    i += 1
  return lista_divisores
  
divisores_1 = divisores(numero1)
divisores_2 = divisores(numero2)
todos_divisores = divisores_1 + divisores_2

def div_comunes():
  divisores_distintos = []
  divisores_comunes = []

  for div in todos_divisores:
    if (div not in divisores_distintos):
      divisores_distintos.append(div)
    else:
      divisores_comunes.append(div)
  return(divisores_comunes)

resultado = div_comunes()
print( "El MCD entre " + str(numero1) + " y " + str(numero2) + " es " + str(resultado[-1]))








