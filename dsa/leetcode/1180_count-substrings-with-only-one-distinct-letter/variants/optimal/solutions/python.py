def solve(s: str) -> int:
    total = 0
    run_length = 0
    previous = ""

    for character in s:
        if character == previous:
            run_length += 1
        else:
            previous = character
            run_length = 1
        total += run_length

    return total
