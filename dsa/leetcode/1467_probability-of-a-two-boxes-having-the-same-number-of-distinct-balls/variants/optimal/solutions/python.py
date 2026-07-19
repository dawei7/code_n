from math import comb


def solve(balls):
    total = sum(balls)
    half = total // 2
    states = {(0, 0): 1}

    for count in balls:
        next_states = {}
        for (used, difference), ways in states.items():
            for take in range(count + 1):
                next_used = used + take
                if next_used > half:
                    break
                next_difference = difference + (take > 0) - (take < count)
                key = (next_used, next_difference)
                next_states[key] = next_states.get(key, 0) + ways * comb(count, take)
        states = next_states

    favorable = states.get((half, 0), 0)
    return favorable / comb(total, half)
