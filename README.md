# MCOC-Proyecto-0
Proyecto #0 MCOC. 

Este proyecto consta en mostrar la implicancia de la pérdida de significancia en cálculos computacionales. Como sabemos, los bits son conjuntos de números binarios (1´s y 0´s) los que, combinados, representan un número computacionalmente. Es por ésto, que está la opción de trabajar en puntos flotantes con una cantidad limitada de decimales. A mayor cantidad de decimales, más exacta la representación numérica, pero requiere más memoria, lo que puede retardar los cálculos en computadores. Esto de la cantidad de decimales alude a la significancia de un número. Uno cuando está trabajando (memoria de cálculo por ejemplo) debe especificar la cantidad de cifras significadas que fueron consideradas, ya que, al ir trabajando un número, es probable que ocurra una pérdida de significancia (loss of significance, catastrophic cancellation) y al seguir usando esos resultados, se va a ir produciendo un error de arrastre acumulativo, que va a producir cierta "incerteza" porcentual en los resultados.

En este ejemplo, se eligió una circunferencia de radio unitaria, a la que se le calcula el área con triángulos adyacentes que forman un polígono, por ejemplo, con 4 triángulos, se calcularía el área de un cuadrado inscrito en la circunferencia. Con 5 sería un pentágono, y así sucesivamente. Con ésto, es fácil ver que mientras mayor sea la partición, mayor será la exactitud del área y más se acercará al número pi. En esta entrega, se obtuvieron las áreas en puntos flotantes 32 y 64, y, también, se compararon los errores para los mismos puntos. 

ej: 
Sea n=300 la partición de 300 triángulos
el área float32 = 3.14136
el área float64 = 3.1413629825
entre ellas existe una diferencia porcentual de 0.00000999999%
ahí se puede ver una diferencia porcentual de
el error.float32 entre n=300 y n=299 = 1.43051e-06
el error.float64 entre n=300 y n=299 = 1.43051147461e-06

Con esto, es bueno precisar la exactitud de los cálculos realizados en cualquier tipo de trabajo.
