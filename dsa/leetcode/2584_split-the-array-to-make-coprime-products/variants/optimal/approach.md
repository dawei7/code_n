## General

**Products are coprime exactly when no prime crosses the split**

Multiplying all values on either side would create enormous integers. Prime factors contain the only information needed.

The left and right products have a greatest common divisor greater than one exactly when some prime divides at least one value on both sides. Therefore, a split after index $i$ is valid if and only if every prime factor appearing in the prefix has its final occurrence at or before $i$.

Equivalently, for each prime $p$, consider the interval from its first array occurrence to its last. A valid split cannot cut through any such interval.

**Factor each value into distinct primes**

For every `nums[i]`, the code tries divisors `j` starting at two while `j <= x // j`. When `j` divides $x$, it records prime factor `j`, then repeatedly divides $x$ by `j` until no copy remains.

Removing all copies is important for two reasons:

- multiplicity inside one value does not change whether the prime occurs at index $i$;
- after smaller factors are removed, any leftover `x > 1` is itself prime.

The division test uses `j <= x // j` instead of `j * j <= x`, avoiding multiplication overflow in fixed-width translations.

The exact implementation increments `j` through all integers, not only primes. Composite candidates no longer divide after their prime factors have been removed, so correctness is preserved, though this is slower than a smallest-prime-factor sieve.

**Store each prime's reach at its first index**

Dictionary `first` maps a prime to the index where it first appeared. Array `last` starts as `[0,1,2,...,n-1]`.

When a prime $p$ first appears at $i$, the code stores `first[p] = i`. On every later occurrence at index $r$, it updates

`last[first[p]] = r`.

Thus the first occurrence's array slot records the farthest index reached by that prime's occurrence interval. If several primes first appear at the same array index, updates occur in increasing scan order, so that slot ultimately contains the maximum last occurrence among them.

No entry is needed at intermediate occurrences. The interval becomes active when the sweep reaches its first index and remains active through its recorded end.

**Sweep merged prime intervals**

Variable `mx` is the farthest endpoint of every prime-occurrence interval whose first position has been reached within the current connected prefix block.

It begins as `last[0]`. As index $i$ is scanned, `mx = max(mx, last[i])` extends the block whenever a prime first occurring at $i$ continues farther right.

If the block currently ends at `mx`, the split after `mx` becomes valid only after every position through `mx` has been inspected. One of those positions may introduce a different prime whose last occurrence extends the block again.

The test `if mx < i: return mx` detects the first position just beyond the completed block. At that point all prime intervals that began at or before `mx` also end at or before `mx`, so no prime appears on both sides of the split.

**Why this returns the smallest valid index**

Before the sweep passes `mx`, some active interval reaches at least through `mx`. Splitting earlier would cut that interval and put the same prime into both products. Those earlier candidates are invalid.

When `i` first exceeds `mx`, every factor from the prefix has finished. Any prime starting at $i$ or later belongs only to the suffix. The split at `mx` is valid, and because all smaller indices were ruled out by an active interval, it is the smallest valid split.

If closure reaches index $n-1$, the scan never steps beyond it while a legal right side remains. Returning $-1$ is correct because splitting after the last index is forbidden.

**Trace a factor chain**

In `[4,7,8,15,3,5]`:

- prime $2$ occurs from index $0$ through $2$, so `last[0]=2`;
- prime $7$ occurs only at index $1$;
- primes $3$ and $5$ first appear at index $3$ and continue within the suffix.

The sweep starting at zero closes at index two. Position one introduces nothing beyond two, and position two does not extend it. On reaching index three, `mx < i` and the function returns two. No prime factor crosses that split.

**Why values equal to one are harmless**

One has no prime factors. Its `last` entry remains its own index and introduces no cross-split constraint. Products involving ones keep the same prime set, which is exactly what the sweep models.

## Complexity detail

Let $n$ be the array length and $M=\max(\texttt{nums})$. The exact trial-division loop can test $O(\sqrt M)$ candidate divisors for a prime input, so factorization costs $O(n\sqrt M)$ time in the worst case. The final sweep is $O(n)$.

This differs from the manifest's sieve-based $O(M\log\log M+n\log M)$ description; no sieve is present in the checked-in code. `last` uses $O(n)$ space, and `first` stores at most all distinct prime factors encountered, also $O(n)$ in input-scale terms. The input is not modified because factor removal affects local `x` only.

## Alternatives and edge cases

- **Smallest-prime-factor sieve:** Precompute factors through $M$ and factor each value quickly, matching the manifest at the cost of $O(M)$ memory.
- **Multiply and compute GCD:** Prefix and suffix products become huge and make arithmetic unnecessarily expensive.
- **Prime occurrence counts:** Track remaining counts while sweeping and detect when no active prime remains; this is another correct factor-based formulation.
- **Array length one:** No legal split exists, so the function returns $-1$.
- **All ones:** No prime interval crosses anything; the earliest split is zero when $n\ge2$.
- **Repeated prime across distant values:** Its first-to-last interval blocks every split in between, even if intermediate values do not contain it.
- **Transitive factor chains:** Overlapping prime intervals merge through `mx` just like overlapping ordinary intervals.
- **Prime input values:** Trial division reaches the square-root boundary, then records the leftover prime.
- **No split before final closure:** If `mx` reaches $n-1$, a nonempty suffix cannot avoid the crossing factor.
- **Manifest distinction:** Complexity must follow the direct divisor loop rather than an absent sieve.
