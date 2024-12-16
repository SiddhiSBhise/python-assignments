def is_prime(number): """is_prime function iteratively checks for factors"""
    """Check if a number is prime using iteration."""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_previous_prime(number):"""find_previous_prime use loops to find nearby primes"""
    """Find the largest prime number less than the given number."""
    for n in range(number - 1, 1, -1):
        if is_prime(n):
            return n
    return None

def find_next_prime(number): """find_next_prime use loops to find primes if nearby"""
    """Find the smallest prime number greater than the given number."""
    n = number + 1
    while True:
        if is_prime(n):
            return n
        n += 1

def get_divisors(number): """get_divisors function results a list of divisors"""
    """Get a list of divisors of the number."""
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def main():
    while True:
        user_input = input("Enter a positive whole number: ").strip()
        if not user_input.isdigit():
            print("Invalid input. Please enter a positive whole number.")
            continue

        number = int(user_input)
        if number <= 0:
            print("Invalid input. Please enter a positive whole number.")
            continue

        previous_prime = find_previous_prime(number)
        next_prime = find_next_prime(number)
        prime_status = is_prime(number)

        print(f"\nResults for number {number}:")
        if previous_prime:
            print(f"a) The prime number before {number} is {previous_prime}.")
        else:
            print(f"a) There is no prime number before {number}.")

        if prime_status:
            print(f"b) {number} is a prime number.")
        else:
            divisors = get_divisors(number)
            print(f"b) {number} is not a prime number.")
            print(f"   Divisors of {number}: {divisors}")

        print(f"c) The next prime number after {number} is {next_prime}.")
        break

if __name__ == "__main__":
    main()