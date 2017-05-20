import pandas as pd
import numpy as np

file_path = 'weather.dat'

# use sep=\s+ to use varying whitespace as the separator 
data = pd.read_table(file_path, sep='\s+')

df = pd.DataFrame(data)

# remove the '*' in the dataframe in pandas
df = df.replace('\*','',regex=True)

# convert to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# get the difference between 'Mxt' and 'Mnt'
df['diff'] = df['MxT'] - df['MnT'] 

# store the maximum spread as well as corresponding day
max_diff = df['diff'].max()

max_day = df.loc[df['diff'] == max_diff, 'Dy'].iloc[0]

print max_day, max_diff







