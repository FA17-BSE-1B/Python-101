def fac(num):
    fac = 1
    for i in range(2, num+1):
        fac *= i
    return fac
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
combination = int(fac(n) / (fac(r) * fac(n-r)))
permutation = int(fac(n) / fac(n-r))
print("The combination of these values is:", combination)
print("The permutation of these values is:", permutation)

