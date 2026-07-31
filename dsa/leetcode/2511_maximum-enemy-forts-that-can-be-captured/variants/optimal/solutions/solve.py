def solve(forts):
    best = 0
    previous = -1

    for index, value in enumerate(forts):
        if value == 0:
            continue
        if previous != -1 and value != forts[previous]:
            best = max(best, index - previous - 1)
        previous = index

    return best
