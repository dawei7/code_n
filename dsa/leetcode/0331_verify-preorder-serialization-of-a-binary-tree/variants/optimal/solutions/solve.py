def solve(preorder: str) -> bool:
    slots = 1
    index = 0
    length = len(preorder)
    while index < length:
        if slots == 0:
            return False
        slots -= 1
        if preorder[index] != "#":
            slots += 2
        while index < length and preorder[index] != ",":
            index += 1
        index += 1
    return slots == 0
