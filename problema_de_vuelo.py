def calcular_cambio(denominaciones, monto):
    monto_centavos = round(monto * 100)
    cambio = []
    for denominacion in denominaciones:
        denom_centavos = int(round(denominacion * 100))
        cantidad = monto_centavos // denom_centavos
        cambio.append(cantidad)
        monto_centavos -= cantidad * denom_centavos
    return cambio
denominaciones = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]

# Solicitamos el monto
while True:
    try:
        monto = float(input("Ingrese el monto a pagar: "))
        if monto < 0:
            print("El monto no puede ser negativo, vuelva a intentarlo")
        else:
            break
    except ValueError:
        print("Valor ingresado no valido, vuelva a intentarlo")

# Calculamos el cambio y mostramos la cantidad de billetes o monedas usadas
resultado = calcular_cambio(denominaciones, monto)
print("\nDesglose del pago:")
for denom, cant in zip(denominaciones, resultado):
    if cant > 0:
        print(f"{cant} billete(s)/moneda(s) de S/ {denom:.2f}")