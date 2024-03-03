#Suma de Gauss:
a= int(input("Escribe un numero: "))
result= (a*(a+1))/2
print(result)


#Suma de Gauss recursivo:
def gauss(n):
   if n==0:
      return 0
   else:
      return n + gauss(n-1)
n=int(input("Escribe un numero: "))
print(gauss(n))


#Suma de Gauss iterativo:
a=1

while a >=1:
   a=int(input("Escribe un numero: "))
   gauss= (a*(a+1))/2
   print ("La suma entre 0 y %d es igual a : \n %d "% (a, gauss))
   a=int(input("¿Seguir sumando? \n si=1 \n no=0 "))

   if a==1:
      a+=1
   else:
      a-=1
      print("Chau")
      break
