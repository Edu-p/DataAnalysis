import pandas as pd

dataset = pd.read_csv( 'datasets/kc_house_data.csv' )

# 1 pergunta

#print(len(dataset))

# 2 pergunta

#print(len(dataset.columns))

# 3 pergunta

#print(dataset.columns)

#  4 pergunta

#print(dataset.max())

# 5 pergunta

#print(dataset.sort_values('bedrooms').max())

# 6 pergunta

print( dataset['bedrooms'].sum())

