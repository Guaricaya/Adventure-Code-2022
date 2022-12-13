def main ():
    with open("Adventure Code 2022\Dia 1\dados.txt","r") as dados:
        calorias = 0
        line = dados.readline()
        lista = []
        while len(line) > 0:
            if line != '\n':
                calorias += int(line)
            elif line == '\n':
                lista.append(calorias)
                calorias = 0
            line = dados.readline()
    lista.sort()
    #resp1 = lista[-1]
    resp2 = sum(lista[-1:-4:-1])
    print(resp2)
    dados.close()
main()