import pandas as pd

# Crear un DataFrame con datos ficticios de ventas
data = {
    'Producto': ['Camisa', 'Pantalon', 'Zapato', 'Camisa', 'Pantalon', 'Zapato', 'Camisa', 'Pantalon', 'Zapato'],
    'Precio': [20, 30, 40, 20, 30, 40, 20, 30, 40],
    'Cantidad Vendida': [2, 3, 1, 4, 2, 3, 1, 2, 1],
    'Fecha': ['2022-01-01', '2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-02', '2022-01-03', '2022-01-03', '2022-01-03']
}

df = pd.DataFrame(data)

print("DataFrame completo:")
print(df)

print("\nMostrar los primeros 5 registros del DataFrame:")
print(df.head(5))

print("\nCalcular el ingreso total por cada producto:")
ingreso_por_producto = df.groupby('Producto')['Precio'].sum() * df.groupby('Producto')['Cantidad Vendida'].sum()
print(ingreso_por_producto)

print("\nCalcular el ingreso total de todas las ventas:")
ingreso_total = (df['Precio'] * df['Cantidad Vendida']).sum()
print(ingreso_total)

print("\nFiltrar los productos vendidos en una fecha específica:")
fecha_especifica = '2022-01-02'
productos_fecha_especifica = df[df['Fecha'] == fecha_especifica]
print(productos_fecha_especifica)

print("\nOrdenar los productos por cantidad vendida en orden descendente:")
productos_ordenados = df.sort_values('Cantidad Vendida', ascending=False)
print(productos_ordenados)