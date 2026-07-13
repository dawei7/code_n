def solve(skill: list[int], mana: list[int]) -> int:
    prefix = [0]
    for value in skill:
        prefix.append(prefix[-1] + value)

    start = 0
    previous_mana = mana[0]
    total_skill = prefix[-1]
    for current_mana in mana[1:]:
        next_start = 0
        for wizard in range(len(skill)):
            previous_done = start + previous_mana * prefix[wizard + 1]
            current_arrival = current_mana * prefix[wizard]
            if previous_done - current_arrival > next_start:
                next_start = previous_done - current_arrival
        start = next_start
        previous_mana = current_mana

    return start + previous_mana * total_skill
