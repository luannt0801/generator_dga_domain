import random
import numpy as np

number_of_sample = 2500
number_file = 1
type_dga = ''


type_for_benign = 1 # choose 0 not random or 1 to random


def corebot(number_of_sample, number_file, type_dga):
    # #corebot
    # #python .\corebot.py -s 231 -d "2012-08-02" -n 500 --output_file corebot\\corebot_200k_1.txt
    type_dga = 'corebot'
    # print(f'mkdir {client_id}\\{type_dga}')
    print(f'mkdir {type_dga}')
    for i in range (1,number_file+1):
        n = random.randint(432, 9348)
        n = random.randint(1,28)
        m = random.randint(1, 12)
        y = random.randint(1000, 5000)
        print(f'python .\corebot.py -s {n} -d "{y}-{m}-{n}" -n {number_of_sample} --output_file corebot\\corebot_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # #dircrypt
    #python dircrypt.py 23 -n 500 --output_file dircrypt\\dircrypt_200k_01.txt
    type_dga = 'dircrypt'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(432, 9348)
        print(f'python dircrypt.py {n} -n {number_of_sample} --output_file dircrypt\\dircrypt_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    #dnschager
    #python dnschanger.py 543 -n 200000 --output_file dnschange\\dnschange_200k_01.txt
    type_dga = 'dnschanger'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1, number_file+1):
        n = random.randint(432, 9348)
        print(f'python dnschanger.py {n} -n {number_of_sample} --output_file dnschanger\\dnschanger_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # #fobber
    #python fobber.py 1 -n 200000 --output_file fobber\\fobber_200k_01.txt
    type_dga = 'fobber'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(1, 2)
        print(f'python fobber.py {n} -n {number_of_sample} --output_file fobber\\fobber_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # #newgoz
    #python newgoz.py -n 200000 --output_file newgoz\\newgoz_200k_01.txt
    type_dga = 'newgoz'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        print(f'python newgoz.py -n {number_of_sample} --output_file newgoz\\newgoz_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # #necurs
    type_dga = 'necurs'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(1,31)
        m = random.randint(1, 13)
        y = random.randint(1000, 5000)
        print(f'python necurs.py -n {number_of_sample} -d "{y}-{m}-{n}" --output_file necurs\\necurs_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # #ramnit
    type_dga = 'ramnit'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        n = random.randint(56, 230928)
        tail_list = ['.com', '.net','.org']
        tail = random.choice(tail_list)
        print(f'python ramnit.py {n} -n {number_of_sample} -t {tail} --output_file ramnit\\ramnit_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # #rambo
    type_dga = 'rambo'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        print(f'python rambo.py -n {number_of_sample} --output_file rambo\\ramdo_{number_of_sample}_{i}.txt')

# def corebot(number_of_sample, number_file, type_dga):
    # # #simda
    # type_dga = 'simda'
    # print(f'mkdir {type_dga}')
    # # print(f'mkdir {client_id}\\{type_dga}')
    # for i in range(1, number_file+1):
    #     print(f'python simda.py -n {number_of_sample} --output_file simda\\simda_{number_of_sample}_{i}.txt')
        
def corebot(number_of_sample, number_file, type_dga):
    # #qakbot
    type_dga = 'qakbot'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,number_file+1):
        n = random.randint(1,31)
        m = random.randint(1, 13)
        y = random.randint(1000, 5000)
        x = random.randint(0,1)
        print(f'python qakbot.py -n {number_of_sample} --date "{y}-{m}-{n}" --seed {x} --output_file qakbot\\qakbot_{number_of_sample}_{i}.txt')

def corebot(number_of_sample, number_file, type_dga):
    # banjori
    type_dga = 'banjori'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        print(f'python banjori.py -n {number_of_sample} --output_file banjori\\banjori_{number_of_sample}_{i}.txt')

def benign(number_of_sample, number_file, type_dga):
    type_dga = 'benign'
    print(f'mkdir {type_dga}')
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range (1,6):
        if type_for_benign == 1:
            print(f'python benign.py -n {10*number_of_sample} --type {type_for_benign} --output_file benign_{i}.txt')
        if type_for_benign == 0:
            line = 1000000/number_of_sample
            print(f'python benign.py --type {type_for_benign} --start {line*i} --end {line*(i+1)} --output_file benign_{i}.txt')

def dirichlet():
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

    
if __name__ == "__main__":
    pass