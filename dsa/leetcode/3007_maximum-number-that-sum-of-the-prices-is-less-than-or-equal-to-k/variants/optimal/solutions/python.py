def solve(k, x):
    def accumulated(number):
        total = 0
        position = x

        while 1 << (position - 1) <= number:
            half = 1 << (position - 1)
            cycle = half << 1
            total += (number + 1) // cycle * half
            total += max(0, (number + 1) % cycle - half)
            position += x

        return total

    lower = 0
    upper = 1
    while accumulated(upper) <= k:
        upper *= 2

    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if accumulated(middle) <= k:
            lower = middle
        else:
            upper = middle

    return lower
