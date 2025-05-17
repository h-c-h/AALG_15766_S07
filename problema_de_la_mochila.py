class Caja:
    def __init__(self, nombre, peso, valor):
        self.nombre = nombre
        self.peso = peso
        self.valor = valor
        self.valor_por_kg = valor / peso

cajas = [
    Caja("A", 10, 4),
    Caja("B", 4, 3),
    Caja("C", 7, 3),
    Caja("D", 5, 2),
    Caja("E", 3, 1),
    Caja("F", 3, 2),
    Caja("G", 2, 1.8),
    Caja("H", 3, 3)
]

while True:
    try:
        peso_max = float(input("Ingrese el peso máximo que puede llevar la mochila (Kg): "))
        if peso_max <= 0:
            print("El peso debe ser mayor a cero. Intente nuevamente.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

cajas.sort(key=lambda x: x.valor_por_kg, reverse=True)
peso_total = 0
valor_total = 0
seleccionadas = []

for caja in cajas:
    if peso_total + caja.peso <= peso_max:
        peso_total += caja.peso
        valor_total += caja.valor
        seleccionadas.append((caja.nombre, caja.peso, 1.0))  # 1.0 indica 100%
    else:
        peso_disponible = peso_max - peso_total
        if peso_disponible > 0:
            fraccion = peso_disponible / caja.peso
            peso_total += peso_disponible
            valor_total += caja.valor * fraccion
            seleccionadas.append((caja.nombre, peso_disponible, round(fraccion, 2)))
        break 

print("\nCajas seleccionadas:")
for nombre, peso_usado, fraccion in seleccionadas:
    porcentaje = f"{int(fraccion * 100)}%" if fraccion < 1 else "100%"
    print(f"- Caja {nombre}: {peso_usado:.2f} Kg ({porcentaje})")

print(f"\nPeso total en la mochila: {peso_total:.2f} Kg")
print(f"Soles totales obtenidos: S/ {valor_total:.2f}")