temperatura = float(input("Temperatura de la CPU (°C): "))

if temperatura < 50:
    print("Temperatura normal")
elif temperatura < 70:
    print("Temperatura elevada")
elif temperatura < 85:
    print("Temperatura alta: revisa la ventilación")
else:
    print("Temperatura crítica: el equipo se apagará")
