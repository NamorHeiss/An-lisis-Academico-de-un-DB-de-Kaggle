import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Cargar los datos
data = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Phys_CompSci_clean.csv')
data = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Research Articles_clean.csv')

# Asegurarse de que no hay NaN en la columna de interés
data['abstract'] = data['abstract'].fillna('')

# Lista de palabras clave para buscar
keywords = ['machine learning', 'climate change', 'covid', 'quantum', 'cancer', 'blockchain']

# Contar la presencia de cada palabra clave
keyword_counts = Counter()
for keyword in keywords:
    # Contar cuántas veces aparece cada palabra clave en 'abstract'
    data['contains_keyword'] = data['abstract'].str.contains(keyword, case=False, na=False)
    keyword_counts[keyword] += data['contains_keyword'].sum()

# Preparar datos para el histograma
keywords, counts = zip(*keyword_counts.items())

# Crear el histograma
plt.figure(figsize=(10, 6))
plt.bar(keywords, counts, color='skyblue')
plt.title('Frecuencia de Palabras Clave en Resúmenes')
plt.xlabel('Palabras Clave')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)  # Rota las etiquetas para mejor visualización
plt.grid(axis='y')
plt.savefig('/home/namor/Documents/Chamba/Article_Bias/venv/PLT/Tendencia.png') 
# Mostrar el gráfico
plt.show()




