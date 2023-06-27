#append me permite ingresar valores a la lista
#clear vaciar la lista
#extend UNIR una una lista con otra
#count Cuenta el número de veces que aparece un ítem
#index Devuelve el índice en el que aparece un ítem
#insert Agrega un ítem a la lista en un índice específico, Primera posición (0), Penúltima posición (-1), Última posición en una lista con len(), una posición fuera de rango añade el elemento al final de la lista (999):
#pop Extrae un ítem de la lista y lo borra, Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):
#remove Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
#reverse Le da la vuelta a la lista actual
#sort Ordena automáticamente los ítems de una lista por su valor de menor a mayor, Podemos utilizar el argumento reverse=True para indicar que la ordene del revés
class Metodos():
    def ingreso(self,lis,tam):
        i=0
        while(i<tam):
            print("Ingrese el [",i,"] valor de la lista")
            num=int(input("numero "))
            lis.append(num)
            i=i+1
    def impresion(self,lis,tam):
        for i in range(tam):
            print(lis[i])
    
    def vaciar_lista(self,lis):
        lis.clear()
    
    def contar_elementos(self, lis, tam, num):
        cantidad = lis.count(num)
        return cantidad

    def obtener_valor_por_indice(self, lista, tam, num):
        if num in lista:
            indice = lista.index(num)
            print("El elemento", num, "se encuentra en el índice", indice)
        else:
            print("El elemento", num, "no se encuentra en la lista.")
    
    def insertar_elemento(self, lista, tam):
        while (True):
            print("==== Menú de Opciones ====")
            print("1. AGREGAR EN LA PRIMERA POSCICION")
            print("2. AGREGAR EN LA PENULTIMA POSICION")
            print("3. AGREGAR EN LA ULTIMA POSICION")
            print("4. SALIR")
            opc = input("Seleccione una opción: ")
            
            if (opc == "1"):
                num= input("Ingrese un elemento: ")
                lista.insert(0, num)  
            elif (opc == "2"):
                num= input("Ingrese un elemento: ")
                lista.insert(-1, num)  
            elif (opc == "3"):
                num = input("Ingrese un elemento: ")
                lista.append(num)
            elif (opc == "4"):
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                
    def borrar_item(self, lista, indice):
        elem = lista.pop(indice)
        print("Se eliminó el elemento", elem, " en la posición ", indice)
    
    def borrar_elemento(self, lista, num):
        elem = lista.remove(num)
        print("Se eliminó el elemento",elem)

    def revertir(self, lista):
        lista.reverse()

    def ordenar_lista(self, lista):
        lista.sort()
        print("La lista se ha ordenado de forma ascendente.")