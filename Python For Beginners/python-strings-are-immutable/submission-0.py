def remove_fourth_character(word: str) -> str:
    new = ''
    new = new + word[:3]
    new = new + word[4:len(word)]
    return new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
