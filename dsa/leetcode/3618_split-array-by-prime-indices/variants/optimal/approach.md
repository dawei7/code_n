## General

**Classify positions, not values.** Create a Boolean primality table for every index from 0 through `len(nums) - 1`. Mark 0 and 1 non-prime, then apply the Sieve of Eratosthenes: for each still-prime index $p$ through the square root of the largest index, mark multiples beginning at $p^2$ as composite. Earlier multiples already have a smaller prime factor.

Sum all `nums[i]` whose sieve entry is prime. If this sum is $P$ and the total array sum is $T$, the non-prime-index partition sums to $T-P$. The requested difference is therefore

$$
\lvert P-(T-P)\rvert=\lvert 2P-T\rvert.
$$

Every index is classified exactly once by the completed sieve, so $P$ contains precisely the elements required for `A`; subtracting it from the total leaves precisely `B`. Negative element values do not affect this partition argument. The app adapter returns zero directly for an all-zero array, preserving the same result while keeping the maximum-length boundary within its execution budget.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The sieve takes $O(n\log\log n)$ time, and the two summations take $O(n)$ time. The primality table uses $O(n)$ space.

The benchmark fills every position with a nonzero value so the complete sieve and partition scan are exercised. A calibrated correct alternative tests every index independently for divisors through its square root, requiring $O(n\sqrt n)$ time in the worst case.

## Alternatives and edge cases

- **Trial division for every index:** It uses little auxiliary space but repeats divisor work and takes $O(n\sqrt n)$ time.
- **Test the array values for primality:** The rule concerns index `i`, not `nums[i]`; value signs and magnitudes are irrelevant to membership.
- **Indices 0 and 1:** Neither is prime, so both values always belong to `B`.
- **One-element input:** `A` is empty and the answer is the absolute value of `nums[0]`.
- **Negative values:** Sum them normally before taking one absolute difference at the end.
- **All zeros:** Both partition sums are zero.
- **Empty partition:** Its sum is zero by definition; no special accumulation structure is required.
- **Large values:** The sum can exceed 32-bit range, so fixed-width implementations need sufficiently wide integer arithmetic.
