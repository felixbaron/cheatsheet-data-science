# %%
import numpy as np
import pandas as pd

# Uncomment to open in DataExplorer
# pd.options.display.html.table_schema = True
# pd.options.display.max_rows = 5000

# Read CSV
df = pd.read_csv(
    'https://opendata.ruhr/dataset/7b4abcb5-9c2f-4763-aab6-9355939c19d6/resour'
    'ce/85e96d35-07fe-4752-9062-26607e0850d9/download/schulerinnen.csv',
    sep=';',
    engine='python',
    index_col=0)

df

# %%
# Access columns
assert type(df['Geschlecht']) == pd.core.series.Series

# %%
# Access two columns
df[['Geschlecht', 'Nationalität']]

# %%
# Show first 4 rows
df[1:4]

# %%
# Introspect one record
df.iloc[[4, 9]]
df.iloc[[4, 9], [1, 4]]

# Show all rows, but only 2 columns
df.loc[:, ['Nationalität', 'Geschlecht']]

# %%
# Filter for schools with many pupils
large_school = df['Schüler/-innen (allgemeinbildend)'] > 1000
df[large_school]

# %%
# Filter for two conditions
female = df['Geschlecht'] == 'weiblich'
school_filter = np.logical_and(female, large_school)
df[school_filter]

# %%
# Filter for 10 rows, while loop
count_max = 10
number_of_pupils = 1000
actual = len(df[large_school].index)
while actual > count_max:
    number_of_pupils = number_of_pupils * 1.01
    large_school = df['Schüler/-innen (allgemeinbildend)'] > number_of_pupils
    actual = len(df[large_school].index)
df[large_school]

# %%
# enumerate function
my_list = [1, 3, 4, 5, ]
list(enumerate(my_list))

# %%
# Iterate over Dictionaries with items()
world = {"afghanistan": 30.25, "albania": 2.77, "algeria": 39.21}
for key, value in world.items():
    print("Key is " + str(key) + " \nValue is: " + str(value) + "\n\n")

# %%
# Iterate over merged Numpy Arrays with nditer()
import numpy as np
np_one = np.array([1.34, 1.23, 4.535, 23.45])
np_two = np.array([2.34, 3.23, 4.535, 23.45])
combined = np.array([np_one, np_two])
for val in np.nditer(combined):
    print(val)

# %%
# Iterate over Pandas DataFrame with iterrows()
df['len_gender'] = df['Geschlecht'].apply(len)
df
