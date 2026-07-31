def solve(n: int, edges: list[list[int]]) -> int:
    has_stronger_team = [False] * n
    for _, weaker in edges:
        has_stronger_team[weaker] = True

    champion = -1
    for team, has_stronger in enumerate(has_stronger_team):
        if not has_stronger:
            if champion != -1:
                return -1
            champion = team

    return champion
