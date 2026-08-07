from typing import List


class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        energy_training = max(0, sum(energy) + 1 - initialEnergy)
        experience_training = 0
        current_experience = initialExperience

        for opponent_experience in experience:
            if current_experience <= opponent_experience:
                needed = opponent_experience + 1 - current_experience
                experience_training += needed
                current_experience += needed
            current_experience += opponent_experience

        return energy_training + experience_training
