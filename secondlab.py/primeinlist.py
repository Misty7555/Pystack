list1 = [1, 2, 3, 4, 5, 6]

for n in list1:
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
