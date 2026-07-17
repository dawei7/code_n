# Number of Ways to Form a Target String Given a Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1639 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) |

## Problem Description
### Goal
You are given a list `words` whose strings all have the same length and a string `target`. Form `target` from left to right by choosing characters from the dictionary.

To form `target[i]`, choose a character `words[j][k]` equal to it. After using column `k`, no character at column $k$ or any earlier column may be used again from any word; the next chosen column must therefore be strictly larger. Different word choices at the same selected columns count as different ways, and multiple chosen characters may come from the same word.

Return the number of valid ways modulo $10^9+7$.

### Function Contract
**Inputs**

- `words`: an array of $W$ lowercase English strings, where $1 \le W \le 1000$.
- Every word has the same length $L$, where $1 \le L \le 1000$.
- `target`: a lowercase English string of length $T$, where $1 \le T \le 1000$.

**Return value**

Return the number of sequences of strictly increasing dictionary columns and matching word choices that spell `target`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `words = ["acca","bbbb","caca"], target = "aba"`
- Output: `6`

For example, columns 0, 1, and 3 can supply `a`, `b`, and `a`; the multiplicities of matching characters in those columns create several distinct word choices.

**Example 2**

- Input: `words = ["abba","baab"], target = "bab"`
- Output: `4`

**Example 3**

- Input: `words = ["abcd"], target = "abcd"`
- Output: `1`

The single word supplies each character from the next column.

### Required Complexity
- **Time:** $O(WL+LT)$
- **Space:** $O(L+T)$

<details>
<summary>Approach</summary>

#### General

**Collapse word identity into column multiplicities.** Once a column is selected for a target character, only the number of words carrying that character in the column matters. Precompute a 26-character frequency table for every one of the $L$ columns by scanning all $W$ words. Choosing a character from a column then has exactly that frequency many distinct word choices.

**Treat each column as a skip-or-use decision.** Let `ways[i]` be the number of ways to form the first $i$ characters of `target` using only columns already processed. Initially `ways[0] = 1`. At a column with `count[c]` copies of character `c`, every existing way for prefix length $i$ can use this column for `target[i]`, contributing `ways[i] * count[target[i]]` to `ways[i + 1]`. It may also skip the column, leaving all existing states unchanged.

**Update target prefixes backward.** Process $i$ from the largest reachable target index down to zero. A descending update prevents a contribution just created with the current column from being reused to form another target character at that same column. Thus every transition either skips the column or consumes it once, and the processing order enforces strictly increasing selected columns.

Every valid construction has a unique last selected column and word choice, so it appears in exactly one use transition. Conversely, every transition appends a matching character from a later column and therefore produces a valid partial construction. Taking all arithmetic modulo $10^9+7$ preserves the required final residue.

#### Complexity detail

Building the column frequency tables takes $O(WL)$ time. Processing each of $L$ columns against at most $T$ target positions takes $O(LT)$ time, for $O(WL+LT)$ total. The 26 counts per column require $O(L)$ space because the alphabet size is constant, and the rolling prefix array requires $O(T)$, giving $O(L+T)$ auxiliary space.

#### Alternatives and edge cases

- **Top-down memoization:** A state consisting of target position and next column can skip or use that column. With precomputed counts it has the same $O(LT)$ DP work, but recursion adds stack overhead and still needs the $O(WL)$ preprocessing.
- **Recount each transition:** Scanning all words whenever a DP state asks for a column's character frequency is correct but increases the transition phase to $O(WLT)$.
- **Enumerate word and column choices:** Direct backtracking grows exponentially with target length because it repeats equivalent suffix subproblems.
- If $T>L$, no strictly increasing sequence has enough columns, so the answer is zero.
- A target character absent from every remaining column makes all later complete-target counts zero.
- Identical words remain distinct dictionary entries; each matching row is a separate choice and must contribute to the multiplicity.
- Choosing multiple characters from one word is permitted as long as their column indices increase.
- Modular reduction must be applied during updates because the unreduced count can be enormous.

</details>
