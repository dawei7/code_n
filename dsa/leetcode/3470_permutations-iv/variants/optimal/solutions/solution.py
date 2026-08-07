class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        factorial = [1] * (n + 1)
        for value in range(2, n + 1):
            factorial[value] = factorial[value - 1] * value

        available = list(range(1, n + 1))
        odd_left = (n + 1) // 2
        even_left = n // 2
        rank = k - 1
        answer = []

        for position in range(n):
            selected = False
            for index, value in enumerate(available):
                parity = value & 1
                if answer and parity == (answer[-1] & 1):
                    continue
                if not answer and odd_left > even_left and parity == 0:
                    continue

                remaining_odds = odd_left - parity
                remaining_evens = even_left - (1 - parity)
                remaining = n - position - 1
                if parity:
                    required_evens = (remaining + 1) // 2
                    required_odds = remaining // 2
                else:
                    required_odds = (remaining + 1) // 2
                    required_evens = remaining // 2
                if remaining_odds != required_odds or remaining_evens != required_evens:
                    continue

                block = factorial[remaining_odds] * factorial[remaining_evens]
                if rank >= block:
                    rank -= block
                    continue

                answer.append(value)
                available.pop(index)
                odd_left = remaining_odds
                even_left = remaining_evens
                selected = True
                break

            if not selected:
                return []

        return answer
