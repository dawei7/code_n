"""Optimal solution for sort_13: Tim Sort (Simplified).

Identify natural runs, extend to minrun, merge pairwise.
"""


def solve(data, n):
    if n <= 1:
        return data
    work = list(data)
    RUN = max(1, min(32, n // 4))
    runs = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and work[j] >= work[j - 1]:
            j += 1
        runs.append((i, j))
        if j - i < RUN:
            end = min(i + RUN, n)
            sub = work[i:end]
            sub.sort()
            work[i:end] = sub
            j = end
            runs[-1] = (runs[-1][0], j)  # update with extended end
        i = j
    while len(runs) > 1:
        new_runs = []
        for k in range(0, len(runs), 2):
            if k + 1 < len(runs):
                lo1, hi1 = runs[k]
                lo2, hi2 = runs[k + 1]
                merged = []
                a, b = lo1, lo2
                while a < hi1 and b < hi2:
                    if work[a] <= work[b]:
                        merged.append(work[a])
                        a += 1
                    else:
                        merged.append(work[b])
                        b += 1
                merged.extend(work[a:hi1])
                merged.extend(work[b:hi2])
                work[lo1:hi2] = merged
                new_runs.append((lo1, hi2))
            else:
                new_runs.append(runs[k])
        runs = new_runs
    return work
