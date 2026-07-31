def solve(coordinate1: str, coordinate2: str) -> bool:
    first_color = (ord(coordinate1[0]) - ord("a") + int(coordinate1[1])) % 2
    second_color = (ord(coordinate2[0]) - ord("a") + int(coordinate2[1])) % 2
    return first_color == second_color
