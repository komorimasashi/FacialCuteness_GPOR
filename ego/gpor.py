import os
import csv
from pickle import TRUE
import gpflow
import numpy as np
import pandas as pd


def load_data(filename):
    mu = pd.read_csv(
        'result/' + filename + '_mu_result.csv',
        header=None).values.tolist()
    var = pd.read_csv(
        'result/' + filename + '_var_result.csv',
        header=None).values.tolist()
    
    mu = np.array(mu)
    mu = mu.reshape(-1, 1)
    var = np.array(var)
    var = var.reshape(-1, 1)
    return mu, var, 


def data_make(filename):
    os.makedirs('./result', exist_ok=True)

    result = pd.read_csv(
        'data/' + filename + '_result.csv',
        header=None).values.tolist()

    response = pd.read_csv(
        'data/' + filename + '_response.csv',
        header=None).values.tolist()
    result = np.array(result) / 2
    response = np.array(response)
    response = response.flatten()

    mu_result, var_result ,cov_result = gaussian_process_ordinal_regression(result, response)
    
    with open('result/' + filename + '_mu_result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(mu_result)
    f.close()

    with open('result/' + filename + '_var_result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(var_result)
    f.close()

    np.save('result/' + filename + '_cov_result.npy', cov_result)
    


def gaussian_process_ordinal_regression(results, responses):
    X = np.array(results)
    X = X.reshape(len(X), 3)
    Y = np.array(responses)
    Y = Y.reshape(len(Y), 1)
    bin_edges = np.array(np.arange(np.unique(Y).size + 1), dtype=float)
    bin_edges = bin_edges - bin_edges.mean()
    likelihood = gpflow.likelihoods.Ordinal(bin_edges)

    # build a model with this likelihood
    kernel = gpflow.kernels.SquaredExponential(lengthscales=0.1)

    m = gpflow.models.VGP(data = (X, Y),
                          kernel=kernel,
                          likelihood=likelihood)

    # fit the model
    optimizer = gpflow.optimizers.Scipy()
    optimizer.minimize(
        m.training_loss,
        variables = m.trainable_variables,
        options = dict(disp = True, maxiter = 100),
        )

    X1array = np.linspace(-1, 1, 11)
    X2array = np.linspace(-1, 1, 11)
    X3array = np.linspace(-1, 1, 11)
    xx1, xx2, xx3 = np.meshgrid(X1array, X2array, X3array)
    Xtest = np.hstack((xx1.reshape(-1, 1), xx2.reshape(-1, 1), xx3.reshape(-1, 1)))

    mu, var = m.predict_y(Xtest)
    mean, cov = m.predict_f(Xtest, full_cov=True)
    print('mu',mu)
    print('mean',mean)
    print('cov',cov)
    cov = np.squeeze(cov)
    mu = mu.numpy().flatten().tolist()
    var = var.numpy().flatten().tolist()
    return mu, var, cov
