# %%
import pandas as pd

my_list = ['mo', 'ma', 'mi']  # is iterable
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
dat = pd.read_csv(
    'https://opendata.zitsh.de/data/zufish/gerichte_2020-09-01.csv', sep='\t')
it = iter(dat[:])
print(next(it))

# %%
# List comprehension
my_list = [1, 2, 3, 4]
# Generators
# num = iterator variable
# my_list = iterable
# num +1 = output expression
my_list_comp = [num + 1 for num in my_list]
# [output expression for iterator variable in iterable]
print(list(my_list_comp))

# %%
# Generator expressions
[num for num in range(10**10000000)] # leads to memory error

# %%
# Conditionals in generator expressions
even_nums = (num for num in range(10) if num % 4 == 0)
print(even_nums)

# %%
# Create generator functions


def num_sequence(n):
    """Generates value from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1


result = num_sequence(10)
for item in result:
    print(item)
