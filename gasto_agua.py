"""Calcular el gasto de agua de una vivienda dado el numero de m3 gastados"""

print("------------------------------------")
print("-------------ACUEDUCTO--------------")
print("------------------------------------")

#input

gasto_agua = int(input("Digite en m3 la cantidad de agua usada: "))
R = 0

if gasto_agua <= 50:
    costo_fijo = 10000
elif gasto_agua <= 200:
    costo_fijo = 10000
    R = (gasto_agua - 50) * 2000
else:
    costo_fijo = 10000
    R1 = 150 * 2000
    R2 = (gasto_agua - 200) * 3000 
    R = R1 + R2

total_gasto = costo_fijo + R

print("El valor a pagar de ", gasto_agua, " m3 es ", total_gasto, "$")
