class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        moduli = (1_000_000_007, 1_000_000_009)
        base = 911_382_323
        n = len(text)
        powers = [[1] * (n + 1) for _ in moduli]
        prefixes = [[0] * (n + 1) for _ in moduli]

        for index, character in enumerate(text):
            value = ord(character) - ord("a") + 1
            for table, modulus in enumerate(moduli):
                powers[table][index + 1] = powers[table][index] * base % modulus
                prefixes[table][index + 1] = (
                    prefixes[table][index] * base + value
                ) % modulus

        def range_hash(table: int, left: int, right: int) -> int:
            modulus = moduli[table]
            return (
                prefixes[table][right]
                - prefixes[table][left] * powers[table][right - left]
            ) % modulus

        echoes = set()
        for half_length in range(1, n // 2 + 1):
            full_length = 2 * half_length
            for start in range(n - full_length + 1):
                middle = start + half_length
                end = start + full_length
                first = (
                    range_hash(0, start, middle),
                    range_hash(1, start, middle),
                )
                second = (
                    range_hash(0, middle, end),
                    range_hash(1, middle, end),
                )
                if first == second:
                    echoes.add((half_length, *first))

        return len(echoes)
