# Subarray Sum Equals K

| | |
|---|---|
| **ID** | `hash_02` |
| **Category** | hashing |
| **Complexity (required)** | O(n) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Hash table](https://en.wikipedia.org/wiki/Hash_table) |

## Problem statement

Given an array of integers `nums` (which may include
**negatives and zeros**) and an integer `k`, count the
number of **contiguous subarrays** whose sum equals `k`.

**Input:** an array `nums`, a target sum `k`.
**Output:** the count of contiguous subarrays with sum `k`.

**Example:**

| nums | k | Answer | Subarrays |
|---|---|---:|---|
| `[1, 1, 1]` | 2 | 2 | `[1,1]@0-1`, `[1,1]@1-2` |
| `[1, 2, 3]` | 3 | 2 | `[1,2]@0-1`, `[3]@2-2` |
| `[1, -1, 1, -1, 1, -1]` | 0 | 9 | (all subarrays of even length) |
| `[3, 4, 7, 2, -3, 1, 4, 2]` | 7 | 4 | |

## When to use it

- The classic "**prefix sum + hash map**" technique. Asked
  in some form at every company; tests whether you remember
  the O(n) trick.
- Foundation for many "**count subarrays with property X**"
  problems where X is sum-related.

## Approach

**Brute force** (O(n²)): try every `(start, end)` pair.

**Prefix sum** (the trick): define `prefix[i]` = sum of
`nums[0..i-1]`. The sum of `nums[i..j-1]` is
`prefix[j] - prefix[i]`. We want this to equal `k`, i.e.
`prefix[i] = prefix[j] - k`.

Iterate `j` from `0` to `n`:
- For each `j`, count how many `i < j` have
  `prefix[i] = prefix[j] - k`.
- This count = number of subarrays ending at `j` with sum `k`.
- Maintain a hash map `count[value] = number of times that
  prefix sum has appeared`.

**Base case:** `count[0] = 1` (the empty prefix; a subarray
starting at index 0 with sum 0 contributes one to the count).

## Algorithm (pseudocode)

```
subarray_sum(nums, k):
    count = {0: 1}
    running = 0
    result = 0
    for x in nums:
        running += x
        result += count.get(running - k, 0)
        count[running] = count.get(running, 0) + 1
    return result
```

## Walk-through

`nums = [1, 1, 1]`, `k = 2`. Answer: 2.

`count = {0: 1}`, `running = 0`, `result = 0`.

| x | running | running - k | count[running - k] | result | count after |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | -1 | 0 | 0 | `{0:1, 1:1}` |
| 1 | 2 | 0 | 1 | **1** | `{0:1, 1:1, 2:1}` |
| 1 | 3 | 1 | 1 | **2** | `{0:1, 1:1, 2:1, 3:1}` |

Answer: 2. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n) | O(n) |
| **Average** | O(n) | O(n) |
| **Worst** | O(n) | O(n) |

Single pass through the array. The hash map holds at most
`n + 1` distinct prefix sums (including the initial 0).

## Variants & optimizations

- **Subarray product equals k** — same shape, but with product
  instead of sum. Doesn't reduce to a clean hash map; needs
  sliding window if all positives, or prefix-suffix-split
  trick if mixed signs.
- **Maximum-length subarray with sum k** — track not just
  count but the earliest occurrence of each prefix sum.
- **Subarray sum divisible by k** — uses modular arithmetic
  on the prefix sums and a hash map of modulo classes.
- **Two-sum variant on a running sum** — given a list of
  bank transactions and a target amount, count how many
  contiguous windows sum to that amount.
- **Count subarrays with sum in [a, b]** — use a 2D BIT or
  a Fenwick tree on coordinate-compressed prefix sums.

## Real-world applications

- **Sales tax / fee reconciliation** — count how many
  contiguous time windows of a daily P&L sum to a target
  (e.g. "the morning shift's profit").
- **Genome analysis** — find the number of subsequences (in
  the contiguous sense) with a target sum of marker counts.
- **Data stream anomaly detection** — track prefix sums of
  a sliding window and count how many sub-windows hit a
  threshold.
- **Network packet analysis** — given a sequence of byte
  counts, count contiguous streams summing to a target
  payload size.
- **Financial backtesting** — count the number of
  contiguous trading days that produced a target return.

## Related algorithms in cOde(n)

- **[hash_01 — Two Sum](hash_01_two-sum.md)** — the
  subarray-of-size-2 version. (d=4/10, r=9/10)
- **[hash_03 — Longest Substring Without Repeating](hash_03_longest-substring-without-repeating.md)** —
  sliding-window + hash-set. (d=4/10, r=9/10)
- **[dp_06 — Subset Sum](dp_06_subset-sum.md)** — the
  subset (non-contiguous) version, with a different shape.
  (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
