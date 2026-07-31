## General

**Count one word with a multinomial coefficient**

If a word has length $m$ and every letter were distinguishable, its letters would have $m!$ orders. Exchanges among the $f_c$ identical copies of a letter $c$ do not change the resulting word, so the number of distinct permutations is

$$
\frac{m!}{\prod_c f_c!}.
$$

The choices for separate word positions are independent. Multiplying this quantity over all words therefore counts every permitted full-string anagram exactly once while never allowing letters or whole words to cross a space.

**Perform division in modular arithmetic**

The modulus $P=10^9+7$ is prime and every needed factorial index is below $P$. Fermat's little theorem gives $a^{-1}\equiv a^{P-2}\pmod P$ for every nonzero $a$. Precompute factorials through the maximum word length. Compute the inverse of the largest factorial with one modular exponentiation, then derive all smaller inverse factorials backwards from

$$
(i-1)!^{-1}=i\cdot i!^{-1}\pmod P.
$$

For each word, count its letters and multiply `factorial[length]` by the inverse factorial for each frequency. Multiplying all word contributions modulo $P$ produces the requested result. The factorial identity supplies exactly the number of distinct permutations for each word, and independence makes their product exact for the complete string.

## Complexity detail

Let $N=\lvert s\rvert$ and let $L$ be the maximum word length. Splitting and counting all letters take $O(N)$ time. Building factorial and inverse-factorial tables takes $O(L)$ time, and $L\le N$, so total time is $O(N)$. The words, frequency counters, and tables use $O(N)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **One modular inverse per frequency:** Applying `pow(factorial[count], P - 2, P)` for every distinct letter is correct, but the shared inverse-factorial table avoids many logarithmic exponentiations.
- **Exact integer factorials:** Forming enormous multinomial integers before reducing modulo $P$ is mathematically correct but incurs superlinear big-integer arithmetic and unnecessary memory growth.
- **Rescan for every position:** Recounting a word from scratch for each character position finds the same frequencies but costs $O(N^2)$ on a long word.
- **Identical letters:** A word containing only one repeated letter contributes exactly `1`.
- **Single-character words:** Each contributes `1` and does not change the product.
- **Word boundaries:** Spaces are separators, not permutable characters; each word stays at its original index.
- **Repeated words:** Equal word texts at different positions still make independent choices, so their permutation counts are multiplied.
