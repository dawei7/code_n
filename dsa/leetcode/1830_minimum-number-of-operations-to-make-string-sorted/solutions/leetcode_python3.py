class Solution:
    def makeStringSorted(self, s: str) -> int:
        modulus = 1_000_000_007
        length = len(s)

        factorial = [1] * (length + 1)
        for value in range(1, length + 1):
            factorial[value] = factorial[value - 1] * value % modulus

        inverse_factorial = [1] * (length + 1)
        inverse_factorial[length] = pow(
            factorial[length], modulus - 2, modulus
        )
        for value in range(length, 0, -1):
            inverse_factorial[value - 1] = (
                inverse_factorial[value] * value % modulus
            )

        frequencies = [0] * 26
        for character in s:
            frequencies[ord(character) - ord("a")] += 1

        denominator_inverse = 1
        for frequency in frequencies:
            denominator_inverse = (
                denominator_inverse * inverse_factorial[frequency] % modulus
            )

        operations = 0
        for index, character in enumerate(s):
            character_index = ord(character) - ord("a")
            smaller = sum(frequencies[:character_index])
            remaining = length - index
            operations += (
                smaller
                * factorial[remaining - 1]
                % modulus
                * denominator_inverse
            )
            operations %= modulus

            frequency = frequencies[character_index]
            denominator_inverse = (
                denominator_inverse * frequency % modulus
            )
            frequencies[character_index] -= 1

        return operations
