from typing import List

def solve(energyA: List[int], energyB: List[int]) -> int:
    n = len(energyA)
    if n == 1:
        return max(energyA[0], energyB[0])

    # dpA[i] is the max energy ending at hour i with drink A
    # dpB[i] is the max energy ending at hour i with drink B
    # To save space, we only need the previous two states.

    # Base cases for hour 0
    prev_a = energyA[0]
    prev_b = energyB[0]

    # Base cases for hour 1
    curr_a = energyA[0] + energyA[1]
    curr_b = energyB[0] + energyB[1]

    # We track the last two states to handle the "skip" rule
    # dpA[i] = max(dpA[i-1] + energyA[i], dpB[i-2] + energyA[i])
    # dpB[i] = max(dpB[i-1] + energyB[i], dpA[i-2] + energyB[i])

    # state_a_minus_2, state_a_minus_1
    # state_b_minus_2, state_b_minus_1
    a_2, a_1 = energyA[0], energyA[0] + energyA[1]
    b_2, b_1 = energyB[0], energyB[0] + energyB[1]

    for i in range(2, n):
        new_a = max(a_1 + energyA[i], b_2 + energyA[i])
        new_b = max(b_1 + energyB[i], a_2 + energyB[i])

        a_2, a_1 = a_1, new_a
        b_2, b_1 = b_1, new_b

    return max(a_1, b_1)
