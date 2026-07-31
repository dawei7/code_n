def solve(num1: int, num2: int) -> int:
    def total_through(bound: int) -> int:
        if bound <= 0:
            return 0

        states = {(False, -1, -1, True): (1, 0)}
        for bound_digit in map(int, str(bound)):
            next_states: dict[tuple[bool, int, int, bool], tuple[int, int]] = {}
            for (started, older, previous, tight), (ways, waves) in states.items():
                limit = bound_digit if tight else 9
                for digit in range(limit + 1):
                    next_tight = tight and digit == limit
                    if not started and digit == 0:
                        state = (False, -1, -1, next_tight)
                        added = 0
                    else:
                        state = (True, previous, digit, next_tight)
                        added = int(
                            started
                            and older != -1
                            and (previous - older) * (previous - digit) > 0
                        )
                    old_ways, old_waves = next_states.get(state, (0, 0))
                    next_states[state] = (
                        old_ways + ways,
                        old_waves + waves + added * ways,
                    )
            states = next_states
        return sum(waves for ways, waves in states.values())

    return total_through(num2) - total_through(num1 - 1)
