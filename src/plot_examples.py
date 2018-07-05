%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dataset = pd.read_csv('../dataset/fake_house_price_data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1:].values

# scatter graph for the data
plt.scatter(x,y,marker="x",s = 20,c="red")
plt.xlim(x.min() * 0.8, x.max() * 1.1)
plt.ylim(y.min() * 0.8, y.max() * 1.1)
plt.ylabel("Price($) in 1000's")
plt.xlabel("Size in feet^2")
# draw approximate line to fit the data
lx = np.arange(800,2200)
ly = 0.20 * lx - 0;
plt.plot(lx,ly,c = 'blue')
plt.show()