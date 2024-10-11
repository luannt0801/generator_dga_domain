import random
import numpy as np
import pandas as pd

def dirichlet(num_clients, rounds):
    np.random.seed(0)
    alpha = np.ones(num_clients)

    data_for_clients = np.random.dirichlet(alpha, size=rounds)

    client_ratios = (2000* data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]).astype(int)
    # client_ratios = (100* data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]).astype(int)

    # Additive smoothing to ensure no zero elements
    client_ratios += 1

    # Add 100 to elements less than 100
    client_ratios[client_ratios < 100] += 50

    return client_ratios
# def dirichlet(num_clients, rounds):
#     np.random.seed(0)
#     alpha = np.ones(num_clients)

#     data_for_clients = np.random.dirichlet(alpha, size=rounds)

#     client_ratios = (4000 * data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]).astype(int)
#     # client_ratios = (100 * data_for_clients / np.sum(data_for_clients, axis=1)[:, np.newaxis]).astype(int)

#     # Additive smoothing to ensure no zero elements
#     client_ratios += 1

#     # Adjust the values to ensure each element is between 100 and 250
#     for i in range(len(client_ratios)):
#         for j in range(len(client_ratios[i])):
#             if client_ratios[i][j] < 100:
#                 client_ratios[i][j] + 50
    
#     return client_ratios

if __name__ == '__main__':
    np.random.seed(0)
    print(dirichlet(num_clients=10, rounds=50))
    # round_50_client_10 = dirichlet(num_class=10, num_clients=50, num_data=100)
    round_50_client_10 = dirichlet(num_clients=10, rounds=50)

    client_1 =[]
    client_2 =[]
    client_3 =[]
    client_4 =[]
    client_5 =[]
    client_6 =[]
    client_7 =[]
    client_8 =[]
    client_9 =[]
    client_10 =[]

    main_dga_in_50rounds = []
    dga_9_in_50_rounds = []


    print("##########@@@@@@@@@@@@##########")
    alpha = 1
    x= 0
    print(alpha)
    for i in range(0, 50):
        # print(f"round {i} : {round_50_client_10[i]*10}")
        # for j in range(0,10):
        #     print(f"client {j}: {round_50_client_10[j][i]*10}")
        # client_1.append(int((round_50_client_10[i][0]*10)/5))
        # client_2.append(int((round_50_client_10[i][1]*10)/5))
        # client_3.append(int((round_50_client_10[i][2]*10)/5))
        # client_4.append(int((round_50_client_10[i][3]*10)/5))
        # client_5.append(int((round_50_client_10[i][4]*10)/5))
        # client_6.append(int((round_50_client_10[i][5]*10)/5))
        # client_7.append(int((round_50_client_10[i][6]*10)/5))
        # client_8.append(int((round_50_client_10[i][7]*10)/5))
        # client_9.append(int((round_50_client_10[i][8]*10)/5))
        # client_10.append(int((round_50_client_10[i][9]*10)/5))
        client_1.append(int(round_50_client_10[i][0]*alpha+x))
        client_2.append(int(round_50_client_10[i][1]*alpha+x))
        client_3.append(int(round_50_client_10[i][2]*alpha+x))
        client_4.append(int(round_50_client_10[i][3]*alpha+x))
        client_5.append(int(round_50_client_10[i][4]*alpha+x))
        client_6.append(int(round_50_client_10[i][5]*alpha+x))
        client_7.append(int(round_50_client_10[i][6]*alpha+x))
        client_8.append(int(round_50_client_10[i][7]*alpha+x))
        client_9.append(int(round_50_client_10[i][8]*alpha+x))
        client_10.append(int(round_50_client_10[i][9]*alpha+x))

    print(f"client 1 - in 50 round: \n {client_1}")
    print(f"client 2 - in 50 round: \n {client_2}")
    print(f"client 3 - in 50 round: \n {client_3}")
    print(f"client 4 - in 50 round: \n {client_4}")
    print(f"client 5 - in 50 round: \n {client_5}")
    print(f"client 6 - in 50 round: \n {client_6}")
    print(f"client 7 - in 50 round: \n {client_7}")
    print(f"client 8 - in 50 round: \n {client_8}")
    print(f"client 9 - in 50 round: \n {client_9}")
    print(f"client 10 - in 50 round: \n {client_10}")

    total_1 = sum(client_1)
    print("DGA Client 1: \n", total_1)
    total_2 = sum(client_2)
    print("DGA Client 2: \n", total_2)
    total_3 = sum(client_3)
    print("DGA Client 3: \n", total_3)
    total_4 = sum(client_4)
    print("DGA Client 4: \n", total_4)
    total_5 = sum(client_5)
    print("DGA Client 5: \n", total_5)
    total_6 = sum(client_6)
    print("DGA Client 6: \n", total_6)
    total_7 = sum(client_7)
    print("DGA Client 7: \n", total_7)
    total_8 = sum(client_8)
    print("DGA Client 8: \n", total_8)
    total_9 = sum(client_9)
    print("DGA Client 9: \n", total_9)
    total_10 = sum(client_10)
    print("DGA Client 10: \n", total_10)

    total = total_1 + total_2 + total_3 + total_4 + total_5 + total_6 + total_7 + total_8 + total_9 + total_10

    print(total)


    for i in range (0,50):
        print(f"round {i} = {client_1[i]+client_2[i]+client_3[i]+client_4[i]+client_5[i]+client_6[i]+client_7[i]+client_8[i]+client_9[i]+client_10[i]}")