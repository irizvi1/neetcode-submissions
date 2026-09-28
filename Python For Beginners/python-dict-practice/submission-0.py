from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    map = {}

    for i in range(len(word)):
        map[word[i]] = map.get(word[i], 0) + 1
    return map




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
