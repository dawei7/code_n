## General

**Reverse the counting perspective**

Enumerating every substring and counting its vowels repeats the same work. Instead, the source asks how many substrings contain each individual vowel occurrence.

Every time a substring contains the vowel at index `i`, that occurrence contributes exactly one to the requested total. Summing this contribution over all vowel indices is equivalent to summing vowel counts over all substrings.

This is a standard double-counting transformation.

**Choose the substring's starting position**

For a substring to contain index `i`, its start may be any index from zero through `i` inclusive.

There are `i+1` choices. Starting later than `i` would exclude the occurrence.

**Choose the substring's ending position**

The end may be any index from `i` through `n-1` inclusive.

There are `n-i` choices. Ending earlier than `i` would exclude the occurrence.

Start and end choices are independent once both are constrained around `i`, so the number of substrings containing that position is

$$
(i+1)(n-i).
$$

**Add contributions only for vowels**

The generator scans `enumerate(word)` and includes the product only when `c in 'aeiou'`.

A consonant occurrence contributes zero to vowel counts and is omitted. A vowel contributes once for every substring containing its position.

The five-character membership string is a fixed constant, so the test takes constant time.

**Trace `"aba"`**

The vowel at index zero has one possible start and three possible ends, contributing three substrings.

The vowel at index two has three possible starts and one possible end, also contributing three.

The middle consonant contributes nothing. Total contribution is six, matching explicit substring enumeration.

**Why multiple vowels in one substring are handled correctly**

Suppose a substring contains two vowel positions. It should contribute two to the requested sum.

The contribution method counts that substring once in the first vowel's product and once in the second vowel's product. This is intentional, not duplicate error: the output sums vowel occurrences, so the substring needs one contribution per vowel it contains.

**Why every contribution corresponds to a real substring**

Each pair of a start in `[0,i]` and an end in `[i,n-1]` defines one unique nonempty contiguous substring containing index `i`.

Different start-end pairs define different substrings. Thus the product neither misses nor invents any substring containing that vowel occurrence.

**Why multiplication, rather than addition, combines the choices**

For every one of the `i+1` possible starts, every one of the `n-i` possible ends remains available. A start choice does not restrict the end beyond the already satisfied condition that it be at least `i`.

The multiplication principle therefore gives `(i+1)(n-i)` pairs. Adding the two choice counts would describe choosing either a start or an end, but a substring requires both endpoints and would severely undercount.

**Why the total is correct**

Consider the set of pairs `(substring, vowel position inside it)`. Counting by substring gives exactly the problem's requested sum, because each substring appears once per vowel it contains.

Counting by vowel position gives `(i+1)(n-i)` pairs for each vowel at `i`. Both methods count the same set of pairs, proving the formula and the returned sum.

**No prefix sums are needed**

Prefix vowel counts could answer the vowel count of one substring quickly, but there are still quadratically many substrings. The contribution formula collapses all substrings containing one position into a single multiplication.

The source expresses the complete algorithm as one generator consumed by `sum`, without materializing contributions in a list.

**Why linear time is asymptotically optimal**

An arbitrary character can change the answer depending on whether it is a vowel. In the worst case, a correct algorithm must inspect every position to distinguish two words that differ only at the final unchecked character.

The source performs exactly one pass and constant work per character, so it matches this $\Omega(N)$ input-reading lower bound.

**Large results**

For a long all-vowel word, the answer grows cubically in scale because many substrings contain many vowels. The description warns that 32-bit integers may overflow.

Python integers expand automatically, so the exact implementation needs no special numeric type or modulus.

## Complexity detail

Let $N=len(word)$. `enumerate` visits each character once, and each iteration performs constant-time membership and arithmetic. Time is $O(N)$.

The generator is lazy, so contributions are not stored. Apart from scalar iteration and summation state, no input-dependent structure is allocated. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate all substrings:** Requires $\Theta(N^2)$ intervals and additional work to count their vowels.
- **Prefix sums:** Give $O(1)$ count per substring but still $O(N^2)$ total enumeration.
- **Running ending contribution:** Maintain how many vowel occurrences contribute to substrings ending at each index; also linear.
- **No vowels:** The generator contributes nothing and `sum` returns zero.
- **All vowels:** Every index contributes its full start-end product.
- **Vowel at index zero:** Appears in exactly $N$ substrings ending at every possible position.
- **Vowel at final index:** Appears in exactly $N$ substrings beginning at every possible position.
- **One-character vowel word:** Contribution is one.
- **One-character consonant word:** Contribution is zero.
- **Repeated vowels:** Each position is a separate occurrence and contributes independently.
- **Substring with several vowels:** Correctly receives one contribution from each included vowel position.
- **Input preservation:** The immutable word is scanned without slicing or modification.
