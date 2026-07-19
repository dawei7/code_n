def solve(colors: str) -> bool:
    alice_moves = 0
    bob_moves = 0

    for index in range(1, len(colors) - 1):
        if colors[index - 1] == colors[index] == colors[index + 1]:
            if colors[index] == "A":
                alice_moves += 1
            else:
                bob_moves += 1

    return alice_moves > bob_moves
