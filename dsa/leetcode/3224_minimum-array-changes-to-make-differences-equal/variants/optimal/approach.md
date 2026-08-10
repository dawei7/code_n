## General

**Each mirrored pair has a simple cost for a chosen target.** The array contains $p=n/2$ pairs

$$
(\texttt{nums}[i],\texttt{nums}[n-1-i]).
$$

Fix a candidate common difference $X$ between zero and $k$. One mirrored pair needs zero, one, or two changed elements to end with absolute difference $X$. Pair costs add independently once $X$ is fixed, so the goal is to evaluate the total cost for every $X$ efficiently.

For a pair, reorder values so $x\le y$ and let

$$
a=y-x.
$$

If $X=a$, the pair already has the desired difference and costs zero changes.

**Find the largest difference reachable with one change.** Keep $y$ unchanged and replace $x$ by any value from zero through $k$. This can realize every difference from zero through $\max(y,k-y)$, but in particular choosing replacement zero reaches difference $y$. Keep $x$ unchanged instead; choosing replacement $k$ reaches difference $k-x$.

Together, one endpoint change can realize every target from zero through

$$
T=\max(y,k-x).
$$

One direct way to see interval coverage is that keeping $y$ and choosing `y-X` works for all $0\le X\le y$, while keeping $x$ and choosing `x+X` works for all $0\le X\le k-x$. Their union is $[0,T]$.

For $X>T$, neither endpoint can stay unchanged, so two changes are necessary. Two changes are always sufficient for $0\le X\le k$, for example by replacing the pair with $(0,X)$.

Thus one pair's cost function is:

$$
\operatorname{cost}(X)=
\begin{cases}
0,&X=a,\\
1,&0\le X\le T,\ X\ne a,\\
2,&T<X\le k.
\end{cases}
$$

**Encode this piecewise function with range differences.** Array `d` is a difference array over candidate targets. Prefix accumulation later recovers total costs.

For each pair, the source performs:

- `d[0] += 1`: begin baseline cost one for targets starting at zero;
- `d[a] -= 1`: drop from one to zero at the pair's current difference;
- `d[a + 1] += 1`: return from zero to one immediately after it;
- `d[T + 1] -= 1` followed by `d[T + 1] += 2`: net increase one, changing cost one to cost two beyond the one-change limit.

The last two statements could be combined as `d[T + 1] += 1`. Written separately, they can be read as ending the one-cost range and starting the two-cost range.

Adding every pair's difference updates superposes their cost functions. `accumulate(d)` yields the total number of changes at each target $X$, and `min` selects the cheapest.

**Why all target values are covered.** Since final values must lie in $[0,k]$, an absolute difference can only be between zero and $k$. `d` has length $k+2$ to hold the sentinel transition at `T+1` when $T=k$. The meaningful targets are zero through $k$.

The source takes the minimum across the whole accumulated length, including sentinel index $k+1$. At that index every pair is in its two-change region, yielding $2p$. Some valid target always costs at most $2p$, so the extra sentinel cannot create an incorrectly smaller result.

**Trace one pair.** Suppose $k=6$ and pair values are $(1,5)$. Then $a=4$ and $T=\max(5,5)=5$. Its costs across targets $0..6$ are `[1,1,1,1,0,1,2]`. The four difference updates reproduce exactly those steps without writing all seven entries individually.

**Why the global minimum is correct.** For each $X$, prefix accumulation sums the independently minimal pair costs for that fixed target. Applying those chosen changes makes every mirrored difference equal to $X$, so the sum is achievable. Any valid final array has some common $X$ and must pay at least each pair's corresponding minimum, so it cannot beat the computed total for that $X$. Minimizing across all candidates yields the true optimum.

## Complexity detail

There are $n/2$ mirrored pairs. Each contributes a constant number of difference-array updates, taking $O(n)$ time. Accumulating the length-$(k+2)$ array and finding its minimum takes $O(k)$ time. Total time is $O(n+k)$.

The difference array uses $O(k)$ auxiliary space. `accumulate` is lazy, so it does not create another length-$k$ list; `min` consumes values as they are produced. The input array is read only.

## Alternatives and edge cases

- **Evaluate every target for every pair:** Direct use of the piecewise formula costs $O(nk)$, too slow at $10^5$.
- **Savings viewpoint:** Start from two changes per pair, range-add savings of one where one change suffices and another saving at the original difference. It leads to an equivalent difference array.
- **Pair already at target:** Cost is zero only at `X = y-x`.
- **Target within one-change reach:** Exactly one replacement suffices unless it is already the original difference.
- **Target above `T`:** Both endpoints must change.
- **Equal pair values:** `a=0`, so target zero costs nothing; positive reachable targets cost one up to `T`.
- **Target zero:** Any pair can reach equal values with at most one change, and an already equal pair needs none.
- **Target `k`:** It may need one change when one original endpoint is zero or $k$ in the right position; otherwise two.
- **Even-$n$ guarantee:** Every element belongs to exactly one mirrored pair, so no unpaired center needs special handling.
- **Transition collision:** If `a+1 == T+1`, updates at the same index add algebraically and still create the correct next cost.
- **Sentinel slot:** Index $k+1$ stores range endings and is not a legal difference, but its cost cannot lower the valid minimum.
- **Input preservation:** Values are swapped only in local variables `x,y`, not inside `nums`.
