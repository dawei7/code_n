def solve(s: str) -> int:
    segments = 0
    for i, c in enumerate(s):
        if c != " " and (i == 0 or s[i - 1] == " "):
            segments += 1
    return segments
