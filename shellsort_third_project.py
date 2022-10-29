
#! La explicacion de 4 lineas esta debajo de la URL del repo no aca, mis comentarios son para guiar en todo el proceso
def shell_sort(arr):
    length = len(arr)
    interval = length // 2
    while interval > 0:
        
        for i in range(interval, len(arr)):  # lineal
            key = arr[i]  # constante
            j = i  # constante
            while j >= interval and arr[j - interval] > key:  # lineal * lineal
                arr[j] = arr[j - interval]  # constante
                j -= interval  # constante
                arr[j] = key  # constante
        interval //= 2 #logaritmica
    return arr  # constante


print(shell_sort([8, 12, 1, 3, 5]))
# Cuadratica

#* 1- se calcula el intervalo en base a la logitud de la pila dividido absolutamente entre 2, una vez obtenida la mitad 
#*    (en este caso la mitad esta en el 1 [8, 12, ->1<-, 3, 5]) se procede a replicar el metodo de insercion con la 
#*    diferencia que en vez de hacer los cambios con respecto a 1 se hacen con respecto al intervalo siendo en este primer
#*    caso 2:     

#*                    [8, 12, 1, 3, 5] => [8, 12, ->1<-, 3, 5] => 1 > 8 = false => [1, 12, 8, 3, 5]                     
#*    insert index = 2 (indice) - 2 (intervalo) = 0 (indice a insertar el valor)    0   1  2  3  4
#*    se busca el siguente indice y se compara segun el intervalo en este caso sigue siendo 2 ya que no ha acabado la lista:
#*
#*                   [1, 12, 8, 3, 5] => [1, 12, 8, ->3<-, 5] => 3 > 12 = false => [1, 3, 8, 12, 5]
#*    insert index = 3 (indice) - 2 (intervalo) = 1 (indice a insertar el valor)    0   1  2  3  4

#* 2- despues de la primera iteracion se actualiza el intervalo dividiendose el mismo entre 2 otra vez hasta llegar a su
#*    minimo divisor en este #2 caso seria 1 el valor del intervalo lo cual nos hara comparaciones unitarias:
#*    1 > 3 = true (sin cambios)
#*    3 > 8 = true (sin cambios)
#*    8 > 12 = true (sin cambios)
#*    12 > 5 = false (cambio)
#*                   [1, 3, 8, 12, 5] => [1, 3, 8, 12, ->5<-] => 5 > 12 = false => [1, 3, 8, 5, 12]
#*    insert index = 4 (indice) - 1 (intervalo) = 3 (indice a insertar el valor)    0   1  2  3  4

"""
una forma mas rapido de verlo seria asi
2 = intervalo
[8, 12, 1, 3, 5]
[1, 12, 8, 3, 5]
[1, 3, 8, 12, 5]
1 = intervalo
[1, 3, 5, 12, 8]
[1, 3, 5, 12, 8]
[1, 3, 5, 12, 8]
[1, 3, 5, 12, 8]
[1, 3, 5, 8, 12]
0 = intervalo = final del shellsort
[1, 3, 5, 8, 12]
"""
