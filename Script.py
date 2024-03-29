import random
import numpy as np
import argparse

def corebot(number_of_sample, number_file, type_dga, machine):
    # #corebot
    # #python .\corebot.py -s 231 -d "2012-08-02" -n 500 --output_file corebot\\corebot_200k_1.txt
    type_dga = 'corebot'
    # print(f'mkdir {client_id}\\{type_dga}')
    print(f'mkdir {machine}\\{type_dga}')
    for i in range (1,number_file+1):
        n = random.randint(432, 9348)
        n = random.randint(1,28)
        m = random.randint(1, 12)
        y = random.randint(1000, 5000)
        print(f'python .\corebot.py -s {n} -d "{y}-{m}-{n}" -n {number_of_sample} --output_file {machine}\\corebot\\corebot_{number_of_sample}_{i}.txt')

def dircypt(number_of_sample, number_file, type_dga, machine):
    # #dircrypt
    #python dircrypt.py 23 -n 500 --output_file dircrypt\\dircrypt_200k_01.txt
    type_dga = 'dircrypt'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(432, 9348)
        print(f'python dircrypt.py {n} -n {number_of_sample} --output_file {machine}\\dircrypt\\dircrypt_{number_of_sample}_{i}.txt')

def dnschanger(number_of_sample, number_file, type_dga, machine):
    #dnschager
    #python dnschanger.py 543 -n 200000 --output_file dnschange\\dnschange_200k_01.txt
    type_dga = 'dnschanger'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1, number_file+1):
        n = random.randint(432, 9348)
        print(f'python dnschanger.py {n} -n {number_of_sample} --output_file {machine}\\dnschanger\\dnschanger_{number_of_sample}_{i}.txt')

def fobber(number_of_sample, number_file, type_dga, machine):
    # #fobber
    #python fobber.py 1 -n 200000 --output_file fobber\\fobber_200k_01.txt
    type_dga = 'fobber'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(1, 2)
        print(f'python fobber.py {n} -n {number_of_sample} --output_file {machine}\\fobber\\fobber_{number_of_sample}_{i}.txt')

def newgoz(number_of_sample, number_file, type_dga, machine):
    # #newgoz
    #python newgoz.py -n 200000 --output_file newgoz\\newgoz_200k_01.txt
    type_dga = 'newgoz'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        print(f'python newgoz.py -n {number_of_sample} --output_file {machine}\\newgoz\\newgoz_{number_of_sample}_{i}.txt')

def necurs(number_of_sample, number_file, type_dga, machine):
    # #necurs
    type_dga = 'necurs'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(1,31)
        m = random.randint(1, 13)
        y = random.randint(1000, 5000)
        print(f'python necurs.py -n {number_of_sample} -d "{y}-{m}-{n}" --output_file {machine}\\necurs\\necurs_{number_of_sample}_{i}.txt')

def ramnit(number_of_sample, number_file, type_dga, machine):
    # #ramnit
    type_dga = 'ramnit'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        n = random.randint(56, 230928)
        tail_list = ['.com', '.net','.org']
        tail = random.choice(tail_list)
        print(f'python ramnit.py {n} -n {number_of_sample} -t {tail} --output_file {machine}\\ramnit\\ramnit_{number_of_sample}_{i}.txt')

def rambo(number_of_sample, number_file, type_dga, machine):
    # #rambo
    type_dga = 'rambo'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        print(f'python rambo.py -n {number_of_sample} --output_file {machine}\\rambo\\ramdo_{number_of_sample}_{i}.txt')
        
def qakbot(number_of_sample, number_file, type_dga, machine):
    # #qakbot
    type_dga = 'qakbot'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        n = random.randint(1,31)
        m = random.randint(1, 13)
        y = random.randint(1000, 5000)
        x = random.randint(0,1)
        print(f'python qakbot.py -n {number_of_sample} --date "{y}-{m}-{n}" --seed {x} --output_file {machine}\\qakbot\\qakbot_{number_of_sample}_{i}.txt')

def banjori(number_of_sample, number_file, type_dga, machine):
    # banjori
    type_dga = 'banjori'
    print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        print(f'python banjori.py -n {number_of_sample} --output_file {machine}\\banjori\\banjori_{number_of_sample}_{i}.txt')

def benign(number_of_sample, number_file, type_for_benign, machine):
    type_dga = 'benign'
    # print(f'mkdir {machine}\\{type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        if type_for_benign == 1:
            print(f'python benign.py -n {number_of_sample*10} --type {type_for_benign} --output_file {machine}\\benign_{i}.txt')
        if type_for_benign == 0:
            line = 1000000/number_of_sample
            print(f'python benign.py --type {type_for_benign} --start {line*i} --end {line*(i+1)} --output_file {machine}\\benign_{i}.txt')

def print_all(number_of_sample, number_file, type_dga, type_for_benign, machine):
    print(f"mkdir {machine}")
    corebot(number_of_sample, number_file, type_dga, machine)
    banjori(number_of_sample, number_file, type_dga, machine)
    dircypt(number_of_sample, number_file, type_dga, machine)
    dnschanger(number_of_sample, number_file, type_dga, machine)
    fobber(number_of_sample, number_file, type_dga, machine)
    necurs(number_of_sample, number_file, type_dga, machine)
    newgoz(number_of_sample, number_file, type_dga, machine)
    qakbot(number_of_sample, number_file, type_dga, machine)
    rambo(number_of_sample, number_file, type_dga, machine)
    ramnit(number_of_sample, number_file, type_dga, machine)
    benign(number_of_sample, number_file, type_dga, type_for_benign, machine)


# def dirichlet(num_class, num_clients, total_data):
#     alpha = np.ones(num_class)

#     data_for_clients = np.random.dirichlet(alpha, size=num_clients)

#     client_ratios = total_data * data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]

#     set_dirichlet_client = []

#     # In ra tỷ lệ dữ liệu cho từng client
#     for i, client_ratio in enumerate(client_ratios, 1):
#         print(f"Client {i}: {client_ratio}")
#         set_dirichlet_client.append(client_ratio)
#     return set_dirichlet_client

def dirichlet(num_class,num_clients, num_data):
    alpha = np.ones(num_class)

    data_for_clients = np.random.dirichlet(alpha, size=num_clients)
    print(f"data for client : " , data_for_clients)

    client_ratios = (num_data * data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]).astype(int)

    # set_dirichlet_client = []

    # # In ra tỷ lệ dữ liệu cho từng client
    # for i, client_ratio in enumerate(client_ratios, 1):
    #     # print(f"Client {i}: {client_ratio}")
    #     set_dirichlet_client.append(client_ratio)        
    # return set_dirichlet_client
    return client_ratios

def generate_samples_for_clients(number_of_sample, number_file, dga_labels, type_for_benign, machine):
    for label in dga_labels:
        if label == 'corebot':
            corebot(number_of_sample, number_file, label, machine)
        elif label == 'dircrypt':
            dircypt(number_of_sample, number_file, label, machine)
        elif label == 'dnschanger':
            dnschanger(number_of_sample, number_file, label, machine)
        elif label == 'fobber':
            fobber(number_of_sample, number_file, label, machine)
        elif label == 'necurs':
            necurs(number_of_sample, number_file, label, machine)
        elif label == 'newgoz':
            newgoz(number_of_sample, number_file, label, machine)
        elif label == 'qakbot':
            qakbot(number_of_sample, number_file, label, machine)
        elif label == 'rambo':
            rambo(number_of_sample, number_file, label, machine)
        elif label == 'ramnit':
            ramnit(number_of_sample, number_file, label, machine)
        elif label == 'banjori':
            banjori(number_of_sample, number_file, label, machine)
        elif label == 'benign':
            benign(number_of_sample, number_file, type_for_benign, machine)

# if __name__ == "__main__":
#     number_of_sample = 2500
#     number_file = 1
#     number_of_client = 10
#     type_dga = ''
#     machine = 'jetson_1'
#     type_for_benign = 1 # choose 0 not random or 1 to random

#     # confict
#     num_class = 11
#     total_data_benign = 50000 # benign or dga
#     total_data_dga_class = total_data_benign/10 # 5000

#     dga_data = np.ones(num_class)

#     # print_all(number_of_sample, number_file, type_dga, type_for_benign, machine)

#     dirichlet_clients = dirichlet(num_class, number_of_client, total_data_dga_class)
    
if __name__ == "__main__":

    # normal confict
    num_of_sample = 2500 # sample in a file
    num_file = 1  # number of file
    num_clients = 5 # machone
    type_for_benign = 1
    machine = 'machine_'
    dga_labels = ['corebot', 'dircrypt', 'dnschanger', 'fobber', 'necurs', 'newgoz', 'qakbot', 'rambo', 'ramnit', 'banjori', 'benign']

    # normal
    # for i in range (1, num_clients + 1):
    #     client_folder_name = f"{machine}_{i}"
    #     generate_samples_for_clients(num_of_sample, num_file, dga_labels, type_for_benign, client_folder_name)

    # # new setup
    num_class = 10
    num_data = 1000

    dirichlet_clients = dirichlet(num_class, num_clients, num_data)
    print(dirichlet_clients)
    print(dirichlet_clients[0][1])
    # for i, client in enumerate(dirichlet_clients):
    #     machine = f"{machine_prefix}{i}"
    #     generate_samples_for_clients(number_of_sample, number_file, dga_labels, machine)WWW
    for 