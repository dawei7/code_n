def solve(nums: list[int], and_values: list[int]) -> int:
    infinity = 10**30
    states = {(0, -1): 0}

    for value in nums:
        next_states = {}
        for (segment, current_and), cost in states.items():
            if segment == len(and_values):
                continue

            current_and &= value
            target = and_values[segment]
            if current_and & target != target:
                continue

            state = (segment, current_and)
            next_states[state] = min(
                next_states.get(state, infinity),
                cost,
            )

            if current_and == target:
                state = (segment + 1, -1)
                next_states[state] = min(
                    next_states.get(state, infinity),
                    cost + value,
                )

        states = next_states

    return states.get((len(and_values), -1), -1)
