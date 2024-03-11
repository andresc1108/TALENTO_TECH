#Variables
capacidad_banera_litros = 500
ritmo_llenado_litros_por_hora = 200
volumen_ocupado_por_persona_litros = 120
tiempo_horas = 2 
altura_banera_cm = 80
altura_sifon_cm = 70 

# Calcular el volumen de agua en la bañera despues de 2 horas
volumen_agua_banera_litros = min(
    capacidad_banera_litros, ritmo_llenado_litros_por_hora * tiempo_horas)

#Verificar si el nivel del agua rebasa el limite de la bañera al agregar el volumen de la persona
nivel_agua_con_ 
# Convertir alturas a metros para cálculos
altura_banera_m = altura_banera_cm / 100
altura_sifon_m = altura_sifon_cm / 100

# Calcular volumen total acumulado en la bañera después de 2 horas
volumen_acumulado_litros = ritmo_llenado_litros_por_hora * 2 - volumen_ocupado_por_persona_litros

# Calcular altura del agua en la bañera después de 2 horas
altura_agua_m = volumen_acumulado_litros / 1000 / (capacidad_banera_litros / 1000)

# Verificar si el agua rebasa el límite de la bañera con el sifón de desagüe
if altura_agua_m > altura_banera_m - altura_sifon_m:
    print("El agua rebasará el límite de la bañera con el sifón de desagüe.")
else:
    print("El agua no rebasará el límite de la bañera con el sifón de desagüe.")
