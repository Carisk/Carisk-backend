# Une todos os datasets da pasta em um

import pandas as pd
df = pd.DataFrame({})
avail_y = ['2020','2019','2018','2017', '2007']
for y in avail_y:
    df = pd.concat([df, pd.read_csv('acidentes' + y + '.csv', delimiter=';')])
df.to_csv('full_dataset.csv', sep=';')