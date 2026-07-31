## General

A palindrome is fixed once its left half and optional center are fixed. If a letter occurs $f_i$ times in `s`, its left-half multiplicity is $c_i=\lfloor f_i/2\rfloor$. The one odd-frequency letter, when present, must occupy the center. Consequently, ranking distinct palindromic permutations is exactly the same as ranking distinct permutations of the multiset $(c_0,\ldots,c_{25})$.

Suppose $r$ half-characters remain and their multiset has

$$
T=\frac{r!}{\prod_i c_i!}
$$

distinct permutations. The lexicographic block beginning with letter $i$ has

$$
B_i=\frac{(r-1)!}{(c_i-1)!\prod_{j\ne i}c_j!}=\frac{T c_i}{r}
$$

members. Scan candidate letters from `a` to `z`. If $B_i<k$, skip that entire block and replace $k$ with $k-B_i$; otherwise fix letter $i$ and continue with its decremented count. If every block is skipped, the requested rank does not exist.

Direct factorials become enormous, although only comparisons with `k` matter. The implementation computes each multinomial as a product of binomial coefficients and saturates it at $k r$. This cap is sufficient: if the true total is at least $kr$, then every nonempty candidate block satisfies $B_i\ge k$, so the smallest available letter is certainly correct. Below the cap, the total is exact and the formula $B_i=T c_i/r$ gives exact block sizes. This preserves every rank decision without constructing unbounded integers.

After all left-half positions are chosen, concatenate the half, the forced center, and the reversed half. Prefix blocks partition all distinct multiset permutations in lexicographic order, so repeatedly choosing the unique block containing rank $k$ returns exactly the requested palindrome.

## Complexity detail

Let $n=\lvert s\rvert$, let $r\le\lfloor n/2\rfloor$ be the current half length, and let the alphabet size be $\Sigma=26$. A capped binomial calculation stops once it reaches at most $kr\le 5\cdot10^9$ under the source constraints. Its multiplicative work is $O(\log(nk))$; each of the $O(n)$ positions evaluates a constant-size frequency table. The resulting bound is $O(n\log(nk))$ time. With the fixed source limits on `k` and the lowercase alphabet, this behaves linearly in the string length.

The two frequency arrays use $O(\Sigma)=O(1)$ space. The selected half and final answer require $O(n)$ space, which determines the recorded space bound.

## Alternatives and edge cases

- **Generate successive permutations:** Advancing the sorted half `k - 1` times can require $O(nk)$ work and times out near the maximum rank.
- **Enumerate with backtracking:** Producing every distinct half before selecting one is factorial in the half length and stores or visits irrelevant results.
- **Use uncapped factorials:** The multinomial formula is correct, but repeatedly manipulating integers with thousands of digits adds avoidable time and memory.
- **Use floating-point logarithms:** Logarithms estimate huge counts compactly but can round on the exact boundary where a block count equals `k`, causing a wrong rank decision.
- **One-character string:** The half is empty; rank 1 returns the forced center, while every larger rank is absent.
- **All characters equal:** There is exactly one distinct palindrome even though equal occurrences admit many indistinguishable rearrangements.
- **Odd length:** The odd-frequency character never participates in the ranked half and is inserted only after unranking.
- **Rank beyond the total:** Skipping every first-character block proves that fewer than `k` distinct palindromes exist, so the result is `""`.
- **Saturated count:** When $T\ge kr$, even a candidate with one remaining copy owns at least `k` completions, making the smallest available letter safe.
