## General

**Remove even candidates from the sieve representation**

All even integers greater than 2 are composite, so the competitive solution
stores only enough slots to represent odd numbers. For odd value `x`, index
`x // 2` identifies its slot: 1 maps to 0, 3 to 1, 5 to 2, and so forth.

Array length `n // 2` is exactly the number of odd positive integers below `n`
for both even and odd `n`. Avoiding even slots roughly halves memory and removes
the work of crossing out multiples of 2.

**Understand the initial count's placeholder trick**

Every slot starts true and `cnt` starts as the number of slots. This initially
counts every odd positive integer below `n`, including 1, which is not prime.
At the same time, prime 2 has no slot and is not explicitly added.

Those two discrepancies cancel: the erroneous count for 1 acts as a placeholder
for the omitted count of 2. For every `n > 2`, 2 belongs in the answer and 1
does not, so replacing one with the other keeps the total correct. The early
return handles `n <= 2`, where that cancellation would not apply.

This is compact but subtle. An alternative implementation could set slot zero
false and initialize `cnt = 1 + number_of_odd_candidates_at_least_3`, making the
special role of 2 explicit.

**Sieve only odd prime candidates**

The outer loop visits odd `i` starting at 3. If `i*i >= n`, it breaks because
every composite below `n` has at least one prime factor no larger than its
square root. All necessary composite marking has then been initiated.

If `is_prime[i//2]` is false, `i` was already marked composite and must not
generate its own marking pass. If it remains true, `i` is prime and the method
marks its odd composite multiples.

**Start at the prime's square**

The inner loop begins at `i*i`. Any smaller multiple `k*i` has factor
`k < i`; it was already handled through a smaller prime factor. Starting at the
square avoids redundant work.

The step is `2*i`, not `i`. Since `i*i` is odd, adding `2*i` moves through odd
multiples only. Adding `i` would alternate odd and even values, wasting time on
even composites that have no stored slot.

**Decrement only on the first composite discovery**

Before changing a slot, the loop checks `if not is_prime[j//2]: continue`.
A composite such as 45 may appear in marking passes for both 3 and 5. The count
must decrease once, not once per prime factor.

On the first discovery, the method decrements `cnt` and sets the slot false.
Later discoveries see false and leave the count unchanged. This makes `cnt`
equal to initial candidate count minus the number of distinct odd composites.

**Trace `n = 10`**

There are `10 // 2 = 5` slots, conceptually for 1, 3, 5, 7, and 9. Initial
count is five, standing for prime 2 plus odd candidates 3, 5, 7, and 9.

Outer candidate 3 has square 9 below 10, so it marks slot for 9 and decrements
the count to four. The next odd candidate 5 has square 25, so the outer loop
breaks. Returned four represents 2, 3, 5, and 7.

**Why the final count is exact**

Every odd composite below `n` has a smallest odd prime factor $p$. When outer
loop reaches $p$, the composite is at least $p^2$ and occurs in the inner
sequence, so its slot is marked and its initial candidate contribution is
removed.

No odd prime is a multiple of a smaller prime, so its slot is never cleared.
After the cancellation between 1 and 2, the remaining count therefore contains
exactly prime 2 and all odd primes below `n`.

**Inactive linear-sieve class**

`Solution_TLE` is not the normal entry point. It builds a smallest-prime-factor
array and a prime list, generating each composite through controlled prime
products. It is called with `n - 1` so the returned list includes primes at most
that value, equivalent to primes strictly below `n`.

Despite its theoretical $O(n)$ work, Python overhead can make this version
slower in practice, which explains its class name. It uses a full-size list and
does not affect selected `Solution` behavior.

## Complexity detail

The odd-only sieve crosses out roughly $n/p$ values for each odd prime $p$ up
to $\sqrt n$. The standard sum over reciprocal primes yields
$O(n\log\log n)$ time. Odd-only storage and the $2p$ stride improve constants,
not the asymptotic class.

`is_prime` has `n // 2` boolean entries, so auxiliary space is $O(n)`. Counter
and loop variables use constant additional state.

## Alternatives and edge cases

- **Explicitly count prime 2:** Initialize count and slot zero without the 1-for-2 placeholder trick; clearer for maintenance.
- **Full boolean sieve:** Easier index interpretation but uses about twice as many candidate slots.
- **Bytearray square-start sieve:** Compact and often faster because slice assignment runs in optimized native code.
- **Linear sieve:** Inactive `Solution_TLE` has linear theoretical work but higher Python-level constants.
- **`n <= 2`:** Early return zero is required before the placeholder initialization.
- **`n = 3`:** One slot for 1 acts as the count for prime 2, returning one.
- **Odd composite with several factors:** Decrement only when its slot is still true.
- **Exclusive upper bound:** Inner and candidate ranges stop before `n`.
- **Even composites:** Never stored and never need marking.
- **Square boundary:** Break when `i*i >= n` because values equal to `n` are excluded.
