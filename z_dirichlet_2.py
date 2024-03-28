import numpy as np

# Số lượng loại domain
num_domains = 11  # 10 loại DGA + 1 loại benign

# Số lượng clients
num_clients = 10

# Tổng lượng dữ liệu muốn phân chia cho mỗi client
total_data = 1000

# Tạo phân phối Dirichlet với alpha đồng đều cho mỗi client
alpha = np.ones(num_domains)

# Tạo dữ liệu theo phân phối Dirichlet cho mỗi client
data_for_clients = np.random.dirichlet(alpha, size=num_clients)

# Tính toán tỷ lệ cho mỗi client sao cho tổng của chúng bằng tổng lượng dữ liệu đã chọn
client_ratios = total_data * data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]

# In ra tỷ lệ dữ liệu cho từng client
for i, client_ratio in enumerate(client_ratios, 1):
    print(f"Client {i}: {client_ratio}")
