import numpy as np
def dirichlet(num_class, num_clients, num_data):
    np.random.seed(0)
    alpha = np.ones(num_class)

    data_for_clients = np.random.dirichlet(alpha, size=num_clients)

    # client_ratios = (num_data * data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]).astype(int)

    # Additive smoothing to ensure no zero elements
    # client_ratios += 1

    # return client_ratios
    return data_for_clients

x = dirichlet(50, 10, 1)
print(x)

for i in range (0, 50):
    