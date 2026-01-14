print("Enter first number:" )
num1 = int(input())
print("Enter second number:" )
num2 = int(input())
def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def compute_lcm(a, b):
    return (a * b) / compute_gcd(a, b)
gcd = compute_gcd(num1, num2)
lcm = compute_lcm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
print("LCM of", num1, "and", num2, "is:", lcm)