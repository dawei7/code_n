# Product of Two Run-Length Encoded Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/) |
| Frontend ID | 1868 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A run-length encoding represents an integer array as pairs `[value, frequency]`. Each pair expands to `frequency` consecutive copies of `value`, and adjacent pairs never store the same value. Two such encodings, `encoded1` and `encoded2`, represent arrays of equal decoded length.

Multiply the two decoded arrays element by element, then return the run-length encoding of that product array. The returned encoding must also be compressed: if consecutive product positions have the same value, they belong to one pair whose frequency covers the whole run. Process the encodings directly rather than materializing the potentially much longer decoded arrays.

### Function Contract

**Inputs**

- `encoded1`: a nonempty list of `[value, frequency]` pairs with positive values and frequencies; adjacent values differ.
- `encoded2`: another valid encoding whose decoded length equals that of `encoded1`.
- Let $M = \lvert\texttt{encoded1}\rvert$ and $N = \lvert\texttt{encoded2}\rvert$.

**Return value**

- Return the run-length encoding of the elementwise product of the two decoded arrays.
- Every returned frequency is positive, and adjacent returned pairs must have different product values.

### Examples

**Example 1**

- Input: `encoded1 = [[1,3],[2,3]]`, `encoded2 = [[6,3],[3,3]]`
- Output: `[[6,6]]`

Both aligned run products equal `6`, so they merge into one six-element run.

**Example 2**

- Input: `encoded1 = [[1,3],[2,1],[3,2]]`, `encoded2 = [[2,3],[3,3]]`
- Output: `[[2,3],[6,1],[9,2]]`

The run boundaries differ, but the pointers consume only the overlap at each step.

**Example 3**

- Input: `encoded1 = [[4,5]]`, `encoded2 = [[2,2],[3,3]]`
- Output: `[[8,2],[12,3]]`

One long run may overlap several runs from the other encoding.
