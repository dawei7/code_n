def solve(s: str, k: int, letter: str, repetition: int) -> str:
    remaining_letter = s.count(letter)
    selected_letter = 0
    stack: list[str] = []

    for index, character in enumerate(s):
        while (
            stack
            and character < stack[-1]
            and len(stack) - 1 + len(s) - index >= k
            and (
                stack[-1] != letter
                or selected_letter - 1 + remaining_letter >= repetition
            )
        ):
            removed = stack.pop()
            if removed == letter:
                selected_letter -= 1

        if len(stack) < k:
            if character == letter:
                stack.append(character)
                selected_letter += 1
            elif k - len(stack) > repetition - selected_letter:
                stack.append(character)

        if character == letter:
            remaining_letter -= 1

    return "".join(stack)
