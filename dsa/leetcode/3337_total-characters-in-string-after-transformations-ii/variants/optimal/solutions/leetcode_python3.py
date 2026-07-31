from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 1_000_000_007
        alphabet_size = 26

        def multiply_matrices(left, right):
            product = [[0] * alphabet_size for _ in range(alphabet_size)]
            for source in range(alphabet_size):
                product_row = product[source]
                for middle, left_value in enumerate(left[source]):
                    if left_value == 0:
                        continue
                    for destination, right_value in enumerate(right[middle]):
                        product_row[destination] = (product_row[destination] + left_value * right_value) % mod
            return product

        def multiply_vector(vector, matrix):
            product = [0] * alphabet_size
            for source, count in enumerate(vector):
                if count == 0:
                    continue
                for destination, ways in enumerate(matrix[source]):
                    product[destination] = (product[destination] + count * ways) % mod
            return product

        transition = [[0] * alphabet_size for _ in range(alphabet_size)]
        for source, length in enumerate(nums):
            for shift in range(1, length + 1):
                transition[source][(source + shift) % alphabet_size] = 1

        counts = [0] * alphabet_size
        for char in s:
            counts[ord(char) - ord("a")] += 1

        while t > 0:
            if t & 1:
                counts = multiply_vector(counts, transition)
            transition = multiply_matrices(transition, transition)
            t >>= 1

        return sum(counts) % mod
