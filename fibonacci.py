#Serie de Fibonacci iterativo:
def fib(n):
   a=0
   b=1
   for x in range(n):
      c=b+a
      a=b
      b=c
   return a
while True:
   n=int(input("Escribe el no. de la serie Fibonacci que desea (o escriba 0 para salir): "))
   if n==0:
      print("Chau")
      break
   else:
      print(fib(n))


#Serie de Fibonacci recursivo:
def fibonacci(n):
   if n==0 or n==1:
      return n
   else:
      return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Escribe el no. de la serie Fibonacci que desea: "))
print(fibonacci(n))
