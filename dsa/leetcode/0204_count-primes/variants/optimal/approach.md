## General
Create a marker for every integer in `[0, n)` and initially regard values from `2` onward as possible primes. Explicitly mark `0` and `1` nonprime.

Process candidates `p` only while $p \cdot p < n$. If `p` is still marked, it is prime: any composite `p` would have a smaller factor that had already cleared it. Mark the multiples

$p ^{2}, p ^{2} + p, p ^{2} + 2p, \ldots$

as composite. Starting at $p^{2}$ is both safe and important. Every smaller multiple `kp` with $2 \le k < p$ has factor `k`, and therefore already has a prime factor smaller than `p`; earlier sieve steps cleared it.

For $n = 10$, candidate `2` clears `4,6,8`, and candidate `3` clears `9`. The remaining marked values `2,3,5,7` give count four. There is no need to process candidate `4` or any larger square root boundary because every composite below ten already has a factor no greater than its square root.

Using a byte array rather than a general-purpose object list reduces memory constants. Some languages can mark a slice of multiples efficiently, but the logical sieve remains the same.

No prime is ever cleared because it is not a positive multiple of a smaller prime other than itself. Every composite $x < n$ has a prime factor $p \le \sqrt{x}$. When that `p` is processed, `x` is one of its multiples at or beyond $p^{2}$ unless it was already cleared by an even smaller factor. Hence every composite is marked nonprime and every prime remains marked. Summing the markers therefore counts exactly the primes below `n`.

## Complexity detail
For each prime $p$, the sieve marks about $n/p$ multiples. The sum of reciprocals over primes yields total $O(n \log \log n)$ marking work. The candidate markers use $O(n)$ space.

## Alternatives and edge cases
- Trial-dividing every candidate up to its square root can require $O(n sqrt n)$ time.
- Starting each marking loop at `2p` remains correct but repeats composites already handled by smaller factors.
- A segmented sieve reduces memory when counting over very large intervals, at the cost of more machinery.
- For $n \le 2$, the interval contains no primes. The upper bound is exclusive, so a prime equal to `n` is never counted.
- Testing $p \cdot p < n$ avoids floating-point square-root rounding; fixed-width languages should guard multiplication overflow for extreme bounds.
