def solve(s: str) -> str:
    partner = [-1] * len(s)
    openings = []

    for index, character in enumerate(s):
        if character == "(":
            openings.append(index)
        elif character == ")":
            opening = openings.pop()
            partner[opening] = index
            partner[index] = opening

    answer = []
    index = 0
    direction = 1
    while 0 <= index < len(s):
        if s[index] in "()":
            index = partner[index]
            direction = -direction
        else:
            answer.append(s[index])
        index += direction

    return "".join(answer)
