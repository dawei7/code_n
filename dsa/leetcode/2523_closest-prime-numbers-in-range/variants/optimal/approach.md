## General

**Generate primality information once**

Let $R = \texttt{right}$. Create a Boolean table for every integer from $0$ through $R$, initially treating all entries from $2$ onward as prime. For each still-prime value $p \le \lfloor\sqrt{R}\rfloor$, mark the multiples starting at $p^2$ as composite. Any smaller multiple of $p$ already has a prime factor below $p$ and was therefore handled earlier. Conversely, every composite at most $R$ has a prime factor at most its square root, so the completed table classifies every value correctly.

**Only consecutive primes can form the answer**

Scan the interval from left to right and remember the preceding prime. If a candidate pair skipped another prime between its endpoints, one of the two adjacent gaps inside that pair would be no larger. It is therefore sufficient to compare consecutive primes. Record a pair only when its gap is strictly smaller than the best gap seen so far. Because the scan is ascending, refusing equal-gap updates automatically preserves the pair with the smaller first value.

If the scan never observes two primes, the initialized answer `[-1, -1]` is returned.

## Complexity detail

The Sieve of Eratosthenes takes $O(R \log \log R)$ time, and scanning the requested interval takes $O(R)$ time in the worst case. The sieve therefore determines the overall $O(R \log \log R)$ time bound. Its primality table uses $O(R)$ space; the scan itself uses constant additional space.

## Alternatives and edge cases

- **Trial division for every candidate:** Testing each integer with divisors through its square root avoids the sieve table, but can require $O(R\sqrt{R})$ time when the interval width grows with $R$.
- **Segmented sieve:** Sieving only the requested interval can reduce storage for a narrow high-valued range, but it needs a separate base-prime sieve and adds implementation complexity that is unnecessary for $R \le 10^6$.
- **Fewer than two primes:** Empty, singleton, and prime-free intervals all return `[-1, -1]`.
- **Values below two:** Neither `0` nor `1` is prime, so scanning begins at `max(2, left)`.
- **Equal minimum gaps:** Updating only for a strictly smaller gap retains the earliest pair, as required.
- **The pair `[2, 3]`:** This is the only consecutive-prime pair with gap $1$ and is handled without a special case.
