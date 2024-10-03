import math
#Datos solicitados al usuario por teclado
nombre = input("Por favor ingrese el nombre del empleado: ")
dias_laborados = int(input("Ingrese los días laborados: "))
salario = float(input("Ingrese el salario del empleado: "))

# Operaciones
prima = salario * dias_laborados / 360
cesantias = salario * dias_laborados / 360
intereses_cesantias = cesantias * 0.12 / dias_laborados
vacaciones = salario * dias_laborados / 720

# Liquidación
liquidacion_total = prima + cesantias + intereses_cesantias + vacaciones

# Resultado
print(f"Señor {nombre} para los {dias_laborados} días laborados y salario ${salario}, su liquidación se compone así:")
print(f"Prima: ${prima:.2f}")
print(f"Cesantías: ${cesantias:.2f}")
print(f"Intereses cesantías: ${intereses_cesantias:.2f}")
print(f"Vacaciones: ${vacaciones:.2f}")
print(f"Liquidación total: ${liquidacion_total:.2f}")