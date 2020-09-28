# %%
my_list = ['mo', 'ma', 'mi'] # is iterable
# Create iterator
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# %%
# Enumreate function
my_enum = enumerate(my_list, 2)
print(list(my_enum))

# %%
# Zip
my_lab = ['mi', 'mo', 'mu']
z = zip(my_list, my_lab)
print(list(z))

# %%
# Working with data chunks
import pandas as pd
dat = pd.read_csv('https://opendata.zitsh.de/data/zufish/gerichte_2020-09-01.csv', sep='\t')
it = iter(dat[:])
print(next(it))
