class Solution:
    def knightDialer(self, n: int) -> int:
        modulus = 1_000_000_007
        moves = ((4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4))
        transition = [[0] * 10 for _ in range(10)]
        for source, destinations in enumerate(moves):
            for destination in destinations:
                transition[destination][source] = 1

        def multiply(left, right):
            product = [[0] * 10 for _ in range(10)]
            for row in range(10):
                for middle in range(10):
                    if left[row][middle] == 0:
                        continue
                    for column in range(10):
                        product[row][column] = (product[row][column] + left[row][middle] * right[middle][column]) % modulus
            return product

        def apply(matrix, vector):
            return [sum(matrix[row][column] * vector[column] for column in range(10)) % modulus for row in range(10)]

        counts = [1] * 10
        exponent = n - 1
        while exponent:
            if exponent & 1:
                counts = apply(transition, counts)
            transition = multiply(transition, transition)
            exponent //= 2
        return sum(counts) % modulus
