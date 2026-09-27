def say_goodbye(name: str, hour: int) -> str:
    new = "Goodbye, " + name + ". See you again at " + str(hour) + " o'clock."
    return new


# do not modify below this line
print(say_goodbye("Bob", 12))
print(say_goodbye("Jane", 4))
print(say_goodbye("NeetCode", 9))
