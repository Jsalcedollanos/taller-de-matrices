# Taller de matrices
import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

#1 Número de casos de Contagiados en el País.
data[(data.Estado == 'Fallecido')].shape[0]