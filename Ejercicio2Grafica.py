import pandas as pd


samsung_data = pd.read_csv("C:\\Users\\Andre\\Downloads\\Samsung-Dataset.csv")

# Display the first few rows of the dataset to understand its structure
samsung_data.head()

# Calcular estadísticas descriptivas
descriptive_stats = samsung_data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].describe(percentiles=[.25, .5, .75])
print(descriptive_stats)

import matplotlib.pyplot as plt

# Graficar tendencia del precio de cierre
plt.plot(samsung_data['Date'], samsung_data['Close'], label='Close Price')
plt.title('Tendencia del Precio de Cierre de Samsung Electronics')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre')
plt.legend()
plt.show()

# Graficar dispersión entre Precio de Cierre y Volumen
plt.scatter(samsung_data['Volume'], samsung_data['Close'], color='grey', marker='o')
plt.title('Dispersión entre Volumen y Precio de Cierre')
plt.xlabel('Volumen')
plt.ylabel('Precio de Cierre')
plt.show()

# Graficar caja para distribución del Precio de Cierre
plt.boxplot(samsung_data['Close'])
plt.title('Distribución del Precio de Cierre')
plt.ylabel('Precio de Cierre')
plt.show()
