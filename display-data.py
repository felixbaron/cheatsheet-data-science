# %%
# Show JSON data
from IPython.display import JSON

data = {"foo": {"bar": "baz"}, "a": 1}
JSON(data)


# %%
# Display HTML inline
from IPython.display import HTML
HTML("<iframe src='https://nteract.io/' width='900' height='490'></iframe>")


# %%
# Plotter/Scatter graphs
import matplotlib.pyplot as plt

x = [1950, 1970, 1990, 2010]
y = [2.519, 3.694, 5.239, 6.849]
s = [333, 9, 1000, 140]


plt.xlabel('X Label')
plt.ylabel('Y Label')
# plt.xscale('log')
plt.title('My title')
plt.yticks([0, 0.5],
           ['1st', '2nd'])

plt.plot(x, y)
plt.scatter(x, y, s=s, c='red', alpha=0.8)
plt.grid(True)
plt.hist(x, bins=10)

plt.show()
