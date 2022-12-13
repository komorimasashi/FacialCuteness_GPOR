import numpy as np
import pandas as pd

from scipy.stats import norm

mean_mu = pd.read_csv('./result/mu_z.csv',header=None).values # mu読み込み
mean_var = pd.read_csv('./result/sig_2_mu.csv',header=None).values

mean_mu = np.array(mean_mu).flatten()
mean_var = np.array(mean_var).flatten()

max_mean = mean_mu.max()
max_var = mean_var[mean_mu.argmax()]
print(max_mean)
print(max_var)

y = norm.cdf(0, loc=max_mean, scale=np.sqrt(max_var))

print(y)
