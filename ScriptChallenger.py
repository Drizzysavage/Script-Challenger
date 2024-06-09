def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    prime_numbers = [num for num in range(n + 1) if is_prime[num]]
    return prime_numbers

def main():
    n = 250
    prime_numbers = sieve_of_eratosthenes(n)

    with open("results.txt", "w") as file:
        for prime in prime_numbers:
            file.write(f"{prime}\n")

    print("Prime numbers generated and saved in results.txt")

if __name__ == "__main__":
    main()
