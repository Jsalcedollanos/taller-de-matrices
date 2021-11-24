# Taller de matrices
import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

#1 Número de casos de Contagiados en el País.
data[(data.Estado == 'Fallecido')].shape[0]

# Número de Municipios Afectados
data['Nombre municipio']

# Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].value_counts()

# Número de personas que se encuentran en atención en casa
Casa = (data['Ubicación del caso'] == 'Casa')

# Número de personas que se encuentran recuperados
data[(data.Recuperado == 'Recuperado')].shape[0]

# Número de personas que ha fallecido
data.Recuperado.replace('fallecido','Fallecido', inplace=True)
data[(data.Recuperado == 'Fallecido')].shape[0]

# =============================================================================
# Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)
# =============================================================================
data['Tipo de contagio'].value_counts()

