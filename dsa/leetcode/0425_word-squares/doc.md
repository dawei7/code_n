# Word Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 425 |
| Difficulty | Hard |
| Topics | Array, String, Backtracking, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/word-squares/) |

## Problem Description
### Goal
Given unique lowercase words of one common length `n`, construct ordered sequences of exactly `n` words. A sequence is a word square when its character grid is symmetric: for every valid pair of indices, character `j` of word `i` equals character `i` of word `j`.

Return every word square formable from the supplied words in any order. A dictionary word may be selected more than once within one square, and different row orders can create different results. Every row and corresponding column must spell the same complete word; matching only prefixes before the final row is not enough.

### Function Contract
**Inputs**

- `words`: a list of distinct lowercase words, all having the same length

**Return value**

- Return every word square that can be formed from the supplied words; a word may be selected more than once, and the squares may be returned in any order.

### Examples
**Example 1**

- Input: `words = ["area", "lead", "wall", "lady", "ball"]`
- Output: `[["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]`

**Example 2**

- Input: `words = ["abat", "baba", "atan", "atal"]`
- Output: `[["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]]`

**Example 3**

- Input: `words = ["a"]`
- Output: `[["a"]]`

### Required Complexity

- **Time:** $O(NL^2 + PL)$
- **Space:** $O(NL^2 + L^2)$

<details>
<summary>Approach</summary>

#### General

**Derive the next row's forced prefix**

Suppose `k` rows have already been chosen. Symmetry requires the next word's character at every earlier column `r` to equal row `r`'s character at column `k`. Therefore the next word must begin with `square[0][k] square[1][k] ... square[k - 1][k]`. No other property of the next word needs to be tested yet.

**Index all words by every prefix**

Build a map from each prefix, including the empty prefix, to the words beginning with it. A backtracking state computes its forced prefix and branches only over the matching map entry instead of rescanning all input words. Start from the empty square; its empty prefix naturally offers every word as the first row.

**Complete exactly at the common word length**

When the partial square contains `L` words of length `L`, every pair of coordinates has been constrained when its later row was added. Copy that sequence into the result. After returning, remove the last word so the same prefix state can explore its remaining candidates.

**Why prefix pruning is complete and sound**

Every emitted sequence satisfies all newly introduced symmetry equations at each depth, hence is a word square. Conversely, any valid completion must use a next word with exactly the derived prefix, so it appears in the indexed candidate list and is never pruned. Induction over the depth shows that backtracking visits every valid square.

#### Complexity detail

Let `N` be the number of words, `L` their length, and `P` the number of partial-square states visited. Materializing all prefixes costs $O(NL^2)$ character work and storage. Each state derives a prefix of length at most `L`, giving $O(PL)$ search time. The active square and derived prefixes use $O(L^2)$ beyond the prefix index and returned output.

#### Alternatives and edge cases

- **Trie with candidate lists:** stores the same prefix information structurally and provides equivalent pruning and asymptotic bounds.
- **Scan every word at every state:** avoids a prefix index but adds an $O(N)$ candidate scan to each state.
- **Try every length-`L` word sequence:** takes $O(NᴸL^2)$ time before symmetry filtering.
- **One-letter words:** each input word independently forms a one-row square.
- **Word reuse:** the same dictionary word may occupy several rows; do not mark words as consumed.
- **No completion:** return an empty list when every partial square is pruned.

</details>
