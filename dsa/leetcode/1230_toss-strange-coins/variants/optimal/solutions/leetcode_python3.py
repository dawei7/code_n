from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        probabilities = [0.0] * (target + 1)
        probabilities[0] = 1.0

        for processed, head_probability in enumerate(prob, 1):
            for heads in range(min(target, processed), 0, -1):
                probabilities[heads] = (
                    probabilities[heads] * (1.0 - head_probability)
                    + probabilities[heads - 1] * head_probability
                )
            probabilities[0] *= 1.0 - head_probability
        return probabilities[target]
