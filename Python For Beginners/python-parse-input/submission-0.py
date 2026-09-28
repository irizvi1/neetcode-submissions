from typing import List

def read_integers() -> List[int]:
    user = str(input())
    list1 = user.split(',') 
    list2= []
    for num in list1:
        list2.append(int(num))
    return list2


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
