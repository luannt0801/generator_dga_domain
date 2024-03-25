import argparse


class RandInt:
    def __init__(self, seed):
        self.seed = seed

    def rand_int_modulus(self, modulus):
        ix = self.seed
        ix = 16807 * (ix % 127773) - 2836 * (ix // 127773) & 0xFFFFFFFF
        self.seed = ix
        return ix % modulus


def get_domains(seed, nr):
    r = RandInt(seed)
    domains = []
    for i in range(nr):
        domain_len = r.rand_int_modulus(12 + 1) + 8
        domain = ""
        for i in range(domain_len):
            char = chr(ord("a") + r.rand_int_modulus(25 + 1))
            domain += char
        domain += ".com"
        domains.append(domain)
    return domains


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate Dircrypt domains")
    parser.add_argument("seed", help="seed as hex")
    parser.add_argument("-n", "--nr", type=int, help="nr of domains to generate")
    parser.add_argument("--output_file", help="output file name", default="domains.txt")
    args = parser.parse_args()

    domains = get_domains(int(args.seed, 16), args.nr)

    with open(args.output_file, "w") as file:
        for domain in domains:
            file.write(domain + "\n")
