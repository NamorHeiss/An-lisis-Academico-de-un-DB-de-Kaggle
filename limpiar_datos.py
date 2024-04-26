import pandas as pd

# Cargar los datos
file1 = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/DB/latest_research_articles.csv')
file2 = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/DB/phys_and_computsci_articles.csv')

# Eliminar filas duplicadas
file1 = file1.drop_duplicates()
file2 = file2.drop_duplicates()

# Manejo de valores faltantes, ejemplo: eliminar filas donde 'citations' es faltante
file1 = file1.dropna(subset=['citations'])
file2 = file2.dropna(subset=['citations'])

# Opcional: Filtrar columnas que no deseas
columns_to_keep = ['title', 'abstract', 'doi', 'citations']
file1 = file1[columns_to_keep]
file2 = file2[columns_to_keep]

# Guardar los datos limpios
file1.to_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Research Articles_clean.csv', index=False)
file2.to_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Phys_CompSci_clean.csv', index=False)


