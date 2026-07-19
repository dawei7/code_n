## General
**Represent each rhombus by a center and radius**

For a positive radius $K$, a center cell $(r,c)$ determines corners at $(r-K,c)$, $(r,c+K)$, $(r+K,c)$, and $(r,c-K)$. The shape fits exactly when all four coordinates stay inside the matrix. Radius zero is handled separately by recording the center cell itself.

**Precompute both diagonal directions**

Build one prefix table along down-right diagonals and another along down-left diagonals. A subtraction within either table gives the sum of any contiguous diagonal edge in constant time. Combining four such edge queries yields a border sum. The chosen half-open edge ranges must count each of the four corners once: in the implemented formula the bottom corner is initially counted twice and the top corner omitted, so subtracting the former and adding the latter restores the exact border.

**Enumerate every valid border**

Visit every possible center and every radius through the largest one that fits around it. This describes every positive-area rhombus uniquely, while adding each cell covers every zero-area rhombus. Therefore every legal sum is considered and no nonzero shape is generated from two different centers and radii.

**Keep only the largest distinct sums**

Maintain a set containing at most three values. After inserting a new sum, remove the minimum if the set grows past three. At every point the set is exactly the three largest distinct sums seen so far, or all of them when fewer than three exist. Sorting this constant-size set in reverse order produces the required result.

## Complexity detail
Let $K=\min(M,N)$. Constructing the two diagonal prefix tables takes $O(MN)$ time and space. Across all centers there are at most $O(MNK)$ valid radii, and each border sum plus top-three update costs $O(1)$. The total time is therefore $O(MNK)$, which is $O(MN\min(M,N))$, and the prefix tables require $O(MN)$ space.

## Alternatives and edge cases
- **Walk every border cell:** It is straightforward and useful as an oracle, but spending $O(K)$ time per rhombus raises the total to $O(MNK^2)$ on square grids.
- **Store and sort every sum:** This is correct but uses space proportional to the number of rhombi and performs unnecessary sorting when only three values are needed.
- **Heap of three values:** A min-heap plus a membership set also maintains the top three distinct sums, with slightly more bookkeeping.
- **One row or one column:** No positive-area rhombus fits, so only distinct cell values can appear.
- **Zero-area shapes:** A single cell is a valid rhombus sum and must not be omitted.
- **Corner accounting:** Summing four closed diagonal edges counts every corner twice; use half-open edges or explicitly correct the duplicates.
- **Repeated sums:** Distinctness concerns numerical sums, not shapes; many different borders may contribute the same value only once.
- **Fewer than three values:** Return the available distinct sums without padding.
