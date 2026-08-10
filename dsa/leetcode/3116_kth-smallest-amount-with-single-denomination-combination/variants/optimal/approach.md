## General

**Each denomination creates one stream of multiples.** Because different coin denominations may not be mixed, coin value `c` can make exactly:

$$
c,2c,3c,\ldots
$$

The required sequence is the sorted union of these streams, with duplicate amounts included only once. For example, amount 6 belongs to both the multiples of 3 and 6 but occupies one position in the union.

Directly merging streams is impossible for very large `k`, which may reach two billion. The source instead answers a prefix-count question: how many distinct constructible amounts are at most `mx`?

**Count one stream with integer division.** There are `mx // c` positive multiples of `c` no larger than `mx`. Summing this count over coins would double-count amounts divisible by several denominations.

**Inclusion-exclusion removes duplicate counting.** For any nonempty subset of denominations, an amount belongs to every stream in that subset exactly when it is divisible by their least common multiple. The number of such amounts through `mx` is:

`mx // lcm(subset)`.

Inclusion-exclusion adds counts for odd-sized subsets and subtracts counts for even-sized subsets. Every amount divisible by at least one coin then contributes exactly once to `cnt`.

The source enumerates masks from 1 through `(1 << len(coins)) - 1`. For every set bit `j`, it updates `v = lcm(v, coins[j])`. `i.bit_count()` gives the subset size and chooses the sign.

**Early LCM termination is safe.** If `v > mx`, no positive multiple of `v` is at most `mx`. Adding more denominations can only keep the LCM equal or increase it, so the inner loop breaks. The later term `mx // v` is zero, regardless of the subset sign. Although unvisited mask bits still contribute to `bit_count`, adding or subtracting zero has no effect.

**The predicate is monotone.** `check(mx)` returns whether the union contains at least `k` values no greater than `mx`. Increasing `mx` cannot remove a multiple, so the count never decreases. The predicate is therefore false for an initial prefix of candidate bounds and true from the desired answer onward.

The $k$th smallest amount is precisely the first `mx` for which the prefix count reaches `k`.

**Binary search through Python's range.** The return statement uses:

`bisect_left(range(10**11), True, key=check)`.

`range(10**11)` is a lazy integer sequence from zero through $10^{11}-1$; it does not allocate one hundred billion integers. Python's keyed `bisect_left` evaluates `check` at logarithmically many midpoint values and finds the first position whose key is at least `True`. Since Boolean order is `False < True`, this is the first true predicate.

The search ceiling is sufficient. The smallest denomination is at most 25, so the $k$th multiple of that denomination alone is at most:

$$
25k\le5\cdot10^{10}<10^{11}.
$$

The union's $k$th amount can only be smaller.

**Trace coins `[5,2]` with `k=7`.** At bound 12, inclusion-exclusion counts six multiples of 2, two multiples of 5, and subtracts one multiple of `lcm(2,5)=10`. The union count is $6+2-1=7$, so `check(12)` is true. At 11 it is only six, so binary search returns 12.

**Why the returned position is an amount.** The searched range contains consecutive integers starting at zero, so a range index and its value are identical. `bisect_left` returns the index of the first true key, which is also the smallest bound satisfying the count and therefore the amount itself.
Inclusion-exclusion makes `cnt(mx)` exactly the number of distinct constructible positive amounts at most `mx`. Monotonic binary search returns the smallest `mx` with `cnt(mx) >= k`. That smallest threshold is the definition of the $k$th element in a sorted distinct set.

## Complexity detail

Let $m$ be the number of denominations and $U=10^{11}$. One `check` enumerates $2^m-1$ subsets and may inspect up to $m$ coins per subset, so it costs $O(m2^m)$ time. Binary search makes $O(\log U)$ checks. The exact source therefore takes:

$$
O(m2^m\log U)
$$

time.

This differs from the manifest's $O(2^m(m+\log U))$ description, which would require precomputing subset LCMs once. `solution.py` recomputes them inside every predicate call.

No subset table is stored. Aside from binary-search internals and scalar loop variables, working space is $O(m)$ for iteration context at most, effectively $O(1)$ beyond the input in this iterative Python implementation. The manifest's $O(2^m+m)$ space does not match the exact source.

## Alternatives and edge cases

- **Precompute subset LCM and sign:** Spend $O(m2^m)$ once, then make each count check $O(2^m)$. This matches the manifest more closely.
- **Remove redundant denominations:** If one coin is a multiple of another, its stream adds no new amounts and may be discarded before inclusion-exclusion.
- **Heap merge of multiple streams:** Suitable for small `k`, but two billion makes it infeasible.
- **One denomination:** The answer is simply `coins[0] * k`; the general method finds the same result.
- **Overlapping multiples:** Inclusion-exclusion ensures each amount is counted once.
- **Pairwise distinct coins:** Given, though one can still divide another.
- **LCM above the bound:** Its contribution is zero and the inner loop can stop.
- **Bound zero:** Every division count is zero, so positive `k` makes the predicate false.
- **Large `k`:** Binary search depends logarithmically on the amount, not linearly on `k`.
- **Search ceiling:** `25 * k` proves $10^{11}$ is safely above every answer.
- **Python range:** It is lazy and does not allocate proportional to the numeric ceiling.
- **Boolean key ordering:** `bisect_left` searches the false-to-true transition.
- **LCM arithmetic:** Python integers prevent overflow; fixed-width languages should cap an LCM once it exceeds the current bound.
- **Subset parity:** Odd sets add and even sets subtract.
- **Source/manifest mismatch:** The source recomputes LCMs per binary-search probe and does not allocate a $2^m$ table.
