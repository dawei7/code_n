# Letter Tile Possibilities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1079 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/letter-tile-possibilities/) |

## Problem Description

### Goal

You have $n$ tiles, and each tile has the uppercase English letter `tiles[i]` printed on it. A tile can be used at most once, while different physical tiles bearing the same letter are indistinguishable in the sequence they produce.

Count the possible non-empty sequences of letters that can be made from the printed letters. A sequence may use any positive number of the available tiles, so arrangements of different lengths and different letter orders are all included, but duplicate strings formed by exchanging equal-letter tiles are counted only once.

### Function Contract

**Inputs**

- `tiles`: a string of $n$ uppercase English letters, where $1 \le n \le 7$.
- Let $D$ be the number of distinct letters, and let $c_j$ be the available count of distinct letter $j$.
- Define the number of possible remaining-count states as

$$
M = \prod_{j=1}^{D}(c_j+1).
$$

**Return value**

- The number of distinct non-empty letter sequences constructible without using any tile more often than it occurs.

### Examples

**Example 1**

- Input: `tiles = "AAB"`
- Output: `8`

The sequences are `"A"`, `"B"`, `"AA"`, `"AB"`, `"BA"`, `"AAB"`, `"ABA"`, and `"BAA"`.

**Example 2**

- Input: `tiles = "AAABBC"`
- Output: `188`

**Example 3**

- Input: `tiles = "V"`
- Output: `1`

### Required Complexity

- **Time:** $O(DM)$
- **Space:** $O(M+n)$

<details>
<summary>Approach</summary>

#### General

**Represent identical tiles by counts:** Count each distinct letter and store only the tuple of remaining counts. This removes physical identities that could otherwise create duplicate branches for equal letters.

**Count suffixes from a state:** For a remaining-count tuple, try each letter whose count is positive. Choosing it contributes one sequence consisting of that letter alone, plus every longer sequence obtained by choosing a suffix from the decremented state. Restore the count after the recursive call before considering the next first letter.

**Reuse equivalent subproblems:** Different prefixes can leave exactly the same multiset of unused tiles. Memoizing by the remaining-count tuple computes the number of possible suffixes from that multiset once. The empty sequence is never added: each term enters the total only when an actual letter is chosen.

Every legal non-empty sequence has a unique first letter and a remaining suffix constructible from the state after consuming that letter, so it belongs to exactly one recurrence branch. Conversely, each branch consumes an available tile and recursively consumes only available tiles, so every counted sequence is legal. Count-state representation makes equal-letter tile swaps the same branch rather than duplicates.

#### Complexity detail

There are at most $M$ remaining-count tuples. Each state checks $D$ letter types, giving $O(DM)$ time. The memo stores at most $M$ results, while the recursion depth is at most $n$, for $O(M+n)$ auxiliary space.

#### Alternatives and edge cases

- **Plain count backtracking:** Omit memoization and construct each distinct sequence implicitly. It is simple and avoids duplicates, but equivalent remaining multisets may be solved repeatedly.
- **Permute physical tile indices into a set:** It eventually deduplicates equal-letter strings, but can explore factorially many redundant index orders when letters repeat.
- **Sort and skip equal choices:** Standard permutation backtracking can avoid duplicates at each depth, but count states express the multiset more directly.
- **All tiles equal:** Exactly the $n$ sequences of lengths one through $n$ are possible.
- **All tiles distinct:** Every ordered selection of every positive length is distinct.
- **Single tile:** The answer is one.

</details>
