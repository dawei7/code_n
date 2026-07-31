def solve(s: str) -> int:
    characters = list(s)
    left = 0
    right = len(characters) - 1
    moves = 0

    while left < right:
        match = right
        while match > left and characters[match] != characters[left]:
            match -= 1

        if match == left:
            characters[left], characters[left + 1] = (
                characters[left + 1],
                characters[left],
            )
            moves += 1
        else:
            while match < right:
                characters[match], characters[match + 1] = (
                    characters[match + 1],
                    characters[match],
                )
                match += 1
                moves += 1
            left += 1
            right -= 1

    return moves
