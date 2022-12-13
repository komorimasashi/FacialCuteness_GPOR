import numpy as np
import gpflow
from scipy.optimize import differential_evolution


def random_gallery():
    x1 = np.random.rand() * 4 - 2
    x2 = np.random.rand() * 4 - 2
    x3 = np.random.rand() * 4 - 2
    x_1 = np.round((x1 + 2) * (20 / 4))
    x_2 = np.round((x2 + 2) * (20 / 4))
    x_3 = np.round((x3 + 2) * (20 / 4))
    x_gallery = np.array([x1, x2, x3])
    x_index = np.array([x_1, x_2, x_3])
    x_index = x_index.astype('i1')
    x_index = list(x_index)
    return x_gallery, x_index


def ucb_gallery(results, responses, standard_deviation=2, separate=21):
    def ucb(landmark):
        landmark_array = np.array([[landmark[0], landmark[1], landmark[2]]])
        global mu, var
        mu, var = m.predict_y(landmark_array)
        ucb_value = var
        return -ucb_value

    X = np.array(results)
    X = X.reshape(len(X), 3)
    Y = np.array(responses)
    Y = Y.reshape(len(Y), 1)

    bin_edges = np.array(np.arange(np.unique(Y).size + 1), dtype=float)
    bin_edges = bin_edges - bin_edges.mean()
    likelihood = gpflow.likelihoods.Ordinal(bin_edges)

    # build a model with this likelihood
    m = gpflow.models.VGP(X, Y,
                          kern=gpflow.kernels.RBF(input_dim=3, lengthscales=0.1, ARD=True),
                          likelihood=likelihood)

    # fit the model
    bounds = [(-1, 1), (-1, 1), (-1, 1)]
    gpflow.train.ScipyOptimizer().minimize(m)
    next_ucb = differential_evolution(ucb,
                                      bounds=bounds,
                                      maxiter=20)

    x1 = next_ucb.x[0]
    x2 = next_ucb.x[1]
    x3 = next_ucb.x[2]

    x_1 = np.round((x1 + 2) * (20 / 4))
    x_2 = np.round((x2 + 2) * (20 / 4))
    x_3 = np.round((x3 + 2) * (20 / 4))

    x_index = np.array([x_1, x_2, x_3])
    x_index = x_index.astype('i1')
    x_index = list(x_index)
    return next_ucb.x, x_index
