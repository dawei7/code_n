from typing import List


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        scale = 1000
        fraction_counts = [0] * scale
        floor_sum = 0
        floor_error = 0
        non_integer_count = 0

        for price in prices:
            whole_text, fraction_text = price.split(".")
            whole = int(whole_text)
            fraction = int(fraction_text)
            floor_sum += whole
            floor_error += fraction
            if fraction:
                fraction_counts[fraction] += 1
                non_integer_count += 1

        round_up_needed = target - floor_sum
        if round_up_needed < 0 or round_up_needed > non_integer_count:
            return "-1"

        error = floor_error
        for fraction in range(scale - 1, 0, -1):
            take = min(round_up_needed, fraction_counts[fraction])
            error += take * (scale - 2 * fraction)
            round_up_needed -= take
            if round_up_needed == 0:
                break

        return f"{error // scale}.{error % scale:03d}"
