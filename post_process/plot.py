import numpy as np
import torch
import matplotlib.pyplot as plt
import os
import pandas as pd
save_fig_dir = './plot/'

if not os.path.isdir(save_fig_dir):
    os.makedirs(save_fig_dir)
    
point_np = np.linspace(-2, 2, 11)
point = np.linspace(-2, 2, 11)
p1, p2, p3 = np.meshgrid(point, point, point)
point_mesh = np.hstack((p1.reshape(-1, 1),
                        p2.reshape(-1, 1),
                        p3.reshape(-1, 1),
                        ))
#mean = pd.read_csv('./result/mu_z.csv', header=None).values.tolist() # 予測平均
mu_sigma = pd.read_csv('./result/sig_2_mu.csv', header=None).values.tolist() # 予測分散
max_point = point_mesh[np.argmax(mu_sigma)] # 予測平均最大点
min_point = point_mesh[np.argmin(mu_sigma)] # 予測平均最大点
mu_sigma = np.array(mu_sigma)
mu_sigma_reshape = mu_sigma.reshape(11,11,11)

plt.clf()
plt.figure(figsize=(12, 10))
plt.xlabel("PC1", fontsize=26)
plt.ylabel("PC2", fontsize=26)        
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.contourf(point_np, point_np, mu_sigma_reshape.mean(axis=2).T, cmap='viridis')
plt.colorbar()
plt.plot(max_point[0], max_point[1], "o", color='red', label="Max")
plt.plot(min_point[0], min_point[1], "o", color='blue', label="Min")
plt.legend(fontsize=22)
plt.savefig(save_fig_dir + "sig_pc1_pc2.pdf")

plt.clf()
plt.figure(figsize=(12, 10))
plt.xlabel("PC1", fontsize=26)
plt.ylabel("PC3", fontsize=26)        
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.contourf(point_np, point_np, mu_sigma_reshape.mean(axis=1).T, cmap='viridis')
plt.colorbar()
plt.plot(max_point[0], max_point[2], "o", color='red', label="Max")
plt.plot(min_point[0], min_point[2], "o", color='blue', label="Min")
plt.legend(fontsize=22)
plt.savefig(save_fig_dir + "sig_pc1_pc3.pdf")
