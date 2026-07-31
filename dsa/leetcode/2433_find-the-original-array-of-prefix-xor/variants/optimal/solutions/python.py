def solve(pref: list[int]) -> list[int]:
    original = [pref[0]]
    for index in range(1, len(pref)):
        original.append(pref[index - 1] ^ pref[index])
    return original
