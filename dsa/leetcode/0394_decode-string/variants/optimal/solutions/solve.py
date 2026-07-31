"""Optimal app-local solution for LeetCode 394: Decode String."""


def solve(s: str) -> str:
    stack: list[tuple[list[str], int]] = []
    chunks: list[str] = []
    repeat = 0

    for character in s:
        if character.isdigit():
            repeat = repeat * 10 + int(character)
        elif character == "[":
            stack.append((chunks, repeat))
            chunks = []
            repeat = 0
        elif character == "]":
            decoded_group = "".join(chunks)
            parent_chunks, group_repeat = stack.pop()
            parent_chunks.append(decoded_group * group_repeat)
            chunks = parent_chunks
        else:
            chunks.append(character)

    return "".join(chunks)
