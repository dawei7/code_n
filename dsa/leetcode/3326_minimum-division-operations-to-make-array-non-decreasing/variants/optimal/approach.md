## General

For a composite number $x$, let $p$ be its smallest prime factor. Its greatest proper divisor is $x/p$, so the required operation changes $x$ into

$$
\frac{x}{x/p}=p.
$$

A prime number has greatest proper divisor $1$, so the same operation leaves it unchanged. Consequently, every array value has only two useful states: its original value, or its smallest prime factor after one operation. Repeating the operation on that prime factor cannot reduce it further.

Precompute the smallest prime factor of every composite value through the legal maximum $U=10^6$. Start each prime's marking at its square and visit candidate factors in increasing order. The first factor stored for a composite is therefore its smallest prime factor; an unmarked value is prime or $1$.

Process a copy of the array from right to left. The value at `index + 1` is already the largest value that can be retained while keeping the processed suffix valid. If `values[index] <= values[index + 1]`, leaving the current value unchanged uses fewer operations than reducing it and cannot hurt any earlier position.

If the current value is larger, it must be reduced: retaining it would violate the adjacent order. Look up its smallest prime factor. An unmarked current value cannot change, and a factor still larger than the right neighbor cannot satisfy the order, so either condition makes the entire task impossible. Otherwise replace the value by that factor and count one operation.

This greedy choice is forced at every inversion. After it is made, the processed suffix is non-decreasing. It also leaves the current position as large as possible among all minimum-operation ways to repair that suffix, which gives the next position to the left the least restrictive upper bound. Induction from the last element proves that a completed scan uses the minimum possible number of operations.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $U=10^6$, the maximum legal element value. The sieve takes $O(U\log\log U)$ time, and the right-to-left scan takes $O(n)$ time, for $O(U\log\log U+n)$ total time. The factor table uses $O(U)$ space and the copied array uses $O(n)$ space, giving $O(U+n)$ auxiliary space.

The native source builds the fixed-domain table once at module load. LeetCode invokes the method across many testcases in the same process, so module-scoped preprocessing prevents the $O(U\log\log U)$ setup from being repeated for every call.

## Alternatives and edge cases

- **Trial division at every inversion:** Testing divisors through the square root avoids the table but can repeat nearly $\sqrt U$ modulus operations for many equal or distinct large composites.
- **Cached trial division:** Memoizing factorizations improves repeated-value inputs, but its worst case remains slower when many distinct values require reduction.
- **Process from left to right:** A choice that appears valid can be invalidated by a later, smaller neighbor; the right-to-left order fixes the necessary upper bound before deciding the current value.
- **Already non-decreasing:** No value is changed, so the answer is zero.
- **Prime at an inversion:** The operation divides the prime by $1$ and leaves it unchanged, making the target ordering impossible.
- **Composite factor still too large:** The smallest prime factor is the composite's only smaller reachable value, so no additional operation can rescue the inversion.
- **One and repeated values:** The value $1$ never needs reduction, and equality is allowed by the non-decreasing condition.
