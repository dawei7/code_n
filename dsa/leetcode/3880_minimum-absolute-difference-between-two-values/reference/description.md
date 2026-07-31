## Description

You are given an integer array `nums` whose entries are limited to `0`, `1`, and `2`.

An index pair `(i, j)` is valid when `nums[i]` is `1` and `nums[j]` is `2`. Either index may occur first in the array because the pair's distance is the absolute difference $\lvert i-j\rvert$.

Return the smallest distance among all valid pairs. If the array does not contain both required values and therefore has no valid pair, return `-1`.
