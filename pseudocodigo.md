 
INICIO 
    MIENTRAS VERDADERO HACER 
        MOSTRAR "Escoja el ejercicio del 1 al 5 y use 6 para salir." 
        LEER opcion 
 
        SEGUN opcion HACER 
            CASO "1": 
                nombre ← "Jefferson" 
                MOSTRAR "Bienvenido", nombre 
 
            CASO "2": 
                MOSTRAR "Introduzca el Radio" 
                LEER radio 
                area ← PI * (radio ^ 2) 
                MOSTRAR "El área del círculo es", area 
 
            CASO "3": 
                MIENTRAS VERDADERO HACER 
                    MOSTRAR "Ingrese un número:" 
                    LEER numero 
                    SI numero >= 100 ENTONCES 
                        MOSTRAR "El número", numero, "es mayor o igual que 100" 
                        SALIR DEL CICLO 
                    SINO 
                        MOSTRAR "El número no es mayor o igual que 100" 
                    FIN SI 
                FIN MIENTRAS 
 
            CASO "4": 
                iva ← 0.19 
                MIENTRAS VERDADERO HACER 
                    MOSTRAR "Ingrese el precio del producto:" 
                    LEER precio_producto 
                    SI precio_producto ES NUMÉRICO ENTONCES 
                        total_pagar ← precio_producto + (precio_producto * iva) 
                        MOSTRAR "El total a pagar es:", total_pagar 
                        SALIR DEL CICLO 
                    SINO 
                        MOSTRAR "El precio debe ser un número." 
                    FIN SI 
                FIN MIENTRAS 
 
            CASO "5": 
                MOSTRAR "Ingrese el primer número:" 
                LEER a 
                MOSTRAR "Ingrese el segundo número:" 
                LEER b 
                MOSTRAR "suma:", a+b 
                MOSTRAR "resta:", a-b 
                MOSTRAR "multiplicación:", a*b 
                MOSTRAR "división:", a/b 
                MOSTRAR "módulo:", a%b 
 
            CASO "6": 
                MOSTRAR "Usted ha escogido salir." 
                SALIR DEL PROGRAMA 
        FIN SEGUN 
    FIN MIENTRAS 
FIN