## General

**Convert divisibility into an exact period.** A balanced substring contains
$t$ vowels and $t$ consonants, so the product in the contract is $t^2$. If

$$
K=\prod_p p^{e_p},
$$

then $K\mid t^2$ exactly when $t$ contains every prime $p$ to exponent at
least $\lceil e_p/2\rceil$. Define

$$
D=\prod_p p^{\lceil e_p/2\rceil}.
$$

Thus the product is divisible by `k` exactly when $D\mid t$. Since the
substring has length $2t$, its length must be divisible by $2D$. Trial
division of `k` constructs this smallest sufficient divisor rather than using
an unnecessarily large period such as $2K$.

**Encode both requirements in a prefix state.** Give a vowel weight $+1$ and
a consonant weight $-1$. Two prefix positions have the same cumulative balance
exactly when the substring between them has equally many vowels and
consonants. That substring's length is divisible by $2D$ exactly when the two
positions have the same remainder modulo $2D$.

Scan all prefix positions and count prior occurrences of
`(balance, position % period)`, where `period = 2 * D`. At each position, every
matching earlier state contributes one distinct beautiful substring ending
there. Add that frequency before recording the current state, and seed the
empty prefix as `(0, 0)`. Equal balances and equal remainders are jointly
necessary and sufficient, so the scan counts every valid substring once.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$ and $K=\texttt{k}$. Factoring `k` by trial
division takes $O(\sqrt K)$ time. The prefix scan takes $O(N)$ expected time
with hash-table operations, for $O(N+\sqrt K)$ total expected time. The
frequency table stores at most $N+1$ states and uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every substring:** Maintaining counts from each starting position is correct but takes $O(N^2)$ time, which is too slow for the larger input bound of this version.
- **Track only prefix balance:** Equal balances enforce equal vowel and consonant counts but do not enforce divisibility by `k`; the position remainder is also necessary.
- **Use period 2k:** This sufficient period rejects valid substrings whenever squared prime factors let $D$ be smaller than $K$.
- **k equals one:** Here $D=1$, so every balanced substring qualifies.
- **Repeated prime factors:** The ceiling in $\lceil e_p/2\rceil$ handles odd exponents, such as requiring a factor $p^2$ when `k` contains $p^3$.
- **All vowels or all consonants:** No nonempty substring can have equal counts.
- **Single character:** A length-one substring cannot be balanced.
- **Overlapping substrings:** Different prefix-position pairs are distinct substrings and are counted independently.
