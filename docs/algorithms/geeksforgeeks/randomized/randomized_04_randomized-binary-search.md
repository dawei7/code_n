# Randomized Binary Search

| | |
|---|---|
| **ID** | `randomized_04` |
| **Category** | randomized |
| **Complexity (required)** | $O(\log N)$ Expected |
| **Difficulty** | 3/10 |
| **Interview relevance** | 2/10 |
| **LeetCode Equivalent** | N/A (Theoretical variation) |

## Problem statement

Given a sorted array of distinct integers `nums` and a `target`, find the index of `target`.
Instead of the standard Binary Search which strictly probes the exact `mid` index, implement a **Randomized Binary Search** that probes a random index within the current bounds.

**Input:** A sorted integer array `nums` and an integer `target`.
**Output:** The index of `target`, or `-1` if not found.

## When to use it

- Primarily an academic exercise to study probabilistic performance bounds.
- Practically, standard Binary Search is vastly superior because calculating `mid = (L + R) / 2` is deterministic and guarantees worst-case log N. Randomization offers no defensive advantages here because Binary Search never behaves worse than $O(\log N)$ on any input permutation (unlike Quicksort).

## Approach

In standard Binary Search, we reduce the search space by choosing `mid = left + (right - left) // 2`. This guarantees the search space is exactly halved.
In Randomized Binary Search, we choose `random_idx = random.randint(left, right)`.

1. Initialize `left = 0`, `right = len(nums) - 1`.
2. While `left <= right`:
   - Pick a random index `r` between `left` and `right`.
   - If `nums[r] == target`, return `r`.
   - If `nums[r] < target`, the target must be to the right! `left = r + 1`.
   - If `nums[r] > target`, the target must be to the left! `right = r - 1`.
3. If the loop terminates without returning, return `-1`.

**Why does this still run in $O(\log N)$ expected time?**
When you pick a random index, you are just as likely to pick an index near the middle (good) as you are near the edges (bad).
On average, a randomly chosen point will split a segment of size N into two segments of expected size N/2 and N/2. Over multiple iterations, the expected reduction factor remains geometric, yielding an expected $O(\log N)$ height for the recursion tree.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_04: Randomized Binary Search.

Given a sorted list of n distinct integers and a
"""


def solve(arr, n, target):
    """Randomized binary search.

    Pick a uniformly random pivot in [lo, hi], then narrow
    the range based on whether arr[pivot] is less than,
    greater than, or equal to target. Expected O(log n).
    """
    import random
    if n == 0:
        return -1
    lo, hi = 0, n - 1
    while lo <= hi:
        pivot = random.randint(lo, hi)
        if arr[pivot] == target:
            return pivot
        if arr[pivot] < target:
            lo = pivot + 1
        else:
            hi = pivot - 1
    return -1
```

</details>

## Walk-through

`nums = [10, 20, 30, 40, 50, 60]`, `target = 50`.
`L = 0, R = 5`.

1. **Iteration 1:** `random.randint(0, 5)` rolls `1`.
   - `nums[1] = 20`. `20 < 50`.
   - Target is to the right. `L = 2, R = 5`.
2. **Iteration 2:** `random.randint(2, 5)` rolls `4`.
   - `nums[4] = 50`. `50 == 50`. Target found!
   - Return `4`. ✓

*Note: If the random number generator rolled `0`, then `1`, then `2`..., it would devolve into $O(N)$ linear search. But the probability of that happening is infinitesimally small.*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ Expected | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The best case is finding the target on the first random guess $O(1)$.
The expected average case is $O(\log N)$ because the expected reduction factor is fractional.
The absolute worst case is $O(N)$ if the RNG consistently rolls the absolute boundary value (e.g., always picking `left` when the target is at `right`).
Space complexity is $O(1)$ for the iterative approach.

## Variants & optimizations

- **Interpolation Search:** Instead of picking a random point or the exact middle point, Interpolation Search predicts the index based on the values at the boundaries: `pos = L + ((target - arr[L]) * (R - L) / (arr[R] - arr[L]))`. For uniformly distributed data, Interpolation Search is $O(log log N)$!

## Real-world applications

- **Theoretical Analysis:** Used heavily in computer science curricula to introduce randomized algorithms and expected value derivations before tackling harder algorithms like Randomized Treaps or Skip Lists.

## Related algorithms in cOde(n)

- **[searching_01 - Binary Search](../searching/searching_01_binary-search.md)** — The deterministic and vastly superior standard approach.
- **[randomized_01 - Randomized Quicksort](randomized_01_randomized-quicksort.md)** — A scenario where randomizing the pivot is actually highly beneficial.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
