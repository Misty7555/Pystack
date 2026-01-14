print("Enter the range :")
low = int(input("Low: "))
high = int(input("High: "))
def primerange(low, high):
    primes = []
    for num in range(low, high + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
prime_numbers = primerange(low, high)
print("Prime numbers between", low, "and", high, "are:", prime_numbers)