cliente = "Papelería Sur"
producto = "Teclado"
unidades = 7
precio_unitario = 24.90
descuento = 0.15
subtotal = unidades * precio_unitario
importe_descuento = subtotal * descuento
total = subtotal - importe_descuento

print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Descuento: {importe_descuento:.2f} €")
print(f"Total: {total:.2f} €")