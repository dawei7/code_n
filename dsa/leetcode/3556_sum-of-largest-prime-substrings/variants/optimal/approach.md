## General

There are only $n(n+1)/2$ nonempty substrings. For each starting index, extend the ending index one digit at a time and update the candidate as `value = value * 10 + digit`. This constructs every value without repeatedly parsing whole substrings and naturally ignores leading zeros.

For each candidate greater than one, test whether any integer from $2$ through $\lfloor\sqrt{\texttt{value}}\rfloor$ divides it. A composite number has at least one factor no larger than its square root, so finding none proves primality. Store every prime in a set; this is necessary because equal numeric values can arise from repeated text or from substrings with different numbers of leading zeros.

Finally sort the distinct primes and sum the last three entries. Python slicing also handles sets containing fewer than three values, including the empty set.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and let $M$ be the largest integer represented by any substring. There are $O(n^2)$ candidates, and one primality test takes $O(\sqrt{M})$ time in the worst case. Thus the total time is $O(n^2\sqrt{M})$. At most $O(n^2)$ distinct prime values are stored; sorting them costs $O(n^2\log n)$ time and the set plus sorted list use $O(n^2)$ space.

## Alternatives and edge cases

- **Trial division through the candidate:** Checking all possible divisors below the number is correct but takes $O(M)$ per candidate instead of $O(\sqrt{M})$.
- **Sieve through the largest substring value:** The largest value may approach $10^{10}$, making a full sieve far too large even though only $O(n^2)$ candidates need testing.
- **Reparse every substring:** Calling integer conversion on every slice remains correct, but incremental construction avoids repeated digit work.
- **Leading zeros:** Values such as `"02"` and `"2"` both represent `2` and must be counted only once.
- **Zero and one:** Neither is prime, so primality testing begins only for candidates greater than one.
- **Fewer than three primes:** Sum every distinct prime found; an empty set yields zero.
- **Integer width:** A ten-digit substring can exceed a signed 32-bit integer, so implementations in fixed-width languages need a 64-bit type.
