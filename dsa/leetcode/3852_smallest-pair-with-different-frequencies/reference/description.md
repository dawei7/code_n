## Description

You are given an integer array `nums`. A value's frequency is the number of times that value occurs in the array.

Consider pairs of distinct values `x` and `y` that both occur in `nums`. A pair is valid only when `x < y` and the two values have different frequencies.

Choose among the valid pairs by minimizing `x` first. If several valid pairs use that same `x`, minimize `y` next.

Return the chosen pair as `[x, y]`. If no pair satisfies both conditions, return `[-1, -1]`.
