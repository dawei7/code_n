## General

Every candidate number comes from a contiguous substring of `s`. Since `s` has at most ten digits, the solution can enumerate all substrings, convert each one into its integer value, test that value for primality, and retain unique primes in a set. After enumeration, it sorts the unique primes and sums the largest three—or all of them when fewer than three exist.

The implementation builds substring values incrementally, which avoids repeatedly slicing and parsing the same digits.

**Enumerating every substring exactly once**

The outer index `i` chooses the substring’s starting position. The inner index `j` moves from `i` to the final position, so it visits:

`s[i:i+1]`, `s[i:i+2]`, ..., `s[i:n]`.

Across all starts, this produces every nonempty contiguous substring exactly once as a position interval. There are

$$
\frac{n(n+1)}{2}
$$

such intervals.

Different intervals may represent the same integer. For example, repeated digits can create identical substrings, and leading zeros can make `"011"` and `"11"` both represent `11`. Enumeration is by substring occurrence; uniqueness is handled later by the set.

**Building values without substring conversion**

At the beginning of each outer iteration, `x = 0`. Extending the current substring by digit `s[j]` uses

`x = x * 10 + int(s[j])`.

Multiplying by ten shifts the existing decimal representation one place to the left, and adding the new digit fills that last place. If the digits from `i` through `j - 1` represented `x` before the update, the new `x` is exactly the integer represented by digits `i` through `j`.

For start `i` in the string `"12234"`, the values grow as `1`, `12`, `122`, `1223`, and `12234`. The earlier digits are reused arithmetically rather than reparsed for each longer substring.

This update also implements the leading-zero rule automatically. Starting from the first character of `"011"` gives `0`, then `1`, then `11`. Decimal arithmetic naturally ignores leading zeros, just as required.

**Testing primality**

`is_prime(x)` first rejects every `x < 2`. This correctly excludes zero and one, neither of which is prime.

For `x \ge 2`, it checks possible divisors from `2` through `\lfloor\sqrt{x}\rfloor`. If `x` is composite, it can be written as `a \cdot b`. Both factors cannot exceed `\sqrt{x}`, because then their product would exceed `x`. Therefore every composite number has at least one divisor no larger than its square root.

Conversely, if no integer in that range divides `x`, no nontrivial factorization exists and `x` is prime.

The expression

`all(x % i for i in range(2, int(sqrt(x)) + 1))`

uses remainders as truth values. A nonzero remainder is truthy and means `i` is not a divisor. A zero remainder is false and makes `all` stop immediately, rejecting the number. When `x` is `2` or `3`, the range is empty; `all` of an empty iterable is true, correctly classifying both as prime.

The source tests every integer divisor, including even divisors after two. This is simple and correct, though not the most optimized trial-division loop.

**Deduplicating prime values**

Whenever a substring value is prime, `st.add(x)` inserts it into a set. A set stores one copy of each integer, so the same prime contributes only once even if:

- the same digit sequence occurs at multiple positions;
- different sequences with leading zeros have the same integer value;
- nested substrings happen to evaluate to the same prime.

The primality test occurs before insertion. Therefore repeated occurrences are tested repeatedly even though the set later deduplicates them. That detail matters when describing the exact runtime: the set prevents duplicate contributions to the sum, not duplicate primality work.

**Selecting up to the three largest primes**

`sorted(st)` returns all unique primes in ascending order. The slice `[-3:]` selects the final three elements.

Python slicing makes the boundary cases convenient:

- if at least three primes exist, it selects exactly the largest three;
- if one or two exist, it selects all of them;
- if the set is empty, it produces an empty list.

`sum` then gives the required total, and `sum([])` is zero. No separate conditional branch is needed for any of these cases.

**A representative trace with leading zeros and repetition**

For `s = "011"`, the start at index zero generates `0`, `1`, and `11`. Only `11` is prime. The start at index one generates `1` and `11`, so `11` is found again. The final start generates `1`.

The set finishes as `{11}`, not two copies of `11`. Sorting and taking the last three returns the single available prime, and the answer is `11`.

This trace shows why position-based enumeration, numeric leading-zero handling, primality, and value deduplication are separate responsibilities.

## Complexity detail

Let `n` be the string length and `M` the largest numeric value represented by any substring. There are `O(n^2)` substrings. Extending a value is constant-time under the usual bounded-integer model, while a worst-case primality test tries `O(\sqrt{x})` divisors and is bounded by `O(\sqrt{M})`.

The enumeration and primality work therefore take

$$
O(n^2\sqrt{M})
$$

time in the worst case. Composite values may stop early, but primes near `M` require the complete divisor range. Sorting the set adds `O(U\log U)` time for `U` unique primes, where `U \le n(n+1)/2`. Under the stated small `n`, the trial-division bound dominates the manifest’s description.

Strictly speaking, Python arithmetic on arbitrarily large integers is not constant-time. Here `n \le 10`, so values are below `10^{10}` and the conventional arithmetic model is entirely reasonable.

The set can hold at most one prime per substring interval, so `U = O(n^2)` and set storage is `O(n^2)` in the worst case. `sorted(st)` creates another `O(U)` list. Thus peak auxiliary space is `O(n^2)`, matching the manifest. Loop state itself is constant.

## Alternatives and edge cases

- **Parse every substring slice:** Using `int(s[i:j+1])` is straightforward and also ignores leading zeros, but it repeatedly creates and parses strings, adding an extra length factor across all substrings. Incremental decimal construction reuses the prior prefix value.
- **Check the set before primality:** Tracking every previously tested numeric value could avoid repeated primality tests for duplicate substrings. It needs an additional set or a combined cache and may improve repeated inputs, but the exact source tests first and stores only primes.
- **Keep a three-element min-heap:** A heap can retain only the three largest unique primes after deduplication, avoiding a full final sort. With at most 55 substrings under `n \le 10`, sorting the set is simpler and easily fast enough.
- **Sieve of Eratosthenes:** Sieving through `M` would make primality lookups fast but could require memory proportional to a number near `10^{10}`, which is completely impractical. Trial division is appropriate for few candidates in a huge numeric range.
- **Faster primality testing:** Deterministic Miller–Rabin for the bounded integer range or optimized trial division skipping even candidates can be much faster. They add complexity unnecessary for the ten-character limit.
- **Zero and one:** `is_prime` rejects both explicitly through `x < 2`.
- **Two and three:** Their divisor ranges are empty, and the mathematical convention `all(empty) == True` correctly accepts them.
- **Leading zeros:** Incremental arithmetic turns `"007"` into values `0`, `0`, and `7`; the prime `7` is counted once by value.
- **Repeated prime occurrences:** A prime is inserted into `st` many times harmlessly, but contributes once to the final sum.
- **Fewer than three unique primes:** The negative slice returns every available element, so their complete sum is returned.
- **No primes:** Sorting an empty set, slicing it, and summing it naturally returns zero.
- **A one-character string:** The only substring is tested normally, so a one-digit prime is returned and any other digit yields zero.
- **Floating square root:** `sqrt(x)` is converted to an integer to obtain the trial bound. Values are at most ten decimal digits here, well within the range where the computed square root is sufficiently represented; for far larger integers, an exact integer square root would be safer.
- **Uniqueness by integer, not text:** `"02"` and `"2"` both represent prime `2` and must count only once; the integer set enforces exactly that interpretation.
