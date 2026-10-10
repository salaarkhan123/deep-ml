def kalman_1d(mu, sigma2, u, Q, z, R):
    # mu, sigma2: prior mean and variance
    # u, Q: control input and process noise variance
    # z, R: observation and measurement noise variance
    # return (posterior_mean, posterior_variance, kalman_gain)

    mu_prev = mu + u 
    sigma2_prev = sigma2 + Q

    K = sigma2_prev/(sigma2_prev + R)
    mu_next = mu_prev + K*(z - mu_prev)
    sigma2_next = (1 - K)*sigma2_prev

    return mu_next, sigma2_next,K 
    pass