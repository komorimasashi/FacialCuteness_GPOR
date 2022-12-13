import numpy as np
import csv
import pandas as pd

from scipy.stats import norm


def main(filename_list):
    all_P = []
    all_mu_max = []
    all_var_max = []
    for name in filename_list:
        mu = pd.read_csv('./result/' + name + '_mu_result.csv',header=None).values.tolist() # mu読み込み
        var = pd.read_csv('./result/' + name + '_var_result.csv',header=None).values.tolist()
        mu = np.array(mu).flatten()
        var= np.array(var).flatten()
        
        max_index = np.argmax(mu)
        mu_max_index = mu[max_index]
        var_mu_max_index = var[max_index]
        sd_var__max_index = np.sqrt(var_mu_max_index)
        
        p_value = norm.cdf(0, loc= mu_max_index, scale = sd_var__max_index)
        all_mu_max.append(mu_max_index)
        all_var_max.append(var_mu_max_index)
        all_P.append(p_value)
    
    all_mu_var_P = np.concatenate((np.array(filename_list).reshape(-1, 1),
                                np.array(all_mu_max).reshape(-1, 1),
                                np.array(all_var_max).reshape(-1, 1),
                                np.array(all_P).reshape(-1, 1)),axis=1)
    
    with open('all_mu_var_P.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Name', 'max_mu','max_mu_index_var','P'])
        writer.writerows(all_mu_var_P)

if __name__ == '__main__':
    filename_list = pd.read_csv('./load_list.csv', header=None)
    filename_list = (np.array(filename_list)).flatten().tolist()
    main(filename_list)  # 全被験者の色々を出す 個人のも出る