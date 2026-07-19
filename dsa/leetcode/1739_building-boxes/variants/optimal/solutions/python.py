def solve(n: int) -> int:
    low, high = 0, n
    while low < high:
        middle = (low + high + 1) // 2
        boxes = middle * (middle + 1) * (middle + 2) // 6
        if boxes <= n:
            low = middle
        else:
            high = middle - 1

    height = low
    complete = height * (height + 1) * (height + 2) // 6
    remainder = n - complete

    low, high = 0, height + 1
    while low < high:
        middle = (low + high) // 2
        if middle * (middle + 1) // 2 >= remainder:
            high = middle
        else:
            low = middle + 1

    return height * (height + 1) // 2 + low
