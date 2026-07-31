class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        modulus = 1_000_000_007
        limit = min(n, x)

        stirling = [0] * (limit + 1)
        stirling[0] = 1
        for performers in range(1, n + 1):
            for bands in range(min(performers, limit), 0, -1):
                stirling[bands] = (stirling[bands - 1] + bands * stirling[bands]) % modulus
            stirling[0] = 0

        answer = 0
        stage_choices = 1
        score_choices = 1
        for bands in range(1, limit + 1):
            stage_choices = stage_choices * (x - bands + 1) % modulus
            score_choices = score_choices * y % modulus
            answer = (answer + stirling[bands] * stage_choices * score_choices) % modulus

        return answer
