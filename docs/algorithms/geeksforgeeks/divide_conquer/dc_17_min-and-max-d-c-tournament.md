# Min and Max in Array (Tournament Method)

| | |
|---|---|
| **ID** | `dc_17` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Maximum and minimum of an array using minimum number of comparisons](https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/) |

## Problem statement

Given an array of size `N`, find both the maximum and minimum elements in the array.
*Constraint:* You must minimize the absolute number of comparison operations performed.

**Input:** An integer array `nums`.
**Output:** A tuple `(min_val, max_val)`.

## When to use it

- When asked to optimize the theoretical constant factor of a linear scan algorithm.
- An introductory Divide and Conquer algorithm that is easier to understand than Merge Sort.

## Approach

**1. The Naive Linear Scan:**
You initialize `min_val = nums[0]` and `max_val = nums[0]`.
For every element, you check `if nums[i] < min_val`, and then check `if nums[i] > max_val`.
Since you check every element twice against two bounds, you perform 2N comparisons.
Can we do fewer?

**2. The Divide and Conquer (Tournament) Method:**
Imagine an arm-wrestling tournament to find the strongest and weakest person.
If we split the array in half perfectly down the middle, we can recursively find the `(min, max)` of the left half, and the `(min, max)` of the right half.
When the recursive calls return, we simply have a "finals" match:
- The global `min` is the smaller of the two left/right `min`s.
- The global `max` is the larger of the two left/right `max`s.

This takes exactly 2 comparisons to merge the halves.

**3. Base Cases:**
- If the array slice has 1 element, return `(nums[0], nums[0])`. (0 comparisons).
- If the array slice has 2 elements, compare them! Return the smaller as `min` and larger as `max`. (1 comparison).

*Mathematical magic:* By grouping elements into pairs at the base case and only sending the winners up the tree, the total number of comparisons mathematically drops from 2N down to \frac{3N}{2} - 2.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_17: Min and Max (D&C tournament).

Given an array of n integers, return the minimum
"""


def solve(arr, n):
    """D&C tournament min/max. Returns [lo, hi]."""
    def rec(lo, hi):
        if lo == hi:
            return [arr[lo], arr[lo]]
        if hi == lo + 1:
            if arr[lo] < arr[hi]:
                return [arr[lo], arr[hi]]
            return [arr[hi], arr[lo]]
        mid = (lo + hi) // 2
        a = rec(lo, mid)
        b = rec(mid + 1, hi)
        return [min(a[0], b[0]), max(a[1], b[1])]
    return rec(0, n - 1)
```

</details>

## Walk-through

`nums = [1000, 11, 445, 1, 330, 3000]`. N = 6.

1. Split into `[1000, 11, 445]` and `[1, 330, 3000]`.
2. **Left Half `[1000, 11, 445]`:**
   - Split into `[1000, 11]` and `[445]`.
   - `[1000, 11]` triggers Base Case 2. (1 comparison). Returns `(11, 1000)`.
   - `[445]` triggers Base Case 1. Returns `(445, 445)`.
   - Merge! `min(11, 445)` is 11. `max(1000, 445)` is 1000. (2 comparisons).
   - Left Half returns `(11, 1000)`.
3. **Right Half `[1, 330, 3000]`:**
   - Split into `[1, 330]` and `[3000]`.
   - `[1, 330]` returns `(1, 330)`. (1 comparison).
   - `[3000]` returns `(3000, 3000)`.
   - Merge! `min(1, 3000)` is 1. `max(330, 3000)` is 3000. (2 comparisons).
   - Right Half returns `(1, 3000)`.
4. **Global Merge:**
   - `min(11, 1)` is 1.
   - `max(1000, 3000)` is 3000. (2 comparisons).

Total comparisons: 8.
Naive linear scan comparisons: 2 x 6 = 12.
We successfully minimized the constant factor!

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(\log N)$ |

The time complexity is strictly $O(N)$ because we process every element. The specific recurrence relation is T(N) = 2T(N/2) + 2 comparisons. According to the Master Theorem, this is $O(N)$.
Space complexity is $O(\log N)$ due to the depth of the recursive call stack.

## Variants & optimizations

- **Iterative Pair Comparison:** You can achieve the exact same \frac{3N}{2} comparison bound WITHOUT the $O(\log N)$ recursion stack space cost!
  Initialize `global_min` and `global_max`. Iterate through the array in steps of 2. For each pair `(arr[i], arr[i+1])`, compare them to EACH OTHER first!
  Take the smaller one and compare it only against `global_min`. Take the larger one and compare it only against `global_max`.
  This is 3 comparisons per pair of elements, resulting in exactly \frac{3N}{2} comparisons in $O(1)$ space.

## Real-world applications

- **Hardware Architecture:** Physical silicon ALUs (Arithmetic Logic Units) that process Vector/SIMD instructions implement this exact tree-structured reduction to find Min/Max values across hardware registers, because the comparisons can be executed completely in parallel in a binary tree circuit.

## Related algorithms in cOde(n)

- **[dc_02 - Majority Element](dc_02_majority-element.md)** — Another algorithm where basic array properties are merged back up a binary recursion tree.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
