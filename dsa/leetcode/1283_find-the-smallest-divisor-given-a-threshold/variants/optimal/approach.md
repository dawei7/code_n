## General
**A monotone feasibility test.** For a candidate divisor $d$, compute the rounded sum using `(value + d - 1) // d`. Increasing $d$ can never increase any quotient, so candidate divisors have a monotone shape: smaller values are infeasible, followed by all feasible values.

**Searching the first feasible divisor.** Divisor $1$ is the smallest possible candidate, and $M$ is always feasible because each positive array value then contributes one and the guaranteed threshold is at least $n$. Binary-search the inclusive interval from $1$ through $M$. If the midpoint's sum is at most the threshold, it may be the answer, so keep it as the right boundary. Otherwise every divisor through the midpoint is also infeasible, so move the left boundary above it. When the boundaries meet, all smaller divisors have been rejected and the remaining divisor is feasible; it is therefore the smallest valid choice.

## Complexity detail
Each feasibility test scans all $n$ values in $O(n)$ time and constant auxiliary space. Binary search performs $O(\log M)$ tests across the divisor range $[1,M]$, giving $O(n \log M)$ time and $O(1)$ extra space. The running sum may stop early once it exceeds the threshold without changing these worst-case bounds.

## Alternatives and edge cases
- **Linear divisor search:** Testing $1,2,3,\ldots$ finds the same first feasible value but can require $O(nM)$ time.
- **Floating-point ceiling:** Integer arithmetic avoids precision issues and implements the required independent rounding exactly.
- **Threshold equals $n$:** Every contribution must be one, so the answer is exactly $M$.
- **Divisor one:** When the threshold is at least `sum(nums)`, the minimum divisor is one.
- **Repeated maximum values:** They do not alter the search bounds or monotonicity.
