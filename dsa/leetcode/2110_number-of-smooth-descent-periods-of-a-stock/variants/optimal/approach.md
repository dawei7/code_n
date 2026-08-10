## General

**Partition the array into maximal smooth runs**

Inside a smooth descent period, each next price must be exactly one less than the preceding price. The source groups the array into maximal contiguous runs satisfying

`prices[j - 1] - prices[j] == 1`.

The pointer `i` is the start of a run. `j` begins at `i + 1` and advances while the exact-difference condition holds. When it stops, the half-open segment `prices[i:j]` is maximal: every adjacent pair inside satisfies the rule, and either `j == n` or the next pair breaks it.

The run length is `cnt = j - i`.

**Count every valid period inside one run**

Every nonempty contiguous subarray wholly inside a smooth run is itself a smooth descent period. If a run has length $c$, the number of its nonempty subarrays is

$$
c+(c-1)+\cdots+1=\frac{c(c+1)}{2}.
$$

The source adds this as

`(1 + cnt) * cnt // 2`.

This includes all $c$ one-day periods. The definition explicitly exempts the first day from needing a predecessor, so every singleton is valid.

**Why no valid period crosses a run boundary**

A run ends only when the next adjacent price difference is not exactly 1. Any contiguous period crossing that boundary includes the invalid adjacent pair and therefore cannot be smooth.

Consequently, valid periods belong to exactly one maximal run. Summing the triangular count for every run neither misses nor duplicates a period.

**Trace the first example**

For `prices = [3, 2, 1, 4]`, the first run is `[3, 2, 1]` with length 3. It contributes

$$
\frac{3\cdot4}{2}=6
$$

periods: three singletons, two length-two periods, and one length-three period.

The next run is `[4]` with length 1 and contributes one. The total is 7.

For `[8, 6, 7, 7]`, no adjacent difference equals 1 in the required direction. Each element forms a separate length-one run, so the answer is four.

**Why the direction and exact amount matter**

The test is `previous - current == 1`. A drop of two is not smooth, an equal price is not smooth, and an increase is not smooth.

Writing only `prices[j] < prices[j - 1]` would accept arbitrary decreases and solve a different problem. Writing an absolute difference would incorrectly accept increases by one.

**Why the algorithm is correct**

The inner loop produces maximal segments where every required adjacency holds. Any contiguous subarray inside such a segment inherits those valid adjacencies, so all triangularly counted periods are valid.

Every valid period's adjacent pairs satisfy the rule, so it cannot cross a boundary where the rule fails. It lies wholly within one produced segment and is included among that segment's nonempty subarrays.

Thus the sum of triangular numbers is exactly the number of smooth descent periods.

After counting a run, `i = j` begins at the first unprocessed day. No index is revisited by the outer segmentation logic.

**Derive the triangular count another way**

Within a run of length $c$, choose a starting position. The first position has $c$ possible ending positions, the second has $c-1$, and the last has one. Adding these possibilities gives the triangular formula.

Equivalently, for each ending day, the number of valid periods ending there equals its one-based position inside the run. This connects the segment formula to the common dynamic-programming view that adds 1, 2, ..., $c$ as the run grows.

**Why maximality simplifies rather than restricts counting**

The method does not claim only maximal periods are answers. A maximal run is a container that compactly represents all smaller valid periods inside it.

Choosing maximal boundaries ensures the containers are disjoint and that every crossing period is invalid at a known broken adjacency. The triangular formula then expands each container into the full number of requested subperiods without listing them.

## Complexity detail

Let $n$ be the number of prices.

Although there are nested `while` loops, `j` advances across each adjacent relationship once within its run, and `i` jumps directly to `j` afterward. Every array element participates in constant work, so total time complexity is $O(n)$.

Only `ans`, `i`, `j`, `cnt`, and `n` are stored. Auxiliary space is $O(1)$.

The answer can reach $n(n+1)/2$ when the entire array is one smooth run. Python integers handle this; fixed-width implementations should use 64-bit storage.

## Alternatives and edge cases

- **Dynamic count ending at each day:** Maintain the number of valid periods ending at the current index, reset it to one at a break, and add it to the answer. This is also $O(n)$ and $O(1)$.
- **Enumerate all subarrays:** Checking every period costs at least $O(n^2)$. Maximal runs aggregate them with a formula.
- **Count only maximal runs:** Returning the number of runs would miss all shorter valid subperiods within them.
- **One price:** One run of length one contributes one.
- **All exact descents:** One length-$n$ run contributes $n(n+1)/2$.
- **No valid adjacent pair:** Every day is a singleton run, so the answer is $n$.
- **Equal neighboring prices:** They create a run boundary.
- **Drop greater than one:** It also creates a boundary despite still being a decrease.
- **Increase by one:** Invalid because direction matters.
- **Large answer:** Use a wide integer type outside Python.
- **Input preservation:** Prices are only read.
- **Nested-loop interpretation:** Monotonic pointer movement keeps the total linear.
- **Maximal versus valid:** Maximal runs are used for grouping; all nonempty subarrays inside them are counted as separate periods.
- **First-day exemption:** It is exactly why every run contributes all of its one-day subarrays.
