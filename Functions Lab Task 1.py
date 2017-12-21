def fac(num):
        fac = 1
        for i in range(2, num+1):
            fac *= i
        return fac
    num = int(input("Enter a number: "))
    print(fac(num))
