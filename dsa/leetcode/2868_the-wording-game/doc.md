# The Wording Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2868 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Two Pointers, String, Greedy, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [The Wording Game](https://leetcode.com/problems/the-wording-game/) |

## Problem Description

### Goal

Alice and Bob own lexicographically sorted word lists `a` and `b`. Alice begins by playing the lexicographically smallest word in `a`. After that forced opening, the players alternate turns and select words from their own lists.

A new word must be lexicographically greater than the word played immediately before it. Its first letter must also be either the same as the previous word's first letter or the next letter of the alphabet. A player who has no legal word on their turn loses.

All words across the two lists are distinct. Assuming both players choose optimally, determine whether Alice can force a win.

### Function Contract

**Inputs**

- `a`: Alice's nonempty list of lowercase words in lexicographic order.
- `b`: Bob's nonempty list of lowercase words in lexicographic order.

Each list contains at most $10^5$ words. Define

$$
S = \sum_{w \in \texttt{a}} \lvert w \rvert + \sum_{w \in \texttt{b}} \lvert w \rvert.
$$

The combined words are distinct and $S \le 10^6$.

**Return value**

- `true` if Alice wins with optimal play; otherwise `false`.

### Examples

**Example 1**

- Input: `a = ["avokado","dabar"], b = ["brazil"]`
- Output: `false`
- Explanation: Alice must open with `"avokado"`. Bob can advance to `"brazil"`, after which Alice cannot legally jump from initial `b` to her remaining `d` word.

**Example 2**

- Input: `a = ["ananas","atlas","banana"], b = ["albatros","cikla","nogomet"]`
- Output: `true`
- Explanation: Bob's only word beginning with `a` is smaller than Alice's forced opening, and he has no playable word beginning with `b`.

**Example 3**

- Input: `a = ["hrvatska","zastava"], b = ["bijeli","galeb"]`
- Output: `true`
- Explanation: Both of Bob's words are lexicographically smaller than Alice's opening and start before `h`, so Bob has no legal move.
