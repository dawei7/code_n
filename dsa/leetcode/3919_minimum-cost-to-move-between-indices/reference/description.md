## Description

You are given a strictly increasing integer array `nums`. For an index `x`, define `closest(x)` as the adjacent index whose value has the smallest absolute difference from `nums[x]`. When an interior index has equal differences to both neighbors, the smaller adjacent index is chosen.

From `x`, a move to any index `y` normally costs `abs(nums[x] - nums[y])`. There is also a discounted move from `x` to `closest(x)` whose cost is exactly `1`.

Each query supplies a starting index and a target index. Find the minimum total cost of any sequence of allowed moves between those indices, and return the answers in query order. Here, the absolute difference between two values $a$ and $b$ is $\lvert a-b\rvert$.
