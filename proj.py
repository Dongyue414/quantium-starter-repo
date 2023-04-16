import pandas as pd
import os


file_names = os.listdir('data')
dfs = []
for file_name in file_names:
    df = pd.read_table('data/'+file_name, sep=',')
    # print(df['product'][0])

    df = df[df['product'] == 'pink morsel']
    df.price = df.price.apply(lambda x: float(x[1:]))
    df['sales'] = df.price * df.quantity
    df = df[['sales','date','region']]
    dfs.append(df)

big_frame = pd.concat(dfs, ignore_index=True)
print(big_frame.head())

big_frame.to_csv('new_data.csv')


