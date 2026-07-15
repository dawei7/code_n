"""Optimal app-local solution for LeetCode 925."""


def solve(name, typed):
    name_index = 0
    for typed_index, character in enumerate(typed):
        if name_index < len(name) and character == name[name_index]:
            name_index += 1
        elif typed_index == 0 or character != typed[typed_index - 1]:
            return False
    return name_index == len(name)
