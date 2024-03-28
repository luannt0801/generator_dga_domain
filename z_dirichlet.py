import numpy as np

# Số lượng loại domain
num_domains = 11  # 10 loại DGA + 1 loại benign

# Số lượng clients
num_clients = 10

# Khởi tạo mảng alpha với giá trị đồng đều
alpha = np.ones(num_domains)
print(alpha)

# Tạo dữ liệu theo phân phối Dirichlet cho 10 clients
data_for_clients = np.random.dirichlet(alpha, size=num_clients)

# In ra dữ liệu cho từng client
for i, client_data in enumerate(data_for_clients, 1):
    print(f"Client {i}: {client_data}")
