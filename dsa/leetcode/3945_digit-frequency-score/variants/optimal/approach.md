## General

**Collapse the frequency expression.** Suppose the decimal representation contains digits $a_1,a_2,\ldots,a_D$. Grouping equal positions by their digit value gives

$$
\sum_{d=0}^{9} d\cdot\operatorname{freq}(d)
=\sum_{i=1}^{D} a_i.
$$

The left side is the score from the problem definition, while the right side is the ordinary sum of all digit occurrences. A frequency table is therefore unnecessary: each decimal position can contribute its digit immediately.

Repeatedly apply `divmod(n, 10)`. The remainder is the current final digit, which is added to the score, and the quotient removes exactly that digit. After $j$ iterations, the accumulator equals the sum of the $j$ removed suffix digits and the remaining number contains precisely the unprocessed prefix. When the quotient becomes zero, every position has contributed exactly once, so the accumulator equals the defined frequency-weighted score.

## Complexity detail

Let $D=\lfloor\log_{10}n\rfloor+1$ be the number of decimal digits in `n`. Each iteration removes one digit and performs constant work, so the running time is $O(D)$. The quotient, current digit, and accumulator use $O(1)$ auxiliary space.

The legal contract fixes $D\le10$. That range is too narrow for a stable runtime-scaling comparison, so complexity verification uses a strict `bounded_domain` certificate. Its replacement evidence proves the ten-iteration work bound and checks the implementation against an independent string-based oracle over exhaustive low-domain values, deterministic values spanning the full range, and authored boundary cases.

## Alternatives and edge cases

- **Digit-frequency table:** Counting the ten possible digits and then evaluating `d * freq(d)` follows the definition literally and is also $O(D)$ time, but the algebraic identity makes the table unnecessary.
- **String conversion:** Converting `n` to text and summing converted characters is concise and remains $O(D)$, but allocates a $D$-character representation instead of using constant auxiliary space.
- **Repeated digits:** Every occurrence must contribute; direct digit extraction naturally adds repeated copies one at a time.
- **Zero digits:** A zero position is still processed but adds zero, including internal and trailing zeroes.
- **Smallest input:** For a one-digit positive number, the only digit is both the score and the returned value.
- **Upper boundary:** `1000000000` is the only legal ten-digit input and scores $1$ because all remaining positions are zero.
