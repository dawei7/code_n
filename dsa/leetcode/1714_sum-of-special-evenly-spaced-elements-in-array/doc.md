# Sum Of Special Evenly-Spaced Elements In Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1714 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/) |

## Problem Description
### Goal

You are given an integer array `nums` and a list of queries. Each query is `[x, y]`. Its special sum starts at index `x` and includes `nums[x]`, `nums[x + y]`, `nums[x + 2 * y]`, and so on while the selected index remains inside the array.

Return the special sum for every query in its original order, with each result reduced modulo $10^9+7$. Queries do not modify `nums`, and repeated starting positions or step sizes must each produce their own output.

### Function Contract
**Inputs**

- `nums`: a list of $n$ non-negative integers
- `queries`: a list of $q$ pairs `[x, y]`, where `x` is a valid array index and $y \ge 1$
- $1 \le n \le 5\cdot 10^4$ and $1 \le q \le 1.5\cdot 10^5$
- every value and query step is at most $10^9$ and $5\cdot10^4$, respectively

Let $S=\lfloor\sqrt n\rfloor+1$.

**Return value**

A length-$q$ list whose entry for `[x, y]` is

$$
\left(\sum_{\substack{k\ge0\\x+ky<n}}\texttt{nums[x + k * y]}\right)
\bmod (10^9+7).
$$

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 3, 4, 5, 6, 7], queries = [[0, 3], [5, 1], [4, 2]]`
- Output: `[9, 18, 10]`

The selected index sequences are `(0, 3, 6)`, `(5, 6, 7)`, and `(4, 6)`.

**Example 2**

- Input: `nums = [100, 200, 101, 201, 102, 202, 103, 203], queries = [[0, 7]]`
- Output: `[303]`

The query selects indices `0` and `7`.

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5], queries = [[0, 2], [1, 2], [4, 1]]`
- Output: `[9, 6, 5]`

Different starts with the same step reuse the same evenly spaced suffix relation.

### Required Complexity

- **Time:** $O((n+q)S)$
- **Space:** $O(n+q)$

<details>
<summary>Approach</summary>

#### General

**Separate small and large steps**

Choose $S=\lfloor\sqrt n\rfloor+1$ and group queries by their step `y`. When `y >= S`, one query visits at most $\lceil n/y\rceil=O(S)$ array positions, so summing its progression directly is already cheap.

When `y < S`, many queries could each visit nearly the whole array. For one such step, build a reverse dynamic-programming array:

`suffix[i] = nums[i] + suffix[i + y]`

whenever `i + y` is valid. Then every query with this step is answered in $O(1)$ by `suffix[x]`. Process all queries sharing that step, discard the temporary array, and continue with the next step.

**Why grouping preserves every progression**

For a fixed step, `suffix[i]` contains `nums[i]` and exactly the special sum starting one step later. Induction from the end of the array therefore shows that it contains every and only index in the progression `i, i + y, i + 2 * y, ...`.

Large-step queries enumerate that same progression explicitly. Grouping changes only the evaluation strategy; saved query indices restore the original output order. Applying the modulus during each DP addition and after direct accumulation preserves the required modular sum.

#### Complexity detail

There are fewer than $S$ possible small steps, and each distinct small step costs $O(n)$ to preprocess, for $O(nS)$ total. Each large-step query visits $O(S)$ positions, for $O(qS)$ total. Grouping and answer placement add $O(q)$, giving $O((n+q)S)$ time.

The query groups and answers use $O(q)$ space. Only one length-$n$ small-step DP array exists at a time, so total space is $O(n+q)$ rather than $O(nS)$.

#### Alternatives and edge cases

- **Traverse every query directly:** this is simple but repeated step-one queries take $O(nq)$ time.
- **Precompute every step in a permanent table:** it answers small-step queries quickly but consumes $O(nS)$ memory unnecessarily.
- **Prefix sums:** ordinary contiguous prefix sums cannot subtract an arithmetic progression with step greater than one.
- **Group without saved indices:** queries must still be returned in their original order, not grouped-step order.
- **Start at the last index:** every positive step selects exactly one value.
- **Step at least the remaining length:** only `nums[x]` contributes.
- **Repeated queries:** each receives the same numeric result at its own output position.
- **Zero values:** they contribute nothing but do not terminate the progression.
- **Large totals:** reduce modulo $10^9+7$ so intermediate DP values remain bounded.

</details>
