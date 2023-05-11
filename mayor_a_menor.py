"""
Se requiere contar con un programa que, dados 3 números diferentes,
los evalúe y entregue el orden de mayor a menor.  
"""
#Se crea variables para que el usuario nos de 3 números distintos
num_1 = int(input("Ingrese primer número, Número 1:  "))
num_2 = int(input("Ingrese segundo número distinto al anterior,  Número 2:  "))
num_3 = int(input("Ingres tercer número distinto a los anteriores, Número 3:  "))
#Se usa if con operador and para determinar que los números sean dististos
if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
    #if para ver sí el primer número es mayor que el segundo
    if num_1 > num_2:
        #if para ver sí el primer número es mayor que el tercero
        if num_1 > num_3:
            #if para ver sí el segundo número es mayor que el tercero
            if (num_2 > num_3):
                #Si se da que los número son ingresados de mayor a menor mostraran de la misma forma
                print(num_1, num_2, num_3)
            else:
                #Si el primer es mayor pero el tercero es mayor que el segundo se imprime en ese orden
                print(num_1, num_3, num_2)
        else:
            #Si el tercero es mayor que el primero y el segundo menor que el primero se imprime en ese orden
            print(num_3, num_1, num_2)
    else:
        #if para ver sí el segundo número es mayor que el tercero
        if num_2 > num_3:
            #if para ver sí el tercer número es mayor que el primero
            if num_3 > num_1:
                #Sí el segundo es mayor que los demás y el tercero mayor que el primero se imprime en ese orden
                print(num_2, num_3, num_1)
            else:
                #Sí el segundo es mayor que los demás y el primero mayor que el tercero se imprime en ese orden
                print(num_2, num_1, num_3)
        else:
            #Sí el tercero es mayor que los demás y el segundo mayor que el primero se imprime en ese orden
            print(num_3, num_2, num_1)
else:
    #Si el usuario ingresa números iguales se le advierte que debe ingresar números distintos
    print("Los números ingresados deben ser distintos: ")