import math
while True:
    opcion = input("Escoja el ejercicio del 1 al 5 y use 6 para salir.")
    match opcion:
        case "1":
            #Punto 1
            nombre = "Jefferson"
            print(f'Bienvenido {nombre}')

        case "2":
            #Punto 2
            radio_string = input("Introduzca el Radio")
            radio = float(radio_string)
            area = math.pi * math.pow(radio, 2)
            print(f'El area del circulo es {area}')

        case "3":
            #punto 3
            while True:
                numero = int(input("Ingrese un numero: "))
                
                if numero >= 100:
                    print(f"El numero {numero} es igual mayor que 100")
                    break
                else:
                    print("El numero no es mayor o igual que 100")
                    continue

        case "4":
            #punto 4
            while True:
                iva = 0.19
                try:
                    precio_producto = float(input("Ingrese el precio del prodcuto: "))
                    total_pagar = precio_producto + (precio_producto*iva)
                    print(f'El total a pagar es: {total_pagar}')
                    break
                except:
                    print("El precio debe ser un número. ")

        case "5":
            #punto 5
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print(f"suma: {a+b}")
            print(f"resta: {a-b} ")
            print(f"multiplicacion: {a*b}")
            print(f"division: {a/b}")
            print(f"modulo: {a%b}")
        
        case "6":
            print("Usted ha escogido salir.")
            break



                





