def solve(preorder: str) -> bool:
    slots = 1
    i = 0
    length = len(preorder)
    while i < length:
        if slots == 0:
            return False
        slots -= 1
        if preorder[i] != "#":
            slots += 2
        while i < length and preorder[i] != ",":
            i += 1
        i += 1
    return slots == 0
