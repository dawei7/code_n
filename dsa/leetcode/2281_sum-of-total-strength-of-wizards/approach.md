## General

**Assign every subarray to one occurrence of its minimum**

Directly enumerating all subarrays is quadratic. Instead, the solution focuses on index `i` and aggregates all subarrays for which `strength[i]` is the designated minimum.

Equal minimum values require a tie rule so a subarray is not counted multiple times. This code lets index `i` extend left through equal values but stops it before an equal value on the right. As a result, the rightmost occurrence of the minimum inside a subarray owns that subarray.

**Find the strict-smaller boundary on the left**

The left-to-right monotonic stack stores indices whose strengths are strictly increasing after popping. For current value `v`, it removes every stack top with strength greater than or equal to `v`.

After those pops, the remaining top, if any, is the nearest index to the left with value strictly smaller than `v`. It is stored in `left[i]`; absence uses minus one.

Equal values are popped, so they do not block current index `i` from claiming subarrays extending left across them.

**Find the smaller-or-equal boundary on the right**

The right-to-left scan pops only values strictly greater than `strength[i]`. An equal value remains on top and becomes a boundary.

Thus, `right[i]` is the nearest index to the right whose value is less than or equal to `strength[i]`, or `n` if none exists.

The asymmetric comparisons are deliberate. For equal minima at positions `p < i`, the earlier position's right boundary stops before `i`, while the later position may extend left across `p`. Exactly one of them owns a subarray containing both.

**Describe the owned start and end ranges**

Set

`l = left[i] + 1` and `r = right[i] - 1`.

Every start `L` from `l` through `i` and every end `R` from `i` through `r` forms a subarray `[L, R]` whose designated minimum is `strength[i]`. There are `i-l+1` choices of start and `r-i+1` choices of end.

No subarray can extend beyond those boundaries without encountering a disqualifying smaller value or the equal value assigned ownership by the tie rule.

**Build a prefix sum of prefix sums**

Let the first prefix array be

$$
P[t] = \sum_{q=0}^{t-1}\texttt{strength}[q],
$$

so subarray sum `[L,R]` is `P[R+1]-P[L]`.

The nested `accumulate` calls build `ss` such that

$$
\texttt{ss}[u] = \sum_{t=0}^{u-1} P[t].
$$

The inner accumulation includes initial zero and produces `P` of length `n+1`. The outer accumulation includes another initial zero and produces `ss` of length `n+2`. Differences of `ss` can therefore sum consecutive values of `P` in constant time.

**Sum all positive prefix terms for one minimum**

Across all owned subarrays, the positive term is `P[R+1]`. For every end `R` from `i` through `r`, that term is paired with all `i-l+1` possible starts.

The sum of these prefix terms is

$$
\sum_{R=i}^{r} P[R+1]
=
\texttt{ss}[r+2]-\texttt{ss}[i+1].
$$

Multiplying by the number of starts gives the code's

`a = (ss[r + 2] - ss[i + 1]) * (i - l + 1)`.

**Sum all negative prefix terms**

The negative term is `P[L]`. Every start `L` from `l` through `i` is paired with all `r-i+1` possible ends.

Its aggregate is

$$
\left(\sum_{L=l}^{i}P[L]\right)(r-i+1)
=
(\texttt{ss}[i+1]-\texttt{ss}[l])(r-i+1),
$$

which is exactly `b` in the source.

Therefore, `a - b` is the sum of the ordinary element sums of every subarray owned by index `i`.

**Convert summed subarray values into total strength**

Every owned subarray has designated minimum `v = strength[i]`. Multiplying `a-b` by `v` gives the sum of “minimum times subarray sum” over the entire owned group.

The update

`ans = (ans + (a - b) * v) % mod`

adds that group contribution and applies the required modulus. Python can hold the unreduced values of `ss`, `a`, and `b` exactly; reducing only the accumulated answer remains mathematically valid.

**Why every subarray is counted exactly once**

Every non-empty subarray has at least one minimum. Choose its rightmost minimum occurrence `i`. There is no smaller value between its endpoints and `i`, no equal minimum to its right, and any equal minima to its left are permitted by `i`'s strict-smaller left boundary. Hence its start and end fall inside `i`'s owned ranges.

No other index can own it. A smaller or greater value cannot be its minimum, and an earlier equal minimum is stopped by the later equal value on its right. Thus, the ownership groups partition all subarrays without omissions or duplicates.

**Why the stack work stays linear**

An index is pushed once in each monotonic-stack pass and popped at most once in that pass. Although a `while` loop is nested inside a `for` loop, total pops are linear rather than quadratic.

Together with constant-time double-prefix formulas for each index, this turns a seemingly quadratic aggregation into a linear algorithm.

## Complexity detail

Let `n` be the number of wizards. Each monotonic-stack pass is `O(n)` amortized. Building the two prefix levels is `O(n)`, and the final contribution loop is `O(n)`. Total time is `O(n)`.

The `left`, `right`, stack, first-prefix temporary, and `ss` structures each use `O(n)` space. Only a constant number coexist beyond these linear arrays, so auxiliary space is `O(n)`.

The answer and intermediate sums can be enormous. Python integers preserve them; the final accumulator is reduced modulo `10^9+7` on every index.

## Alternatives and edge cases

- **Enumerate all subarrays:** Even with a running sum and minimum, `O(n^2)` work is too slow for `n=10^5`.
- **Segment tree for minima:** It can divide by minimum positions, but summing all subarray sums still requires careful aggregation and is more complex.
- **Symmetric stack inequalities:** Using strict or non-strict comparisons on both sides double-counts or omits subarrays with equal minima.
- **Opposite tie ownership:** Smaller-or-equal on the left and strict-smaller on the right is also valid if formulas are adjusted consistently; the exact source chooses rightmost ownership.
- **Only one prefix level:** It gets one subarray sum in constant time but cannot sum a whole range of prefix values in constant time.
- **Single wizard:** Both boundaries enclose only that index, and its contribution is `strength[0]^2`.
- **All equal strengths:** The asymmetric boundaries assign every subarray to its rightmost element exactly once.
- **Strictly increasing array:** Left boundaries are immediate predecessors while right boundaries extend to the end as allowed by minima.
- **Strictly decreasing array:** Left boundaries extend far left and right boundaries are immediate successors.
- **Large strengths:** Wide intermediate arithmetic is essential before modular reduction.
- **Modulo subtraction:** Python's final `% mod` normalizes a possibly negative intermediate difference.
- **Boundary sentinels:** Minus one and `n` make `l` and `r` valid without separate edge branches.
- **Inclusive choice counts:** Start count is `i-l+1` and end count is `r-i+1`.
- **Input preservation:** Stacks and prefix arrays are derived; `strength` is never modified.
