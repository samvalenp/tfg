import numpy
import pandas as pd


# Script para pasar un archivo h5 a csv. 

with pd.HDFStore('dfvalid.h5', 'r') as train:
	df = train.get('dfvalid')
	df.to_csv('dfvalid.csv')
