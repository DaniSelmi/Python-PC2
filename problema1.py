def get_fraction():
    while True:
        try:
            fraction = input("Ingrese una fracción en el formato X/Y: ")
            x, y = fraction.split("/")
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

def calculate_percentage(x, y):
    percentage = (x / y) * 100
    return round(percentage)

def main():
    x, y = get_fraction()
    percentage = calculate_percentage(x, y)

    if percentage < 1:
        print("E")
    elif percentage > 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()