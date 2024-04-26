import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data1 = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Research Articles_clean.csv')
data2 = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Phys_CompSci_clean.csv')

# Agrupar por número de citas y contar las entradas en cada archivo
citation_counts1 = data1['citations'].value_counts().reset_index()
citation_counts2 = data2['citations'].value_counts().reset_index()

# Renombrar columnas para unificar
citation_counts1.columns = ['Citations', 'Count1']
citation_counts2.columns = ['Citations', 'Count2']

# Combinar los conteos en un solo DataFrame
combined_counts = pd.merge(citation_counts1, citation_counts2, on='Citations', how='outer').fillna(0)

# Sumar los conteos de ambos archivos
combined_counts['Total Count'] = combined_counts['Count1'] + combined_counts['Count2']

# Crear un scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(combined_counts['Citations'], combined_counts['Total Count'], color='blue')
plt.xticks(rotation=90)  # Rota las etiquetas del eje x para mejor visualización
plt.title('Número Total de Publicaciones por Cantidad de Citas')
plt.xlabel('Número de Citas')
plt.ylabel('Número Total de Publicaciones')
plt.grid(True)

# Guardar el gráfico en un archivo
plt.savefig('/home/namor/Documents/Chamba/Article_Bias/venv/PLT/plt1.png')  # Ajusta la ruta según necesites

plt.show()
