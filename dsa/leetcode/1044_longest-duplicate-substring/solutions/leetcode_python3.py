class Solution:
    def longestDupSubstring(self, s: str) -> str:
        modulus_one = 1_000_000_007
        modulus_two = 1_000_000_009
        base = 27
        values = [ord(character) - 96 for character in s]
        string_length = len(s)

        def duplicate_start(length: int) -> int:
            hash_one = 0
            hash_two = 0
            for value in values[:length]:
                hash_one = (hash_one * base + value) % modulus_one
                hash_two = (hash_two * base + value) % modulus_two

            power_one = pow(base, length, modulus_one)
            power_two = pow(base, length, modulus_two)
            starts_by_hash = {(hash_one, hash_two): [0]}

            for start in range(1, string_length - length + 1):
                outgoing = values[start - 1]
                incoming = values[start + length - 1]
                hash_one = (
                    hash_one * base - outgoing * power_one + incoming
                ) % modulus_one
                hash_two = (
                    hash_two * base - outgoing * power_two + incoming
                ) % modulus_two
                key = (hash_one, hash_two)

                for previous in starts_by_hash.get(key, ()):
                    if s[previous : previous + length] == s[start : start + length]:
                        return start
                starts_by_hash.setdefault(key, []).append(start)

            return -1

        low = 1
        high = string_length - 1
        best_start = 0
        best_length = 0

        while low <= high:
            length = (low + high) // 2
            start = duplicate_start(length)
            if start >= 0:
                best_start = start
                best_length = length
                low = length + 1
            else:
                high = length - 1

        return s[best_start : best_start + best_length]

