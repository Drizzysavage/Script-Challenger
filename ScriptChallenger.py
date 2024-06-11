def sieve(n):
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])
    return [x for x in range(n + 1) if primes[x]]

def main():
    n = 250
    with open("results.txt", "w") as file:
        file.write('\n'.join(map(str, sieve(n))))
    print("Prime numbers generated and saved in results.txt")

if __name__ == "__main__":
    main()
