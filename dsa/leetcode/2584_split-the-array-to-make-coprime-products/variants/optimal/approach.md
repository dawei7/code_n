## General

The products themselves may be enormous, but their exact magnitudes do not matter. Two positive products are coprime exactly when no prime divides a number on both sides of the split.

**Turn primes into crossing intervals:** For each distinct prime factor, record the last array index at which it occurs. While scanning candidate split positions from left to right, factor the current value and extend `rightmost` to the largest last occurrence of any prime encountered in the prefix. Every such prime must remain entirely on the left before a split can be valid.

At index `i`, if `rightmost > i`, some prime already present in the prefix also occurs in the suffix, so the two products share that divisor. If `rightmost == i`, every prime seen in the prefix ends by `i`; no prime can divide both products, making the split valid. Because indices are scanned in increasing order and the last array position is excluded, the first returned index is exactly the smallest legal answer.

**Factor efficiently:** Build a smallest-prime-factor table through $M=\max(\texttt{nums})$. Repeatedly divide a value by its recorded smallest factor, removing all copies before continuing, so each distinct prime is processed once per occurrence-bearing value. A value of `1` contributes no prime factors.

## Complexity detail

Let $n$ be the array length and $M=\max(\texttt{nums})$. Building the smallest-prime-factor table takes $O(M\log\log M)$ time. Factoring all values twice and scanning the array takes $O(n\log M)$ time in the worst case. The table, last-occurrence map, and iteration state use $O(M+n)$ space.

## Alternatives and edge cases

- **Direct prefix and suffix products:** Arbitrary-precision multiplication and repeated greatest-common-divisor checks retain far more numeric information than necessary and can become prohibitively expensive.
- **Trial division per value:** Dividing each value by candidates through its square root avoids the sieve but has an $O(n\sqrt M)$ worst-case factorization bound.
- **Store factor sets per index:** Factoring once and retaining every set avoids the second factorization pass, trading $O(n\log M)$ additional storage for less repeated work.
- **Single element:** When $n=1$, no index leaves two non-empty sides, so the answer is `-1`.
- **Values equal to one:** One has no prime factors and therefore never extends the crossing boundary.
- **Smallest-index requirement:** Returning as soon as the boundary closes is necessary; later valid cuts do not replace the earliest one.
