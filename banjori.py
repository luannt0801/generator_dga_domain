import argparse
import random


def map_to_lowercase_letter(s):
    return ord('a') + ((s - ord('a')) % 26)

def next_domain(domain):
    dl = [ord(x) for x in list(domain)]
    dl[0] = map_to_lowercase_letter(dl[0] + dl[3])
    dl[1] = map_to_lowercase_letter(dl[0] + 2*dl[1])
    dl[2] = map_to_lowercase_letter(dl[0] + dl[2] - 1)
    dl[3] = map_to_lowercase_letter(dl[1] + dl[2] + dl[3])
    return ''.join([chr(x) for x in dl])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nr", type=int, help="nr of domains to generate")
    parser.add_argument("--output_file", help="Output file name", default="domains.txt")
    args = parser.parse_args()
    seed_list = ['earnestnessbiophysicalohax.com', 'bandepictom.com', 'telemachuslazaroqok.com', 'texanfoulilp.com'] # 15372 equal to 0 (seed = 0)
    domain = random.choice(seed_list)
    list_domain = []
    for i in range(args.nr):
        # print(domain)
        domain = next_domain(domain)
        list_domain.append(domain)
    
    with open(args.output_file, "w") as file:
        for domain in list_domain:
            # print(domain)  # In domain ra console
            file.write(domain + "\n")  # Ghi domain vào file .txt