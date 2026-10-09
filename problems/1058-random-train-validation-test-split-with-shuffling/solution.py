import numpy as np

def random_split(data: np.ndarray, train_frac: float,

                 validation_frac: float, seed: int = 123) -> list:

    # Number of rows/observations

    n = data.shape[0]

    # Randomly shuffle the row indices

    indices = np.random.default_rng(seed).permutation(n)

    # Find where training set ends

    train_end = int(n * train_frac)

    # Find where validation set ends

    validation_end = train_end + int(n * validation_frac)

    # Split the shuffled indices

    train_indices = indices[:train_end]

    validation_indices = indices[train_end:validation_end]

    test_indices = indices[validation_end:]

    # Use those indices to select the actual rows

    train = data[train_indices]

    validation = data[validation_indices]

    test = data[test_indices]

    # Return the three datasets

    return [train, validation, test]


    pass