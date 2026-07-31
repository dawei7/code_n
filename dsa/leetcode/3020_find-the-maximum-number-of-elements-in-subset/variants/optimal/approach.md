## General

**Count occurrences before following chains.** Store the multiplicity of every value. For a starting value $x>1$, two copies of $x$ can form the outermost pair, two copies of $x^2$ can form the next pair, and this continues through repeated squaring.

Walk the chain while the current value has at least two copies, adding two positions at each level. When the walk first reaches a value with fewer than two copies, there are two cases:

- If one copy exists, use it as the center and add one.
- If no copy exists, the most recently counted pair cannot remain a pair without a center beyond it. Use one copy of that previous level as the center instead, which changes the accumulated length by $-1$.

This always produces an odd valid length. Trying every distinct starting value covers the outer value of every possible non-one pattern.

**Treat one separately.** Squaring $1$ never advances, so the general loop would not terminate. Any odd number of ones forms a valid mirrored pattern because every level equals one. Use all copies when their count is odd, or one fewer when it is even.

The construction is feasible because every paired level consumes exactly two recorded occurrences and the center consumes one. It is maximal for its chosen start because extending the chain requires the first unavailable pair, and ending earlier cannot use more elements. Taking the maximum over starts and the all-one case is therefore globally optimal.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$, let $U$ be the number of distinct values, and let $M=\max(\texttt{nums})$. Building the frequency map costs $O(N)$. Repeated squaring grows double-exponentially, so a chain has $O(\log\log M)$ relevant levels before leaving the stored value range. The total time is $O(N+U\log\log M)$, commonly written $O(N\log\log M)$, and the frequency map uses $O(N)$ space.

## Alternatives and edge cases

- **Sort and run-length encode:** Sorting first can recover the same multiplicities, but costs $O(N\log N)$ time instead of expected linear hash counting.
- **Repeated full-array counts:** Calling `nums.count` for each candidate and square is correct but can cost $O(N^2\log\log M)$ time.
- **Only singletons:** Any one value forms a valid length-one pattern, so the answer is always at least one.
- **Even count of ones:** One copy must be omitted because every valid pattern length is odd.
- **Missing next center:** After counting a pair whose square is absent, convert that innermost pair into a single center by subtracting one.
- **Large squares:** Python integers grow safely; fixed-width implementations should use a wide type and stop once the square exceeds the source value range.
