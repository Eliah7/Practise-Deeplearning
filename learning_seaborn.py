import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.xkcd()
np.random.seed(sum(map(ord,"aesthetics")))

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x + i * .5)*(7 - i) * flip)

sns.set()
sns.set_style("darkgrid")  # default is the darkgrid
sns.set_context("paper")
sinplot()
plt.show()
