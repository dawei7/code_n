# Vowels Game in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3227 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Game Theory, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/vowels-game-in-a-string/) |

## Problem Description

### Goal

Alice and Bob play on a lowercase English string `s`, with Alice moving first. Alice must remove a nonempty substring containing an odd number of vowels. Bob must remove a nonempty substring containing an even number of vowels, where zero is even.

After removal, the remaining prefix and suffix join to form the next string. A player who has no legal substring on their turn loses, and both players choose optimally. Return `true` exactly when Alice has a winning strategy. The vowels are `a`, `e`, `i`, `o`, and `u`.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert\texttt{s}\rvert \leq 10^5$.

**Return value**

Return whether Alice wins under optimal play.

### Examples

**Example 1**

- Input: `s = "leetcoder"`
- Output: `true`
- Explanation: The string contains vowels, so Alice can force the winning parity invariant.

**Example 2**

- Input: `s = "bbcd"`
- Output: `false`
- Explanation: No substring contains an odd number of vowels, so Alice cannot move.

**Example 3**

- Input: `s = "a"`
- Output: `true`
- Explanation: Alice removes the entire one-vowel string and Bob receives the empty string.
