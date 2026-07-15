# Valid Permutations for DI Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 903 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-permutations-for-di-sequence/) |

## Problem Description
### Goal
You are given a string `s` of length `n` whose characters are `"D"` for decreasing or `"I"` for increasing.

Consider every permutation `perm` of all $n+1$ integers in the range $[0,n]$. It is valid when each character describes the corresponding adjacent pair: `"D"` requires `perm[i] > perm[i + 1]`, while `"I"` requires `perm[i] < perm[i + 1]`. All comparisons are strict because the permutation contains distinct values.

Return the number of valid permutations modulo $10^9+7$.

### Function Contract
Let $n=\lvert\texttt{s}\rvert$ and $P=10^9+7$.

**Inputs**

- `s`: a string with $1 \leq n \leq 200$ consisting only of `"D"` and `"I"`.

**Return value**

Return the number of permutations of $[0,n]$ satisfying every encoded adjacent relation, reduced modulo $P$.

### Examples
**Example 1**

- Input: `s = "DID"`
- Output: `5`

**Example 2**

- Input: `s = "D"`
- Output: `1`

**Example 3**

- Input: `s = "I"`
- Output: `1`

### Required Complexity
- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Represent values only by their remaining rank**

Start with an array of $n+1$ ones. At a stage with `m` possible ranks, `dp[j]` counts completions when the current first value has rank `j` among those values. After fixing the next relation, remove the current value; the next state has `m-1` ranks.

For `"I"`, a next value of rank `j` can follow precisely the smaller current ranks, so its count is a prefix sum through `dp[j]`. For `"D"`, it can follow larger current ranks, giving a suffix sum beginning at `dp[j + 1]`. Compute these cumulative sums in one pass, reduce modulo $P$, and replace `dp`. After all $n$ relations, one state remains and its count is the answer.

The initial ones correctly count the single completion after all relations have been assigned. Working backward through a relation, the prefix or suffix transition sums exactly the allowed current ranks for every next rank, with no invalid comparison included. Induction therefore makes every state equal to its number of valid completions. The final sole state counts all valid permutations.

#### Complexity detail

The state lengths decrease from $n+1$ to one. Each prefix or suffix transition scans its current array once, so the total work is $O(n^2)$. Two rolling arrays hold at most $n+1$ values, using $O(n)$ space.

#### Alternatives and edge cases

- **Recompute every range sum:** The same rank recurrence is correct, but summing each prefix or suffix separately takes $O(n^3)$ time.
- **Enumerate all permutations:** Direct checking takes factorial time and becomes infeasible almost immediately.
- **Two-dimensional dynamic programming:** Retaining every stage is correct but uses $O(n^2)$ space instead of rolling one row.
- **Single relation:** Both `"D"` and `"I"` admit exactly one of the two permutations.
- **All increasing:** Only `[0,1,\ldots,n]` is valid.
- **All decreasing:** Only `[n,n-1,\ldots,0]` is valid.
- **Alternating relations:** Prefix and suffix transitions alternate without changing the state definition.
- **Modulo reduction:** Apply $P$ during every cumulative sum so intermediate counts stay bounded.

</details>
