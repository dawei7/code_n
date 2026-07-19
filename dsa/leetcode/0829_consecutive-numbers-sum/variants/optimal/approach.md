## General
**Describe a representation by its length**

Let a sequence have positive first term $a$ and length $k$. Its sum is

$$
a+(a+1)+\cdots+(a+k-1)
=ka+\frac{k(k-1)}{2}.
$$

For a fixed length $k$, solving for the start gives

$$
a=\frac{n-\frac{k(k-1)}{2}}{k}.
$$

Therefore that length produces exactly one representation when the numerator is positive and divisible by $k$. In the implementation, compute `remainder = n - length * (length - 1) // 2` and test `remainder % length == 0`; the loop bound below already guarantees positivity.

**Stop when even the smallest positive sequence is too large**

The smallest positive sequence of length $k$ starts at $1$ and sums to

$$
\frac{k(k+1)}{2}.
$$

Once this value exceeds $n$, no longer length can have a positive start. Thus only lengths through $O(\sqrt n)$ need examination. Integer multiplication and division avoid any floating-point boundary error near $10^9$.

**Why every representation is counted once**

Every valid sequence has one definite length $k$, and substituting that length into the equation recovers its unique starting value $a$. The divisibility test accepts it. Conversely, every accepted length yields a positive integer $a$, and the sum formula proves that its consecutive sequence totals $n$. Distinct accepted lengths describe distinct sequences, so the count has neither omissions nor duplicates.

## Complexity detail
The condition $k(k+1)/2 \le n$ permits only $O(\sqrt n)$ lengths. Each iteration performs constant-time integer arithmetic, giving $O(\sqrt n)$ time. The algorithm stores only counters and arithmetic temporaries, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Count odd divisors:** The number of representations equals the number of odd divisors of $n$. Removing powers of two and factoring the remaining odd part also takes $O(\sqrt n)$ time, but the length equation connects more directly to the positivity condition.
- **Sliding window of positive integers:** Expanding and shrinking a consecutive window is correct but can take $O(n)$ time.
- **Enumerate every starting value:** Growing a sum from each possible start repeats work and can be quadratic without careful window reuse.
- **Single-term sequence:** Every positive `n` has at least the representation containing `n` alone.
- **`n = 1`:** The only valid sequence is $1$.
- **Positive start:** Lengths whose triangular offset leaves zero or a negative numerator are invalid; the loop bound excludes them.
- **Exact divisibility:** A fractional starting value does not describe an integer sequence and must not be rounded.
- **Large input:** Use integer arithmetic for triangular values rather than floating-point square roots.
