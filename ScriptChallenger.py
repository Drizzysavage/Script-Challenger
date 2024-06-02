def criba_eratostenes(n):
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            for j in range(i*i, n + 1, i):
                es_primo[j] = False

    numeros_primos = [num for num in range(n + 1) if es_primo[num]]
    return numeros_primos

def main():
    n = 250
    numeros_primos = criba_eratostenes(n)

    with open("results.txt", "w") as archivo:
        for primo in numeros_primos:
            archivo.write(f"{primo}\n")

    print("Números primos generados y guardados en results.txt")

if __name__ == "__main__":
    main()