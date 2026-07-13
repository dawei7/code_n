from bisect import bisect_right


def solve(arr1, arr2):
    candidates = sorted(set(arr2))
    states = {-1: 0}
    for value in arr1:
        next_states = {}
        for previous, operations in states.items():
            if value > previous:
                next_states[value] = min(next_states.get(value, float("inf")), operations)
            index = bisect_right(candidates, previous)
            if index < len(candidates):
                replacement = candidates[index]
                next_states[replacement] = min(next_states.get(replacement, float("inf")), operations + 1)
        states = next_states
        if not states:
            return -1
    return min(states.values())
