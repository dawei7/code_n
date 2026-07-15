from typing import List


class Solution:
    def fairCandySwap(
        self, aliceSizes: List[int], bobSizes: List[int]
    ) -> List[int]:
        difference = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_boxes = set(bobSizes)
        for alice_box in aliceSizes:
            bob_box = alice_box - difference
            if bob_box in bob_boxes:
                return [alice_box, bob_box]
