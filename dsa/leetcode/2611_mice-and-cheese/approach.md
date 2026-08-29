## General

**Separate the unavoidable choice from the incremental benefit**

Every cheese must be assigned to exactly one mouse, and the first mouse must receive exactly $k$ cheeses. For cheese $i$, switching its owner from the second mouse to the first changes the score by

$$
\Delta_i=\texttt{reward1[i]}-\texttt{reward2[i]}.
$$

This difference may be positive, zero, or negative even though both reward arrays contain positive values. A positive difference favors the first mouse; a negative difference means the second mouse would score more on that cheese.

One way to view the total is to give every cheese to the second mouse first:

$$
B=\sum_{i=0}^{n-1}\texttt{reward2[i]}.
$$

Then select exactly $k$ indices to transfer to the first mouse. Transferring index $i$ adds $\Delta_i$, so a selected set $S$ has total

$$
B+\sum_{i\in S}\Delta_i,
\qquad |S|=k.
$$

The baseline $B$ is the same for every valid assignment. Maximizing the score is therefore exactly the problem of selecting the $k$ largest differences.

**Sort indices rather than rewards**

The code creates `range(n)` and sorts those indices using

`reward1[i] - reward2[i]`

as the key, in descending order. The resulting list `idx` puts the most favorable transfers first.

Sorting indices preserves the connection between the two rewards for one cheese. Sorting `reward1` and `reward2` independently would destroy that pairing and could combine rewards that belong to different cheese types.

After sorting:

- indices in `idx[:k]` go to the first mouse;
- indices in `idx[k:]` go to the second mouse.

The return expression sums `reward1` for the first group and `reward2` for the second group. The slices partition all indices, so every cheese is used exactly once.

**Why the largest differences are optimal**

Consider any valid assignment that does not choose the $k$ largest differences. Then some selected index $a$ has a smaller difference than an unselected index $b$:

$$
\Delta_a<\Delta_b.
$$

Swap their owners: give $b$ to the first mouse and $a$ to the second. The first mouse still has exactly $k$ cheeses, but the total changes by

$$
\Delta_b-\Delta_a>0.
$$

So the original assignment could not have been optimal. Repeating such exchanges removes every inversion until the selected set consists of $k$ largest differences.

If differences tie, swapping tied indices changes the score by zero. Any ordering among them is valid, which is why the algorithm does not need a special tie rule.

**Negative differences do not change the rule**

It can feel wrong to assign a cheese to the first mouse when its difference is negative. However, the requirement says exactly $k$, not at most $k$. If fewer than $k$ differences are positive, some unfavorable transfers are mandatory.

Choosing the largest differences still minimizes the damage. For example, transferring a cheese with difference $-1$ loses only one point relative to the all-second-mouse baseline, while difference $-10$ loses ten. Therefore $-1$ must be preferred.

This distinction is a common semantic trap: selecting only positive gains solves an “at most $k$” problem, not this exact contract.

**Trace the first example**

For `reward1 = [1,1,3,4]` and `reward2 = [4,4,1,1]`, the differences are

$$
[-3,-3,2,3].
$$

With $k=2$, indices three and two have the two largest differences. They go to the first mouse for rewards four and three. Indices zero and one go to the second mouse for four and four. The total is

$$
4+3+4+4=15.
$$

The baseline view reaches the same result: all second-mouse rewards total ten, and adding the two selected gains $3+2$ gives fifteen.

For equal reward arrays, every difference is zero. Any $k$ indices may go to the first mouse without changing the total. When $k=n$, the first slice contains every index and the second slice is empty, so the code correctly sums only `reward1`.

**Why direct two-group summation is equivalent to the baseline**

The exact return statement does not explicitly calculate $B$ or add differences. For a selected index $i$,

$$
\texttt{reward2[i]}+\Delta_i
=\texttt{reward1[i]}.
$$

Thus replacing that index's baseline contribution with `reward1[i]` performs the same algebra implicitly. Summing `reward1` on the first slice and `reward2` on the rest is exactly $B$ plus selected differences.

**What the algorithm stores**

Only indices are reordered. Both reward arrays remain unchanged, and no cheese record needs to be copied. The index order encodes the complete ownership decision: the boundary at position $k$ separates the first mouse's choices from the second mouse's choices.

Python's sort is stable, but stability has no correctness significance here because equal differences are interchangeable. The generator expressions then traverse each slice once to compute the score.

## Complexity detail

Let $n$ be the number of cheese types. Building the index range and sorting it by differences takes $O(n\log n)$ time. Each key evaluation is $O(1)$, and Python's key-based sort computes the key once per element.

The two final sums together visit exactly $n$ indices, adding $O(n)$ time. The total remains $O(n\log n)$.

The sorted index list and its cached sort keys require $O(n)$ space. The slices `idx[:k]` and `idx[k:]` also create lists whose combined length is $n$, still $O(n)$ overall. The reward arrays are read only.

## Alternatives and edge cases

- **Min-heap of size $k$:** Scan all differences and retain the $k$ largest in $O(n\log k)$ time and $O(k)$ space, then add them to the second-mouse baseline.
- **Quickselect:** Partition around the $k$th largest difference for expected $O(n)$ time, though implementation and worst-case guarantees are more involved.
- **Dynamic programming:** A state by prefix and number assigned to mouse one works in $O(nk)$ time, but ignores the independent additive structure.
- **Sort rewards independently:** This is invalid because rewards at the same index describe the same cheese and must remain paired.
- **`k = 0`:** The first slice is empty, so every cheese goes to the second mouse.
- **`k = n`:** The second slice is empty, so every cheese goes to the first mouse.
- **All differences negative:** Exactly $k$ transfers are still required; choose the least negative ones.
- **Tied differences:** Any tied ownership choice gives the same total.
- **Large raw reward versus difference:** Selection must use comparative gain, not `reward1[i]` alone.
- **Input preservation:** Sorting a separate index list leaves both reward arrays in their original order.
