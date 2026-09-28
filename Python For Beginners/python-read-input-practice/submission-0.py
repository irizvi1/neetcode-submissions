def add_two_numbers() -> int:
    list = []
    sum = 0
    user = str(input())
    list = user.split(",")
    for num in list:
        sum += int(num)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
