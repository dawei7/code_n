"""Optimal app-local solution for LeetCode 1147."""

BASE = 911_382_323
MODULI = (1_000_000_007, 1_000_000_009)


def solve(text: str) -> int:
    left = 0
    right = len(text) - 1
    chunk_left = 0
    left_hashes = [0, 0]
    right_hashes = [0, 0]
    powers = [1, 1]
    pending_length = 0
    chunks = 0

    while left < right:
        left_code = ord(text[left]) - ord("a") + 1
        right_code = ord(text[right]) - ord("a") + 1
        pending_length += 1
        for position, modulus in enumerate(MODULI):
            left_hashes[position] = (left_hashes[position] * BASE + left_code) % modulus
            right_hashes[position] = (
                right_code * powers[position] + right_hashes[position]
            ) % modulus

        hashes_match = left_hashes == right_hashes
        characters_match = hashes_match and all(
            text[chunk_left + offset] == text[right + offset]
            for offset in range(pending_length)
        )
        if characters_match:
            chunks += 2
            chunk_left = left + 1
            left_hashes = [0, 0]
            right_hashes = [0, 0]
            powers = [1, 1]
            pending_length = 0
        else:
            for position, modulus in enumerate(MODULI):
                powers[position] = powers[position] * BASE % modulus

        left += 1
        right -= 1

    if left == right or pending_length:
        chunks += 1
    return chunks
