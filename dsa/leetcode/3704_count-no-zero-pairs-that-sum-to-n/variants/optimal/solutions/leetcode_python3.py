class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = [int(digit) for digit in reversed(str(n))]
        digits.append(0)

        states = {(0, True, True): 1}

        for position, target_digit in enumerate(digits):
            next_states: dict[tuple[int, bool, bool], int] = {}

            for (carry, a_active, b_active), ways in states.items():
                a_digits = range(1, 10) if position == 0 else range(10)
                b_digits = range(1, 10) if position == 0 else range(10)

                if not a_active:
                    a_digits = (0,)
                if not b_active:
                    b_digits = (0,)

                for a_digit in a_digits:
                    for b_digit in b_digits:
                        digit_sum = a_digit + b_digit + carry
                        if digit_sum % 10 != target_digit:
                            continue

                        state = (
                            digit_sum // 10,
                            a_active and a_digit != 0,
                            b_active and b_digit != 0,
                        )
                        next_states[state] = next_states.get(state, 0) + ways

            states = next_states

        return states.get((0, False, False), 0)
