## General

**Reduce every value to its first popcount.** The value 1 is the only integer with depth 0. For every `x > 1`, one popcount operation produces `popcount(x)`, so the depth of `x` is one plus the depth of that set-bit count. Because `n` has at most $L=\lfloor\log_2 n\rfloor+1$ binary digits, the first popcount is an integer from 1 through $L$. Compute the depth of each such small integer from the already known depth of its own popcount.

**Count numbers with a fixed number of one-bits.** For each set-bit count `ones` whose depth is `k - 1`, count the integers at most `n` that contain exactly that many ones. Scan the binary digits of `n` from most significant to least significant. Whenever the current bound bit is 1, numbers that put 0 there are already smaller than `n`; if `remaining` ones still need to be placed, their suffix contributes $\binom{b}{\texttt{remaining}}$, where $b$ lower positions remain. Then follow the equal prefix by consuming the bound's 1. If all required ones are consumed after the scan, include `n` itself.

Summing these counts over all qualifying `ones` values counts every desired integer exactly once because each integer has one unique popcount. For `k = 1`, the qualifying popcount is 1, but this combinatorial count includes `x = 1`; subtract it because 1 has depth 0 rather than depth 1.

## Complexity detail

Let $L=\lfloor\log_2 n\rfloor+1$. Computing the depths of values through $L$ takes $O(L)$ time. There are at most $L$ qualifying set-bit counts, and counting each one scans $L$ bits, for $O(L^2)=O((\log n)^2)$ time. The depth table uses $O(L)=O(\log n)$ space; Python's fixed-input binomial computations do not change the stated auxiliary bound.

The legal domain has $L\le 50$, too few tiers for a reliable fourfold scaling experiment in the governing bit-length variable. The package therefore uses a bounded-domain certificate with an explicit work proof and boundary cases instead of a measured runtime verdict.

## Alternatives and edge cases

- **Enumerate all integers through `n`:** Computing every value's depth is correct but takes $O(n\log\log n)$ or worse and is infeasible for $n=10^{15}$.
- **Binary digit DP:** Tracking position, accumulated ones, and tightness also works in $O(L^2)$ time, but the direct combinatorial scan has less state.
- **Depth zero:** Only `x = 1` qualifies, and the constraint guarantees it lies in the range.
- **Depth one:** Powers of two greater than 1 qualify; the separately handled value 1 must not be counted.
- **Inclusive upper bound:** The final equality check adds `n` when its own number of set bits matches the requested count.
- **Unattainable depth:** If no possible set-bit count has depth `k - 1`, the sum is zero; this includes depth 5 throughout the legal domain.
- **Large result:** The count can be close to `n`, so implementations need a wide integer return type.
