import pandas as pd
import matplotlib.pyplot as plt
# Leer el archivo Excel
df = pd.read_excel("C:\\Users\\Andre\\Downloads\\Datos.xlsx")
data = pd.read_excel("C:\\Users\\Andre\\Downloads\\Datos.xlsx")

# Mostrar las primeras filas del dataframe para entender su estructura
data.head()

# Convertirlo a CSV
df.to_csv("archivo.csv", index=None, header=True)

# Asegúrate de que los nombres de las columnas coincidan con los nombres en el archivo Excel
# Crear el gráfico de dispersión
plt.scatter(data['x'], data['y'], color='grey', marker='o')
plt.title('Gráfico de Dispersión de los Datos')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True)
plt.show()