## Description

You receive an integer array `nums`. It is **beautiful** when every position after the first contains a value divisible by the value immediately before it: for each $i > 0$, `nums[i] % nums[i - 1] == 0`.

One operation increments `nums[i]` by `1`, but only an index with $i > 0$ may be changed. Determine the fewest operations needed to make the entire array beautiful.
