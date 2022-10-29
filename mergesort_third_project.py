
#! La explicacion de 4 lineas esta debajo de la URL del repo no aca, mis comentarios son para guiar en todo el proceso
def merge_sort(arr):

    if len(arr) <= 1:  # constante
        return

    mid = len(arr)//2  # constante

    left_arr = arr[:mid]  # constante
    right_arr = arr[mid:]  # constante

    print(left_arr, right_arr)  # constante

    merge_sort(left_arr)  # lineal
    merge_sort(right_arr)  # lineal

    left_index = 0  # constante
    right_index = 0  # constante
    arr_index = 0  # constante

    while left_index < len(left_arr) and right_index < len(right_arr):  # cuadratico

        if left_arr[left_index] < right_arr[right_index]:  # constante
            arr[arr_index] = left_arr[left_index]  # constante
            left_index += 1

        else:
            arr[arr_index] = right_arr[right_index]  # constante
            right_index += 1  # constante

        arr_index += 1  # constante

    if left_index < len(left_arr):  # constante
        del arr[arr_index:]  # logaritmico
        arr += left_arr[left_index:]  # constante

    elif right_index < len(right_arr):  # constante
        del arr[arr_index:]  # logaritmico
        arr += right_arr[right_index:]  # constante

    return arr  # constante


print(merge_sort([8, 12, 1, 3, 5]))

#? merge_sort([8, 12, 1, 3, 5])
#* 1- lo primero que hace es dividir la lista a la mitad absoluta = [8, 12]<->[1, 3, 5]
#* 2- despues aplica la recursividad para dividirlos hasta no tener mas
#*    mitades en la lista = [8]<->[12],[1]<->[3, 5] => [3]<->[5]
#* 3- cuando no tiene mas mitades empieza a compararse los subarreglos entre si con la iteracion (while) y la condicional (if)
#*    cuando encuentra los elementos de menor denominacion los pone al principio de sus respectivos sub arreglos terminando asi
#*    [8, 12] [1, 3, 5]
#* 4- luego se comparan entre ellos y se añaden a la pila o lista en la que se guarda nustro resultado:
#*    [8, 12] ? [1, 3, 5] 8 < 1 = false => nueva lista =[1]
#*    [8, 12] ? [3, 5] 8 < 3 = false => nueva lista =[1, 3]
#*    [8, 12] ? [5] 8 < 5 = false => nueva lista =[1, 3, 5]
#*    [8, 12] ? [] 8 < null = null => nueva lista =[1, 3, 5]
#*    en este caso como no hay elementos en el otro subarreglo se compara con ella misma
#*    [8, 12] => 8 < 12 = true => nueva lista =[1, 3, 5, 8] 
#*    otra vez el [12] no tiene nadie con quien compararse por lo que se asume que es el mayor valor y se añade a la ultima
#*    posicion de la lista o pila terminando asi:
#*    [12] => 12 < null = true => nueva lista =[1, 3, 5, 8, 12]
#*    [] => null < null = false => nueva lista =[1, 3, 5, 8, 12]
#* 5- final del mergesort terminando con nuestra lista asi [1, 3, 5, 8, 12]

