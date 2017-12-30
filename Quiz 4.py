name = input("Enter the name of the student: ")
marks = int(input("Enter the marks of the student: "))
topperlist = []
highest = marks
topperlist.append(name)
topperlist.append(marks)
for i in range(10):
    name = input("Enter the name of the student: ")
    marks = int(input("Enter the marks of the student: "))
    if marks > highest:
        topperlist = []
        highest = marks
        topperlist.append(name)
        topperlist.append(marks)
    elif marks == highest:
            highest = marks
            topperlist.append(name)
            topperlist.append(marks)
for x in topperlist:
    print(x)
