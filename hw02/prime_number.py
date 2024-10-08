def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

def main():
    n=10

    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

if __name__ == "__main__":
    main()
