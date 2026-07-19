## General
For divisibility by three, the exact accumulated sum matters only for maximizing value within each remainder class. Maintain `dp[r]` as the largest sum obtainable from processed elements with remainder $r$. Initially, zero is reachable with remainder zero, while remainders one and two are unreachable.

**Include or exclude each value**

Copy the three previous states before processing a value. Excluding the value preserves every old state. Including it transforms a reachable residue `r` into `(r + value) % 3` with candidate sum `dp[r] + value`; maximize the destination state with that candidate. Reading only the old snapshot prevents one array value from being used more than once.

**Why three maxima are sufficient**

Suppose two processed subsets have the same remainder and one has the larger sum. Adding any identical future selection changes both sums by the same amount and preserves their shared remainder, so the smaller sum can never lead to a better final answer. Keeping only the maximum for each residue therefore loses no optimal solution.

After all values, `dp[0]` is the largest reachable sum divisible by three. The initial empty-subset state ensures it is at least zero.

## Complexity detail
Each of the $n$ values updates exactly three remainder states, taking $O(n)$ time. The current and previous arrays contain three entries each, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate all subsets:** It directly checks every selection but takes $O(2^n)$ time.
- **Remove the cheapest residues greedily:** Starting from the total sum and removing one residue-one item or two residue-two items can be made correct, but requires careful symmetric cases and minimum tracking.
- **Recompute every prefix:** Rebuilding remainder DP from scratch for each prefix returns the same final answer but takes $O(n^2)$ time.
- **All values divisible by three:** Selecting every value is optimal.
- **No positive divisible subset:** The empty subset yields the required answer `0`.
- **Duplicate values:** Treat positions independently; equal values may all be selected when available.
