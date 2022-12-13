from traceback import print_tb
import numpy as np
import csv
import pandas as pd

from scipy.stats import norm

def main(filename_list):

    mu_z = pd.read_csv('./result/mu_z.csv', header=None).values
    mu_z = np.array(mu_z)
    mu_z = mu_z.reshape(-1, 1)   
    mu_z_max_index = mu_z.argmax()

    if len(filename_list) != 1:
        for x in filename_list:
            print(x)
            cov = np.load('result/' + x + '_cov_result.npy') #共分散の読み込み
            cov = np.array(cov)
            print('cov',cov)
            mu = pd.read_csv(
                'result/' + x + '_mu_result.csv',
                header=None).values.tolist() # 予測平均の読み込み
            mu = np.array(mu)
            mu = mu.reshape(-1, 1)
            
            cov = cov[mu_z_max_index]
            cov = cov.reshape(-1, 1)

            print(cov.shape)
            mu_max = mu[mu_z_max_index] # 予測平均最大
            mu_prod = mu_max * mu  
            
            if  x == "1_001_2019_Nov_15_1717": #一人目の読み込み
                mu_prod_list = mu_prod
                cov_list = cov
            else: # それ以外の共分散の結合
                mu_prod_list = np.hstack((mu_prod_list, mu_prod))
                cov_list = np.hstack((cov_list, cov))
            
        print('mu_prod_list',mu_prod_list.mean(axis=1))
        print('cov_list',cov_list.mean(axis=1))
        cov_z = ((mu_prod_list.mean(axis=1).reshape(-1,1) + cov_list.mean(axis=1).reshape(-1,1)) - (mu_z[mu_z_max_index] * mu_z)) # 予測平均共分散
        print('cov_z',cov_z)
        np.save('result/cov_z.npy', cov_z)

    sig_2 = pd.read_csv( # 予測分散の読み込み
                'result/sig_2_mu.csv',
                header=None).values.tolist()
    sig_2 = np.array(sig_2)
    sig_2 = sig_2.reshape(-1, 1)

    dif_var =(sig_2[mu_z_max_index] + sig_2) - (2 * cov_z) # 予測平均最大点の分散の差
    dif_var[mu_z_max_index] = 10000 
    print('sqrt',np.sqrt(dif_var))
    dif_sd = np.sqrt(dif_var)

    dif_mean = (mu_z[mu_z_max_index] - mu_z) # 予測平均最大点と予測平均の差
    dif_mean[mu_z_max_index] = 0
    

    p_value = norm.cdf(0, loc= dif_mean, scale= dif_sd)
    p_value[mu_z_max_index] = 1
    p_count = np.count_nonzero(p_value <= 0.05)
    print(p_count)
    
    with open('result/P_val.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(p_value)
    f.close()    

if __name__ == '__main__':
    filename_list = pd.read_csv('./load_list.csv', header=None)
    filename_list = (np.array(filename_list)).flatten().tolist()
    main(filename_list)  # 全被験者の色々を出す 個人のも出る


