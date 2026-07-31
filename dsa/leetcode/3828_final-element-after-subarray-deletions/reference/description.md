## Description

Consider an integer array `nums`.

Alice and Bob play an alternating-turn deletion game on this array, with Alice taking the first turn.

- On each turn, the current player selects a nonempty subarray `nums[l..r]`. If the array currently has length `m`, the chosen block must satisfy `r - l + 1 < m`.
- The chosen subarray is deleted, after which the elements on its two sides are concatenated into the new array.
- Play continues until exactly one element remains.

Alice tries to maximize the value of that final element, whereas Bob tries to minimize it. Assuming optimal decisions from both players, return the value left at the end of the game.
