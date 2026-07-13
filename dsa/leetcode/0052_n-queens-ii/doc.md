# N-Queens II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 52 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/n-queens-ii/) |

## Problem Description
### Goal
Place exactly `n` queens on an $n \times n$ chessboard so that no queen can attack another. Thus each row and column contains one queen, and no two selected cells share either diagonal direction.

Return the number of distinct valid placements rather than constructing their board representations. Placements using different queen cells count separately, including mirror images or rotations when they occupy different coordinates. For board sizes with no solution, return zero; the $1 x 1$ board has one placement.

### Function Contract
**Inputs**

- `n`: the board width and number of queens, with $1 \le n \le 9$

**Return value**

The integer number of valid placements.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1`

**Example 2**

- Input: `n = 4`
- Output: `2`

**Example 3**

- Input: `n = 5`
- Output: `10`

### Required Complexity

- **Time:** $O(n!)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count placements without constructing board strings**

Search one row at a time. The recursion depth fixes the row, so only columns and diagonal attacks are needed. Let the low `n` bits of `board_mask` represent board columns. Free positions in the current row are:

```text
board_mask & ~(columns | descending | ascending)
```

Unlike problem 51, no column path or rendered board is required. A recursive call can return the number of solutions below its state, and the parent sums those counts.

**Enumerate set bits and propagate attacks**

Extract the lowest free bit with `bit = available & - available`, then remove it from the local candidate mask. Recurse with `columns | bit`. For the next row, shift the two diagonal masks in opposite directions because each diagonal attack moves one column as the row increases.

If `columns = board_mask`, all `n` columns contain queens. Since recursion places at most one queen per row and advances once per queen, this state is one complete placement and contributes `1`. A state with no available bit before completion contributes `0`.

**Each recursive state represents a unique partial placement**

At recursion depth `row`, exactly `row` mutually nonattacking queens have been placed, `columns` identifies their distinct columns, and the shifted diagonal masks identify exactly the columns those queens attack in this row. Every available bit therefore extends the state safely.

Masks are passed by value, so sibling branches require no explicit undo operation. Different sequences of selected column bits produce different queen coordinates and cannot reach the same placement leaf.

**Trace the two $n = 4$ branches**

For $n = 4$, a first queen in column 1 leaves only compatible bits in each following row and reaches one complete placement. The branch beginning in column 2 reaches its reflection. All other prefixes lose every free bit, so the final count is 2.

**Count leaves of the exact placement tree**

Every followed bit selects a column safe from all earlier queens, and each recursive level advances to a new row. A depth-`n` leaf is therefore one valid complete placement and contributes exactly one to the count.

Any valid placement supplies a safe column bit at every row prefix, so none of its choices is pruned and the search reaches its leaf. Distinct sequences of row bits describe distinct queen placements, so summing leaves counts every solution once without constructing boards.

#### Complexity detail

The decreasing-column search has an $O(n!)$ upper bound, with diagonal conflicts pruning many prefixes earlier. Recursion depth is `n`, and each frame stores constant mask state, for $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Generate boards as in N-Queens:** produces information the count-only contract does not need and spends output-allocation time.
- **Enumerate all column permutations:** checks diagonal conflicts only after complete placements and explores all $n!$ leaves.
- **Boolean arrays or sets:** preserve the same pruning but use more state and per-operation overhead than integer masks.
- $n = 1$ reaches one complete state. For $n = 2$ and $n = 3$, every branch runs out of safe bits and the sum remains zero.
- Symmetry can nearly halve some searches by pairing reflected first-row choices, but requires careful handling of the center column for odd `n`; the direct enumeration is simpler and already within the constraints.

</details>
