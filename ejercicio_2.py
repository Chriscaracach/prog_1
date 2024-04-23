hora_actual = int(input("Ingrese la hora actual (en formato de 24 horas): "))
horas_a_sumar = int(input("Ingrese el número de horas a sumar: "))
nueva_hora = (hora_actual + horas_a_sumar) % 24
print("La hora después de", horas_a_sumar, "horas será:", nueva_hora)
