## General
**Only remainders determine compatibility**

Write each value as a multiple of $K$ plus its normalized remainder in $[0, K-1]$. If two values have remainders $r$ and $s$, their sum is divisible by $K$ exactly when

$$
(r+s) \bmod K = 0.
$$

For a nonzero remainder $r$, the required partner class is $K-r$. Negative input values cause no special mathematical case once they are normalized; Python's `value % k` already produces a remainder in the needed range for positive `k`.

Count the represented remainder classes in a hash map. The original magnitudes
and indices no longer matter because any member of a class is interchangeable
with any other member of that class for divisibility. A sparse map also avoids
examining all $K$ possible classes when only a few occur.

**Match complementary remainder counts**

For every represented nonzero remainder $r$, each of its values must consume
one value of remainder $K-r$. A complete pairing is possible only if those two
counts are equal. Equality is also sufficient for these two classes: pair
their members arbitrarily one-for-one.

Looking up the complement in the map takes expected constant time. Visiting
both $r$ and $K-r$ merely repeats the same equality check, so it does not
change correctness and still costs only $O(R)$ total work.

**Handle the self-complementary classes**

Remainder $0$ can pair only with remainder $0$, so its count must be even. When $K$ is even, remainder $K/2$ is also its own complement because $K/2 + K/2 = K$; that count must be even as well.

These parity tests are not implied by comparing a class count with itself. In particular, an odd number of $K/2$ remainders would pass a naïve equality check but leave one unpaired element.

**Why the conditions construct a complete pairing**

Assume all checks pass. Pair the zero-remainder values among themselves. If $K$ is even, do the same for the $K/2$ values. For every remaining complementary class pair, equal counts let us form one pair from each side until both classes are empty. Every constructed pair sums to a multiple of $K$, and every input element is consumed exactly once.

Conversely, any valid complete partition must obey the same conditions. A value in class $r$ has no legal partner outside class $K-r$, except for the two self-complementary classes. Unequal complementary counts or an odd self-complementary count necessarily leaves an element without a valid partner. The conditions are therefore both necessary and sufficient.

## Complexity detail
Building the remainder-frequency map examines all $N$ values once. Checking
every represented class and its complement takes $O(R)$ expected time, so the
total is $O(N+R)$. The map stores $R$ counts, giving $O(R)$ auxiliary space.
Because $R \le \min(N,K)$, both bounds remain linear in the input length.

The benchmark fixes $K=97$ and varies $N$ over arrays whose first half has remainder $1$ and second half has remainder $96$. Frequency counting remains linear. A correct implementation that repeatedly scans the unpaired list for one complement performs $O(N^2)$ work, completes all legal tiers, and is rejected by scaling.

## Alternatives and edge cases
- **Fixed frequency array:** allocate one counter for every remainder and check
  the whole range. This is deterministic $O(N+K)$ time and $O(K)$ space, but
  it does unnecessary work when $K$ is large and few remainders occur.
- **Sort normalized remainders:** after sorting, a two-ended pairing check can match complementary values in $O(N \log N)$ time and $O(N)$ space.
- **Repeated complement search:** remove one value and linearly search the remaining values for a compatible partner. Arbitrary compatible choices are safe, but repeated searches take $O(N^2)$ time.
- **Remainder zero:** its members cannot be rescued by any nonzero class; their count must be even.
- **Even divisor:** remainder $K/2$ is self-complementary and also needs an even count.
- **Divisor one:** every integer has remainder zero, and the promised even array length makes every pairing valid.
- **Negative values:** normalize modulo $K$ before counting; language-specific negative-remainder behavior may require `((value % k) + k) % k`.
- **Duplicate values:** pairing depends on counts, not distinctness, so every occurrence must be counted.
- **Using only some elements:** the contract requires a partition of the entire array; one unmatched value makes the answer `false`.
- **Even length alone:** it guarantees the right number of elements for pairs but does not guarantee compatible remainder counts.
