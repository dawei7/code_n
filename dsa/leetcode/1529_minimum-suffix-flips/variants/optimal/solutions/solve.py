def solve(target):
    flips = 0
    current = "0"
    for bit in target:
        if bit != current:
            flips += 1
            current = bit
    return flips
