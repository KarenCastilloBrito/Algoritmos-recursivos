# Algoritmos-recursivos

## Diferencias entre algoritmo recursivo e iterativo de las funciones de la serie de Fibonacci y la suma de Gauss
### Diferencias en la serie de Fibonacci
Ambos códigos calculan la serie de Fibonacci, que es una secuencia de números donde cada número es la suma de los dos números anteriores.Sin embargo, utilizan diferentes enfoques para lograrlo.

El código iterativo utiliza un bucle "for" para calcular los números de Fibonacci hasta el número deseado "n". Comienza con "a=0" y "b=1", y en cada iteración del bucle, actualiza "a" y "b" para obtener el siguiente número de Fibonacci. Este enfoque es más eficiente en términos de uso de memoria y tiempo de ejecución para números grandes, ya que evita la sobrecarga asociada con la recursión.

Por otro lado, el código recursivo utiliza la técnica de recursión para calacular los números de Fibonacci. La función "fibonacci(n)" se llama a sí misma con valores más pequeños de "n" hasta llegar a los casos base (cuando "n" es 0 o 1). Luego, utliza la suma de los resultados de las llamadas recursivas para calcular el número de Fibonacci para "n". Este enfoque puede ser más fácil de entender y escribir, pero puede ser menos eficiente para números grandes debido a la sobrecarga asociada con las múltiples llamadas recursivas.
