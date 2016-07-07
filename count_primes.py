def primes(count):
    """Return count number of prime numbers, starting at 2."""
    list_of_primes = []
#contains count number of primes
    current_count_of_primes = len(list_of_primes)
    n = 2
    while current_count_of_primes != count:
        number_range = range(2, (n/2) + 1)
        for i in number_range:
            if n % i == 0:
                break
            else:
                list_of_primes.append(n)
        n = n + 1
    return list_of_primes


print primes(5)

#numbers only divisible by half of self or less (we can check for prime numbers within this range)
#these prime numbers should already be in our list_of_primes