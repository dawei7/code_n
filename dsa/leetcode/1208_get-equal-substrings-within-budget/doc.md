# Get Equal Substrings Within Budget

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1208 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/get-equal-substrings-within-budget/) |

## Problem Description

### Goal

You are given lowercase English strings `s` and `t` of the same length, together with an integer `maxCost`. Changing `s[i]` into the corresponding character `t[i]` costs the absolute difference between their ASCII values, $\lvert\operatorname{ord}(\texttt{s[i]})-\operatorname{ord}(\texttt{t[i]})\rvert$.

Choose one contiguous substring of `s` and change all of its characters to match the substring at the same indices in `t`. Return the maximum possible substring length whose total conversion cost is at most `maxCost`. If no nonempty corresponding substring is affordable, return 0.

### Function Contract

**Inputs**

- `s` and `t`: Lowercase English strings of equal length $n$, where $1\le n\le10^5$.
- `maxCost`: The available conversion budget, where $0\le\texttt{maxCost}\le10^6$.

**Return value**

- The greatest length of a contiguous index interval whose character-conversion costs sum to at most `maxCost`.

### Examples

**Example 1**

- Input: `s = "abcd"`, `t = "bcdf"`, `maxCost = 3`
- Output: `3`

Changing `"abc"` into `"bcd"` costs $1+1+1=3$.

**Example 2**

- Input: `s = "abcd"`, `t = "cdef"`, `maxCost = 3`
- Output: `1`

Each corresponding character costs 2, so two adjacent changes would exceed the budget.

**Example 3**

- Input: `s = "abcd"`, `t = "acde"`, `maxCost = 0`
- Output: `1`

Only positions that already match can belong to a zero-cost answer.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Convert the strings into nonnegative costs conceptually.** At index `i`, the only relevant quantity is `abs(ord(s[i]) - ord(t[i]))`. A candidate substring is affordable exactly when the sum of these per-index costs over its contiguous interval does not exceed `maxCost`.

**Maintain the longest affordable suffix.** Extend a right pointer one index at a time and add that position's cost to a running total. If the total exceeds the budget, repeatedly subtract the cost at the left pointer and advance `left` until the current window becomes affordable again.

**Why discarded starts never become useful.** Every cost is nonnegative. Once the window ending at the current right boundary is over budget, keeping its leftmost position cannot help any extension; adding later positions can only preserve or increase the total. Removing left positions until affordability is restored therefore discards no possible optimal future window. After restoration, the current left boundary is the earliest affordable start for this right endpoint, so the window is its longest valid ending interval. Taking the maximum of those lengths gives the global optimum.

#### Complexity detail

The right pointer visits each of the $n$ positions once. The left pointer also advances at most $n$ times across the entire run, so total time is $O(n)$. Costs are computed when they enter and leave the window; only the two pointers, running cost, and best length are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every start:** Extending a fresh substring from each starting index is correct but takes $O(n^2)$ time when many long windows are affordable.
- **Prefix sums plus binary search:** A prefix-cost array can test interval sums and locate a boundary in $O(n\log n)$ time with $O(n)$ space.
- **Binary search the answer length:** Nonnegative costs make feasibility monotone by length, but each feasibility scan adds a logarithmic factor.
- **Zero budget:** Only contiguous runs of positions with zero conversion cost are usable.
- **No affordable character:** If every single-position cost exceeds the budget, return 0.
- **Identical strings:** Every position costs zero, so the entire string is valid.
- **Exact budget:** A total equal to `maxCost` is allowed.
- **One expensive index:** Shrinking may remove several cheap positions along with it; the pointers still consider the longest interval for every right endpoint.

</details>
