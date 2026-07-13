# Lonely Pixel II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 533 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/lonely-pixel-ii/) |

## Problem Description
### Goal
Given a black-and-white picture and a positive integer `target`, inspect each black pixel at `(row, col)`. Its row and column must each contain exactly `target` black pixels.

The pixel qualifies only if every row that has a black pixel in column `col` is identical to its own row across all columns. Return the total number of qualifying black pixels, counting each coordinate separately. Matching row counts without identical row patterns is insufficient, and a column containing the required number of black pixels may contribute all of them when their rows satisfy the shared-pattern rule.

### Function Contract
**Inputs**

- `picture`: a rectangular matrix containing `"B"` and `"W"`
- `target`: the required number of black pixels in the qualifying row and column

**Return value**

- The number of black pixels satisfying both count conditions and the identical-row condition

### Examples
**Example 1**

- Input: `picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3`
- Output: `6`

**Example 2**

- Input: `picture = [["B","W","B"],["B","W","B"]], target = 2`
- Output: `4`

**Example 3**

- Input: `picture = [["B","W","B"],["B","W","B"],["B","W","B"]], target = 2`
- Output: `0`

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(rows \cdot cols)$

<details>
<summary>Approach</summary>

#### General

**Count columns and whole-row patterns**

Scan each row, add its black pixels to the column counts, and represent the entire row as an immutable pattern. Only patterns containing exactly `target` black cells can satisfy the row condition; count how many times each such pattern occurs.

**Recognize the required block of identical rows**

If a qualifying pattern occurs exactly `target` times, each black position in that pattern appears in all of those rows. A column at that position is valid precisely when its total black count is also `target`; then no additional, different row can contain a black pixel in that column.

**Count pixels by groups rather than individually**

For every pattern occurring `target` times, inspect its black positions. Each position whose column count is `target` contributes all `target` pixels from the identical rows at once.

**Why the grouped count is exact**

Every contributed column has exactly the `target` identical pattern rows as its black rows, so every contributed pixel meets all conditions. Conversely, a valid pixel's row pattern has `target` black cells, its column has `target` black cells, and all black rows in that column are identical; therefore that pattern occurs exactly `target` times and the grouped calculation includes the pixel.

#### Complexity detail

Creating patterns, counting columns, and inspecting qualifying patterns process $O(rows \cdot cols)$ characters. Stored row-pattern keys can occupy $O(rows \cdot cols)$ space, while column counts use $O(cols)$.

#### Alternatives and edge cases

- **Validate every black pixel directly:** repeatedly counts axes and compares rows, which can become polynomially slower on a dense picture.
- **Group row indices by serialized row:** is equivalent to pattern frequencies but retains unnecessary index lists.
- **Correct row count but wrong column count:** contributes nothing.
- **Correct counts with differing rows:** violates the identical-row condition even if every axis total matches.
- **Pattern occurring more than `target` times:** makes each of its black columns exceed the target count.
- **No qualifying pattern:** returns zero without any special case.

</details>
