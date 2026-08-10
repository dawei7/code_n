
## Solution
---
### Approach 1: Equal Ones

**Intuition**

Each part has to have the same number of ones in their representation.  The algorithm given below is the natural continuation of this idea.

**Algorithm**

Say `totalOnes` is the number of ones in `arr`.  Since every part has the same number of ones, they all should have $targetOnes = totalOnes / 3$ ones.

If `totalOnes` isn't divisible by 3, the task is impossible.

Let T stand for `targetOnes`. We can find the position of the $1^{st}$, $T^{th}$, $(T+1)^{th}$, $2T^{th}$, $(2T+1)^{th}$, and $3T^{th}$ one.  The positions of these ones form 3 intervals: `[i1, j1]`, `[i2, j2]`, and `[i3, j3]`.  If there are only 3 ones, then the intervals are each length 1.

Between them, there may be some number of zeros.  The zeros after `j3` must be included in each part: say there are `trailingZeros` of them $(trailingZeros = \text{arr.length} - j3)$.

So the first part, `[i1, j1]`, is now `[i1, j1+trailingZeros]`.  Similarly, the second part, `[i2, j2]`, is now `[i2, j2+trailingZeros]`.

If all this is actually possible, then the final answer is `[j1+trailingZeros, j2+trailingZeros+1]`.

```python
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        IMPOSSIBLE = [-1, -1]

        # If total number of ones is not evenly divisible by 3, then no solution exists.
        total_ones = sum(arr)
        if total_ones % 3:
            return IMPOSSIBLE

        # Otherwise, each part should contain an equal amount of ones.
        target_ones = total_ones // 3
        if target_ones == 0:
            return [0, len(arr) - 1]

        # Find the index of the first and last 1 in each block of ones.
        breaks = []
        one_count = 0
        for i, bit in enumerate(arr):
            if bit == 1:
                one_count += bit
                if one_count in {1, target_ones + 1, 2 * target_ones + 1}:
                    breaks.append(i)
                if one_count in {target_ones, 2 * target_ones, 3 * target_ones}:
                    breaks.append(i)

        # i1, j1 marks the index of the first and last one in the first block of 1s, etc.
        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where each [i, j] is a block of 1s and W, X, Y, and Z represent blocks of 0s.
        if not(arr[i1 : j1 + 1] == arr[i2 : j2 + 1] == arr[i3 : j3 + 1]):
            return [-1, -1]

        # The number of zeros after the left, middle, and right parts
        trailing_zeros_left = i2 - j1 - 1
        trailing_zeros_mid = i3 - j2 - 1
        trailing_zeros = len(arr) - j3 - 1

        if trailing_zeros > min(trailing_zeros_left, trailing_zeros_mid):
            return IMPOSSIBLE

        j1 += trailing_zeros
        j2 += trailing_zeros
        return [j1, j2 + 1]
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `arr`.

* Space Complexity:  $O(N)$ because $O(N)$ space is used when checking if the three intervals of ones are the same.
<br />
<br />