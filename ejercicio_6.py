def imprimir_triangulo(num_filas):
    for i in range(1, num_filas + 1):
        print("*" * i)

def main():
    num_filas = int(input("Ingrese el número de filas para el triángulo: "))
    imprimir_triangulo(num_filas)

main()
