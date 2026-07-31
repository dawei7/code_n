## Description

You are given an integer array `nums`. Its element `nums[i]` is the number of points available in game $i$.

Exactly two players participate. Before any game is processed, the first player is active and the second player is inactive.

Process the games from left to right. For every index $i$, apply these rules in order:

1. If `nums[i]` is odd, swap which player is active.
2. On every sixth game—indices `5`, `11`, `17`, and so on—swap the active player again.
3. The player who is active after both possible swaps plays game $i$ and receives `nums[i]` points.

Return the first player's total score minus the second player's total score.
