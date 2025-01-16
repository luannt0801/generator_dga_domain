import random
import numpy as np
import argparse

def gen_scripts(number_of_sample, number_file, dga_types, machine):
    print(f"mkdir {machine}")
    for type in dga_types:
        if type == 'corebot':
            print(f'mkdir {machine}\\{type}')
            for i in range (1,number_file+1):
                n = random.randint(432, 9348)
                n = random.randint(1,28)
                m = random.randint(1, 12)
                y = random.randint(1000, 5000)
                print(f'python .\corebot.py -s {n} -d "{y}-{m}-{n}" -n {number_of_sample} --output_file {machine}\\corebot\\corebot_{number_of_sample}_{i}.txt')
        elif type == 'dircrypt':
            print(f'mkdir {machine}\\{type}')
            for i in range(1,number_file+1):
                n = random.randint(432, 9348)
                print(f'python dircrypt.py {n} -n {number_of_sample} --output_file {machine}\\dircrypt\\dircrypt_{number_of_sample}_{i}.txt')

        elif type == 'dnschanger':
            print(f'mkdir {machine}\\{type}')
            for i in range (1, number_file+1):
                n = random.randint(432, 9348)
                print(f'python dnschanger.py {n} -n {number_of_sample} --output_file {machine}\\dnschanger\\dnschanger_{number_of_sample}_{i}.txt')

        elif type == 'fobber':
            print(f'mkdir {machine}\\{type}')
            for i in range(1,number_file+1):
                n = random.randint(1, 2)
                print(f'python fobber.py {n} -n {number_of_sample} --output_file {machine}\\fobber\\fobber_{number_of_sample}_{i}.txt')

        elif type == 'newgoz':
            print(f'mkdir {machine}\\{type}')
            for i in range (1,number_file+1):
                print(f'python newgoz.py -n {number_of_sample} --output_file {machine}\\newgoz\\newgoz_{number_of_sample}_{i}.txt')

        elif type == 'necurs':
            print(f'mkdir {machine}\\{type}')
            for i in range(1,number_file+1):
                n = random.randint(1,31)
                m = random.randint(1, 13)
                y = random.randint(1000, 5000)
                print(f'python necurs.py -n {number_of_sample} -d "{y}-{m}-{n}" --output_file {machine}\\necurs\\necurs_{number_of_sample}_{i}.txt')

        elif type == 'ramnit':
            print(f'mkdir {machine}\\{type}')
            for i in range (1,number_file+1):
                n = random.randint(56, 230928)
                tail_list = ['.com', '.net','.org']
                tail = random.choice(tail_list)
                print(f'python ramnit.py {n} -n {number_of_sample} -t {tail} --output_file {machine}\\ramnit\\ramnit_{number_of_sample}_{i}.txt')

        elif type == 'rambo':
            print(f'mkdir {machine}\\{type}')
            for i in range(1,number_file+1):
                print(f'python rambo.py -n {number_of_sample} --output_file {machine}\\rambo\\ramdo_{number_of_sample}_{i}.txt')
 
        elif type == 'qakbot':
            print(f'mkdir {machine}\\{type}')
            for i in range (1,number_file+1):
                n = random.randint(1,31)
                m = random.randint(1, 13)
                y = random.randint(1000, 5000)
                x = random.randint(0,1)
                print(f'python qakbot.py -n {number_of_sample} --date "{y}-{m}-{n}" --seed {x} --output_file {machine}\\qakbot\\qakbot_{number_of_sample}_{i}.txt')

        elif type == 'banjori':
            print(f'mkdir {machine}\\{type}')
            for i in range(1,number_file+1):
                print(f'python banjori.py -n {number_of_sample} --output_file {machine}\\banjori\\banjori_{number_of_sample}_{i}.txt')
    
if __name__ == "__main__":
    np.random.seed(0)

    parser = argparse.ArgumentParser(description='Test Algorithms.')
    parser.add_argument('--n', default='100', type=int, help='input number of sample for each file')
    parser.add_argument('--num_file', default='1', type=int, help='input number of file in each type data')
    parser.add_argument('--name_client', default='jetson', type=str, help='choose jetson or machine')
    parser.add_argument('--num_client', default=5,type= int , help='so luong client')
    args = parser.parse_args()

    type_for_benign = 1

    dga_labels = ['corebot', 'dircrypt', 'dnschanger', 'fobber', 'necurs', 'newgoz', 'qakbot', 'rambo', 'ramnit', 'banjori', 'benign']

    gen_scripts(number_of_sample=args.n, number_file=args.num_file, dga_types=dga_labels, machine=args.name_client)


# python Script.py --n 100000 --num_file 1 --name_client dai --num_client 1