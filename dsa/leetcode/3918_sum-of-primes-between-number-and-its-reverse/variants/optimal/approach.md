## General

Reverse the decimal representation of `n` and convert it back to an integer. Integer conversion naturally removes any leading zeroes created by the reversal. Let $L$ be the smaller of `n` and its reversal, and let $U$ be the larger.

Use the Sieve of Eratosthenes to classify every integer from `0` through $U$. Begin by treating all positions as potentially prime, then mark `0` and `1` composite. For each still-prime value $p\le\sqrt U$, mark

$$
p^2, p^2+p, p^2+2p, \ldots
$$

as composite. Starting at $p^2$ is sufficient because every smaller multiple of $p$ has a factor below $p$ and was handled by an earlier prime.

After the sieve, sum exactly those values from $L$ through $U$ whose flags remain prime. The loop includes both endpoints, as required.

Every composite number at most $U$ has a prime factor no greater than its square root, so the corresponding sieve iteration marks it. Conversely, only multiples of known primes are marked, and no prime is a multiple of a smaller prime. Thus the surviving flags identify precisely the primes through $U$; restricting their sum to `[L, U]` returns every and only the primes in the requested interval.

## Complexity detail

Constructing the sieve through $U$ takes $O(U\log\log U)$ time, and summing the interval takes $O(U)$ time, so the combined bound is $O(U\log\log U)$. The Boolean sieve uses $O(U)$ auxiliary space. Reversing the at-most-four-digit input is dominated by these bounds.

## Alternatives and edge cases

- **Trial division for every candidate:** Test each number in `[L, U]` with divisors through its square root. This uses $O(1)$ auxiliary space but takes $O(U\sqrt U)$ time in the worst case.
- **Segmented sieve:** Sieve only `[L, U]` after generating base primes through $\sqrt U$. This can reduce memory for a very narrow interval with huge endpoints, but the contract caps $U$ at `1000`, so a direct sieve is clearer.
- **Prefix sums over primes:** A reusable prefix table would answer many interval queries quickly, but this function receives only one `n`.
- **Trailing zeroes:** Reversing `10` or `1000` yields `1`; the range endpoints must use the integer reversal, not a fixed-width string.
- **Reversal smaller than `n`:** Always sort the two endpoints before scanning.
- **Palindromic input:** When `n == r`, the answer is `n` if `n` is prime and `0` otherwise.
- **Value one:** `1` is not prime and must be marked explicitly.
- **Inclusive endpoints:** A prime equal to either `n` or `r` contributes to the sum.
