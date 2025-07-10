#productos
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1],
    'FS1230HD': [249990,0],
}

#funcion para stock por marca
def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if(datos[1].lower() == marca.lower()):
            total+= stock[codigo][1]
    print(f"El stock total para '{marca}'es:{total}")

#funcion busqueda por precio
def buscar_por_precio(precio_min, precio_max):
    resultados = []
    for codigo, datos in stock.items():
        precio = datos[0]
        if(precio >= precio_min and precio <= precio_max) and (stock[codigo][1] > 0):
            resultados.append(codigo + "--" + datos[2])
    if(resultados):
        resultados.sort()
        print("productos encontrados:", resultados)
    else:
        print("No hay productos en ese rango de precio")

#funcion para listado de productos



#programa inicial
def main():
    while True:
        print("  *** MENU PRINCIPAL ***  ")
        print("1. Stock marca")
        print("2. Bussqueda por precio")
        print("3. Listado de productos")
        print("4. Salir")
        opc = int(input("Ingrese opcion: "))

        if(opc == 1):
            marca = input("Ingrese una marca para ver su stock: ")
            stock_marca(marca)
        elif(opc == 2):
            try:
                precio_min = float(input("Ingrese precio minimo: "))
                precio_max = float(input("Ingrese precio maximo: "))
                buscar_por_precio(precio_min, precio_max)
            except ValueError:
                print("Debe ingresar valores numericos validos!!")
        elif(opc == 3):
            continue

        elif(opc == 4):
            print("Programa finalizado.")
            break
                    
#ejecutar programa
if __name__ == "__main__":
  main()


