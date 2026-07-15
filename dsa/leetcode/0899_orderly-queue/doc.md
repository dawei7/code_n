# Orderly Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 899 |
| Difficulty | Hard |
| Topics | Math, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/orderly-queue/) |

## Problem Description
### Goal
You are given a lowercase English string `s` and an integer `k`. In one move, choose any one of the first `k` characters currently in the string, remove that character from its position, and append it to the end.

The move may be applied any number of times, including zero. Each choice changes which characters occupy the first `k` positions and can therefore enable later choices.

Return the lexicographically smallest string reachable through this process.

### Function Contract
Let $n$ be the length of `s`.

**Inputs**

- `s`: a string of lowercase English letters with $1 \leq n \leq 1000$.
- `k`: the size of the selectable prefix, where $1 \leq k \leq n$.

**Return value**

Return the lexicographically smallest string obtainable after any number of valid moves.

### Examples
**Example 1**

- Input: `s = "cba", k = 1`
- Output: `"acb"`

Only the first character can move, so the reachable strings are rotations; moving `"c"` and then `"b"` produces the smallest rotation.

**Example 2**

- Input: `s = "baaca", k = 3`
- Output: `"aaabc"`

**Example 3**

- Input: `s = "abc", k = 1`
- Output: `"abc"`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**When only the first character may move**

For $k=1$, every move removes the first character and appends it, which is exactly a left rotation. No other relative ordering is reachable, so the answer is the lexicographically smallest rotation of `s`.

Find that rotation with Booth's algorithm. Compare two candidate starting indices in the doubled string `s + s`. If their first differing offset has a larger character for one candidate, that candidate and every start skipped through that offset cannot be minimal; advance it past the mismatch and restart the offset comparison. Each starting position is discarded at most once, so the minimum rotation is found in linear time.

**When at least two characters may move**

For $k \geq 2$, choosing among the first two positions is already enough to reach every permutation. Moving the second character and then rotating the remaining prefix to the end can swap the first two characters while preserving the others. Ordinary rotations move any adjacent pair into those positions, so arbitrary adjacent swaps—and therefore arbitrary permutations—are reachable.

The smallest permutation is the characters in sorted order. Because the alphabet has exactly 26 lowercase letters, count each letter and emit them from `"a"` through `"z"` in $O(n)$ time.

These two cases exhaust all valid `k`. Booth's algorithm selects the minimum of exactly the reachable rotations when $k=1$. For $k \geq 2$, reachability of every permutation proves that the globally sorted arrangement is attainable, and no permutation can be lexicographically smaller. Thus the returned string is optimal in either case.

#### Complexity detail

Booth's algorithm examines and discards candidate starts in $O(n)$ time, and the doubled string uses $O(n)$ space. For $k \geq 2$, counting and rebuilding the string take $O(n)$ time; the fixed 26-entry count table is constant auxiliary storage, while the returned string occupies $O(n)$ space. The overall bounds are $O(n)$ time and $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every rotation:** For $k=1$, constructing and comparing all $n$ rotations is correct but takes $O(n^2)$ time.
- **Comparison sort for multiple choices:** Returning `"".join(sorted(s))` for $k \geq 2$ is correct and concise, but comparison sorting costs $O(n \log n)$ instead of exploiting the fixed alphabet.
- **Breadth-first search of reachable strings:** State exploration becomes factorial when $k \geq 2$ and is unnecessary after proving full permutation reachability.
- **One character:** The sole string is already the answer for the only valid value `k = 1`.
- **Repeated characters:** Booth's algorithm tolerates equal candidate prefixes, and counting preserves the exact multiplicity of every letter.
- **Already smallest rotation:** Applying zero moves is allowed, so the original string may remain the answer.
- **Full prefix:** When `k = n` and $n \geq 2$, every permutation remains reachable and the sorted string is returned.

</details>
