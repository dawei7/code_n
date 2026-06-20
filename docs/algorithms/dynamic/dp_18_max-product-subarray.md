# Max Product Subarray

| | |
|---|---|
| **ID** | `dp_18` |
| **Category** | dynamic |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem) (related) |

## Problem statement

Given an array of integers `nums` (which may include
**negatives and zeros**), find the **contiguous subarray**
with the largest product.

**Input:** an array `nums`.
**Output:** the maximum product of any contiguous subarray.

**Example:**

| nums | Answer | Subarray |
|---|---:|---|
| `[2, 3, -2, 4]` | 6 | `[2, 3]` |
| `[-2, 0, -1]` | 0 | `[]` or `[0]` (any product ≤ 0 is OK) |
| `[-2, 3, -4]` | 24 | `[-2, 3, -4]` |
| `[0, 2]` | 2 | `[2]` |
| `[-1, -2, -3, -4]` | 24 | `[-1, -2, -3, -4]` |

## When to use it

- The classic "**subarray with max sum**" problem, but with
  product instead of sum. The interesting twist: when two
  negatives multiply, the sign flips, so we need to track
  both min and max.
- Common at Google, Meta, and Amazon — a great "did you
  remember the negative-edge case?" interview question.

## Approach

For maximum sum, Kadane's algorithm tracks only the max
ending at each position. For **maximum product**, multiplying
by a negative flips the sign, so the largest product ending
at position `i` might come from the *smallest* (most
negative) product at position `i-1`.

Define two arrays:
- `max_ending[i]` = max product of a subarray ending at `i`.
- `min_ending[i]` = min product of a subarray ending at `i`.

**Recurrence:** at position `i`:
```
candidate_a = nums[i]
candidate_b = max_ending[i-1] * nums[i]
candidate_c = min_ending[i-1] * nums[i]
max_ending[i] = max(candidate_a, candidate_b, candidate_c)
min_ending[i] = min(candidate_a, candidate_b, candidate_c)
```

(The `candidate_a` covers the case where starting fresh at
`i` is better than extending.)

**Zeros:** if `nums[i] == 0`, the max and min are both 0
(an empty subarray would suffice, but we use 0 for the
"zero resets" semantic).

**Space optimization:** same as Kadane's — keep only the
last `max_ending` and `min_ending`, plus a running answer.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_18: Max Product Subarray.

Track both cur_max and cur_min (negatives flip sign).
"""


def solve(arr):
    if not arr:
        return 0
    best = arr[0]
    cur_max = arr[0]
    cur_min = arr[0]
    for v in arr[1:]:
        if v < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(v, cur_max * v)
        cur_min = min(v, cur_min * v)
        if cur_max > best:
            best = cur_max
    return best
```

</details>

## Walk-through

`nums = [2, 3, -2, 4]`. Expected: 6.

| i | x | x<0? | max_ending (before) | min_ending (before) | new max | new min | best |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2 | no | 2 (init) | 2 (init) | 2 | 2 | 2 |
| 1 | 3 | no | 2 | 2 | max(3, 2·3=6) = 6 | min(3, 2·3=6) = 3 | 6 |
| 2 | -2 | yes | 6 | 3 | swap→ max=3, min=6, then max(-2, 3·-2=-6)=-2, min(-2, 6·-2=-12)=-12 | -2 | -12 | 6 |
| 3 | 4 | no | -2 | -12 | max(4, -2·4=-8) = 4 | min(4, -12·4=-48) = -48 | **6** |

Answer: 6. ✓ (subarray [2, 3] → product 6.)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(1)$ |
| **Average** | $O(n)$ | $O(1)$ |
| **Worst** | $O(n)$ | $O(1)$ |

Single pass, two variables, $O(1)$ extra space.

## Variants & optimizations

- **Divide and conquer** — for very large arrays where
  parallelism matters, D&C gives $O(n log n)$ work with
  $O(log n)$ depth.
- **Modular product** — if `nums` can have very large values
  and you need the product mod M, use modular arithmetic in
  the recurrence.
- **Count subarrays with product < K** — sliding window.
  Different problem, similar flavor.
- **Reconstruct the subarray** — track the start index of
  the best subarray; reset to `i` when starting fresh.

## Real-world applications

- **Maximum profit from a sequence of price changes** — if
  you can long and short, the maximum product captures
  both directions.
- **Signal processing** — finding the largest "gain" sequence
  in a noisy signal.
- **Genetic algorithms** — fitness can be modeled as a
  product of multipliers; finding the optimal sub-window
  matches this DP.
- **Portfolio analytics** — the maximum geometric mean over
  a window is the log of the max product.
- **Image processing** — convolution kernels often have
  negative values; max-product finds the most "amplifying"
  region.

## Related algorithms in cOde(n)

- **[dp_11 — House Robber](dp_11_house-robber.md)** — same
  rolling shape, but a max-of-two decision, not
  min-and-max. (d=5/10, r=9/10)
- **[dp_12 — Min Cost Path](dp_12_min-cost-path.md)** —
  another max-product-of-path variant, on a grid.
  (d=4/10, r=9/10)
- **[dp_09 — Rod Cutting](dp_09_rod-cutting.md)** — same
  1D DP, different objective. (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
