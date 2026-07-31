## Function Contract

**Inputs**

- `nums`: A nonempty array in which `nums[i]` is the positive point value of zero-indexed game $i$.

The active-player state persists between games. An odd point value toggles that state first. A game whose one-based number $i+1$ is divisible by $6$ toggles it second. Therefore, an odd-valued sixth game performs two swaps and leaves the same player active as before that game's rules began.

Let $S_1$ and $S_2$ be the accumulated scores of the first and second players. Exactly one of them receives `nums[i]` in each game, after the two swap conditions have been evaluated in the required order.

**Return value**

Return the signed integer difference

$$
S_1-S_2.
$$

The result may be negative when the second player finishes with more points.
