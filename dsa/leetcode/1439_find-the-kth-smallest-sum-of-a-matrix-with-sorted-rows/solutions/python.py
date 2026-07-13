import heapq


def solve(mat, k):
    sums = [0]
    for row in mat:
        if not isinstance(row, list):
            row = [row]
        row = sorted(row)
        merged = []
        for base in sums:
            for value in row:
                merged.append(base + value)
        sums = heapq.nsmallest(max(1, k), merged)
    return sorted(sums)[max(0, min(k, len(sums)) - 1)] if sums else 0
