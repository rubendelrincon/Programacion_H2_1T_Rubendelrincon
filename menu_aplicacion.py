import clientes
import Pedidos

def menu():
    contador_pedidos = 1  # Inicializa el contador de pedidos
    while True:
        print("\nMenu Principal")
        print("1. Registrar clientes")
        print("2. Mostrar clientes")
        print("3. Realizar compra")
        print("4. Seguimiento de Compra")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
#Ejecuta la opcion que elija el usuario 
        if opcion == "1":
            clientes.registrar_cliente()
        elif opcion == "2":
            clientes.mostrar_clientes()
        elif opcion == "3":
            contador_pedidos = Pedidos.realizar_compra(contador_pedidos)  
        elif opcion == "4":
            Pedidos.seguimiento_compra()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta, seleccione una válida")

if __name__ == "__main__":
    menu()
     #Ejecuta la aplicacion 