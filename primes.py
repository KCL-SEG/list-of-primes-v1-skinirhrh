"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    if num == 2 or num ==3:
        return True
    for i in range (2, num - 1):
        if num % i == 0:
            return False
    return True



def primes(number_of_primes):
    list = []
    i=2
    while len(list) < number_of_primes:
        if isPrime(i):
            list.append(i)
        i += 1
    return list
