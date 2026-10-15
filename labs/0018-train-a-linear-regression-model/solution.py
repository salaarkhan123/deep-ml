def train(X, y, W, b):

    # Add intercept column
    X_new = np.column_stack((np.ones(X.shape[0]), X))

    # Solve for beta
    beta = np.linalg.pinv(X_new) @ y

    # Separate intercept and weights
    b = beta[0]
    W = beta[1:]

    return W, b