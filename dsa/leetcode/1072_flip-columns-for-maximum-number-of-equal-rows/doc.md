# Flip Columns For Maximum Number of Equal Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1072 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) |

## Problem Description

### Goal

Given an $M \times N$ binary matrix, choose any number of columns. Flipping a chosen column changes every `0` in that column to `1` and every `1` to `0`, across all rows.

After applying one shared set of column flips, count the rows whose values are all equal within that row: a qualifying row may consist entirely of zeros or entirely of ones. Return the maximum possible number of such rows over every choice of columns.

### Function Contract

**Inputs**

- `matrix`: an $M \times N$ binary matrix, where $1 \le M,N \le 300$.
- Every `matrix[i][j]` is either `0` or `1`.

**Return value**

- The greatest number of rows that can simultaneously have all values equal after flipping some set of columns.

### Examples

**Example 1**

- Input: `matrix = [[0, 1], [1, 1]]`
- Output: `1`
- Explanation: With no flips, the second row already has equal values; no flip pattern makes both rows uniform.

**Example 2**

- Input: `matrix = [[0, 1], [1, 0]]`
- Output: `2`
- Explanation: Flip the first column to turn the rows into `[1, 1]` and `[0, 0]`.

**Example 3**

- Input: `matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]`
- Output: `2`
- Explanation: Flipping the first two columns makes the last two rows uniform.

### Required Complexity

- **Time:** $O(MN)$
- **Space:** $O(MN)$

<details>
<summary>Approach</summary>

#### General

**Characterize a row's successful flip patterns:** To turn a row into all zeros, flip exactly the columns where that row contains `1`. To turn it into all ones, flip exactly the columns where it contains `0`. Those two patterns are bitwise complements.

**Normalize complements to one key:** XOR every value in a row with its first value. A row beginning with zero remains unchanged, while a row beginning with one is complemented. Thus identical rows and complementary rows produce the same normalized tuple, and no other pair does.

**Count compatible rows:** Store the frequency of every normalized tuple. All rows sharing a key can be made uniform by one column-flip set, some becoming all zeros and the complementary originals becoming all ones. Return the largest frequency.

If two rows share a normalized key, their original bits agree in every column when their first bits agree and differ in every column otherwise, so one flip pattern makes both uniform. Conversely, rows simultaneously made uniform must each equal the flip pattern or its complement before flipping, making them identical or complementary and therefore giving them the same key.

#### Complexity detail

Normalizing each of $M$ rows reads all $N$ entries, for $O(MN)$ time. Up to $M$ tuple keys of length $N$ are stored, requiring $O(MN)$ auxiliary space in the worst case.

#### Alternatives and edge cases

- **Compare every pair of rows:** Group rows by testing whether each pair is identical or complementary. It is correct but costs $O(M^2N)$ time.
- **Enumerate column subsets:** Trying all $2^N$ flip patterns is exponential and repeats equivalent work.
- **Count only identical rows:** It misses complementary rows, which can become uniform under the same flips with opposite final values.
- **One column:** Every row is already uniform, so the answer is $M$.
- **All rows identical:** Their normalized keys match and all $M$ qualify together.
- **All rows complementary pairs:** Both orientations belong to the same key.
- **Uniform rows of zeros and ones:** They normalize to the same all-zero key and require no flips to qualify together.
- **Duplicate rows:** Every occurrence is a separate row and contributes to the frequency.

</details>
