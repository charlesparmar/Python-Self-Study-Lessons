import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Data = { 'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
         'Exchange Rate': [65, 69, 71, 64, 62, 59, 72, 71, 75, 78, 81]}

df = pd.DataFrame(Data)
print(df)

df.plot(x = 'Year', y = 'Exchange Rate', kind = 'bar')
plt.show()
