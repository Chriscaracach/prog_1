def es_bisiesto(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def main():
    year = int(input("Ingrese un año para verificar si es bisiesto: "))
    if es_bisiesto(year):
        print(f"{year} es un año bisiesto.")
    else:
        print(f"{year} no es un año bisiesto.")

main()
