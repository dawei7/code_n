"""Optimal solution for greedy_13: Stable Marriage (Gale-Shapley).

Each free man proposes to his next-best. The woman accepts
iff she prefers him to her current match.
"""


def solve(n, men_prefs, women_prefs):
    if n == 0:
        return []
    next_w = [0] * n
    woman_engaged_to = [-1] * n
    man_engaged_to = [-1] * n
    woman_rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for rank, m in enumerate(women_prefs[w]):
            woman_rank[w][m] = rank
    free_men = list(range(n))
    while free_men:
        m = free_men.pop(0)
        w = men_prefs[m][next_w[m]]
        next_w[m] += 1
        if woman_engaged_to[w] == -1:
            woman_engaged_to[w] = m
            man_engaged_to[m] = w
        else:
            current = woman_engaged_to[w]
            if woman_rank[w][m] < woman_rank[w][current]:
                woman_engaged_to[w] = m
                man_engaged_to[m] = w
                man_engaged_to[current] = -1
                free_men.append(current)
            else:
                free_men.insert(0, m)
    return man_engaged_to
