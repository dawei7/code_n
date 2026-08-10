## General

**Reinterpret the requested sum per subsequence**

For each positive `g`, beauty is

`g * number of strictly increasing subsequences whose GCD is g`.

Summing beauty over all `g` is the same as summing the GCD of every strictly increasing subsequence once:

`answer = sum over increasing subsequences S of gcd(S)`.

Grouping by GCD gives the statement’s definition; ungrouping gives this per-subsequence view.

Directly tracking every possible exact GCD together with every ending value would be expensive. The source uses the divisor identity

`h = sum of phi(d) over all divisors d of h`,

where `phi` is Euler’s totient function.

Apply it to each subsequence GCD:

`gcd(S) = sum_{d divides gcd(S)} phi(d)`.

A divisor `d` divides the GCD of `S` exactly when every element of `S` is divisible by `d`. Swapping the order of summation yields

`answer = sum over d of phi(d) * C[d]`,

where `C[d]` is the number of strictly increasing subsequences consisting entirely of values divisible by `d`.

This is the central number-theoretic transformation. The source counts divisibility-based subsequences, which are easier to update, and combines them with totients at the end.

**Compute all Euler totients with a sieve**

The array `phi` begins as `phi[x] = x`.

When `phi[prime] == prime` for a number at least two, that number has not been reduced by any smaller prime and is therefore prime.

For every multiple of that prime, the source performs

`phi[multiple] -= phi[multiple] // prime`.

This applies the product formula

`phi(x) = x * product over distinct prime p dividing x of (1 - 1/p)`.

After all primes are processed, `phi[d]` is available for every possible divisor up to `maximum = max(nums)`.

**For one divisor, count increasing subsequences by ending value**

Fix a divisor `d`. Consider only input values divisible by `d`. A subsequence remains strictly increasing if its previous last value is smaller than the current value.

Processing `nums` from left to right automatically preserves index order. For a current value `value` divisible by `d`, define

`quotient = value // d`.

Dividing every eligible value by the same positive `d` preserves strict ordering:

`previous_value < value` exactly when `previous_quotient < quotient`.

The source maintains a Fenwick tree for `d`. At index `q`, it stores counts of increasing subsequences processed so far whose last divided value is `q`.

**Query only strictly smaller ending values**

To append the current value, an existing subsequence must end at a value strictly smaller than it. The Fenwick prefix query therefore stops at

`quotient - 1`.

The returned `prefix` is the number of eligible previous subsequences.

Each can be extended by the current occurrence, and the current value alone forms one new singleton subsequence. Thus

`ways = prefix + 1`.

The source adds `ways` to `divisible_counts[d]` because these are exactly the new all-divisible-by-`d` increasing subsequences whose final index is the current position.

It also updates Fenwick index `quotient` by `ways` so later larger values can extend them.

Using `quotient - 1` rather than `quotient` enforces strict increase. Equal values at different indices create separate singleton and earlier-chain counts but cannot extend one another.

**Why processing order preserves subsequences**

A subsequence must retain original index order. The outer loop processes values exactly in `nums` order.

When current `value` queries its tree, the tree contains only subsequences ending at earlier indices. Appending the current index is therefore legal. Future values see the newly added subsequences, while past values never see future state.

The Fenwick dimension handles value ordering, and the outer scan handles index ordering. Both are necessary for a strictly increasing subsequence.

**Create divisor trees lazily**

Different divisors need independent ending-value states. Dictionary `trees` maps divisor `d` to its Fenwick tree.

A divisor tree is created only when some input value is divisible by `d`. Its maximum quotient is `maximum // d`, so its length is

`maximum // d + 1`.

Large divisors receive short trees; divisor one receives the longest.

This avoids allocating a full `maximum`-length tree for every divisor, which would be quadratic.

**Enumerate only divisors of the current value**

Current `value` contributes to `C[d]` exactly for divisors `d` of `value`.

The source loops `divisor` from one through `floor(sqrt(value))`. Whenever `value % divisor == 0`, it calls `extend` for that divisor and for paired divisor `value // divisor`.

For a perfect square, the two divisors are equal, so the `other != divisor` check prevents double processing.

This enumeration finds every positive divisor once in `O(sqrt(value))` trial steps.

**Understand the Fenwick operations**

For a prefix query, the source begins at `quotient - 1` and repeatedly clears the lowest set bit:

`index -= index & -index`.

Those Fenwick nodes partition the desired prefix into disjoint stored ranges.

For an update, it starts at `quotient` and repeatedly adds the lowest set bit:

`index += index & -index`.

Those nodes are exactly the Fenwick aggregates whose ranges include the updated point.

Both operations take `O(log(maximum / d))` time, bounded by `O(log maximum)`.

All counts are reduced modulo `1,000,000,007`. The source maintains each running sum below the modulus, so subtracting the modulus once after adding another reduced value is sufficient.

**Recover exact GCD contributions at the end**

`divisible_counts[d]` counts increasing subsequences whose every element is divisible by `d`. A subsequence with GCD `h` appears in this count for every `d` dividing `h`.

The final sum includes its contribution

`sum_{d divides h} phi(d)`,

which equals `h`. Therefore that subsequence contributes exactly its GCD—no more and no less—even though it was counted in several divisor buckets.

The source computes

`sum(phi[d] * divisible_counts[d]) mod MOD`.

This proves that the divisibility counts reconstruct the requested exact-GCD beauty sum.

**Trace `[4, 6]`**

The increasing subsequences are `[4]`, `[6]`, and `[4, 6]`.

For divisor two, all three are counted because both values are divisible by two. For divisor four, only `[4]` is counted; for divisor six, only `[6]` is counted. Other relevant divisor counts overlap similarly.

Totient weighting ensures:

- Singleton `[4]` receives `sum phi(d) over d|4 = 4`.
- Singleton `[6]` receives six.
- Pair `[4,6]` has common divisors one and two and receives `phi(1) + phi(2) = 1 + 1 = 2`.

Total is twelve.

**Why the source does not maintain exact GCD states**

Appending a value to a subsequence changes its GCD to `gcd(old_gcd, value)`, creating many transition combinations across ending values. The totient transform replaces those transitions with a simpler invariant: divisibility by `d` is preserved when appending another multiple of `d`.

Each divisor can then use an ordinary increasing-subsequence Fenwick tree.

## Complexity detail

Let `V = max(nums)`. Let `T` be the total number of divisor occurrences processed:

`T = sum over values of tau(value)`,

where `tau` is the divisor-count function.

The totient sieve takes `O(V log log V)` time in the standard analysis and `O(V)` space.

Trial divisor enumeration performs `O(sqrt(value))` checks per input value, bounded by `O(n sqrt(V))` total. Each actual divisor triggers one Fenwick query and update in `O(log V)`, for `O(T log V)`.

There is an additional exact-source allocation cost. Creating tree `d` initializes `floor(V/d) + 1` zeros. Across all encountered divisors, let

`A = sum of those allocated tree lengths`.

In the worst case, `A = O(V log V)` by the harmonic series. List initialization takes `O(A)` time and space. A conservative exact bound is therefore

`O(V log log V + n sqrt(V) + T log V + A)` time

and

`O(V + A)` space, with `A <= O(V log V)`.

The manifest states `O(V log log V + n sqrt(V) + T log V)` time and `O(V log V)` space. Its time expression omits the potentially material zero-initialization cost of the lazily created Fenwick lists, while its space bound acknowledges their harmonic total.

Modulo arithmetic does not change these asymptotic bounds.

## Alternatives and edge cases

- **DP by exact GCD and ending value:** It follows the definition directly but can create many GCD transitions and large state.
- **Enumerate all subsequences:** There are exponentially many and this is infeasible.
- **Möbius inversion:** Exact-GCD counts can sometimes be recovered from divisible counts by subtracting multiples. Totient weighting is more direct because the desired weight is the GCD itself.
- **Segment tree per divisor:** It can query smaller endings but uses more constants and similar or greater storage than Fenwick trees.
- **Use quotient `q` in the prefix query:** Querying through `q` would allow equal values to extend and count non-decreasing rather than strictly increasing subsequences.
- **Process values out of input order:** Sorting `nums` would destroy subsequence index order and overcount.
- **Duplicate values:** Each occurrence forms its own singleton, but equal values cannot extend each other because the query stops at `q - 1`.
- **Value one:** Its only divisor is one, and it can begin or extend only according to strict value order.
- **Perfect-square value:** Its square-root divisor is processed once rather than twice.
- **Singleton subsequences:** The `+1` in `ways` ensures every individual element is counted for each of its divisors.
- **Modulo wrap:** If `prefix + 1 == MOD`, the source stores zero, which is the correct modular result.
- **Lazy trees:** Only divisors appearing in at least one input value allocate Fenwick storage.
- **Maximum value domain:** `V <= 70000` bounds the sieve and tree universe.
- **Input preservation:** The method reads `nums` without sorting or modifying it.
