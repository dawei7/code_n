def solve(s, indices):
    shuffled = [""] * len(s)
    for character, destination in zip(s, indices):
        shuffled[destination] = character
    return "".join(shuffled)
