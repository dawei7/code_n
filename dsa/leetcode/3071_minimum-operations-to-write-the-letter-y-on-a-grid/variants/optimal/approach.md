## General

**Classify every cell as inside or outside the Y.** Let center index be $h=\lfloor n/2\rfloor$. A cell $(i,j)$ belongs to the Y when it satisfies at least one of:

- `i == j and i <= h`: the upper-left diagonal through the center;
- `i + j == n - 1 and i <= h`: the upper-right diagonal through the center;
- `j == h and i >= h`: the vertical stem from center downward.

The three pieces overlap at the center, but the source combines them with `a or b or c`, so that cell is counted only once.

**Count existing values in the two regions.** `cnt1` counts values 0, 1, and 2 among Y cells. `cnt2` counts them among all other cells.

The precise positions no longer matter after classification because the desired final state assigns one common value to every Y cell and another common value to every non-Y cell.

**Evaluate every legal target assignment.** The Y target `i` can be 0, 1, or 2. The outside target `j` can also be 0, 1, or 2, but it must differ from `i`. There are $3\cdot2=6$ assignments.

For one assignment, `cnt1[i]` Y cells already have their target and need no change. `cnt2[j]` outside cells already have their target. Every other cell must change exactly once, because one operation can set any cell directly to any of the three values.

Thus the cost is

$$
n^2-\texttt{cnt1}[i]-\texttt{cnt2}[j].
$$

The generator computes this for all distinct target pairs, and `min` returns the best.

**Why no cell ever needs two operations.** The operation can replace a cell's value with the final desired value directly. There is no intermediate constraint or neighboring interaction. A mismatching cell costs one, and a matching cell costs zero.

**A trace of counts.** Suppose the Y has counts $\{0:2,1:5,2:1\}$ and outside has $\{0:6,1:3,2:8\}$. Choosing Y value 1 and outside value 2 preserves $5+8=13$ cells. If the grid has 25 cells, the cost is 12. The source compares that with the other five assignments.

**Why maximizing preserved cells equals minimizing changes.** Total cell count $n^2$ is fixed. Every assignment changes precisely the complement of preserved cells. Minimizing $n^2-\text{preserved}$ is identical to maximizing the count already correct.
The membership predicates exactly reproduce the three geometric parts of the Y. For any legal pair of distinct final values, the formula counts its necessary and sufficient changes. Enumerating all six pairs includes the optimal final coloring, so the minimum is globally optimal.

**Fixed-value counters are constant space.** Although `Counter` is a dictionary type, it can have only keys 0, 1, and 2 under the input contract. Storage does not grow with $n$.

## Complexity detail

The nested loops visit all $n^2$ cells once and perform constant membership tests and one counter increment. Evaluating six assignments is constant work. Time is $O(n^2)$.

The two counters hold at most three entries each, so auxiliary space is $O(1)$. No copy of the grid or Y mask is created. The input remains unchanged.

The generator passed to `min` is lazy and also uses constant incremental space.

## Alternatives and edge cases

- **Build an explicit Boolean Y mask:** It can simplify visualization but uses $O(n^2)$ extra space when the coordinate predicates suffice.
- **Try editing cells greedily:** A cell's best target depends on the global pair of region values; counting all six assignments is simpler and exact.
- **Choose most frequent value independently in each region:** This works unless both regions choose the same value. Enumerating distinct pairs handles the required conflict correctly.
- **Center cell:** It satisfies all three geometric predicates but is counted once because of logical OR.
- **Top row endpoints:** Both belong to the two arms of the Y.
- **Bottom half:** Only the center column belongs to the stem.
- **Region already uniform with distinct values:** One assignment has cost zero.
- **Both regions dominated by the same value:** One region must use a second choice; the six-way minimum finds which change is cheaper.
- **Odd $n$:** It guarantees one unambiguous center `n//2`.
- **Values restricted to three choices:** This makes target enumeration constant-sized.
- **Y and outside are both nonempty:** For odd $n\ge3$, the defined arms/stem occupy some but not all cells, so both target values have meaningful regions.
- **Counter missing key behavior:** `Counter` returns zero for an unobserved target value, allowing all six assignments to be evaluated without initializing explicit zero counts.
- **Why target values must differ:** The filter `i != j` enforces the defining visual contrast. Allowing equality could make a uniform grid appear to contain a Y.
- **Geometric predicates at the center row:** Above and including the center, diagonals count; from the center downward, only the center column counts, exactly matching the stated junction.
