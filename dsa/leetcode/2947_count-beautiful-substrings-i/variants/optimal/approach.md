## General

**Translate beauty into a length period.** A balanced substring has $t$ vowels
and $t$ consonants, so its count product is $t^2$. Write the prime
factorization of $K$ as

$$
K=\prod_p p^{e_p}.
$$

The condition $K\mid t^2$ holds exactly when $t$ contains each prime factor
$p$ at least $\lceil e_p/2\rceil$ times. Define

$$
D=\prod_p p^{\lceil e_p/2\rceil}.
$$

Then a balanced substring satisfies the divisibility rule exactly when $D$
divides $t$. Its total length $2t$ must therefore be divisible by $2D$.
Trial division computes $D$ from `k`.

**Pair compatible prefix states.** Let the prefix balance add $1$ for a vowel
and $-1$ for a consonant. A substring between prefix positions $l$ and $r$ has
equal vowel and consonant counts exactly when the balances at those positions
are equal. Its length is divisible by $2D$ exactly when
$l\bmod 2D=r\bmod 2D$.

Scan prefix positions from left to right and count prior occurrences of each
pair `(balance, position % (2 * D))`. Every prior matching pair defines one
beautiful substring ending at the current position, so add its frequency to
the answer before recording the current prefix. Seed position zero with
balance zero and remainder zero. These two state equalities are both necessary
and sufficient, so every beautiful substring is counted exactly once.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$ and $K=\texttt{k}$. Trial division takes
$O(\sqrt K)$ time, and the prefix scan takes $O(N)$ expected time with hash
lookups. Total time is $O(N+\sqrt K)$. At most $N+1$ prefix states are stored,
so auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Enumerate every substring:** Updating vowel and consonant counts for each left endpoint is correct but takes $O(N^2)$ time.
- **Use only prefix balance:** Equal balances enforce equal counts but do not enforce divisibility by `k`; the prefix-index remainder is also required.
- **Test the length modulo 2k:** This is sufficient but unnecessarily restrictive when `k` contains squared prime factors; the derived period $2D$ is exact.
- **k equals one:** Here $D=1$, so every balanced even-length substring is beautiful.
- **All vowels or all consonants:** No nonempty substring can have equal counts.
- **Single character:** It cannot be balanced and contributes zero.
- **Overlapping substrings:** Each distinct pair of prefix positions is counted independently, as required.

