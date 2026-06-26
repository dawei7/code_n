# Two Sum

| | |
|---|---|
| **ID** | `hash_01` |
| **Category** | hashing |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Hash table](https://en.wikipedia.org/wiki/Hash_table) |

## Problem statement

Given an array of integers `nums` and a target `target`, return
the **indices of the two numbers** that add up to `target`.
You may assume that each input has exactly one solution, and
you may not use the same element twice.

**Input:** an array `nums` and an integer `target`.
**Output:** two indices `i ≠ j` with `nums[i] + nums[j] = target`.

**Example:**

| nums | target | Answer | Sum |
|---|---|---|---:|
| `[2, 7, 11, 15]` | 9 | `[0, 1]` | 2 + 7 |
| `[3, 2, 4]` | 6 | `[1, 2]` | 2 + 4 |
| `[3, 3]` | 6 | `[0, 1]` | 3 + 3 |

## When to use it

- The single most-asked **warm-up / phone-screen question** in
  coding interviews. LeetCode's #1. The point isn't whether
  you know the algorithm (it's the dictionary lookup); the
  point is whether you can:
  - **Argue the complexity** ($O(n²)$ brute force vs. $O(n)$ hash
    map)
  - **Discuss the trade-offs** (extra space for the map vs.
    $O(1)$ extra space for the sorted two-pointer variant)
  - **Generalize** to 3-Sum, 4-Sum, K-Sum, or to "two numbers
    close to a target" (binary search on the sorted array)
- Excellent test of whether you reach for the right data
  structure (hash map) when the problem asks for "find a
  complement" in $O(n)$ time.

## Approach

For each element `nums[i]`, we need to find whether
`target - nums[i]` has appeared earlier in the array.

**Brute force** ($O(n²)$): nested loop. Try every pair.

**Sort + two pointers** ($O(n log n)$): sort the array, then walk
two pointers from the ends. The "answer indices" need to be
preserved separately because sorting destroys the original
ordering. The two-pointer variant is $O(1)$ extra space.

**Hash map** ($O(n)$, the production version): for each
`nums[i]`, check whether `target - nums[i]` is in the map.
- If yes: we found our answer, return `[map[target - nums[i]], i]`.
- If no: store `nums[i] -> i` in the map and move on.

This is $O(n)$ time and $O(n)$ extra space. Single pass.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for hash_01: Two Sum.

Single pass: walk the array, for each value check whether
target - value has been seen. If yes, return the two indices.
Otherwise, store the current value's index in the map. O(n).
"""


def solve(arr, target, n):
    seen = {}
    for i in range(n):
        complement = target - arr[i]
        if complement in seen:
            return sorted([seen[complement], i])
        seen[arr[i]] = i
    return [-1, -1]
```

</details>

## Walk-through

`nums = [2, 7, 11, 15]`, `target = 9`.

| i | x | complement | seen before | action | seen after |
|---:|---:|---:|---|---|---|
| 0 | 2 | 7 | `{}` | store 2→0 | `{2: 0}` |
| 1 | 7 | 2 | `{2: 0}` | found! return `[0, 1]` | — |

Answer: `[0, 1]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(n)$ |
| **Average** | $O(n)$ | $O(n)$ |
| **Worst** | $O(n)$ | $O(n)$ |

Hash table lookups and inserts are expected $O(1)$ (worst-case
$O(n)$ with a bad hash, but in practice $O(1)$ for integer keys).

## Variants & optimizations

- **Sorted + two pointers** ($O(n log n)$ time, $O(1)$ space) —
  when you can't afford the extra hash map. The downside is
  you have to track the original indices through the sort.
- **3-Sum, 4-Sum, K-Sum** — extend the pattern. 3-Sum:
  sort, then for each `i` solve "two sum" on the rest of the
  array with target `-nums[i]`. Skip duplicates. $O(n²)$ for
  3-Sum.
- **Two Sum II (sorted input)** — the array is already sorted;
  the two-pointer solution is $O(n)$ with $O(1)$ extra space.
- **Two Sum BST** — given a BST, find two nodes that sum to a
  target. Use the in-order iterator + reverse in-order
  iterator (two-pointer on a BST) for $O(n)$ time and $O(log n)$
  space.
- **Subarray sum equals k** — the related prefix-sum +
  hash-map problem (`hash_02`).

## Real-world applications

- **Invoice reconciliation** — match incoming payments to
  outstanding invoices; the "two invoices that sum to the
  deposit" is exactly Two Sum.
- **Pair finding in financial datasets** — find two
  transactions that net to zero (a transfer + the matching
  fee, a buy + a sell, etc.).
- **Cache key construction** — given a request with two
  parameters `a, b`, check if the (ordered) pair `(a, b)` is
  in a result cache; this is the "two sum" pattern in
  disguise.
- **Sudoku and crossword solvers** — "two cells that sum to
  N" is a common sub-probe.

## Related algorithms in cOde(n)

- **[hash_02 — Subarray Sum Equals K](hash_02_subarray-sum-equals-k.md)** —
  the prefix-sum generalization. (d=4/10, r=9/10)
- **[hash_03 — Longest Substring Without Repeating](hash_03_longest-substring-without-repeating.md)** —
  hash-set with sliding window. (d=4/10, r=9/10)
- **[search_02 — Binary Search](search_02_binary-search.md)** —
  the alternative $O(n log n)$ / $O(1)$ approach for sorted
  input. (d=3/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
