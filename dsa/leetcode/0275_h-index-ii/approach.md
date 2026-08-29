## General

**Search candidate h-values, not citation values**

The array is already sorted in non-decreasing order, so the algorithm should use that ordering instead of sorting again. The exact solution binary-searches the answer $h$ directly over the integer range from 0 through $n$, where $n$ is the number of papers.

The maximum possible h-index is $n$: even if every paper has millions of citations, there cannot be more than $n$ papers satisfying the definition. Zero is always a valid lower bound. Thus `[0, n]` contains every possible answer.

**Locate the h-th largest paper in an ascending array**

For a candidate $h\ge1$, the last $h$ array entries form a suffix of length $h$. Its first index is `n - h`:

```text
indices:       0 ... n-h-1 | n-h ... n-1
suffix length:               <--- h --->
```

Because the array is ascending, `citations[n - h]` is the smallest citation count within that suffix. Candidate $h$ is feasible exactly when

$$
\texttt{citations}[n-h]\ge h.
$$

If this comparison succeeds, all $h$ entries from index `n - h` through `n - 1` are at least as large, so at least $h$ papers have at least $h$ citations. If it fails, even the $h$-th largest paper has fewer than $h$ citations; only the $h-1$ larger positions could possibly reach the threshold, so $h$ is impossible.

This rank test is the ascending-order counterpart of examining index `h - 1` after a descending sort. The `n - h` expression is not arbitrary: it precisely converts “$h$-th largest” into an ascending-array index.

**Why feasibility is monotone**

Binary search needs a predicate whose truth values change in only one direction. Here, if a candidate $h$ is feasible, every smaller candidate $g<h$ is feasible. The definition already proves this: at least $h$ papers each have at least $h$ citations, so at least $g$ papers each have at least $g$ citations.

The sorted-index formula shows the same fact mechanically. Since $g<h$, index `n - g` lies to the right of `n - h`, so

$$
\texttt{citations}[n-g]
\ge
\texttt{citations}[n-h]
\ge h
>g.
$$

Conversely, if $h$ is infeasible, any larger candidate $q>h$ is also infeasible. Index `n - q` lies farther left, so its citation value is no greater than `citations[n - h]`, while its required threshold $q$ is larger.

Candidate values therefore have the pattern

```text
true, true, ..., true, false, false, ..., false
```

starting with the trivially feasible zero. The h-index is the rightmost true candidate.

**Maintain an inclusive candidate interval**

The source initializes `left = 0` and `right = n`. Throughout the loop, the maximum feasible candidate remains somewhere in the inclusive interval `[left, right]`. `left` is a known feasible lower bound—initially zero—and `right` is an upper boundary that has not yet been eliminated.

It chooses

$$
\texttt{mid}=\left\lfloor\frac{\texttt{left}+\texttt{right}+1}{2}\right\rfloor.
$$

The source expresses division by two as a right shift, `>> 1`. The added one makes this the upper midpoint. When two candidates remain, `mid` becomes the right candidate rather than repeating `left`.

If `citations[n - mid] >= mid`, candidate `mid` is feasible. Monotonicity means every candidate below it is also feasible, so none can be the maximum while `mid` remains available. The algorithm moves `left` to `mid`.

If the test fails, `mid` and every larger candidate are infeasible. The algorithm moves `right` to `mid - 1`.

Each update strictly shrinks the interval. When `left == right`, only one possible maximum remains, and the method returns `left`.

**Why the upper midpoint is essential**

The feasible branch uses `left = mid`, not `left = mid + 1`, because `mid` itself may be the answer. With an ordinary lower midpoint, an interval such as `[2,3]` would choose `mid = 2`; if 2 were feasible, assigning `left = 2` would make no progress and the loop could repeat forever.

The upper midpoint selects 3 for `[2,3]`. Either 3 is feasible and becomes the new lower bound, or it is infeasible and `right` becomes 2. Both outcomes collapse the interval.

**Why index `n - mid` is always valid**

Candidate zero would require index `n`, which is outside the array. The loop never evaluates the predicate at zero. While `left < right` and `right >= 1`, the upper midpoint is at least 1. If the search narrows to `[0,0]`, the loop ends before indexing. The nonempty-array constraint guarantees all tested indices for candidates 1 through $n$ fall from `n - 1` down to zero.

**Trace the examples**

For `citations = [0,1,3,5,6]`, $n=5$:

| `left` | `right` | `mid` | Checked value | Result |
|---:|---:|---:|---:|---|
| 0 | 5 | 3 | `citations[2] = 3` | `3 >= 3`, so `left = 3` |
| 3 | 5 | 4 | `citations[1] = 1` | `1 < 4`, so `right = 3` |

The bounds meet at 3, which is returned. The suffix `[3,5,6]` supplies three papers with at least three citations, while the fourth-largest value is only 1, so 4 is impossible.

For `[1,2,100]`, $n=3$. Candidate 2 checks `citations[1] = 2` and succeeds. Candidate 3 then checks `citations[0] = 1` and fails. The returned h-index is 2.

**Why the final value is the maximum, not merely a valid one**

Every feasible midpoint moves the lower bound up to that midpoint, never discarding it. Every infeasible midpoint removes itself and all larger candidates. The monotone predicate guarantees these discarded sides cannot contain the answer. At termination, `left` is feasible and every larger candidate has been proven infeasible, which is exactly the definition of the maximum feasible $h$.

## Complexity detail

The candidate interval contains $n+1$ integers. Each iteration removes roughly half of the remaining interval, so the loop executes $O(\log n)$ times. Every iteration performs constant-time index arithmetic, one array access, and one comparison. Total time is $O(\log n)$, satisfying the required logarithmic bound.

The algorithm stores only `n`, `left`, `right`, and `mid`. It allocates no array, recursion stack, or collection, so auxiliary space is $O(1)$. It does not modify `citations`.

The complexity depends on the supplied sortedness. Checking from scratch that the entire array is sorted would cost $O(n)$ and defeat the logarithmic requirement; sorted order is a contract guarantee rather than something this method revalidates.

## Alternatives and edge cases

- **Linear suffix scan:** Find the first index `i` with `citations[i] >= n - i` and return `n - i`. This is straightforward and $O(1)$ space but costs $O(n)$ time, missing the problem's logarithmic requirement.
- **Binary-search the first qualifying index:** Search indices for the first `i` satisfying `citations[i] >= n - i`, then return `n - i`. This is equivalent to the exact candidate-space search and also runs in $O(\log n)$ time.
- **Sort again:** Unnecessary because the input is already ascending. Sorting would increase time to $O(n\log n)$ and may mutate the input.
- **Single paper with zero citations:** Candidate 1 fails, the interval collapses to zero, and the result is 0.
- **Single cited paper:** If its count is at least 1, candidate 1 succeeds and the answer is 1.
- **All zeros:** Every positive candidate fails; the search safely returns the always-feasible lower bound 0 without ever indexing for candidate zero.
- **Every paper has at least `n` citations:** Candidate `n` succeeds, so the returned h-index reaches its maximum possible value `n`.
- **Very large citation counts:** Counts above `n` do not require special handling. The search range itself is capped at `n`, which enforces the paper-count limit.
- **Duplicate counts:** Non-decreasing order permits duplicates. The suffix-minimum test remains valid because it depends on rank, not distinctness.
- **Feasible without equality:** The answer does not require some citation count to equal `h`. For `[100,100]`, candidate 2 succeeds because `100 >= 2`, and the answer is 2.
- **Upper midpoint:** Removing the `+1` while keeping `left = mid` can cause an infinite loop when only two candidates remain and the lower one is feasible.
- **Unsorted input outside the contract:** The monotonic index proof fails if values are out of order. This method intentionally trusts the stated ascending-order guarantee.
