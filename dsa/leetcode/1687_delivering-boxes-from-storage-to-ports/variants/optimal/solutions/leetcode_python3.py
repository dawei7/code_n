from collections import deque
from typing import List


class Solution:
    def boxDelivering(
        self,
        boxes: List[List[int]],
        portsCount: int,
        maxBoxes: int,
        maxWeight: int,
    ) -> int:
        n = len(boxes)
        weight_prefix = [0] * (n + 1)
        port_changes = [0] * n
        for index, (port, weight) in enumerate(boxes):
            weight_prefix[index + 1] = weight_prefix[index] + weight
            if index > 0:
                port_changes[index] = port_changes[index - 1] + (
                    port != boxes[index - 1][0]
                )

        minimum_trips = [0] * (n + 1)
        candidates = deque([0])

        for delivered in range(1, n + 1):
            while candidates and (
                delivered - candidates[0] > maxBoxes
                or weight_prefix[delivered] - weight_prefix[candidates[0]]
                > maxWeight
            ):
                candidates.popleft()

            start = candidates[0]
            minimum_trips[delivered] = (
                port_changes[delivered - 1]
                + minimum_trips[start]
                - port_changes[start]
                + 2
            )

            if delivered < n:
                candidate_value = (
                    minimum_trips[delivered] - port_changes[delivered]
                )
                while candidates and (
                    minimum_trips[candidates[-1]]
                    - port_changes[candidates[-1]]
                    >= candidate_value
                ):
                    candidates.pop()
                candidates.append(delivered)

        return minimum_trips[n]
