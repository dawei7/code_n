def solve(firstString: str, secondString: str) -> int:
    first_occurrence = {}
    for index, character in enumerate(firstString):
        first_occurrence.setdefault(character, index)

    last_occurrence = {}
    for index, character in enumerate(secondString):
        last_occurrence[character] = index

    differences = [
        first_index - last_occurrence[character]
        for character, first_index in first_occurrence.items()
        if character in last_occurrence
    ]
    if not differences:
        return 0

    minimum = min(differences)
    return sum(difference == minimum for difference in differences)
