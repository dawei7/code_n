## General

A Sieve of Eratosthenes supplies both facts the task needs: which integers through `n` are prime and the primes themselves in increasing order. Initialize every index as potentially prime, exclude `0` and `1`, and for each surviving factor through $\lfloor\sqrt N\rfloor$, mark its multiples beginning at the factor's square as composite.

Scan the sieve from `2` upward and add each prime encountered to one running sum. This generates exactly

$$
2,\quad 2+3,\quad 2+3+5,\quad\ldots
$$

in their required order. If a new sum is still at most `n`, the same sieve immediately determines whether that sum is prime; whenever it is, record it as the current answer. Once the sum exceeds `n`, every later prefix is larger because all added primes are positive, so the scan can stop.

Every recorded value is prime, is at most `n`, and is a sum of consecutive primes starting at `2`, so it is valid. Conversely, every permitted sum is one of the prefixes generated before the stopping point and is tested for primality. Since those prefixes strictly increase and the algorithm keeps the latest prime one, the final recorded value is the largest valid answer. If none is recorded, returning zero implements the specified fallback.

## Complexity detail

Let $N=\texttt{n}$. The sieve takes $O(N\log\log N)$ time and stores $O(N)$ primality flags. Scanning the flags and accumulating the prime prefix takes $O(N)$ additional time and $O(1)$ additional space, so the overall bounds are $O(N\log\log N)$ time and $O(N)$ space.

## Alternatives and edge cases

- **Trial-divide every integer:** Testing successive candidates by divisors through their square roots can generate the same prime sequence, but its worst-case work is substantially larger than a sieve over the full interval.
- **Linear sieve:** Euler's sieve can generate the primes in $O(N)$ time and use the same prefix scan, but it needs a more involved inner-loop invariant and prime list.
- **Search a prime list for every sum:** Keeping all primes in an ordinary list and testing each prefix with linear membership is correct, but repeats a growing scan; the sieve flag provides the same answer in constant time.
- **Arbitrary consecutive-prime windows:** Prefix sums or a sliding window over all prime intervals solve a different problem; every legal sum here must begin with `2`.
- **Composite prefix sums:** A sum such as `2 + 3 + 5 = 10` is skipped even though all of its terms are prime.
- **No qualifying value:** When `n = 1`, even the first sum exceeds the limit, so the answer is `0`.
- **One-term sum:** For `n = 2`, the prime `2` qualifies as a sum containing one prime.
- **Monotonic stopping:** After a prefix sum exceeds `n`, adding more positive primes can never produce another legal candidate.
