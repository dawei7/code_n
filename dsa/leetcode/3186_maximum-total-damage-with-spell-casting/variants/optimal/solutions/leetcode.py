from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damage_by_power = Counter(power)
        unique_powers = sorted(damage_by_power)
        best = [0] * (len(unique_powers) + 1)
        compatible_count = 0

        for index, value in enumerate(unique_powers):
            while unique_powers[compatible_count] < value - 2:
                compatible_count += 1

            take = value * damage_by_power[value] + best[compatible_count]
            best[index + 1] = max(best[index], take)

        return best[-1]
