## General

At each index, changing `s[i]` to `t[i]` has a fixed nonnegative cost. A substring’s conversion cost is the sum of these per-index costs. The exact solution builds prefix sums for constant-time substring-cost queries, then binary-searches the greatest feasible substring length.

**Build a prefix sum of conversion costs**

The generator over `zip(s, t)` computes `abs(ord(a) - ord(b))` for corresponding characters. `accumulate(..., initial=0)` produces a list `f` with $n+1$ entries, where

$$
\texttt{f[r]}=\sum_{j=0}^{r-1}\lvert\texttt{ord(s[j])}-\texttt{ord(t[j])}\rvert.
$$

Thus the cost of the length-`x` substring starting at `i` is `f[i + x] - f[i]`. The earlier prefix cancels, leaving exactly the desired contiguous range.

**Test whether a particular length is possible**

The nested `check` function scans possible starts. Although its parameter is named `x`, the exact body uses the surrounding binary-search variable `mid`. Every call is `check(mid)`, so those values agree and the function behaves correctly, but using `x` internally would make the dependency clearer.

For start `i`, it sets `j = i + mid - 1`, the inclusive end. `j < n` confirms the window fits, and `f[j + 1] - f[i] <= maxCost` tests its total. The function returns true as soon as any feasible window exists.

**Why feasibility is monotone in length**

All individual costs are nonnegative. If a length-$L$ substring fits the budget, removing characters from either end cannot increase its cost. Therefore every shorter length is also feasible. Conversely, if no length-$L$ window fits, no longer window can become feasible merely by adding nonnegative costs while containing some length-$L$ subwindow.

Feasible lengths form an initial interval from zero through the answer. This is exactly the shape required for binary search.

**Find the greatest true length**

The bounds start at `l = 0` and `r = n`. Length zero is always feasible, while the maximum cannot exceed the string length.

`mid = (l + r + 1) >> 1` uses the upper midpoint. If `check(mid)` succeeds, the answer is at least `mid`, so `l = mid`. Otherwise, `mid` is too large and `r = mid - 1`.

The upper midpoint prevents an infinite loop when two candidate lengths remain: it ensures that a successful test advances the lower bound. When the bounds meet, `l` is the greatest feasible length.

For `s = "abcd"`, `t = "bcdf"`, the costs are one, one, one, and two. Length three succeeds with total three at the first start, while length four costs five. Binary search returns three.

**Why the returned length is exact**

Prefix subtraction gives the exact cost of every tested window. `check` is true precisely when at least one window of that length respects the budget. Monotonicity makes the binary-search invariant valid: all lengths at or below `l` are feasible, and discarded upper lengths are infeasible. At termination, no longer length can work and `l` itself can, so it is the maximum.

**Trace the bounds on a four-character example**

With `n = 4`, the first upper midpoint is two. If some length-two window fits, `l` becomes two rather than advancing by only one. The next midpoint is three. A successful length-three test raises `l` to three; the final test considers four. If length four fails, `r` becomes three and the bounds meet at the answer.

At no point does the algorithm assume that the feasible window for one length must share a start with the feasible window for another length. `check` scans every legal start independently. Monotonicity concerns existence: a feasible longer window contains a feasible shorter subwindow somewhere, even though a different shorter window may be the first one found. This is why binary search can operate on lengths without tracking window positions between iterations.

## Complexity detail

Let $n$ be the common string length.

Building `f` takes $O(n)$ time. Binary search performs $O(\log n)$ iterations, and each `check` may scan $O(n)$ starts, so the exact running time is $O(n\log n)$. This differs from the linear sliding-window alternative described in the editorial.

The prefix list stores $n+1$ integers and uses $O(n)$ auxiliary space. The binary-search and check variables use $O(1)$ additional space. The output is one integer.

## Alternatives and edge cases

- **Sliding window:** Expand a window while adding costs and shrink from the left whenever the budget is exceeded. Nonnegative costs give $O(n)$ time and $O(1)$ space.
- **Binary search without prefix sums:** Recomputing every window sum would add another factor of window length and be unnecessarily slow.
- **Zero budget:** Only positions where corresponding characters already match can belong to a feasible window; consecutive zero-cost positions are handled naturally.
- **Every position affordable:** Length `n` succeeds and becomes the returned upper bound.
- **No positive-length window affordable:** Length zero remains feasible, so the method returns zero.
- **Exact budget equality:** The `<=` comparison correctly accepts it.
- **Parameter shadowing detail:** `check(x)` uses `mid` rather than `x`. It works only because every call passes the current `mid`.
- **Equal string lengths:** `zip` covers every position because the contract guarantees equal lengths.
- **Upper midpoint:** The added one before halving is required for a maximum-true binary search.
- **ASCII cost:** `ord` converts lowercase letters to numeric codes, and absolute subtraction implements the stated cost.
