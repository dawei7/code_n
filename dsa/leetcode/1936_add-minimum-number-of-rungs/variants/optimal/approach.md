## General

**Treat every consecutive height gap independently**

The climber starts at height zero, so the floor must participate in the same calculation as every rung. The solution creates `[0] + rungs`, producing a sequence whose adjacent pairs are the floor and first rung, then every pair of consecutive original rungs.

Because `rungs` is strictly increasing, every adjacent pair `(a, b)` defines a positive gap $g=b-a$. Added rungs inside one gap do not help cross a different gap, so the minimum total is the sum of the independently minimum numbers needed for all gaps.

**Derive the exact formula for one gap**

Suppose $k$ new rungs are inserted strictly between heights $a$ and $b$. Those rungs divide the distance $g=b-a$ into $k+1$ climbs. Every climb must have length at most `dist`. At least

$$
\left\lceil\frac{g}{\texttt{dist}}\right\rceil
$$

climbs are required, so at least

$$
\left\lceil\frac{g}{\texttt{dist}}\right\rceil-1
$$

new rungs are required.

For positive integers, this quantity equals

$$
\left\lfloor\frac{g-1}{\texttt{dist}}\right\rfloor.
$$

That is the exact expression `(b - a - 1) // dist` used by the solution. Subtracting one before floor division handles the “at most” boundary correctly.

Consider several cases:

- If $g\le\texttt{dist}$, then $0\le g-1<\texttt{dist}$ and the formula returns zero.
- If $g=2\cdot\texttt{dist}$, one inserted rung halfway creates two legal climbs. The formula returns $(2d-1)//d=1$.
- If $g=2\cdot\texttt{dist}+1$, two inserted rungs are necessary, and the formula returns $2d//d=2$.

Using `g // dist` directly would be wrong when $g$ is an exact multiple of `dist` because it would add one rung too many.

**Why the lower bound can always be achieved**

Starting at $a$, place new rungs at $a+\texttt{dist}$, $a+2\cdot\texttt{dist}$, and so on while the next original rung is still farther than `dist` away. Every inserted height is an integer because both $a$ and `dist` are integers. Consecutive inserted rungs are exactly `dist` apart, and the final remainder to $b$ is between one and `dist`.

This construction uses exactly $\lceil g/\texttt{dist}\rceil-1$ rungs, matching the lower bound. Therefore the formula is not merely sufficient; it is minimum for that gap.

The implementation does not need to construct these heights because the output asks only for their count. `pairwise(rungs)` lazily yields each adjacent pair, the generator computes its minimum, and `sum` combines the results.

**Why summing local minima gives the global minimum**

Any route to the last rung must cross every original consecutive gap in order. A rung inserted inside one gap lies between that gap's endpoints and cannot reduce a climb in another disjoint gap. Thus every valid global solution must pay at least the per-gap lower bound for each gap. Combining the achieving construction in every gap gives a valid ladder using exactly the sum of those bounds. The summed result is globally optimal.

## Complexity detail

Let $N$ be the number of original rungs.

Creating `[0] + rungs` copies $N$ input references and adds one element, taking $O(N)$ time. `pairwise` yields exactly $N$ adjacent pairs, and each formula evaluation is constant time. Total time is $O(N)$.

The exact Python source allocates a new length-$(N+1)$ list when it prepends zero, so its peak auxiliary space is $O(N)$. The generator and `pairwise` iterator themselves use $O(1)$ state. The manifest's $O(1)$ space describes an index-based version that treats zero as a previous-height variable without copying the list; it is not the strict allocation bound of `[0] + rungs`.

## Alternatives and edge cases

- **Track a previous height:** Initialize `previous = 0`, scan original rungs, add `(height - previous - 1) // dist`, then update `previous`. This preserves $O(N)$ time and achieves true $O(1)$ auxiliary space.
- **Actually insert rungs:** Constructing every new height is unnecessary and can be enormous relative to the input length when a gap is large. Arithmetic gives the count directly.
- **Binary search the answer:** Feasibility is monotone, but there is a closed-form independent answer for every gap, so binary search adds complexity.
- **Gap at most `dist`:** It contributes zero, including a gap exactly equal to `dist`.
- **Exact multiple of `dist`:** The subtraction by one prevents an extra rung; a gap $kd$ needs $k-1$ additions.
- **First rung too high:** Prepending the floor makes the floor-to-first-rung gap use the same formula automatically.
- **Single rung:** There is one floor-to-rung pair, and the expression returns its exact minimum additions.
- **Very large heights:** The method uses integer arithmetic, so it avoids floating-point precision issues in ceiling calculations.
- **Strictly increasing input:** Positive gaps are guaranteed. Duplicate or descending heights would invalidate the independent climbing interpretation but are outside the contract.
- **Choice of insertion heights:** Many placements may achieve the minimum. Only the count matters, so the algorithm need not select one.
- **Imported helper:** The exact solution assumes `pairwise` is available in its execution environment.
