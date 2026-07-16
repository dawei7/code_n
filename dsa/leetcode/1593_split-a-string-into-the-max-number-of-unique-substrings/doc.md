# Split a String Into the Max Number of Unique Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1593 |
| Difficulty | Medium |
| Topics | Hash Table, String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/) |

## Problem Description
### Goal
Given a string `s`, divide it into a list of non-empty substrings whose concatenation, in order, is exactly `s`. Every chosen piece must be a substring in the contiguous sense, so a split only places boundaries between existing adjacent characters; it may not reorder or omit characters.

The pieces in the resulting list must be pairwise unique. Different occurrences with the same text still count as equal and therefore cannot both appear in a valid split. Return the maximum number of pieces among all splits that satisfy this uniqueness rule.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters with $1 \le n \le 16$, where $n = \lvert s \rvert$.

**Return value**

Return the greatest possible number of pairwise distinct, non-empty substrings in a valid split of `s`.

### Examples
**Example 1**

- Input: `s = "ababccc"`
- Output: `5`
- Explanation: `"a"`, `"b"`, `"ab"`, `"c"`, and `"cc"` form one maximum valid split.

**Example 2**

- Input: `s = "aba"`
- Output: `2`
- Explanation: One valid maximum split is `"a"`, `"ba"`.

**Example 3**

- Input: `s = "aa"`
- Output: `1`

### Required Complexity
- **Time:** $O(n2^n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**A split is a sequence of boundary choices.** At an index `start`, every end position from `start + 1` through $n$ defines one possible next non-empty piece. Try those choices with depth-first search. A set records the pieces already selected on the current path, so a candidate already in the set is skipped immediately. After exploring a new candidate, remove it before trying the next end position; this restores precisely the state belonging to the caller's partial split.

**Keep the best complete split.** Reaching `start == n` means the selected pieces concatenate to all of `s`. Because insertion was allowed only for text absent from the set, that path is valid, and the set size can update the maximum. Conversely, every valid split corresponds to one sequence of end positions considered by the search. None of its pieces is rejected, so the search reaches its final boundary and considers its piece count. Taking the maximum over these paths therefore returns the requested optimum.

**Prune with an optimistic upper bound.** If $r = n - \texttt{start}$ characters remain, no continuation can add more than $r$ pieces because every piece is non-empty. Thus the current path can reach at most `len(used) + r` pieces. When that value is no greater than the best complete result already found, the branch cannot improve the answer and may safely stop. Trying short pieces first tends to establish a strong best value early, making this bound more effective without changing correctness.

#### Complexity detail

There are $2^{n-1}$ possible placements of boundaries between adjacent characters. In the worst case, the search examines an exponential number of corresponding partial splits. Creating and hashing a candidate slice can cost $O(n)$, giving the conservative time bound $O(n2^n)$; pruning often makes actual execution much smaller.

At one moment, the selected substrings are disjoint pieces of one prefix, so their total stored text is at most $n$ characters. The recursion depth is also at most $n$. The path set and call stack therefore use $O(n)$ auxiliary space, excluding short-lived candidate slices.

#### Alternatives and edge cases

- **Enumerate every boundary mask:** Each of the $2^{n-1}$ masks describes one split and can be checked afterward for duplicate pieces. This is simpler conceptually but cannot discard a duplicate prefix or a branch that is already unable to beat the best result.
- **Memoization by index alone:** This is incorrect because the legal choices at an index depend on every substring already used. A complete memoization key must include that path-dependent set and may itself have exponentially many states.
- A one-character string has no boundary to place and therefore returns `1`.
- Repeated letters may still form distinct pieces of different lengths; for example, `"aaaa"` can use `"a"` and `"aaa"`, so the answer is `2` rather than `1`.
- If every character is different, splitting into individual characters is valid and achieves the upper bound $n$.

</details>
