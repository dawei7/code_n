# Decode the Slanted Ciphertext

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2075 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-the-slanted-ciphertext/) |

## Problem Description

### Goal

A slanted transposition cipher arranges an original string in a matrix with a fixed number of rows. Starting in successive columns of the top row, it writes characters along diagonals that move one row down and one column right. Any matrix cells left unused are spaces, and the number of columns is the smallest one for which the rightmost column receives a character.

The encoded text is obtained afterward by reading the entire matrix row by row. Given that row-major string and the matrix's row count, recover the original diagonal reading order. The original text has no trailing spaces, and every input is guaranteed to identify exactly one original string.

### Function Contract

**Inputs**

- `encodedText`: a valid row-major cipher string of length $L$, containing only lowercase English letters and spaces, where $0 \le L \le 10^6$.
- `rows`: the fixed number of matrix rows, where $1 \le \texttt{rows} \le 1000$. The matrix has $C = L / \texttt{rows}$ columns; when $L=0$, $C=0$.

**Return value**

- Return the uniquely decoded original string without trailing spaces.

### Examples

**Example 1**

- Input: `encodedText = "ch   ie   pr", rows = 3`
- Output: `"cipher"`
- Explanation: Reading diagonally from successive top-row columns produces the letters of `cipher`.

**Example 2**

- Input: `encodedText = "iveo    eed   l te   olc", rows = 4`
- Output: `"i love leetcode"`
- Explanation: Diagonal traversal restores both the letters and the meaningful spaces inside the original text.

**Example 3**

- Input: `encodedText = "coding", rows = 1`
- Output: `"coding"`
- Explanation: A one-row matrix has the same row-major and diagonal reading orders.
