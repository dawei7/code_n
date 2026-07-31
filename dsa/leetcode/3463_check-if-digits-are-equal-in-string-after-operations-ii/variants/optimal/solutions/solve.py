def solve(s: str) -> bool:
    steps = len(s) - 2
    choose_mod_five = (
        (1, 0, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (1, 2, 1, 0, 0),
        (1, 3, 3, 1, 0),
        (1, 4, 1, 4, 1),
    )

    def binomial_mod_five(total: int, selected: int) -> int:
        result = 1
        while total or selected:
            top = total % 5
            bottom = selected % 5
            if bottom > top:
                return 0
            result = result * choose_mod_five[top][bottom] % 5
            total //= 5
            selected //= 5
        return result

    difference = 0
    for index in range(steps + 1):
        mod_two = int((index & (steps - index)) == 0)
        mod_five = binomial_mod_five(steps, index)
        coefficient = mod_five if mod_five % 2 == mod_two else mod_five + 5
        difference = (difference + coefficient * (ord(s[index]) - ord(s[index + 1]))) % 10
    return difference == 0
