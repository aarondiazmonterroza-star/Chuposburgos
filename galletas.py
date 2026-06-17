precio = 10
descuento = precio * 0.60

galletas   = int(input("Ingresa la cantidad de galletas vendidos: "))

precio_final = precio - descuento 

total = precio_final * galletas

print("Precio habitual de una galleta: $", precio)
print("Precio final por galletas con descuento: $", precio_final)
print("Costo final total: $", total)
