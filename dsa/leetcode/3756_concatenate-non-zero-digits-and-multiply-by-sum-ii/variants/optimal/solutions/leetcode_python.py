from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        modulo = 1_000_000_007
        nonzero_count = [0] * (len(s) + 1)
        prefix_value = [0]
        prefix_sum = [0]
        powers_of_ten = [1]

        for index, character in enumerate(s):
            nonzero_count[index + 1] = nonzero_count[index]
            if character != "0":
                digit = int(character)
                nonzero_count[index + 1] += 1
                prefix_value.append((prefix_value[-1] * 10 + digit) % modulo)
                prefix_sum.append(prefix_sum[-1] + digit)
                powers_of_ten.append((powers_of_ten[-1] * 10) % modulo)

        answer = []
        for left, right in queries:
            compressed_left = nonzero_count[left]
            compressed_right = nonzero_count[right + 1]
            length = compressed_right - compressed_left
            value = (
                prefix_value[compressed_right]
                - prefix_value[compressed_left] * powers_of_ten[length]
            ) % modulo
            digit_sum = prefix_sum[compressed_right] - prefix_sum[compressed_left]
            answer.append(value * digit_sum % modulo)

        return answer
