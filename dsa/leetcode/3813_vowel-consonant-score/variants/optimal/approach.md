## General

The score depends only on two totals, so there is no need to retain characters or revisit any prefix. Maintain counters for vowels and consonants and inspect `s` from left to right.

For each character, use three mutually exclusive cases:

- If it is one of `a`, `e`, `i`, `o`, or `u`, increment the vowel counter.
- Otherwise, if it lies between `'a'` and `'z'`, increment the consonant counter.
- Otherwise it is a space or digit under the input contract, so leave both counters unchanged.

These cases assign every English letter to exactly the category defined by the problem and exclude every non-letter. After the scan, the two counters are therefore precisely `v` and `c`. If `c` is positive, integer division computes the required floor of the non-negative quotient. If `c` is zero, return `0` directly so no division by zero occurs. These are exactly the two branches in the score definition, which establishes that the result is correct.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Each character is examined once and each examination performs constant work, so the running time is $O(N)$. Only two counters are retained, giving $O(1)$ auxiliary space.

The legal contract caps $N$ at 100. That domain is too narrow for runtime timings to separate a one-pass scan reliably from plausible slower implementations once process and harness overhead are included. The package therefore uses a `bounded_domain` certificate: the loop structure proves at most 100 character examinations, and dedicated regression evidence compares the implementation with an independent classification oracle over exhaustive representative strings and deterministic inputs spanning every legal length.

## Alternatives and edge cases

- **Set membership for vowels:** A five-element set also provides constant-time membership, but a five-character literal is sufficient and avoids a separate mutable-looking object.
- **Subtract vowel count from all characters:** Treating every non-vowel as a consonant is incorrect because spaces and digits belong to neither category.
- **Built-in alphabetic classification:** `str.isalpha()` recognizes letters outside the English alphabet. The input is constrained to ASCII characters, but an explicit `'a' <= char <= 'z'` test states the required domain more precisely.
- **Repeated `count` calls:** Counting each vowel separately and deriving consonants with another scan remains linear because there are only five vowels, but the one-pass classification follows the contract directly.
- **No consonants:** Even when vowels are present, `c = 0` requires a score of `0` and must be handled before division.
- **No vowels:** With at least one consonant, integer division gives `0 // c = 0` naturally.
- **Spaces and digits:** They must leave both counters unchanged, including when the entire string contains no letters.
- **Floor semantics:** Both counts are non-negative, so Python's `//` operator gives exactly $\lfloor v/c\rfloor$ for positive `c`.
