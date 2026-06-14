# Longest Increasing Subsequence (LIS)

| | |
|---|---|
| **ID** | `dp_07` |
| **Category** | dynamic |
| **Complexity (required)** | O(n log n) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Longest increasing subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) |

## Problem statement

Given a sequence of numbers `a[0..n-1]`, find the length of
the longest **strictly increasing subsequence** (not
necessarily contiguous). A subsequence is a subset that
preserves order; "increasing" means each element is
strictly greater than the previous one.

**Input:** an array of comparable elements.
**Output:** the length of the LIS.

**Example:**

| Input | LIS | Length |
|---|---|---:|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | `[2, 3, 7, 18]` or `[2, 3, 7, 101]` | 4 |
| `[0, 1, 0, 3, 2, 3]` | `[0, 1, 2, 3]` | 4 |
| `[7, 7, 7, 7]` | (none strictly increasing) | 1 |
| `[]` | (empty) | 0 |

## When to use it

- The canonical "**O(n²) DP that becomes O(n log n) with a
  patience-sorting trick**" problem. The O(n log n) version
  is asked at every top-tier company.
- Whenever you need to find an **order-preserving subset** that
  satisfies a monotonicity constraint, LIS or a variant
  applies.
- Foundation for the **patience-sorting-based sorting
  algorithms** and the **minimum-number-of-increasing-
  subsequences** decomposition (Dilworth's theorem).

## Approach

There are two canonical approaches. cOde(n)'s engine checks
against the O(n log n) one, so we'll focus on that.

### The O(n log n) patience-sorting approach

Maintain an array `tails[]` where `tails[i]` is the **smallest
possible tail value** of any increasing subsequence of
length `i+1` seen so far. This array is always sorted.

For each element `x` in the input:
- Find the **leftmost position** in `tails` that is `>= x`
  (using binary search).
- Replace `tails[pos]` with `x`.
- If `x` is bigger than every existing tail, it extends the
  longest subsequence — append.

The length of `tails` at the end is the LIS length.

**Why it works:** the array `tails` is a decreasing-by-length
summary of all candidate subsequences. For each length, we
keep only the "smallest possible tail" because a smaller tail
is always at least as good as a larger one (more elements can
follow it).

### The O(n²) DP approach (for understanding)

`dp[i]` = length of LIS ending at `a[i]`. Recurrence:
`dp[i] = 1 + max(dp[j])` over all `j < i` with `a[j] < a[i]`.
Answer: `max(dp)`. The O(n log n) version above is a strict
improvement and is the one to memorize.

## Algorithm (pseudocode)

```
lis_length(a):
    tails = []
    for x in a:
        # leftmost position where tails[pos] >= x
        pos = lower_bound(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)
```

`lower_bound` is a standard binary search: the first index
where `tails[i] >= x`. For strict increase, use `>` here
instead of `>=` (i.e. upper bound).

## Walk-through

`a = [10, 9, 2, 5, 3, 7, 101, 18]`.

| x | lower_bound(tails, x) | tails after |
|---:|---:|---|
| 10 | 0 | `[10]` |
| 9 | 0 | `[9]` (replaces 10) |
| 2 | 0 | `[2]` (replaces 9) |
| 5 | 1 | `[2, 5]` |
| 3 | 1 | `[2, 3]` (replaces 5) |
| 7 | 2 | `[2, 3, 7]` |
| 101 | 3 | `[2, 3, 7, 101]` |
| 18 | 3 | `[2, 3, 7, 18]` (replaces 101) |

`len(tails) = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n log n) | O(n) |
| **Average** | O(n log n) | O(n) |
| **Worst** | O(n log n) | O(n) |

The binary search is O(log n) per element, and we do it n
times. The `tails` array is at most n elements.

For the strictly-decreasing-input case, `tails` never has a
tail replaced, so binary search does the full O(log n) on
each step — still O(n log n) total.

## Variants & optimizations

- **Strictly increasing → non-decreasing** — change
  `lower_bound` (first `>=`) to `upper_bound` (first `>`).
  This handles equal elements correctly.
- **Reconstruct the actual sequence** — store a parallel
  `parent[i]` array (the index `j` that was replaced when
  we updated `tails[pos]`). Then walk back from the last
  element to reconstruct the LIS in reverse. O(n) extra
  space and O(n) reconstruction time.
- **Longest non-decreasing subsequence of 2D points** —
  sort by x, then apply LIS on y. Used in the Russian doll
  envelopes problem.
- **Patience sort** — this algorithm is exactly patience
  sorting; the number of piles is the LIS length, and the
  full patience sort produces a stable sort in O(n log n).

## Real-world applications

- **Diff and merge tools** — find the longest matching block
  of lines between two file versions. The diff algorithm
  reduces to LCS (related) but a similar DP appears.
- **Molecular biology** — finding conserved subsequences in
  DNA / protein sequences.
- **Financial analysis** — find the longest streak of
  increasing stock prices, used in trend analysis.
- **Patience sorting** — the algorithm above IS patience
  sorting; the pile count is the LIS length. Patience sort
  is O(n log n) and stable.

## Related algorithms in cOde(n)

- **[dp_29 — LIS (Patience Sort)](dp_29_lis-patience-sort.md)** —
  same algorithm, framed as a sorting result rather than a
  pure DP. (d=5/10, r=9/10)
- **[dp_04 — Longest Common Subsequence](dp_04_longest-common-subsequence.md)** —
  similar shape, but on two sequences instead of one.
  (d=5/10, r=9/10)
- **[stack_02 — Next Greater Element](stack_02_next-greater-element.md)** —
  another classic "longest increasing-like" problem, solved
  with a monotonic stack in O(n). (d=4/10, r=7/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
