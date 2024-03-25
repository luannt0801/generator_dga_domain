import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nr", type=int, help="nr of domains to generate")
    parser.add_argument("--output_file", help="output file name", default="domains.txt")
    args = parser.parse_args()

    list_domain = []
    length = 7
    tld = "com"
    key = "1676d5775e05c50b46baa5579d4fc7"
    base = 0x45AE94B2

    consonants = "qwrtpsdfghjklzxcvbnmv"
    vowels = "eyuioa"

    step = 0
    for m in key:
        step += ord(m)

    for nr in range(args.nr):
        domain = ""
        base += step

        for i in range(length):
            index = int(base / (3 + 2 * i))
            if i % 2 == 0:
                char = consonants[index % 20]
            else:
                char = vowels[index % 6]
            domain += char

        domain += "." + tld
        list_domain.append(domain)
        print(domain)
        
    with open(args.output_file, "w") as file:
        for domain in list_domain:
            print(domain)  # In domain ra console
            file.write(domain + "\n")  # Ghi domain vào file .txt
