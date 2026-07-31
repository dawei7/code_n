from collections import Counter


def solve(s: str) -> int:
    frequencies = [0] * 26
    for character, frequency in Counter(s).items():
        frequencies[ord(character) - ord("a")] = frequency

    answer = len(s)
    for target in range(1, max(frequencies) + 1):
        dp = [float("inf")] * 27
        dp[0] = 0

        for index in range(26):
            frequency = frequencies[index]
            individual_cost = min(
                frequency,
                abs(frequency - target),
            )
            dp[index + 1] = min(
                dp[index + 1],
                dp[index] + individual_cost,
            )

            if index == 25:
                continue

            next_frequency = frequencies[index + 1]
            pair_cost = float("inf")
            for current_goal in (0, target):
                for next_goal in (0, target):
                    surplus = max(frequency - current_goal, 0)
                    deficit = max(next_goal - next_frequency, 0)
                    cost = abs(frequency - current_goal) + abs(next_frequency - next_goal) - min(surplus, deficit)
                    pair_cost = min(pair_cost, cost)

            dp[index + 2] = min(
                dp[index + 2],
                dp[index] + pair_cost,
            )

        answer = min(answer, dp[26])

    return answer
