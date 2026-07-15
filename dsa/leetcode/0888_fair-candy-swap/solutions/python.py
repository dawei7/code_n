"""Optimal app-local solution for LeetCode 888."""


def solve(aliceSizes, bobSizes):
    difference = (sum(aliceSizes) - sum(bobSizes)) // 2
    bob_boxes = set(bobSizes)
    for alice_box in aliceSizes:
        bob_box = alice_box - difference
        if bob_box in bob_boxes:
            return [alice_box, bob_box]
