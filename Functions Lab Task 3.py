def listsum(num):
        n_sum = 0
        for i in num:
            n_sum += i
        return n_sum
    num = []
    for i in range(5):
        num.append(int(input("Enter a number: ")))
    print(listsum(num))
