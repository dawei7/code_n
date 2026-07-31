class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        answer = -n

        for odd_digit in "01234":
            for even_digit in "01234":
                if odd_digit == even_digit:
                    continue

                odd_prefix = [0] * (n + 1)
                even_prefix = [0] * (n + 1)
                for index, digit in enumerate(s, 1):
                    odd_prefix[index] = odd_prefix[index - 1] + (digit == odd_digit)
                    even_prefix[index] = even_prefix[index - 1] + (digit == even_digit)

                infinity = n + 1
                best_prefix = [[infinity, infinity], [infinity, infinity]]
                left = 0

                for right in range(k, n + 1):
                    while (
                        left <= right - k
                        and even_prefix[left] <= even_prefix[right] - 2
                    ):
                        odd_parity = odd_prefix[left] & 1
                        even_parity = even_prefix[left] & 1
                        difference = odd_prefix[left] - even_prefix[left]
                        best_prefix[odd_parity][even_parity] = min(
                            best_prefix[odd_parity][even_parity], difference
                        )
                        left += 1

                    needed_odd_parity = 1 - (odd_prefix[right] & 1)
                    needed_even_parity = even_prefix[right] & 1
                    smallest = best_prefix[needed_odd_parity][needed_even_parity]
                    if smallest != infinity:
                        answer = max(
                            answer,
                            odd_prefix[right] - even_prefix[right] - smallest,
                        )

        return answer
