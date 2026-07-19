class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        length = len(s)
        base = 911_382_323
        moduli = (1_000_000_007, 1_000_000_009)
        powers = [[1] * (length + 1) for _ in moduli]
        prefixes = [[0] * (length + 1) for _ in moduli]

        for modulus_index, modulus in enumerate(moduli):
            for index, character in enumerate(s):
                powers[modulus_index][index + 1] = (
                    powers[modulus_index][index] * base % modulus
                )
                prefixes[modulus_index][index + 1] = (
                    prefixes[modulus_index][index] * base + ord(character)
                ) % modulus

        def window_hash(start: int, window_length: int):
            end = start + window_length
            return tuple(
                (
                    prefixes[modulus_index][end]
                    - prefixes[modulus_index][start]
                    * powers[modulus_index][window_length]
                )
                % modulus
                for modulus_index, modulus in enumerate(moduli)
            )

        def has_repeat(window_length: int) -> bool:
            starts_by_hash = {}
            for start in range(length - window_length + 1):
                signature = window_hash(start, window_length)
                for previous in starts_by_hash.get(signature, []):
                    if s[previous : previous + window_length] == s[
                        start : start + window_length
                    ]:
                        return True
                starts_by_hash.setdefault(signature, []).append(start)
            return False

        low = 0
        high = length - 1
        while low < high:
            middle = (low + high + 1) // 2
            if has_repeat(middle):
                low = middle
            else:
                high = middle - 1
        return low
