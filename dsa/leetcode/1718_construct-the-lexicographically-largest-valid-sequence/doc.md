# Construct the Lexicographically Largest Valid Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1718 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/) |

## Problem Description

### Goal

Given an integer `n`, construct a sequence whose elements lie in the range from $1$ through $n$. The value $1$ must occur exactly once. Every value $i$ with $2 \le i \le n$ must occur exactly twice, and the absolute difference between the indices of its two occurrences must equal $i$. These multiplicities make the sequence length $2n - 1$.

Among all sequences satisfying those distance rules, return the lexicographically largest one. Two equal-length sequences are compared at their first differing position, where the sequence containing the larger value ranks higher. A valid sequence is guaranteed to exist for every legal `n`.

### Function Contract

**Inputs**

- `n`: the largest value in the sequence, with $1 \le n \le 20$.

**Return value**

- Return the lexicographically largest valid integer sequence of length $2n - 1$.

### Examples

**Example 1**

- Input: `n = 3`
- Output: `[3,1,2,3,2]`
- Explanation: Both copies of $2$ and $3$ are separated by their values, and no valid sequence begins with a larger lexicographic prefix.

**Example 2**

- Input: `n = 5`
- Output: `[5,3,1,4,3,5,2,4,2]`
- Explanation: Each value above $1$ appears at indices whose difference equals that value.

**Example 3**

- Input: `n = 1`
- Output: `[1]`
- Explanation: The sole required value is also the complete sequence.

### Required Complexity

- **Time:** $O(n!)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Fix the earliest undecided position**

Maintain an array of length $2n - 1$, initially filled with zeroes, and a set of values already placed. At each recursive step, advance to the first zero position. If a value greater than $1$ is chosen there, its second occurrence has only one possible location: `index + value`. The placement is legal exactly when that paired index is in bounds and still empty. The value $1$ occupies only the current position.

**Try candidates in descending order**

At the first undecided position, consider unused values from `n` down to `1`. This orders the search by lexicographic preference: every completion under a larger current value is lexicographically greater than every completion under a smaller one, regardless of their suffixes. After a legal placement, recurse; if the suffix cannot be completed, erase the placed occurrence or occurrences and try the next value.

**Stop at the first complete arrangement**

When no zero position remains, every value has the required multiplicity because each recursive choice marks one previously unused value, and every value above $1$ was placed at exactly the required index distance. Descending candidate order means all lexicographically greater prefixes were either tried or proved impossible before this complete sequence was reached. Therefore the first complete arrangement is the required maximum, and no enumeration of later valid sequences is necessary.

#### Complexity detail

There are at most $n$ candidate values at the first level, at most $n-1$ unused candidates at the next, and so on. The resulting worst-case search is bounded by $O(n!)$ recursive choices; range checks, placements, and removals are constant-time, while filled positions are skipped across a path. The sequence, used-value table, and recursion stack each require $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every valid sequence:** Exploring all complete arrangements and retaining the largest is correct, but it discards the decisive early-stop benefit of descending lexicographic search.
- **Ascending candidate order:** This can find a valid sequence, but its first completion is biased toward the lexicographically smallest prefix and cannot be returned as the requested maximum.
- **Copy state at every recursion:** Passing fresh sequence and used-value copies simplifies undo logic but adds allocation and copying overhead at every search node.
- **The value one:** It occurs once and therefore has no paired index; treating it like the other values would incorrectly require a second copy.
- **Occupied paired positions:** A value above $1$ cannot be placed unless both its current position and `index + value` are empty.
- **Minimum input:** For `n = 1`, the backtracking immediately places the single `1` and returns `[1]`.

</details>
