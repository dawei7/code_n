## General

**Binary-search the answer rather than the cut positions**

There are many ways to place \(k\) cuts among the chunks. Instead of enumerating them, ask a decision question:

> For a proposed sweetness \(x\), can the bar be divided into at least \(k+1\) contiguous pieces, each having total sweetness at least \(x\)?

If \(x\) is feasible, every smaller threshold is feasible using the same division. If \(x\) is infeasible, every larger threshold is infeasible. This monotone true-then-false structure allows binary search for the greatest feasible \(x\), which is exactly the maximum possible minimum piece sweetness.

**The greedy feasibility check**

`check(x)` scans chunks from left to right. The variable `s` accumulates the current unfinished piece. As soon as `s >= x`, the function counts one qualifying piece, resets `s` to zero, and begins a new piece at the next chunk.

Making a cut at the earliest moment the threshold is reached is optimal for maximizing the number of qualifying pieces. All sweetness values are positive. Extending an already sufficient piece would consume positive chunks that could only help later pieces; it cannot make the current piece more useful to the yes-or-no question.

The variable `cnt` is therefore the maximum number of disjoint consecutive threshold-reaching pieces obtainable for that \(x\). `return cnt > k` is equivalent to requiring at least \(k+1\) pieces.

**Why the greedy count is maximal**

Consider the greedy first piece. It ends at the earliest index whose prefix sum reaches \(x\). Any valid first piece must end at that index or later, because an earlier prefix has sum below \(x\). Thus the greedy choice leaves at least as many chunks for all remaining pieces as any other valid first cut.

Apply the same argument to the suffix after that cut. By induction, no alternative cutting strategy can produce more qualifying pieces than the greedy scan.

**At least \(k+1\) pieces is enough for exactly \(k+1\)**

The contract requires exactly \(k\) cuts, hence exactly \(k+1\) nonempty pieces. If the greedy scan produces more than \(k+1\) qualifying pieces, adjacent pieces can be merged until exactly \(k+1\) remain. Merging positive-sum pieces cannot lower their sweetness below \(x\).

If a trailing suffix remains after the last counted piece and has sum below \(x\), attach it to the final qualifying piece. This also cannot decrease that piece’s sum. Therefore, `cnt > k` is both necessary and sufficient for an exact complete division with minimum at least \(x\).

**The binary-search interval**

The exact source initializes `l = 0` and `r = sum(sweetness)`. Zero is always feasible, and the total sweetness is an unquestionable upper bound on any one piece’s sweetness. The interval is wider than necessary but valid.

While `l < r`, it calculates

`mid = (l + r + 1) >> 1`.

Right shift by one performs integer division by two for these nonnegative values. Adding one chooses the upper midpoint. If `check(mid)` succeeds, `mid` remains a candidate and `l = mid` searches for a greater feasible value. If it fails, `r = mid - 1` removes `mid` and everything above it.

The upper midpoint prevents an infinite loop when `l` and `r` differ by one. In that situation, `mid` equals `r`; either it becomes the new feasible lower bound or the upper bound drops to `l`.

**Loop invariant and correctness**

At the start of every iteration, the true optimal answer lies in the inclusive interval from `l` through `r`, and `l` is feasible. Initially, the optimum cannot be negative or exceed the total, and zero is feasible.

If `mid` is feasible, monotonicity allows discarding values below it while keeping `mid`. If it is infeasible, monotonicity allows discarding it and all larger values. The invariant is preserved and the interval strictly shrinks.

When the bounds meet, the interval contains one value. It must be the greatest feasible threshold, so returning `l` gives the optimal minimum piece sweetness.

**Following the first example**

For `[1,2,3,4,5,6,7,8,9]` with five friends, six pieces are needed. Testing \(x=6\), the greedy scan cuts after sums 6, 9, 6, 7, 8, and 9, producing six qualifying pieces. Thus six is feasible.

Testing a larger threshold eventually yields fewer than six pieces. Binary search locates the boundary at six. One corresponding division is `[1,2,3]`, `[4,5]`, `[6]`, `[7]`, `[8]`, `[9]`, whose minimum sum is six.

**Why resetting to zero is correct**

When `s >= x`, all chunks accumulated belong to the piece just cut. Any amount above \(x\) cannot be split off fractionally because chunks are indivisible. Resetting to zero accurately begins the next piece; carrying the surplus forward would use part of a chunk in two pieces and violate the model.

## Complexity detail

Let \(n=\lvert\texttt{sweetness}\rvert\) and \(S=\sum\texttt{sweetness}\). Each `check` call scans \(n\) chunks in \(O(n)\) time. The exact search range is from zero through \(S\), so binary search makes \(O(\log(S+1))\) checks. Including the initial sum, total time is \(O(n\log(S+1))\).

Only scalar counters and boundaries are stored, giving \(O(1)\) auxiliary space. The manifest’s \(O(n\log(S/(k+1)))\) bound corresponds to using the tighter upper bound \(\lfloor S/(k+1)\rfloor\). This exact source uses `r = S`, so \(O(n\log S)\) is its direct bound.

## Alternatives and edge cases

- **Tighter upper bound:** Initialize `r = sum(sweetness) // (k + 1)` because \(k+1\) pieces cannot all exceed their average. This reduces the numeric search interval without changing the answer.
- **Enumerate cut combinations:** Trying all placements is combinatorial and infeasible for \(n\) up to \(10^4\).
- **Dynamic programming by cuts and positions:** It can express the optimization but is much slower than monotone feasibility plus binary search.
- **No friends:** When `k == 0`, one piece contains the entire bar. The check accepts thresholds through \(S\), and the method returns \(S\).
- **One chunk per person:** When `k == n - 1`, every chunk must stand alone, so the answer is the minimum chunk sweetness.
- **Threshold zero:** It is trivially feasible because positive chunks immediately reach it; it serves as a safe lower bound rather than a likely final answer.
- **Trailing insufficient sweetness:** It can be merged into the final completed piece, preserving the threshold and full-bar coverage.
- **More than \(k+1\) greedy pieces:** Merge adjacent pieces until exactly the required count remains.
- **Positive sweetness requirement:** The earliest-cut proof relies on every chunk being positive. Zero or negative values would require different reasoning.
- **Upper midpoint:** Using the lower midpoint with `l = mid` can stall when the bounds are adjacent. The added one prevents that.
