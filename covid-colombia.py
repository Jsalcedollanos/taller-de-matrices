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


