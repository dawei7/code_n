from typing import List


class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        monster_rewards = sorted(zip(monsters, coins))
        answers = [0] * len(heroes)
        monster_index = 0
        collected = 0

        for hero_power, hero_index in sorted((power, index) for index, power in enumerate(heroes)):
            while monster_index < len(monster_rewards) and monster_rewards[monster_index][0] <= hero_power:
                collected += monster_rewards[monster_index][1]
                monster_index += 1
            answers[hero_index] = collected

        return answers
