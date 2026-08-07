from typing import List


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        modulo = 1_000_000_007
        full_or = 0
        for value in nums:
            full_or |= value

        bit_positions = [bit for bit in range(full_or.bit_length()) if full_or & (1 << bit)]
        state_count = 1 << len(bit_positions)
        subset_counts = [0] * state_count

        for value in nums:
            dense_mask = 0
            for dense_bit, original_bit in enumerate(bit_positions):
                if value & (1 << original_bit):
                    dense_mask |= 1 << dense_bit
            subset_counts[dense_mask] += 1

        half_block = 1
        while half_block < state_count:
            block = half_block << 1
            for start in range(0, state_count, block):
                upper = start + half_block
                for offset in range(half_block):
                    subset_counts[upper + offset] += subset_counts[start + offset]
            half_block = block

        powers_of_two = [1] * (len(nums) + 1)
        for exponent in range(1, len(nums) + 1):
            powers_of_two[exponent] = powers_of_two[exponent - 1] * 2 % modulo

        full_mask = state_count - 1
        answer = 0
        for missing_bits in range(1, state_count):
            allowed_bits = full_mask ^ missing_bits
            term = powers_of_two[subset_counts[allowed_bits]]
            if missing_bits.bit_count() & 1:
                answer += term
            else:
                answer -= term

        return answer % modulo
