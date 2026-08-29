## General

The difficulty is that bursting one balloon changes the neighbors used by future coin calculations. If the first balloon in a range is chosen, the balloons on its left and right are not independent: after that burst, future choices on one side can determine which value eventually borders the other side.

The solution becomes manageable by reversing the decision. Instead of asking which balloon is burst first, ask which balloon is burst last inside a fixed interval. At the moment that final interior balloon is burst, every other balloon inside the interval has already disappeared. Its two surviving neighbors are therefore the interval's fixed boundaries.

**Adding virtual boundaries**

The source creates

`arr = [1] + nums + [1]`.

The added values represent the rule that a missing neighbor outside the original array behaves like a balloon valued 1. They are permanent sentinels and are never burst.

If the original array has length $n$, `arr` has indices 0 through $n+1$. Original balloon `nums[t]` appears at `arr[t + 1]`. The answer must burst all values strictly between sentinel indices 0 and $n+1$.

Using sentinels removes boundary special cases. Every real balloon always has a value available on both sides in the recurrence, even when the balloon is currently the leftmost or rightmost survivor.

**Meaning of the dynamic-programming state**

Define `f[i][j]` as the maximum coins obtainable by bursting every balloon whose `arr` index lies strictly between `i` and `j`, while balloons `arr[i]` and `arr[j]` remain unburst as boundaries.

The interval is open:

$$
(i,j)=\{i+1,i+2,\ldots,j-1\}.
$$

When `j = i + 1`, there is no interior balloon. Nothing can be burst and the value is zero. The table is initialized with zeros, so all such empty base intervals are already correct.

The boundaries are not necessarily the original array edges. In a smaller subproblem, they are real balloons deliberately left alive until all balloons between them have been removed.

**Choosing the last interior balloon**

For a nonempty interval `(i, j)`, suppose index `k`, with $i<k<j$, is the last interior balloon burst.

Before that final burst, all balloons between `i` and `k` have disappeared, and all balloons between `k` and `j` have disappeared. Those two sets can be optimized independently:

- `f[i][k]` gives the best coins from the left open interval;
- `f[k][j]` gives the best coins from the right open interval.

After both sides are empty, the surviving local sequence is `arr[i], arr[k], arr[j]`. Bursting `k` earns

$$
\texttt{arr}[i]\cdot\texttt{arr}[k]\cdot\texttt{arr}[j].
$$

Thus, choosing `k` last gives

$$
f[i][k]+f[k][j]+	exttt{arr}[i]\cdot\texttt{arr}[k]\cdot\texttt{arr}[j].
$$

Every interior index is a possible last balloon, so the recurrence takes the maximum:

$$
f[i][j]
=
\max_{i<k<j}
\left(
f[i][k]+f[k][j]+	exttt{arr}[i]\texttt{arr}[k]\texttt{arr}[j]
\right).
$$

**Why “last” creates independent subproblems**

If `k` were chosen first, removing it would connect some eventual survivor from its left with some eventual survivor from its right. The rewards on the two sides would depend on each other's burst orders.

When `k` is chosen last, it remains present throughout all earlier work. It permanently separates the left and right interior sets. Bursting balloons on the left cannot change the right boundary of the left subproblem—it is always `arr[k]`. Symmetrically, the left boundary of the right subproblem is always `arr[k]`.

That fixed separator is what justifies adding the two optimal subproblem values. The global order may interleave left-side and right-side bursts, but their coin totals do not interact while `k` survives, so an optimal order for each side can be combined.

**The bottom-up loop order**

The source fills `i` from `n - 1` down to 0. For each `i`, it fills `j` from `i + 2` upward through $n+1$.

To compute `f[i][j]` for a chosen `k`, two states must already exist:

- `f[i][k]` has the same left boundary and a smaller right boundary. Because `j` increases within the current row, this state was computed earlier in the inner progression.
- `f[k][j]` has a larger left boundary `k`. Because outer `i` values are processed in descending order, row `k` was completed before row `i`.

Therefore, every dependency is ready before its parent interval. Intervals with no interior remain at their initialized zero and need no loop iteration.

The final call is not recursive; after table filling, `f[0][-1]` reads `f[0][n + 1]`, the interval strictly between the two virtual sentinels. It includes every original balloon and excludes both fake ones.

**Tracing the sample's last decision**

For `nums = [3,1,5,8]`, the augmented array is `[1,3,1,5,8,1]`.

One optimal order is to burst values 1, 5, 3, then 8. In the global interval `(0, 5)`, the balloon valued 8 at index 4 is last. Its contribution at that moment is

$$
1\cdot8\cdot1=8.
$$

The left subproblem `(0, 4)` contains values 3, 1, and 5 with boundaries 1 and 8. Its optimum is 159, corresponding to earlier gains 15, 120, and 24. The right subproblem `(4, 5)` is empty and contributes zero. The total for this last choice is

$$
159+0+8=167.
$$

The DP compares this with every other possible global last balloon and retains 167.

**Why the recurrence is exact**

Take any complete burst order for interval `(i, j)`. It has one unique last interior index `k`. All earlier bursts belong either to `(i, k)` or `(k, j)`, and their totals cannot exceed the optimal values `f[i][k]` and `f[k][j]`. The final burst earns the fixed boundary product. Therefore, the order's total cannot exceed the recurrence candidate for its `k`.

Conversely, choose any `k`, execute an optimal order for `(i, k)`, execute an optimal order for `(k, j)`, then burst `k`. Because `k` and the outer boundaries remain alive, this is a legal order achieving exactly the recurrence candidate. Taking the maximum produces the true optimum for every interval, including the global one.

## Complexity detail

There are $O(n^2)$ boundary pairs `(i, j)` in the table. For each nonempty interval, the source tries up to $O(n)$ possible last indices `k`. Each candidate performs constant-time table reads, multiplication, addition, and comparison. Total time complexity is $O(n^3)$.

The table has $(n+2)^2$ integer entries, using $O(n^2)$ space. The augmented array uses another $O(n)$ space, which is dominated by the table. The iterative method uses no recursion stack.

The loops include only valid ordered boundary pairs, but allocating a square table keeps indexing simple. Unused cells do not change the asymptotic bound.

## Alternatives and edge cases

- **Top-down interval memoization:** Use the same open-interval recurrence recursively and cache `(i, j)`. It has $O(n^3)$ time and $O(n^2)$ cache space, plus an $O(n)$ recursion stack.
- **Choose the first burst:** The remaining left and right parts are not independent because their future boundary neighbors can cross the removed position. A simple interval split on the first choice is invalid.
- **Memoize the set of surviving balloons:** It models the process directly but has exponentially many subsets and expensive state representations.
- **Remove zero-valued balloons first:** A zero balloon yields zero when burst and can optimally be removed before positive interactions. Filtering zeros can reduce practical DP size, but the exact source retains them and remains correct.
- **No virtual boundaries:** The recurrence then needs special cases whenever an interval touches an original edge. Sentinels valued 1 encode the rule uniformly.
- **Burst a sentinel:** The fake balloons are outside the open global interval and never appear as `k`; they serve only as fixed neighbors.
- **One balloon:** The only interval candidate earns `1 * nums[0] * 1`, so the answer is that value.
- **Two balloons:** Either may be last. The DP compares both possible orders and returns the better total.
- **Zero balloon values:** Products can be zero, but later removal may allow nonzero balloons to become profitable neighbors. The interval recurrence considers the best timing.
- **All values zero:** Every candidate contribution is zero, and the initialized table correctly returns zero.
- **Repeated values:** Indices remain distinct possible last choices even when values are equal. The maximum value is still computed correctly.
- **Large intermediate totals:** Python integers preserve exact products and sums without fixed-width overflow.
- **Inclusive-versus-open state:** `f[i][j]` excludes both boundaries. Treating either boundary as burstable would double-count or invalidate the fixed-neighbor product.
- **Loop direction:** Filling `i` upward would request `f[k][j]` before it exists. Descending `i` and ascending `j` satisfy both dependency directions.
- **Reconstructing an order:** Store the maximizing `k` for every interval, recursively reconstruct both sides, then append `k` as the interval's final burst. The current contract asks only for the coin total.
