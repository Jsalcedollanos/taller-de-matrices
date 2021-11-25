# Taller de matrices
import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

#1 Número de casos de Contagiados en el País.
data[(data.Estado == 'Fallecido')].shape[0]

#2 Número de Municipios Afectados
data['Nombre municipio']

#3 Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].value_counts()

#4 Número de personas que se encuentran en atención en casa
Casa = (data['Ubicación del caso'] == 'Casa')

#5 Número de personas que se encuentran recuperados
data[(data.Recuperado == 'Recuperado')].shape[0]

#6 Número de personas que ha fallecido
data.Recuperado.replace('fallecido','Fallecido', inplace=True)
data[(data.Recuperado == 'Fallecido')].shape[0]

# =============================================================================
#7 Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)
# =============================================================================
data['Tipo de contagio'].value_counts()

# =============================================================================
#8 Número de departamentos afectados
# =============================================================================
data['Nombre departamento']

# =============================================================================
#9 Liste los departamentos afectados(sin repetirlos)
# =============================================================================
data['Nombre departamento'].value_counts()

# =============================================================================
#10 Ordene de mayor a menor por tipo de atención
# =============================================================================
data['Recuperado'].value_counts()

# =============================================================================
# 11 Liste de mayor a menor los 10 departamentos con mas casos de
# contagiados
# =============================================================================
data['Nombre departamento'].value_counts().head(10)

# =============================================================================
# 12 Liste de mayor a menor los 10 departamentos con mas casos de
# fallecidos
# =============================================================================
fallecidos = data[(data['Recuperado'] == 'Fallecido')]
fallecidos.groupby(['Nombre departamento','Recuperado']).size().head(10).sort_values(ascending=False)

# =============================================================================
# 13 Liste de mayor a menor los 10 departamentos con mas casos de 
# recuperados
# =============================================================================
recuperados = data[(data['Recuperado'] == 'Recuperado')]
recuperados.groupby(['Nombre departamento','Recuperado']).size().head(10).sort_values(ascending=False)

# =============================================================================
# Liste de mayor a menor los 10 municipios con mas casos de 
# contagiados
# =============================================================================
data['Nombre municipio'].value_counts().head(10)

# =============================================================================
# 15. Liste de mayor a menor los 10 municipios con mas casos de 
# fallecidos
# =============================================================================
fallecidos = data[(data['Recuperado'] == 'Fallecido')]
fallecidos.groupby(['Nombre municipio','Recuperado']).size().head(10).sort_values(ascending=False)