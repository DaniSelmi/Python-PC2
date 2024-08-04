def conseguir_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en el formato X/Y: ")
            x, y = fraccion.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
                
            return x, y
        except ValueError:
            print("Error: Solo se permiten números enteros y el numerador debe ser menor o igual al denominador.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero.")

def calcula_porcentage(x, y):
    porcentage = (x / y) * 100
    return round(porcentage)

def main():
    x, y = conseguir_fraccion()
    porcentage = calcula_porcentage(x, y)

    if porcentage < 1:
        print("E")
    elif porcentage > 99:
        print("F")
    else:
        print(f"{porcentage}%")

if __name__ == "__main__":
    main()