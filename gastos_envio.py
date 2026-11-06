importe = float(input("Importe del pedido (€): "))
zona = input("Zona (peninsula/baleares/canarias): ").lower()

envio = None

if zona == "peninsula":
    envio = 0 if importe >= 50 else 4.95
elif zona == "baleares":
    envio = 9.95
elif zona == "canarias":
    envio = 14.95

if envio is None:
    print("Zona no válida")
else:
    mensaje = "Envío gratuito" if envio == 0 else f"Gastos de envío: {envio:.2f} €"
    print(mensaje)
    print(f"Total a pagar: {importe + envio:.2f} €")
