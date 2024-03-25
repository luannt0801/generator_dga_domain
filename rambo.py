import argparse


def dga(seed, nr):
    s = 2 * seed * (nr + 1)
    r = s ^ (26 * seed * nr)
    domain = ""
    for i in range(16):
        r = r & 0xFFFFFFFF
        domain += chr(r % 26 + ord("a"))
        r += r ^ (s * i**2 * 26)

    domain += ".org"
    return domain

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nr", type=int, help="nr of domains to generate")
    parser.add_argument("--output_file", help="output file name", default="rambo.txt")
    args = parser.parse_args()
    list_domain = []
    for nr in range(args.nr):
        list_domain.append(dga(0xD5FFF, nr))
        # print(dga(0xD5FFF, nr))
    
    with open(args.output_file, "w") as file:
        for domain in list_domain:
            # print(domain)  # In domain ra console
            file.write(domain + "\n")  # Ghi domain vào file .txt
