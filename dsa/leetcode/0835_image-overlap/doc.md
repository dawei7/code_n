# Image Overlap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 835 |
| Difficulty | Medium |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/image-overlap/) |

## Problem Description
### Goal
Two images, `img1` and `img2`, are represented by binary square matrices of size `n` by `n`. A translation slides all `1` bits of one image together by any number of units left, right, up, and/or down before that image is placed over the other. The overlap is the number of positions containing `1` in both images.

Translation never rotates an image. Any `1` bit moved beyond a matrix border disappears. Choose any translation of either image and return the largest overlap that can be obtained.

### Function Contract
**Inputs**

- `img1`: an `n` by `n` matrix containing only `0` and `1`.
- `img2`: another binary `n` by `n` matrix.
- Both images have the same side length, with $1 \leq n \leq 30$.

**Return value**

Return the maximum number of aligned positions at which both images contain `1` after translating one image without rotation.

### Examples
**Example 1**

- Input: `img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]], img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]`
- Output: `3`

Moving `img1` one unit right and one unit down aligns three of its `1` bits with `1` bits in `img2`.

**Example 2**

- Input: `img1 = [[1]], img2 = [[1]]`
- Output: `1`

**Example 3**

- Input: `img1 = [[0]], img2 = [[0]]`
- Output: `0`

### Required Complexity
- **Time:** $O(n^3)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Compress each row into one word**

Since $n \leq 30$, encode every matrix row as an integer bitmask that fits in one machine word. A horizontal translation becomes a left or right bit shift. Taking bitwise AND with the corresponding row of the other image retains exactly the positions where both images contain `1`, and the resulting population count is that row pair's overlap.

**Enumerate every meaningful translation**

A horizontal or vertical displacement outside $[-(n-1),n-1]$ cannot preserve any matrix position, so only $(2n-1)^2$ translations matter. For each vertical displacement, pair every still-in-bounds row from `img1` with its translated row in `img2`. Apply the horizontal shift, intersect the two row masks, and add the number of set bits. Bits shifted beyond the border cannot contribute because no bit is set there in the fixed-width `img2` row mask.

Every allowed translation is inspected. For a fixed translation, each aligned `1` pair is counted once in its shared row and column, while every non-aligned or erased bit contributes zero. The largest total over the enumeration is therefore exactly the largest possible overlap. Translating `img2` instead would merely negate both displacement components and yields the same set of overlap totals.

#### Complexity detail

There are $O(n^2)$ relevant translations, and each examines at most $n$ pairs of row masks. With $n \leq 30$, shifts, AND, and population count operate on one machine word, so the total is $O(n^3)$ time. The two arrays of row masks use $O(n)$ space.

#### Alternatives and edge cases

- **Cell scan for every translation:** Testing all $n^2$ cells for each of $O(n^2)$ displacements is correct but costs $O(n^4)$ time.
- **Count coordinate differences:** Pairing every `1` coordinate from `img1` with every `1` coordinate from `img2` and counting their displacement is elegant for sparse images, but its dense worst case is $O(n^4)$.
- **All-zero image:** If either image contains no `1`, every translation has overlap zero.
- **No movement:** The zero displacement is included and may be optimal when the images already align.
- **Discarded border bits:** A shifted bit outside the square is ignored rather than wrapped to the opposite edge.
- **Translation symmetry:** It is sufficient to move `img1`; moving `img2` covers the same relative displacements with reversed signs.

</details>
