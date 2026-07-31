def solve(s1: str, s2: str) -> int:
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    dp = [0] * (len(s2) + 1)
    for column, character in enumerate(s2, start=1):
        dp[column] = dp[column - 1] + ord(character)

    for first_character in s1:
        diagonal = dp[0]
        dp[0] += ord(first_character)

        for column, second_character in enumerate(s2, start=1):
            above = dp[column]
            if first_character == second_character:
                dp[column] = diagonal
            else:
                dp[column] = min(
                    above + ord(first_character),
                    dp[column - 1] + ord(second_character),
                )
            diagonal = above

    return dp[-1]
