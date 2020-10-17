# %%
# Sorting in python
import pandas as pd

df = pd.read_csv(file_name,
                 decimal=',',
                 sep=';',
                 thousands='.'
                 )

# Sort ascending or descending
df[['Sender / Empfänger', 'Betrag in EUR']
   ].sort_values('Betrag in EUR', ascending=True)

df[df['Betrag in EUR'] > 500].sort_values('Betrag in EUR', ascending=False)
own_transfers = df['Sender / Empfänger'].isin([''])
df[own_transfers]
