from clientes import clientes  

# Productos disponibles
productos = {
    1: {"nombre": "Producto A", "precio": 10},
    2: {"nombre": "Producto B", "precio": 20},
    3: {"nombre": "Producto C", "precio": 30},
}

#  almacenar pedidos
pedidos = {}

# Función para realizar una compra
def realizar_compra(contador_pedidos):
    print("REALIZANDO COMPRA")
    nombre_cliente = input("ID DEL CLIENTE ")
    
    if nombre_cliente not in clientes:
        print(" EL CLIENTE NO SE HA ENCONTRADO PRUEBA A REGISTRARLO")
        return contador_pedidos

    print(" PRODUCTOS DISPONIBLES ")
    for id_producto, info in productos.items():
        print(f"{id_producto}. {info['nombre']} - €{info['precio']}")
# Te enseña los productos disponibles y tiene un registro de ellos 
    seleccion = input("SELECCIONA LOS PRODUCTOS POR SU NUMERO SEPARADO POR COMAS ")
    try:
        ids_productos = list(map(int, seleccion.split(",")))
    except ValueError:
        print(" SELECCION INCORRECTA, RECUERDA SEPARARLO POR COMAS")
        return contador_pedidos

    detalles_compra = []
    total = 0
    for id_producto in ids_productos:
        if id_producto in productos:
            producto = productos[id_producto]
            detalles_compra.append(producto)
            total += producto["precio"]
        else:
            print(f" PRODUCTO {id_producto} NO ENCONTRADO")
#Te dice los detalles de la compra 
    if detalles_compra:
        numero_pedido = contador_pedidos
        pedidos[numero_pedido] = {
            "cliente": clientes[nombre_cliente],
            "productos": detalles_compra,
            "total": total,
        }
        contador_pedidos += 1
        print(f" COMPRA REALIZADA, SU NUMERO DE PEDIDO ES : {numero_pedido}")
    else:
        print("NO SE PUDO HACER LA COMPRA")
    
    return contador_pedidos

# Función para realizar el seguimiento de una compra
def seguimiento_compra():
    print(" SEGUIMIENTO DE LA COMPRA")
    try:
        numero_pedido = int(input("INTRODUCE EL NUMERO DE PEDIDO  "))
    except ValueError:
        print(" NUMERO DE PEDIDO INCORRECTO")
        return

    if numero_pedido in pedidos:
        pedido = pedidos[numero_pedido]
        cliente = pedido["cliente"]
        print(f"Cliente: {cliente['nombre']} (Email: {cliente['email']})")
        print("Productos:")
        for producto in pedido["productos"]:
            print(f"- {producto['nombre']} - €{producto['precio']}")
        print(f"Total: €{pedido['total']}")
    else:
        print(" PEDIDO NO ENCONTRADO")



