# Flipping an Image

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 832 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Bit Manipulation, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flipping-an-image/) |

## Problem Description

### Goal

You are given an $n \times n$ binary matrix `image`. First flip the image horizontally, which means reversing the order of the entries within every row while leaving the row order unchanged.

Then invert the flipped image: replace every `0` with `1` and every `1` with `0`. Return the matrix after both operations have been applied in that order, with the same dimensions as the input.

### Function Contract

**Inputs**

- `image`: an $n \times n$ matrix containing only `0` and `1`, where $1 \le n \le 20$

**Return value**

- The binary matrix obtained by reversing each row and then inverting every entry

### Examples

**Example 1**

- Input: `image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]`
- Output: `[[1, 0, 0], [0, 1, 0], [1, 1, 1]]`
- Explanation: Reversing the rows produces `[[0, 1, 1], [1, 0, 1], [0, 0, 0]]`; inverting those bits gives the output.

**Example 2**

- Input: `image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]`
- Output: `[[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]`

**Example 3**

- Input: `image = [[0]]`
- Output: `[[1]]`
- Explanation: Reversal leaves the one-cell row in place, and inversion changes its bit.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Map each output position directly to its source**

In a row of length $n$, output column $c$ receives the input value from column $n-1-c$ after the horizontal flip. Because that value is binary, XOR with `1` inverts it. Build each output row with the executable transformation `value ^ 1` while iterating through `reversed(row)`.

**Combine the two required operations without an intermediate image**

Reversal changes only positions, and inversion changes only values, so applying the inversion as each reversed value is emitted has exactly the same result as materializing a fully flipped matrix and scanning it again. Process every input row independently and append its transformed row to the result.

Each output cell uses the unique input cell at the mirrored column and stores its complement. Thus every row is horizontally reversed, every bit is inverted once, and row order is preserved. Since this establishes the required value at every matrix coordinate, the returned image is correct.

#### Complexity detail

The square image contains $n^2$ cells. Each cell is read once and one output cell is written for it, so the time is $O(n^2)$. The returned matrix contains $n^2$ entries and therefore uses $O(n^2)$ space; apart from that output, the construction needs only loop state.

#### Alternatives and edge cases

- **Two explicit passes:** Reverse every row first and then scan the matrix to invert it. This is also $O(n^2)$ but performs an avoidable second traversal.
- **In-place two pointers:** Swap mirrored cells while inverting both, handling the center cell separately for odd $n$. It uses $O(1)$ auxiliary space when mutation is acceptable.
- **Repeated mirrored-source search:** Scanning a row from the beginning to locate the source of every output column is correct but takes $O(n^3)$ time across the matrix instead of using direct indexing.
- **One-cell image:** Reversal has no positional effect, but inversion still changes the bit.
- **Odd row length:** The center cell maps to itself and must still be inverted exactly once.
- **Symmetric row:** Even when reversal leaves the pattern visually unchanged, every bit is complemented.
- **Operation order:** For this bitwise transformation, direct mirrored complementation is equivalent to the required flip-then-invert sequence.

</details>
