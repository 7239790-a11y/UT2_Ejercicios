nombre = input("Nombre: ")
apellidos = input("Apellidos: ")
edad = int(input("Edad: "))
nota = float(input("Nota media de 1º: "))

if nota >= 5:
    situacion = "Promociona"
else:
    situacion = "Repite"

print("=" * 34)
print(f"{'FICHA DEL ALUMNO':^34}")
print("=" * 34)
print(f"{'Nombre:':<13}{nombre} {apellidos}")
print(f"{'Edad:':<13}{edad} años")
print(f"{'Nota media:':<13}{nota:.2f}")
print(f"{'Situación:':<13}{situacion}")
