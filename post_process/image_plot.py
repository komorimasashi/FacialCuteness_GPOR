import numpy as np
import pandas as pd
import shutil
import os
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

def main(filename_list):
    X1array = np.linspace(-2, 2, 11)
    X2array = np.linspace(-2, 2, 11)
    X3array = np.linspace(-2, 2, 11)
    xx1, xx2, xx3 = np.meshgrid(X1array, X2array, X3array)
    Xtest = np.hstack((xx1.reshape(-1, 1), xx2.reshape(-1, 1), xx3.reshape(-1, 1)))

    for name in filename_list:
        image_dir = "./max_min_image/" 
        if not os.path.isdir(image_dir):
            os.makedirs(image_dir)

        mu = pd.read_csv('./result/' + name + '_mu_result.csv',header=None).values.tolist() # mu読み込み
        max_index = trance_index(Xtest[np.argmax(mu)])
        min_index = trance_index(Xtest[np.argmin(mu)])
        mu_max_index = Xtest[np.argmax(mu)]
        mu_min_index = Xtest[np.argmin(mu)]
        print('mu_max_index', mu_max_index)
        print('mu_min_index', mu_min_index)
        print('max', max_index)
        print('min', min_index)
  
        shutil.copyfile("../image_data/" + str(max_index[0])[:3] + "/" + str(max_index[1])[:3] + "/" + str(max_index[2])[:3] + ".png", image_dir + name + "_max.png")
        shutil.copyfile("../image_data/" + str(min_index[0])[:3] + "/" + str(min_index[1])[:3] + "/" + str(min_index[2])[:3] + ".png", image_dir + name + "_min.png")

    mu = pd.read_csv('./result/mu_z.csv',header=None).values.tolist() # mu読み込み
    max_index = trance_index(Xtest[np.argmax(mu)])
    min_index = trance_index(Xtest[np.argmin(mu)])
    shutil.copyfile("../image_data/" + str(max_index[0])[:3] + "/" + str(max_index[1])[:3] + "/" + str(max_index[2])[:3] + ".png", image_dir  + "mu_z_max.png")
    shutil.copyfile("../image_data/" + str(min_index[0])[:3] + "/" + str(min_index[1])[:3] + "/" + str(min_index[2])[:3] + ".png", image_dir  + "mu_z_min.png")
    
    mu_max_index = Xtest[np.argmax(mu)]
    mu_min_index = Xtest[np.argmin(mu)]
    print('mu_max_index', mu_max_index)
    print('mu_min_index', mu_min_index)
    print('max', max_index)
    print('min', min_index)


if __name__ == '__main__':
    filename_list = pd.read_csv('./load_list.csv', header=None)
    filename_list = (np.array(filename_list)).flatten().tolist()
    main(filename_list)  # 全被験者の色々を出す 個人のも出る