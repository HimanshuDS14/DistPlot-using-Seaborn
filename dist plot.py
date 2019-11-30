import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

number = np.random.randn(150)
print(number)

sns.distplot(number , color = "cyan")
plt.grid()

plt.show()

sns.distplot(number , hist=False)
plt.show()