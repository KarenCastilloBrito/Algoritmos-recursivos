# Algoritmos-recursivos

## Diferencias entre algoritmo recursivo e iterativo de las funciones de la serie de Fibonacci y la suma de Gauss
### Diferencias en la serie de Fibonacci
Ambos códigos calculan la serie de Fibonacci, que es una secuencia de números donde cada número es la suma de los dos números anteriores.Sin embargo, utilizan diferentes enfoques para lograrlo.

El código iterativo utiliza un bucle "for" para calcular los números de Fibonacci hasta el número deseado "n". Comienza con "a=0" y "b=1", y en cada iteración del bucle, actualiza "a" y "b" para obtener el siguiente número de Fibonacci. Este enfoque es más eficiente en términos de uso de memoria y tiempo de ejecución para números grandes, ya que evita la sobrecarga asociada con la recursión.

Por otro lado, el código recursivo utiliza la técnica de recursión para calacular los números de Fibonacci. La función "fibonacci(n)" se llama a sí misma con valores más pequeños de "n" hasta llegar a los casos base (cuando "n" es 0 o 1). Luego, utliza la suma de los resultados de las llamadas recursivas para calcular el número de Fibonacci para "n". Este enfoque puede ser más fácil de entender y escribir, pero puede ser menos eficiente para números grandes debido a la sobrecarga asociada con las múltiples llamadas recursivas.

###Diferencias en la suma de Gauss
Ambos códigos calculan la suma de los números desde 0 hasta un número dado pero utlizan enfoques distintos.

El código recursivo utiliza la técnica de recursión para calcular la suma. La función "gauss(n)" se llama a sí misma con valores más pequeños de "n" hasta llegar al caso base (cuando "n" es igual a 0). Luego, utiliza la suma de los resultados de las llamadas recursivas más "n" para calcular la suma total. Este enfoque puede ser más fácil de entender y escribir, pero puede ser menos eficiente para números grandes debido a la sobrecarga asociada con las múltiples llamadas recursivas.

Por otro lado, el código iterativo utiliza un bucle "while" para calcular la suma. Comienza con "a=1" y solicita al usuario un número "a". Luego calcula la suma de los primeros "a" números naturales usando la fórmula de Gauss (a*(a+1))/2. Este enfoque puede ser más eficiente en términos de tiempo de ejecución y uso de memoria para valores grandes de "a", ya que evita la sobrecarga asociada con la recursión.

##Conclusiones
En resumen, el enfoque iterativo utiliza un bucle para calcular los números de Fibonacci y la suma de Gauss, mientras que el enfoque recursivo utiliza llamdas recursivas a una función para lograrlo. La diferencia principal radica en la eficiencia y en la facilidad de comprensión del código.
