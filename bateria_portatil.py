porcentaje = int(input("Porcentaje de batería: "))

if porcentaje < 20:
    print("Batería baja: conecta el cargador")
else:
    print("Nivel de batería correcto")

minutos_totales = porcentaje * 300 // 100
horas = minutos_totales // 60
minutos = minutos_totales % 60

print(f"Autonomía estimada: {horas} h {minutos} min")
