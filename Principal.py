from Listas import Metodos

Listas = []
_tam = int(input("Ingrese el tamaño de la Lista: "))

# llamando métodos de la otra clase 
c = Metodos()
c.ingreso(Listas, _tam)
print("BIENVENIDO AL PROGRAMA DE LOS SIGUIENTES METODS DE PYTHON")

while True:
    print("==== Menú de Opciones ====")
    print("1. MOSTRAR LOS VALORES DE LA LISTA")
    print("2. AGREGAR UNA NUEVA LISTA")
    print("3. CONTAR ELEMENTOS")
    print("4. BUSCAR EL INDICE DEL ELEMENTO")
    print("5. INSERTAR ELEMENTO")
    print("6. BORRAR UN INDICE")
    print("7. BORRAR UN ELEMENTO")
    print("8. REVERTIR LISTA")
    print("9. ORDENAR LA LISRA DE MENOR A MEYOR")
    print("10. VACIAR LA LISTA")
    print("11. SALIR")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        c.impresion(Listas, _tam)
        print("--------------------------------")
        print("")
    elif opcion == "2":
        Lista2 = []
        tama = int(input("Ingrese el tamaño de la nueva Lista: "))
        c.ingreso(Lista2, tama)
        Listas.extend(Lista2)
        print("Lista extendida correctamente.")
        #la función len() devuelve la longitud actual de una lista
        c.impresion(Listas, len(Listas))
        print("--------------------------------")
        print("")
    elif opcion == "3":
        num = int(input("Ingrese el numero a contar: "))
        cantidad = c.contar_elementos(Listas, _tam, num)
        print("La cantidad de veces que aparece el elemento en la lista es de: ", cantidad)
        print("--------------------------------")
        print("")
    elif opcion == "4":
        num = int(input("Ingrese el numero para conocer su posicion: "))
        c.obtener_valor_por_indice(Listas, _tam, num)
        print("--------------------------------")
        print("")
    elif opcion == "5":
        c.insertar_elemento(Listas, _tam)
        print("Se inserto el nuevo elemento a la lista correctamente.")
        c.impresion(Listas, len(Listas))
        print("--------------------------------")
        print("")
    elif opcion == "6":
        indice = int(input("Ingrese el indice borrar: "))
        c.borrar_item(Listas, indice)
        print("Se elimino correctamente.")
        c.impresion(Listas, len(Listas))
        print("--------------------------------")
        print("") 
    elif opcion == "7":
        num = int(input("Ingrese el elemento a borrar: "))
        c.borrar_elemento(Listas, num)
        print("Se elimino correctamente.")
        c.impresion(Listas, len(Listas))
        print("--------------------------------")
        print("") 
    elif opcion == "8":
        c.revertir(Listas)
        print("Se revirtio la lista correctamente.")
        c.impresion(Listas, len(Listas))
        print("--------------------------------")
        print("")
    elif opcion == "9":
        c.ordenar_lista(Listas)
        c.impresion(Listas, len(Listas))
        print("--------------------------------")
        print("")  
    elif opcion == "10":
        c.vaciar_lista(Listas, _tam)
        print("LISTA VACIA")
    elif opcion == "11":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
