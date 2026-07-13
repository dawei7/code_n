def solve(colors, needed_time):
    if not colors:
        return 0
    times = list(needed_time) + [0] * max(0, len(colors) - len(needed_time))
    total = 0
    group_sum = times[0]
    group_max = times[0]
    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]:
            group_sum += times[i]
            group_max = max(group_max, times[i])
        else:
            total += group_sum - group_max
            group_sum = times[i]
            group_max = times[i]
    total += group_sum - group_max
    return total
