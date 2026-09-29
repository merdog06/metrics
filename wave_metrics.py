import numpy as np


def bias(obs, model):
    """
    Mean Bias Error.

    Bias = mean(model - obs)

    Parameters
    ----------
    obs : array-like
        Observed/reference values.
    model : array-like
        Modelled values.

    Returns
    -------
    float
        Mean bias.
    """
    obs = np.asarray(obs)
    model = np.asarray(model)

    return np.mean(model - obs)


def nmb(obs, model):
    """
    Normalized Mean Bias.

    NMB = sum(model - obs) / sum(obs)

    Parameters
    ----------
    obs : array-like
        Observed/reference values.
    model : array-like
        Modelled values.

    Returns
    -------
    float
        Normalized mean bias.
    """
    obs = np.asarray(obs)
    model = np.asarray(model)

    return np.sum(model - obs) / np.sum(obs)


def rmse(obs, model):
    """
    Root Mean Square Error.

    RMSE = sqrt(mean((model - obs)^2))
    """
    obs = np.asarray(obs)
    model = np.asarray(model)

    return np.sqrt(np.mean((model - obs) ** 2))


def scatter_index(obs, model):
    """
    Scatter Index.

    SI = RMSE / mean(obs)

    Returns
    -------
    float
        Scatter index.
    """
    obs = np.asarray(obs)
    model = np.asarray(model)

    return rmse(obs, model) / np.mean(obs)


def correlation(obs, model):
    """
    Pearson correlation coefficient.
    """
    obs = np.asarray(obs)
    model = np.asarray(model)

    return np.corrcoef(obs, model)[0, 1]


def metrics(obs, model):
    """
    Calculate all standard wave-model metrics.

    Returns
    -------
    dict
        Dictionary containing Bias, NMB, RMSE, SI and correlation.
    """
    return {
        "bias": bias(obs, model),
        "nmb": nmb(obs, model),
        "rmse": rmse(obs, model),
        "si": scatter_index(obs, model),
        "r": correlation(obs, model),
    }


