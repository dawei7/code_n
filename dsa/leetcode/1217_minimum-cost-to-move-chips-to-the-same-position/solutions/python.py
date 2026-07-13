def solve(position):
    odd = sum(value % 2 for value in position)
    return min(odd, len(position) - odd)
