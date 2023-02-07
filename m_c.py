import math
peso = float(input("¿Cuál es su peso en kilos?"))
estatura = float(input("Cuál es su estatura en metros?"))
mc = round((peso / (estatura**2)),2)
print(f"El índice de masas corporal es de {mc}")