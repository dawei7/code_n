## General

An interior index is special when its value is strictly greater than both adjacent values. Since operations may only increase elements, the cheapest way to make a chosen index special is to raise that index itself just enough. Increasing either neighbor would move the goal farther away.

The problem first asks for the greatest possible number of special indices and only then asks for the cheapest way to obtain that many. The source exploits the simple shape of every maximum-size selection and uses a memoized recursion to compare their costs.

**The price of selecting one index**

For an interior index $i$, the smallest legal final value is

$$
\max(\texttt{nums}[i-1],\texttt{nums}[i+1])+1.
$$

The extra $1$ is essential because the comparison is strict. If `nums[i]` is already at least that large, no operation is needed. Otherwise, the exact number of increments is

$$
c_i=
\max\!\left(
0,\,
\max(\texttt{nums}[i-1],\texttt{nums}[i+1])+1-\texttt{nums}[i]
\right).
$$

This is the `cost` computed inside `dfs`. The formula covers both already-special indices, whose cost is zero, and indices that require many increments.

**Why chosen special indices cannot be adjacent**

If both $i$ and $i+1$ were special, their definitions would require

$$
\texttt{nums}[i]>\texttt{nums}[i+1]
$$

and simultaneously

$$
\texttt{nums}[i+1]>\texttt{nums}[i],
$$

which is impossible. Thus the chosen indices must form an independent set on the path of interior positions $1,2,\ldots,n-2$.

There are $n-2$ interior positions. The maximum number of pairwise nonadjacent positions in a path of that length is

$$
q=\left\lceil\frac{n-2}{2}\right\rceil
=
\left\lfloor\frac{n-1}{2}\right\rfloor.
$$

The algorithm never needs to consider a solution with fewer than $q$ peaks, because the first objective is to maximize their number.

**Why the individual costs can be added**

Two selected indices are never adjacent. Therefore increasing one selected index does not change either original neighbor used by another selected index's threshold. There is also no benefit in increasing an unselected index: it creates no chosen peak and can only make an adjacent peak more expensive.

For any valid selected set $P$, the minimum total cost is consequently

$$
\sum_{i\in P} c_i.
$$

The numerical part of the problem has now become a weighted selection problem: among all independent sets of the maximum cardinality $q$, minimize the sum of their weights $c_i$.

**Odd lengths have one forced maximum pattern**

Let $n=2r+1$ be odd. There are $2r-1$ interior positions, and choosing $r$ nonadjacent ones leaves no flexibility. The only maximum-cardinality pattern is

$$
1,3,5,\ldots,n-2.
$$

For odd `n`, the expression `len(nums) & 1 ^ 1` evaluates to zero. The initial state is therefore `dfs(1, 0)`. When the second argument `j` is zero, the recursion always takes the current index and advances by two. It visits exactly the forced odd-index pattern.

**Even lengths permit one parity change**

Let $n=2r$ be even. The interior path contains $2r-2$ positions, and a maximum set has $r-1$ members. Several patterns are possible. For $n=6$, for example, the interior positions are $1,2,3,4$, and the maximum sets are

$$
\{1,3\},\quad \{1,4\},\quad \{2,4\}.
$$

Every maximum pattern alternates by steps of two, but it may switch once from the odd-index alignment to the even-index alignment. Equivalently, there is one unused gap that can be placed at the beginning, somewhere in the middle, or implicitly at the end.

For even `n`, `len(nums) & 1 ^ 1` evaluates to one, so the source starts with `dfs(1, 1)`. The state `dfs(i, j)` represents the minimum remaining cost from candidate index `i`, where `j = 1` means the one parity-switch opportunity is still available.

The ordinary choice is

```text
cost at i + dfs(i + 2, j)
```

which selects $i$, excludes its adjacent successor, and preserves any unused switch.

When `j` is one, the recursion may instead use

```text
dfs(i + 1, 0)
```

which skips $i$, moves the alternating pattern one position to the right, and consumes the only switch. Once the flag is zero, every later candidate is forced at distance two.

If the recursion reaches `i >= n - 1`, there are no interior positions left and the additional cost is zero. An unused switch at this boundary simply represents placing the extra gap at the end. These branches enumerate every maximum-cardinality pattern and no smaller pattern.

**Why taking the minimum recurrence gives the intended mathematical answer**

For odd length, there is only one maximum set, and the recursion sums exactly its independent costs. For even length, each maximum set has a unique place where its alignment begins or changes; that choice corresponds to retaining the flag for some number of take steps and then either spending it on one skip or leaving it unused at the end. The recurrence evaluates the cost of every such pattern and takes the minimum.

The `@cache` decorator prevents overlapping suffix states from being recomputed. Thus the recurrence correctly solves the weighted maximum-cardinality selection problem—subject to the execution limitation described below.

## Complexity detail

Each state is identified by an index `i` and a binary flag `j`. Only $O(n)$ such states are reachable. Computing one state performs constant work besides its cached recursive calls, so the running time is

$$
O(n).
$$

The memoization table stores $O(n)$ results. In addition, a chain of recursive calls can contain $\Theta(n)$ stack frames in asymptotic terms—roughly one frame per one or two array positions. The exact auxiliary space of the checked-in source is therefore

$$
O(n),
$$

not the $O(1)$ space stated in the Optimal manifest.

An iterative parity sweep can implement the same mathematical optimization with constant extra storage, which likely explains the manifest summary, but that is not the implementation present in `solution.py`.

There is also a practical correctness risk at the maximum constraint. Standard CPython normally permits only about one thousand nested calls. With $n$ as large as $10^5$, this recursion can raise `RecursionError` unless the surrounding runner explicitly raises the recursion limit. The source file does not do so. Its recurrence produced the right result in exhaustive small-state comparisons, but as written it is not robust across the full documented input range under an ordinary Python recursion limit.

The source also assumes `List` and `cache` are available from the execution environment. Those names do not alter the asymptotic analysis, but they are required for standalone execution.

## Alternatives and edge cases

- **Iterative parity-switch sweep:** Precompute each $c_i$, sum one alternating pattern, and move the single even-length gap across the array while updating the sum. This can achieve the manifest's intended $O(n)$ time and $O(1)$ extra space without recursion-depth risk.
- **General weighted independent-set DP:** A table indexed by position and selected count can solve broader versions, but it costs more time or space than necessary because this problem always demands the known maximum cardinality.
- **Odd array length:** The maximum pattern is forced to indices $1,3,\ldots,n-2$; the recursion begins with no skip opportunity.
- **Even array length:** The skip flag enumerates the possible single alignment change, including an implicit unused gap at the end.
- **Minimum length:** For $n=3$, index 1 is the only candidate and must be made special; the returned cost is exactly $c_1$.
- **Already-special index:** Its weight is zero, so selecting it contributes no operations while still counting toward the maximum.
- **Equal neighbor value:** Strict inequality requires raising the selected index to one more than that neighbor, not merely to the same value.
- **Large integer values:** Python integers safely evaluate `max(neighbors) + 1 - nums[i]` without fixed-width overflow.
- **Increasing neighbors is never useful:** It cannot make the selected center more special and may raise the required center value, so an optimal construction raises only selected peaks.
- **Recursion-depth defect:** At the stated $n=10^5$ limit, the checked-in memoized recursion may fail before producing an answer unless the harness changes Python's recursion limit.
- **Manifest mismatch:** The source is $O(n)$ in time but $O(n)$ in memoization and stack storage; the documented $O(1)$ space describes a different iterative realization.
