## General

**Collapse the transformations into one weighted sum.** Each round is a linear operation modulo $10$: a new digit is the sum of two adjacent digits. Repeating this rule combines neighboring coefficients exactly as Pascal's identity does. If $n=\lvert s\rvert$, set $k=n-2$, and let $d_i$ be the integer value of `s[i]`. After $k$ rounds, the two remaining digits satisfy

$$
L \equiv \sum_{i=0}^{k}\binom{k}{i}d_i \pmod{10}
$$

and

$$
R \equiv \sum_{i=0}^{k}\binom{k}{i}d_{i+1} \pmod{10}.
$$

Therefore, it is sufficient to accumulate

$$
L-R \equiv \sum_{i=0}^{k}\binom{k}{i}(d_i-d_{i+1}) \pmod{10}.
$$

The answer is `True` precisely when this difference is congruent to zero modulo $10$.

**Recover each coefficient modulo 10.** Computing the exact binomial coefficients is impractical at the maximum length, but a residue modulo $10$ is uniquely determined by its residues modulo $2$ and modulo $5$. Lucas's theorem states that for a prime $p$, after writing $k$ and $i$ in base $p$,

$$
\binom{k}{i} \equiv \prod_j \binom{k_j}{i_j} \pmod p.
$$

For $p=5$, repeatedly inspect one base-$5$ digit pair and multiply entries from the fixed $5\times5$ table of small binomial coefficients. If any selected digit exceeds its corresponding total digit, the residue is zero. For $p=2$, Lucas's condition has a compact bit test: the residue is one exactly when adding $i$ and $k-i$ creates no binary carry, which is equivalent to `(i & (k - i)) == 0`.

Let the resulting residues be $a$ modulo $2$ and $b$ modulo $5$. Of the two values $b$ and $b+5$ modulo $10$, exactly one has parity $a$; choose that value as the coefficient modulo $10$. Multiplying it by `ord(s[i]) - ord(s[i + 1])` is valid because subtracting the character codes gives the same difference as subtracting the digit values.

## Complexity detail

There are $n-1$ coefficients. The base-$5$ Lucas calculation examines $O(\log_5 n)$ digit positions for each coefficient, while the modulo-$2$ test and the Chinese-remainder reconstruction take constant time. The total time is therefore $O(n\log n)$, more precisely $O(n\log_5 n)$, and the fixed lookup table plus scalar accumulators use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Literal round-by-round simulation:** This directly follows the statement, but processes $(n-1)+(n-2)+\cdots+2=O(n^2)$ adjacent pairs and is too slow for $n=10^5$.
- **Building Pascal's triangle:** Storing all coefficient rows also costs $O(n^2)$ time and space, although only one row modulo $10$ is needed.
- **Exact multiplicative binomial recurrence:** Consecutive coefficients can be generated with exact division, but their integer sizes grow to $\Theta(n)$ bits near the center; this is suitable for the small Operations I bound, not this problem's bound.
- **Reducing before exact division:** Updating consecutive binomial coefficients modulo $10$ with the usual multiplicative formula is invalid because the denominator may not be invertible modulo $10$.
- **Reusing a freshly produced digit:** Every round is simultaneous. Feeding a new digit into the next pair during the same round changes the transformation.
- **Leading zeroes:** `s` is a positional string. Leading zeroes remain digits and must not be discarded by parsing the whole input as an integer.
- **Minimum length:** When $n=3$, $k=1$, the coefficient row is $(1,1)$ and exactly one operation remains.
- **Uniform digits:** If every input digit is equal, the two weighted sums are identical regardless of the coefficient residues.
