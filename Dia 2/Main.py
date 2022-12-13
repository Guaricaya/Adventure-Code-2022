def main():
    with open("Adventure Code 2022\Dia 2\dados.txt", "r") as dados:
        line = dados.readline()
        result = []
        Total = 0
        while len(line) > 0:
            line = line.replace('\n','')
            result = line.split()
            """if result[1] == "X": #1ª Parte do Desafio
                Total += 1
                if result[0] == "A":
                    Total += 3
                elif result[0] == "C":
                    Total += 6
                else:
                    Total += 0
            elif result[1] == "Y":
                Total += 2
                if result[0] == "B":
                    Total += 3
                elif result[0] == "A":
                    Total += 6
                else:
                    Total += 0
            elif result[1] == "Z":
                Total += 3
                if result[0] == "C":
                    Total += 3
                elif result[0] == "B":
                    Total += 6
                else:
                    Total += 0
            else:
                Total += 0"""
            if result[0] == "A": #2ª Parte do Desafio
                if result[1] == "Y":
                    Total += 4
                elif result[1] == "Z":
                    Total += 8
                else:
                    Total += 3
            elif result[0] == "B":
                if result[1] == "Y":
                    Total += 5
                elif result[1] == "Z":
                    Total += 9
                else:
                    Total += 1
            elif result[0] == "C":
                if result[1] == "Y":
                    Total += 6
                elif result[1] == "Z":
                    Total += 7
                else:
                    Total += 2
            else:
                Total += 0        
            line = dados.readline()
        print(Total)
        dados.close()

main()        