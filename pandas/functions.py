# %%
# Random numbers
np.random.seed(24)
rand = np.random.randint(3)
print(rand)

# %%
# Lambda functions
nums = [48, 7, 9, 10]
square_all = map(lambda num: num ** 2, nums)
print(list(square_all))

# %%
# Functions excpetions


def sqrt(x):
    """Returns the square root of a number"""
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')


sqrt(-1)
