def _remove_duplicate_letters(s: str) -> str:
    last_index = {letter: index for index, letter in enumerate(s)}
    stack: list[str] = []
    selected: set[str] = set()

    for index, letter in enumerate(s):
        if letter in selected:
            continue
        while stack and letter < stack[-1] and last_index[stack[-1]] > index:
            selected.remove(stack.pop())
        stack.append(letter)
        selected.add(letter)

    return "".join(stack)


def solve(s: str) -> str:
    return _remove_duplicate_letters(s)
