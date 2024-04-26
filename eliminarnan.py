import pandas as pd

# Cargar los datos
data = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Phys_CompSci_clean.csv')
data = pd.read_csv('/home/namor/Documents/Chamba/Article_Bias/venv/Clean Data/Research Articles_clean.csv')

# Eliminar filas donde 'abstract' es NaN
data = data.dropna(subset=['abstract'])

# Calcular la longitud del resumen
data['abstract_length'] = data['abstract'].apply(len)
