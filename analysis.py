import json

with open("data.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

ventas = datos["ventas"]


def total_facturado():
    total = 0

    for venta in ventas:
        total += venta["cantidad"] * venta["precio_unitario"]

    return total


def ventas_por_categoria():
    categorias = {}

    for venta in ventas:
        categoria = venta["categoria"]

        if categoria not in categorias:
            categorias[categoria] = 0

        categorias[categoria] += venta["cantidad"]

    return categorias


def producto_mas_vendido():
    productos = {}

    for venta in ventas:
        producto = venta["producto"]

        if producto not in productos:
            productos[producto] = 0

        productos[producto] += venta["cantidad"]

    return max(productos, key=productos.get)