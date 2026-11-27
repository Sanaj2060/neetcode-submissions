from typing import List

def read_integers() -> List[int]:
    inp = input().split(",")
    for i in range(len(inp)):
        inp[i] = int(inp[i])
    return inp

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
