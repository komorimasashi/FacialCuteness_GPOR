import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import ego
from ego.gpor import data_make, load_data


def plot_distribution_mu(x, y, z):
    X, Y = np.meshgrid(x, y)  # (x, y)にはnumpy_arrayを入れる
    Z = z
    plt.pcolormesh(X, Y, Z, cmap='hsv')
    p = plt.colorbar(orientation="vertical")  # カラーバーの表示
    p.set_label('mu', fontname="Arial", fontsize=15)  # カラーバーのラベル
    plt.xlabel('PC1', fontsize=24)
    plt.ylabel('PC2', fontsize=24)
    plt.savefig('mu_distribution.pdf')


def plot_distribution_var(x, y, z):
    X, Y = np.meshgrid(x, y)  # (x, y)にはnumpy_arrayを入れる
    Z = z
    plt.pcolormesh(X, Y, Z, cmap='hsv')
    p = plt.colorbar(orientation="vertical")  # カラーバーの表示
    p.set_label('var', fontname="Arial", fontsize=15)  # カラーバーのラベル
    plt.xlabel('PC1', fontsize=24)
    plt.ylabel('PC2', fontsize=24)
    plt.savefig('var_distribution.pdf')


def trance_index(pc):
    index = list(pc)
    x1 = index[0]
    x2 = index[1]
    x3 = index[2]

    index[0] = np.round((x1 + 2) * (20 / 4))
    index[1] = np.round((x2 + 2) * (20 / 4))
    index[2] = np.round((x3 + 2) * (20 / 4))
    if index[0] <= 9:
        index[0] = '00' + str(index[0])
    elif index[0] <= 99:
        index[0] = '0' + str(index[0])
    else:
        index[0] = str(index[0])

    if index[1] <= 9:
        index[1] = '00' + str(index[1])
    elif index[1] <= 99:
        index[1] = '0' + str(index[1])
    else:
        index[1] = str(index[1])

    if index[2] <= 9:
        index[2] = '00' + str(index[2])
    elif index[2] <= 99:
        index[2] = '0' + str(index[2])
    else:
        index[2] = str(index[2])

    return index


def main():
    filename_list = pd.read_csv('./load_list.csv', header=None)
    filename_list = (np.array(filename_list)).flatten().tolist()

    for x in filename_list:
        print("Now data making..", x)
        data_make(x)

    print('Now Loading...', filename_list[0])
    mu_list, sig_2_list = load_data(filename_list[0])

    if len(filename_list) != 1:
        for x in filename_list[1:]:
            print('Now Loading...', x)
            mu_result, sig_2_result= load_data(x)
            mu_list = np.hstack((mu_list, mu_result))  # 全被験者の予測平均のリスト
            sig_2_list = np.hstack((sig_2_list, sig_2_result))  # 全被験者の予測分散のリスト)

    mu_z = mu_list.mean(axis=1)  # ある座標における全被験者分の予測平均の平均値のリスト
    mu_z_2 = (mu_list * mu_list).mean(axis=1)  # ある座標における全被験者分の予測平均の2乗の平均値のリスト

    sig_2_mu = mu_z_2 + sig_2_list.mean(axis=1) - (mu_z * mu_z)  # ある座標における全被験者分の予測分散の平均値のリスト

    X1array = np.linspace(-2, 2, 11)
    X2array = np.linspace(-2, 2, 11)
    X3array = np.linspace(-2, 2, 11)
    xx1, xx2, xx3 = np.meshgrid(X1array, X2array, X3array)
    Xtest = np.hstack((xx1.reshape(-1, 1), xx2.reshape(-1, 1), xx3.reshape(-1, 1)))

    index_max_all = [0, 0, 0]
    index_max_all[0] = Xtest[mu_z.argmax()][0]
    index_max_all[1] = Xtest[mu_z.argmax()][1]
    index_max_all[2] = Xtest[mu_z.argmax()][2]

    print(mu_z.shape)
    print(sig_2_mu.shape)

    with open('result/result.txt', mode='w') as f:
        f.write('予測平均の平均値の最大値:' + str(mu_z.max()) + '\n'
                + '予測平均の平均値が最大値をとるときの主成分得点' + str(Xtest[mu_z.argmax()]) + '\n'
                + '予測平均の平均値が最大値をとるときの画像のインデックス' + str(trance_index(Xtest[mu_z.argmax()])) + '\n'
                + '予測分散の平均値の最大値:' + str(sig_2_mu.max()) + '\n'
                + '予測平均の平均値の最小値:' + str(mu_z.min()) + '\n'
                + '予測平均の平均値が最小値をとるときの主成分得点' + str(Xtest[mu_z.argmin()]) + '\n'
                + '予測平均の平均値が最小値をとるときの画像のインデックス' + str(trance_index(Xtest[mu_z.argmin()])) + '\n'
                + '予測分散の平均値の最小値:' + str(sig_2_mu.min()) + '\n'
                )
        f.close()

    with open('result/mu_z.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(mu_z)
    f.close()

    with open('result/sig_2_mu.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(sig_2_mu)
    f.close()

    for x in range(len(filename_list)):
        with open('result/' + filename_list[x] + 'result.txt', mode='w') as f:
            f.write('予測平均の最大値:' + str(mu_list[:, x].max()) + '\n'
                    + '予測平均の最大値をとるときの主成分得点' + str(Xtest[np.argmax(mu_list[:, x])]) + '\n'
                    + '予測平均の最大値をとるときの画像のインデックス' + str(trance_index(Xtest[np.argmax(mu_list[:, x])])) + '\n'
                    + '予測分散の最大値:' + str(sig_2_list[:, x].max()) + '\n'
                    + '予測平均の最小値:' + str(mu_list[:, x].min()) + '\n'
                    + '予測平均の最小値をとるときの主成分得点' + str(Xtest[np.argmin(mu_list[:, x])]) + '\n'
                    + '予測平均の最小値をとるときの画像のインデックス' + str(trance_index(Xtest[np.argmin(mu_list[:, x])])) + '\n'
                    + '予測分散の最小値:' + str(sig_2_list[:, x].min()) + '\n'
                    )
            f.close()

    # plot_distribution_mu(X1array, X2array, mu_z)
    # plot_distribution_var(X1array, X2array, sig_2_mu)


if __name__ == '__main__':
    main()  # 全被験者の色々を出す 個人のも出る
