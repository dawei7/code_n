def solve(num: str, change: list[int]) -> str:
    digits = list(num)
    mutating = False

    for index, character in enumerate(digits):
        digit = int(character)
        replacement = change[digit]

        if replacement > digit:
            digits[index] = str(replacement)
            mutating = True
        elif replacement < digit and mutating:
            break

    return "".join(digits)
