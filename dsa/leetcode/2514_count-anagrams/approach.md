## General

**Count permutations independently inside each word**

Words cannot exchange positions, and letters cannot move from one word to another. Only the letters inside each word are permuted.

For a word of length $L$ with character frequencies $f_1,f_2,\ldots$, the number of distinct permutations is the multinomial count

$$
\frac{L!}{\prod_c f_c!}.
$$

$L!$ counts arrangements if every occurrence were distinguishable. Dividing by $f_c!$ removes the overcount from permuting identical copies of character $c$.

Choices for different words are independent, so the total number of full-string anagrams is the product of these per-word counts.

**Accumulate all numerator factorials**

`ans` starts at one. For each word, `enumerate(w,1)` produces positions `i=1,2,...,L`.

The update

`ans = ans*i % mod`

multiplies by

$$
1\cdot2\cdots L=L!.
$$

Because this repeats independently for every word, `ans` eventually contains the product of all word-length factorials modulo `mod`.

The name `ans` is temporary at this stage: it contains only the numerator until modular division is applied at the end.

**Build denominator factorials without tables**

A new `Counter` is created for each word because equal letters in different word positions do not belong to one shared permutation group.

When character `c` is seen for the $r$-th time, `cnt[c]` becomes $r$, and the code multiplies `mul` by $r$.

If a letter occurs $f$ times in one word, its successive contributions are

$$
1\cdot2\cdots f=f!.
$$

Doing this for every distinct letter and every word makes `mul` equal to the complete product of frequency factorials.

This incremental technique avoids precomputing factorial and inverse-factorial arrays, despite the manifest summary describing such tables.

**Trace one word**

For `"too"`:

- position 1 contributes 1 to the numerator; first `t` contributes 1 to the denominator;
- position 2 contributes 2; first `o` contributes 1;
- position 3 contributes 3; second `o` contributes 2.

The word contributes

$$
\frac{3!}{1!\,2!}=\frac{6}{2}=3
$$

distinct permutations: `"too"`, `"oto"`, and `"oot"`.

For `"hot"`, all frequencies are one, so it contributes $3!=6$. Their independent product is $3\cdot6=18$.

**Perform modular division with an inverse**

Ordinary integer division cannot be applied after values have been reduced modulo $10^9+7$. Instead, division by `mul` is multiplication by its modular inverse:

`pow(mul,-1,mod)`.

The modulus is prime. Every factorial factor is at most the input length, which is below the modulus, so `mul` is not divisible by the modulus and its inverse exists.

The final expression

`ans*inverse(mul) % mod`

is congruent to the product of all multinomial counts.

**Why reducing throughout is safe**

Modular multiplication is compatible with ordinary multiplication:

$$
(ab)\bmod p
=
\bigl((a\bmod p)(b\bmod p)\bigr)\bmod p.
$$

Reducing `ans` and `mul` after each factor prevents unnecessary integer growth while preserving the final residue. Applying the denominator inverse at the end yields the same modular result as multiplying each word's multinomial count separately.

**Word boundaries are preserved**

`s.split()` returns the words in their original order. The single-space guarantee means no empty words appear.

The algorithm multiplies counts and never permutes the word list itself. For example, arrangements of `"abc def"` never include swapping `"abc"` and `"def"`, which the definition forbids.


For each word, the numerator loop contributes its length factorial and the counter loop contributes exactly every duplicate-frequency factorial. Their quotient is precisely that word's distinct permutation count.

Multiplication combines independent choices across all fixed word slots. Modular inversion performs the quotient correctly under the prime modulus, so the returned value is exactly the number of distinct anagrams modulo the required constant.

## Complexity detail

Let $N=\lvert s\rvert$. Splitting and scanning every character takes $O(N)$ time. Counter operations are expected $O(1)$, and modular multiplications occur once per non-space character. Computing the modular inverse costs $O(\log \texttt{mod})$, effectively constant relative to input size. Total expected time is $O(N)$.

The exact `s.split()` call materializes all word substrings and a list, using $O(N)$ space. A per-word counter contains at most 26 entries. Thus peak auxiliary space is $O(N)$, matching the manifest bound even though no factorial tables are allocated.

## Alternatives and edge cases

- **Factorial tables:** Precompute factorials and inverse factorials through $N$; it also gives $O(N)$ time and space but is not the exact implementation.
- **One-letter word:** It contributes exactly one permutation.
- **All identical letters:** Numerator and denominator factorial cancel, producing one.
- **All distinct letters:** The word contributes its full length factorial.
- **Repeated letters across different words:** Their frequencies must remain separate because words are permuted independently.
- **Word order:** It never changes.
- **Single-space input:** `split` produces no empty tokens.
- **Modular inverse:** It exists because all factors are smaller than the prime modulus.
- **Large answer:** Reducing after each multiplication keeps values controlled.
- **Manifest mismatch:** The source accumulates factorial products incrementally instead of building shared tables.
