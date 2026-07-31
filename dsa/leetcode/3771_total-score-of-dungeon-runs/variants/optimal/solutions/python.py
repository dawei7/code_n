def solve(hp: int, damage: list[int], requirement: list[int]) -> int:
    prefixes = [0]
    cumulative_damage = 0
    score_total = 0

    for loss, minimum_health in zip(damage, requirement):
        cumulative_damage += loss
        target = cumulative_damage + minimum_health - hp

        low = 0
        high = len(prefixes)
        while low < high:
            middle = (low + high) // 2
            if prefixes[middle] < target:
                low = middle + 1
            else:
                high = middle

        score_total += len(prefixes) - low
        prefixes.append(cumulative_damage)

    return score_total
