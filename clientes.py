# Para almacenar los clientes
clientes = {}

# Registrar un cliente
def registrar_cliente():
    print("REGISTRANDO UN CLIENTE")
    ID_cliente = input("INTRODUCE UN ID PARA EL CLIENTE: ")
    if ID_cliente in clientes:
        print("EL CLIENTE YA ESTÁ REGISTRADO, PRUEBA CON OTRO ID")
        return

    # Personalización del cliente
    nombre = input("NOMBRE DEL CLIENTE: ")
    email = input("EMAIL DEL CLIENTE: ")
    clientes[ID_cliente] = {"nombre": nombre, "email": email}
    print("CLIENTE REGISTRADO")

# Visualizar clientes
def mostrar_clientes():
    print("LOS CLIENTES")
    if not clientes:
        print("NO HAY CLIENTES REGISTRADOS")
        return
    for nombre_cliente, datos in clientes.items():
        print(f"ID: {nombre_cliente}, Nombre: {datos['nombre']}, Email: {datos['email']}")


