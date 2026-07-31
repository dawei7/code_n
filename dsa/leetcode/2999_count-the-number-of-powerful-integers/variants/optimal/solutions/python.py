def solve(start, finish, limit, s):
    suffix = int(s)
    place = 10 ** len(s)

    def count(bound):
        if bound < suffix:
            return 0

        maximum_prefix = (bound - suffix) // place
        digits = str(maximum_prefix)
        total = 0

        for index, character in enumerate(digits):
            digit = int(character)
            remaining = len(digits) - index - 1
            total += min(digit, limit + 1) * (limit + 1) ** remaining
            if digit > limit:
                return total

        return total + 1

    return count(finish) - count(start - 1)
