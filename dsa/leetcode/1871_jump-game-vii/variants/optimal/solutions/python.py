def solve(s: str, min_jump: int, max_jump: int) -> bool:
    reachable = [False] * len(s)
    reachable[0] = True
    window_reachable = 0

    for index in range(1, len(s)):
        entering = index - min_jump
        if entering >= 0:
            window_reachable += reachable[entering]

        leaving = index - max_jump - 1
        if leaving >= 0:
            window_reachable -= reachable[leaving]

        reachable[index] = s[index] == "0" and window_reachable > 0

    return reachable[-1]
