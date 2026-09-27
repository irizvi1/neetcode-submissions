def concatenate(s1: str, s2: str) -> str:
    new = ""
    for i in range(len(s1)):
        new = new + s1[i]
    for i in range(len(s2)):
        new = new + s2[i]
    if len(new) > 10:
        return "Too long!"
    return new





# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
