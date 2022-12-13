import string


def main():
    with open('Dia 3\dados.txt', 'r') as dados:
        line = dados.readline()
        lis = list(string.ascii_letters)
        total = 0
        while len(line) > 0:
            n = len(line) - 1
            x = int(n/2)
            parts = [line[i:i+x] for i in range(0, n, x)]
            for i in range(0, x):
                if parts[0][i] in parts[1]:
                    total += (lis.index(parts[0][i]) + 1)
                    break
                else:
                    total += 0
            line = dados.readline()
    print(total)
    dados.close()


main()
