## General

**Separate prime discovery from pair discovery**

The desired pairs must satisfy two independent facts: both numbers are prime, and their sum is `n`. Testing primality from scratch for every possible pair would repeat the same divisibility work many times. The exact solution first builds a table that answers “is this number prime?” in constant time, then performs a simple complement scan.

The table is the list `primes` of length `n`. An index represents the number with the same value. It is initially true everywhere, and the sieve marks composite indices false. Although indices zero and one are never explicitly corrected, this does not affect the result because the later pair scan only examines `x >= 2` and its complement `y = n - x >= x >= 2`.

**How the sieve eliminates composites**

The outer loop considers every `i` from 2 through `n - 1`. If `primes[i]` is still true, no smaller prime has marked `i`, so `i` is prime. The inner loop visits `2i, 3i, 4i, ...` below `n` and marks each multiple false.

Every marked value is composite because it is a product of `i` and an integer of at least two. In the opposite direction, take any composite `c < n`. It has some prime divisor `p` smaller than `c`. When the outer loop reaches `p`, `p` is still true and its multiples include `c`, so `c` becomes false. Thus, for every queried index from two onward, the table is true exactly for primes.

The exact code starts marking at `i + i` rather than `i * i`. Multiples below `i * i` may already have been marked by smaller factors, so starting at the square would avoid redundant writes. Starting at `2i` is nevertheless correct and retains the standard sieve asymptotic bound.

**Only scan through half of the target**

After the sieve, the solution loops over

`x = 2, 3, ..., n // 2`

and defines `y = n - x`. The sum condition is then automatic: `x + y = n`. The upper limit gives `x <= y`, which is exactly the ordering required inside each pair. It also prevents producing both `[x, y]` and `[y, x]`.

The test `primes[x] and primes[y]` is now constant-time. If both entries are true, the pair satisfies all requirements and is appended.

There is no need to search for `y`, factor it, or use a second nested loop. Every possible partner for a chosen `x` is uniquely determined by subtraction.

**Why output order comes for free**

The problem wants pairs sorted by increasing first value. Python's `range` produces `x` in strictly increasing order, and the solution appends each accepted pair immediately. Therefore the answer list is already sorted and requires no final sorting pass.

The equality case is included. When `n` is even and `x = n / 2` is prime, `y` is the same number, and `[x, x]` is a legal pair because the contract allows `x <= y` rather than requiring strict inequality.

**A walkthrough with `n = 10`**

The sieve makes 2, 3, 5, and 7 the true prime indices relevant below 10. The pair scan considers:

- `x = 2`, so `y = 8`; 8 is composite.
- `x = 3`, so `y = 7`; both are prime, so append `[3, 7]`.
- `x = 4`, so `y = 6`; both fail.
- `x = 5`, so `y = 5`; both table lookups identify the same prime index, so append `[5, 5]`.

The result is `[[3, 7], [5, 5]]` in the required order.

**Why every and only valid pair is returned**

Every appended pair uses `y = n - x`, so its sum is correct. The scan guarantees `2 <= x <= y <= n`, and the sieve checks that both values are prime. Hence no invalid pair is appended.

Now consider any valid pair `[a, b]`. Because `a <= b` and `a + b = n`, `a <= n / 2`. Since primes are at least two, `a` appears in the scan. At that iteration the complement is exactly `n - a = b`, and both sieve entries are true, so the pair is appended. This proves completeness as well as soundness.

**Small-target safety**

The list has indices zero through `n - 1`, not an index `n`. This is still safe: the pair scan starts at two, making `y = n - x <= n - 2`. When `n` is too small to admit such an `x`, the range is empty and no lookup occurs. For `n = 2`, for example, there is no pair of two positive primes summing to two, and the code correctly returns an empty list.

## Complexity detail

Let `n` be the target. Initializing the Boolean list takes `O(n)` time and space. For each prime `p < n`, the inner loop marks about `n / p` multiples. The sum over primes is `O(n log log n)`, which dominates the initialization and the final `O(n)` half-range scan. The total time is therefore `O(n log log n)`.

Starting each marking loop at `2p` performs more constant-factor work than starting at `p^2`, but it does not change that asymptotic sieve bound. Composite outer indices do not launch an inner loop because they have already been marked false.

The `primes` table uses `O(n)` auxiliary space. The returned list can contain at most `O(n)` pairs, although in practice it contains far fewer. Complexity conventions usually report the sieve's `O(n)` working storage; including the output does not change the same linear upper bound.

## Alternatives and edge cases

- **Trial division for every complement:** Checking each `x` and `n - x` up to their square roots avoids the sieve array but repeats work and can take about `O(n sqrt n)` time in the straightforward form.
- **Sieve from `i * i`:** This is a safe constant-factor optimization because smaller multiples already have smaller prime factors. The exact solution starts at `2i` and remains correct.
- **Generate a prime list and use two pointers:** Two pointers can find sums in the sorted prime list, but constructing that list still needs primality preprocessing and the direct complement scan is simpler here.
- **Scan all `x < n`:** Doing so produces reversed duplicates unless extra deduplication is added. Stopping at `n // 2` enforces `x <= y` directly.
- **`n < 4`:** Two primes cannot sum to these targets under the minimum prime value two, so the scan is empty and the answer is empty.
- **Odd `n`:** Since every prime except two is odd, an odd target can only use two as one member. The general scan handles that fact without a special branch.
- **Equal prime pair:** When `n` is twice a prime, the midpoint pair is legal and included once.
- **Indices zero and one remain true:** They are never queried by the pair scan, so this unconventional initialization does not create a false result.
- **Largest allowed target:** The linear table for `n <= 10^6` is practical, while checking every pair by repeated factorization would be considerably slower.
- **Output ordering:** Appending during the increasing `x` scan already satisfies the sort requirement; sorting again would be redundant.
