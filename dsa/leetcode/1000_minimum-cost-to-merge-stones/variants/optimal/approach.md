## General

**First determine whether one pile is reachable at all**

Every operation replaces exactly `K` piles with one pile. Therefore, one operation reduces the total pile count by exactly `K - 1`.

Starting from `n` piles and ending with one requires a total reduction of `n - 1`. That is possible only if

`(n - 1) % (K - 1) == 0`.

If the remainder is nonzero, no choice of consecutive groups can change the size reduction per move, so the method returns `-1` immediately. This is a mathematical impossibility check, not a heuristic.

When the divisibility condition holds, repeatedly merging any legal group demonstrates that the pile count can eventually reach one; the dynamic program then finds the minimum cost among valid merge orders.

**Why interval dynamic programming is appropriate**

Only consecutive piles may be merged. Any pile that exists later represents the sum of one contiguous interval of the original array. Consequently, subproblems can be described by an original interval and the number of piles into which that interval has already been reduced.

The solution uses one-based interval endpoints and defines:

`f[i][j][p]` as the minimum cost to merge original piles `i` through `j` into exactly `p` piles.

States use `1 <= p <= K`. There is no need to retain more than `K` output piles for the transition that ultimately combines exactly `K` piles into one.

An unreachable state stays at `inf`. This lets the same minimum recurrence ignore impossible pile counts without separate feasibility branches.

**Initialize one original pile**

An interval containing one original pile is already one pile and requires no operation:

`f[i][i][1] = 0`.

It cannot be reduced further, and states with other pile counts remain infinite.

This is the base from which longer intervals are assembled.

**Split an interval into one left pile and the remaining piles**

To reduce interval `[i, j]` to `p` piles, choose a split point `h` between `i` and `j`:

- reduce `[i, h]` to exactly one pile;
- reduce `[h + 1, j]` to exactly `p - 1` piles.

The combined interval then contains `p` piles, and its cost is

`f[i][h][1] + f[h + 1][j][p - 1]`.

The transition tries every `h` and keeps the minimum.

Why is it enough to make the left part one pile? Any final configuration of `p` piles partitions the original interval into `p` contiguous groups. The first final pile covers some prefix `[i, h]`, and the other `p - 1` final piles cover the remaining suffix. Trying every boundary enumerates every possible first group.

The transition for `p = 1` refers to the unused pile-count-zero states and remains infinite. The real one-pile transition is handled separately because forming one pile requires paying for a final `K`-pile merge.

**Merge exactly `K` intermediate piles into one**

After the split recurrence has found the cheapest way to turn `[i, j]` into exactly `K` piles, those `K` consecutive piles can be merged in one operation.

Their total number of stones is simply the sum of all original piles in `[i, j]`, regardless of how the intermediate piles were formed. Therefore:

`f[i][j][1] = f[i][j][K] + interval_sum(i, j)`.

If the interval cannot legally become `K` piles, `f[i][j][K]` is infinite and the one-pile state stays unreachable.

This separation is important: partitioning an interval into several piles costs only the internal merges used inside each group. The sum of the entire interval is charged exactly when those `K` groups are actually merged together.

**Compute interval sums in constant time**

Prefix array `s` is created with a leading zero:

`s = list(accumulate(stones, initial=0))`.

With one-based DP endpoints, the number of stones from pile `i` through `j` is

`s[j] - s[i - 1]`.

Without prefix sums, calculating this cost inside many interval states would repeatedly scan the same stones and add another factor to the running time.

**Fill shorter intervals before longer ones**

The outer length loop runs from two through `n`. Every split state refers to proper subintervals, whose lengths are smaller and have already been computed.

For a fixed length `l`, start `i` ranges over every interval that fits, and `j = i + l - 1` gives its end. The nested pile-count and split loops then fill all reachable output counts before the final one-pile assignment is made.

**Trace `[3, 2, 4, 1]` with `K = 2`**

The feasibility check passes because every binary merge reduces the pile count by one.

For interval `[3, 2]`, the DP can form two singleton piles at cost zero, then merge them for interval sum five. Thus its one-pile cost is five. Similarly, interval `[4, 1]` has one-pile cost five.

For the complete interval, splitting after the second original pile allows:

- left half reduced to one pile for cost five;
- right half reduced to one pile for cost five.

This creates the two piles needed for the final merge at internal cost ten. Their total stone count is ten, so the final merge costs another ten, giving total twenty.

The DP also tries every other split and retains twenty as the minimum.

For the same four piles with `K = 3`, each move reduces the count by two. Reducing four piles to one would require a reduction of three, which is not divisible by two, so the method correctly returns `-1` before allocating meaningful work.

**Why the recurrence gives the minimum**

Every value inserted into a state combines legal subplans on disjoint consecutive subintervals, so it represents a legal way to obtain the stated pile count. Adding the interval sum only after obtaining exactly `K` piles represents a legal final merge.

Conversely, consider an optimal plan for `[i, j]` ending with `p > 1` piles. Its first resulting pile occupies some prefix ending at `h`, and the rest form `p - 1` piles in the suffix. The recurrence tries that `h` and, by optimal substructure, uses costs no greater than those subplans.

For `p = 1`, the final operation must merge exactly `K` piles and costs the fixed interval sum; `f[i][j][K]` minimizes everything before it. Induction over interval length and output pile count proves every finite state is minimal. The requested answer is `f[1][n][1]`.

## Complexity detail

Let `N` be the number of original piles.

The exact protected implementation has `O(N^2K)` table states. For each interval and pile count it scans up to `O(N)` split points. Its time complexity is therefore `O(N^3K)`, and its three-dimensional table uses `O(N^2K)` space.

Some optimized formulations exploit pile-count feasibility to skip split points in steps of `K - 1` and collapse the pile dimension, reaching `O(N^3/(K - 1))` time and `O(N^2)` space. That is a related optimization, but it is not the literal loop and storage structure of the solution documented here.

## Alternatives and edge cases

- **Two-dimensional optimized DP:** Store only the minimum cost for each interval and consider split points separated by `K - 1`. It reduces storage and matches the tighter standard bound but has a less explicit state meaning.
- **Top-down memoization:** Cache `(i, j, p)` states recursively. It can avoid unreachable states naturally but uses recursion and the same core recurrence.
- **Greedily merge the cheapest current group:** A locally cheap merge changes which future consecutive groups exist and can lead to a larger total, so greedy selection is not reliable.
- **`N = 1`:** The feasibility check passes, the singleton base cost is zero, and no merge is needed.
- **`K > N` with several piles:** The divisibility test rejects most such cases; no group of `K` can be formed.
- **Unreachable subinterval pile counts:** They stay `inf` and cannot improve a minimum.
- **Large interval sums:** Prefix sums make each final-merge cost constant-time and Python integers avoid overflow.
- **Exactly `K` piles initially:** The DP can merge the whole array once, with cost equal to its total sum.
- **Consecutive restriction:** Every transition splits into contiguous intervals; noncontiguous groupings are never introduced.
- **Parameter name:** The implementation uses uppercase `K` for the required merge size and lowercase `k` as a loop variable for target pile count.
