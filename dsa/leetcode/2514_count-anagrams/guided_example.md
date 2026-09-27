# Guided Example: Count Anagrams

## 1. Anagrams here are word-wise permutations

The input is a sentence: one or more words with a single space between
consecutive words. A string $t$ is an anagram of $s$ when **the $i$-th word of
$t$ is a permutation of the $i$-th word of $s$** — for every position $i$,
independently.

That definition forbids two things that a looser reading would allow. Letters may
not cross a word boundary, so `ab ba` is *not* an anagram of `abba`: the space
positions are fixed and the word lengths are fixed. And words may not be
reordered, so `ba ab` is not an anagram of `ab ba`, even though each word is a
permutation of the corresponding one. The only freedom is *within* each word.

Because the constraint is imposed position by position and nothing is shared
between different word positions, the choices multiply. If word $i$ has $A_i$
distinct arrangements, the total number of distinct anagrams is

$$
A_1 \cdot A_2 \cdots A_g = \prod_{i=1}^{g} A_i,
$$

where $g$ is the number of words. The whole problem therefore reduces to one
question: how many distinct arrangements does a single word have?

## 2. Counting the distinct arrangements of one word

A word of length $L$ has $L!$ orderings of its positions, but equal letters make
some of those orderings produce the same string. If the word uses $r$ distinct
letters with multiplicities $m_1, m_2, \dots, m_r$ (so $\sum_j m_j = L$), then
each distinct string is produced by exactly $m_1! \, m_2! \cdots m_r!$ position
orderings — the orderings that permute equal letters among themselves. Dividing
removes that over-count and gives the multinomial coefficient

$$
A = \frac{L!}{m_1! \, m_2! \cdots m_r!}.
$$

Two anchor cases check the formula. If all $L$ letters are distinct then every
$m_j = 1$, all the denominators are $1$, and $A = L!$. If all letters are the
same then $r = 1$, $m_1 = L$, and $A = L!/L! = 1$: a string of identical
characters has exactly one anagram, itself.

The counting target is **distinct strings**, not position permutations. The word
`too` has $3! = 6$ position orderings but only $6/2! = 3$ distinct strings —
`too`, `oto`, and `oot` — because the two `o` positions are interchangeable.

## 3. Worked trace of the official instance `s = "too hot"`

The statement's first example is the two-word sentence `too hot`, whose expected
answer is `18`. Applying the product rule word by word:

| Word | Length $L$ | Letter multiplicities | $L!$ | $\prod_j m_j!$ | Arrangements $A$ |
|:---|:---:|:---|:---:|:---:|:---:|
| `too` | 3 | `t`: 1, `o`: 2 | 6 | $1! \cdot 2! = 2$ | $6 / 2 = 3$ |
| `hot` | 3 | `h`: 1, `o`: 1, `t`: 1 | 6 | $1$ | $6$ |

The product is $3 \cdot 6 = 18$, matching the expected output. The three
arrangements of the first word are `too`, `oto`, `oot`, and the six arrangements
of the second are the permutations of three distinct letters: `hot`, `hto`,
`oht`, `oth`, `tho`, `toh`. Pairing them gives eighteen distinct sentences, which
is why the official explanation can list `too hot`, `oot hot`, `oto toh`, and
`too oht` as separate anagrams of the same input.

The second word is worth one extra glance: it contains the same letters `t` and
`o` as the first word, but with multiplicity one each, so its arrangement count
is 6 rather than 3. Multiplicities are a property of *each word separately*,
never of the whole sentence.

## 4. The incremental state that avoids factorials

Computing $L!$ and the denominator factorials directly is unnecessary and, under
a modulus, undesirable: the numerator and denominator can grow to astronomically
large integers before the division is applied. A single pass over each word keeps
both quantities as running products instead.

The trick is to accumulate two products while scanning the word left to right. At
position $i$ (starting from 1), multiply a numerator by $i$ — after $L$ steps this
is $L!$. Simultaneously increment the count of the current letter and multiply a
denominator by that *new* count. A letter occurring $m$ times therefore
contributes the factors $1, 2, \dots, m$ to the denominator product, whose
product is exactly $m!$. Here is the state for the whole official instance:

| Word | Position $i$ | Letter | Occurrences of that letter so far | Numerator $\times i$ | Denominator $\times$ count |
|:---|:---:|:---:|:---:|:---:|:---:|
| `too` | 1 | `t` | 1 | 1 | 1 |
| `too` | 2 | `o` | 1 | 2 | 1 |
| `too` | 3 | `o` | 2 | 6 | 2 |
| `hot` | 1 | `h` | 1 | 6 | 2 |
| `hot` | 2 | `o` | 1 | 12 | 2 |
| `hot` | 3 | `t` | 1 | 36 | 2 |

The scan ends with numerator $36 = 3! \cdot 3!$ and denominator $2 = 2!$ from the
two occurrences of `o` in the first word. Their ratio is $36/2 = 18$, the answer.
Notice how the letter counters reset at each new word: the `o` in `hot` starts
again at 1 and does not continue the count of the `o`s in `too`, because words are
counted independently.

## 5. Independence across words, and a second instance

Because the words never interact, the denominator of the whole sentence is simply
the product of the per-word denominators, and the numerator is the product of the
per-word factorials. The authored case `aab bbbc` exercises that structure with
different multiplicities in each word.

| Word | Length $L$ | Multiplicities | $L!$ | $\prod_j m_j!$ | Arrangements $A$ | Running product |
|:---|:---:|:---|:---:|:---:|:---:|:---:|
| `aab` | 3 | `a`: 2, `b`: 1 | 6 | $2! \cdot 1! = 2$ | $3$ | 3 |
| `bbbc` | 4 | `b`: 3, `c`: 1 | 24 | $3! \cdot 1! = 6$ | $4$ | $3 \cdot 4 = 12$ |

The final running product is `12`, the authored expectation. The second word
shows the reduction clearly: four positions would give 24 orderings, but the
three identical `b`s collapse them to 4 distinct strings — `bbbc`, `bbcb`,
`bcbb`, `cbbb`. Two more authored cases confirm the two extremes of the formula:

| Instance | Input | Per-word arrangements | Answer | Why |
|:---|:---|:---|:---:|:---|
| all distinct | `abc def` | $3! = 6$ and $3! = 6$ | 36 | every denominator is 1 |
| all identical | `zzzz yyyy x` | $1$, $1$, $1$ | 1 | each word has a single distinct string |
| single character | `z` | $1! = 1$ | 1 | the shortest possible sentence |
| repeated pair | `aa` | $2!/2! = 1$ | 1 | the two positions are interchangeable |

## 6. The modulus, and why the division becomes an inverse

The answer can be enormous — a sentence of $10^{5}$ distinct letters would produce
a factorial with more digits than atoms in any practical computation — so the
statement asks for the count modulo

$$
p = 10^{9} + 7.
$$

Modular division is not ordinary integer division: $36/2$ must be computed as
$36 \cdot 2^{-1} \bmod p$, where $2^{-1}$ is the multiplicative inverse of 2
modulo $p$, that is the value $x$ with $2x \equiv 1 \pmod p$. Because $p$ is
prime, every denominator factor is invertible (the factorials involve only
numbers below $p$, and $p$ is far larger than any multiplicity in a word of
length at most $10^{5}$), and the inverse of the whole accumulated denominator
can be taken once at the end:

$$
\text{answer} = \text{numerator} \cdot \left(\text{denominator}\right)^{-1} \bmod p .
$$

The failure mode this avoids is exact: dividing before reducing, or reducing the
numerator and denominator and *then* dividing, gives a wrong result whenever the
reduced denominator does not divide the reduced numerator. Reducing first and
multiplying by the inverse is always valid, because the numerator is divisible by
the denominator as an integer before reduction — the multinomial coefficient is a
whole number — and the inverse operation commutes with reduction.

The authored case `trial-modular-product` uses the sentence `abcdefghij
abcdefghij`, whose true count is $(10!)^2 = 13{,}168{,}189{,}440{,}000$. Reduced
modulo $p$ that value is `189347824`, exactly the authored expectation. A method
that computed the count naively and reduced at the end would match on this input
but still risk unbounded intermediate growth on longer inputs; a method that
divided integers before reducing would corrupt it.

## 7. Boundary and edge cases

| Instance | Input condition | Expected | Deciding reason |
|:---|:---|:---:|:---|
| word order fixed | `ab ba` | 4 | $2! \cdot 2! = 4$; swapping the words is not an anagram |
| repeated letters | `aa` | 1 | identical characters leave exactly one distinct string |
| distinct letters only | `abc def` | 36 | each word contributes its full factorial |
| multiple identical letters | `zzzz yyyy x` | 1 | each denominator cancels its word's factorial |
| mixed multiplicities | `aab bbbc` | 12 | $3 \cdot 4$, computed word by word |
| large modulo | `abcdefghij abcdefghij` | 189347824 | $(10!)^2 \bmod p$ |
| one letter | `z` | 1 | $L = 1$ with a single multiplicity |
| single space only | any two-word sentence | — | every space is a fixed separator, never a slot for a letter |

Three traps deserve explicit mention. First, treating the whole sentence as one
multiset of letters is wrong: for `ab ba` that reading yields $4!/(2! \cdot 2!) =
6$, but the fixed word boundaries give 4, since `baab` and `abab` — the strings
the other reading would permit — are not anagrams of the sentence at all. Second,
allowing words to change places is wrong for the same instance; the definition
ties word $i$ of the anagram to word $i$ of the input. Third, treating distinct
letters as the unit of counting rather than occurrences is wrong: `aa` has two
distinct *characters* in the sense of two positions, yet exactly one distinct
string.

## 8. Correctness: the counting invariant

Two invariants carry the argument, one per word and one across words.

> **Per-word invariant.** While scanning a word of length $L$ from left to right,
> after processing the first $i$ characters the numerator holds $i!$ and the
> denominator holds $\prod_j m_j(i)!$, where $m_j(i)$ is the number of occurrences
> of letter $j$ among those $i$ characters.

The numerator claim is immediate: each step multiplies by the current position
$i$, so the running product is $1 \cdot 2 \cdots i = i!$. For the denominator,
each step multiplies by the *updated* count of the current letter; a letter whose
final multiplicity is $m$ is multiplied by $1, 2, \dots, m$ in that order, so its
total contribution is $m!$, and letters never interact. At $i = L$ the ratio is
exactly the multinomial coefficient, hence the number of distinct arrangements of
that word.

> **Product invariant.** After processing $g$ words, the accumulated ratio equals
> $\prod_{i=1}^{g} A_i$, the number of anagrams of the corresponding prefix
> sentence.

Multiplication of the two running accumulators continues seamlessly across word
boundaries, and the counters must be *reset* at each new word — a step that the
invariant makes precise. Both facts follow from the definition: an anagram of the
whole sentence is a choice of one arrangement for each word position, and distinct
tuples of arrangements yield distinct sentences because the words occupy disjoint
positions. There is no collision to correct: two different tuples differ in some
word, and that word's two arrangements are different strings of the same length,
so the sentence containing them differs.

Soundness and completeness therefore hold together — every counted tuple
produces a distinct anagram, and every anagram is produced by exactly one tuple of
arrangements — so the product is exactly the number of distinct anagrams, and
reducing modulo $p$ with a modular inverse, as argued in the previous section,
returns that number modulo $p$.

## 9. Alternatives and their failure modes

| Approach | How it works | Time | Auxiliary space | Failure mode |
|:---|:---|:---|:---|:---|
| Incremental numerator and denominator products | one pass per word, multiply by the position and by the running letter count, invert once at the end | $O(\lvert s \rvert + \log p)$ | $O(\sigma)$ with $\sigma = 26$ | none; this is the method traced above |
| Factorials with a modular inverse table | precompute factorials up to $\lvert s \rvert$ and use inverse factorials | $O(\lvert s \rvert)$ preprocessing, $O(\lvert s \rvert)$ counting | $O(\lvert s \rvert)$ | correct but needs arrays proportional to the input that the incremental scan does not |
| Enumerate arrangements | generate every permutation of each word and count distinct strings | factorial in each word length | factorial | unusable: a ten-letter word already has over three million orderings, and $L$ can reach $10^{5}$ |
| Exact big-integer arithmetic, then reduce | compute the multinomial exactly with unbounded integers | super-linear in digit count | super-linear | correct in principle but spends enormous effort on digits that the modulus discards |
| Divide before reducing | compute the ratio in modular arithmetic by ordinary division | $O(\lvert s \rvert)$ | $O(\sigma)$ | wrong: modular division must be multiplication by the inverse, never integer division |
| Whole-sentence multiset | count letters over the entire sentence and form one multinomial | $O(\lvert s \rvert)$ | $O(\sigma)$ | wrong on any multi-word input, e.g. returns 6 instead of 4 for `ab ba` |

## 10. Complexity: time and auxiliary space

Let $L_{\text{tot}} = \lvert s \rvert$ be the number of characters, including the
spaces, and let $\sigma = 26$ be the alphabet size.

**Time.** Splitting the sentence into words costs $O(L_{\text{tot}})$. Each
character is then visited exactly once by the scan, and each visit performs one
counter increment, one multiplication by the position, one multiplication by the
counter, and two reductions modulo $p$ — all $O(1)$ on machine-word-sized values,
because every product is immediately reduced below $10^{9} + 7$. The modular
inverse at the end costs $O(\log p)$ by fast exponentiation. The total is

$$
O(\lvert s \rvert + \log p),
$$

which is linear in the input length.

**Auxiliary space.** The only per-word state is the letter counter, whose size is
bounded by the alphabet, so the scan needs $O(\sigma)$ space and never stores
factor tables, arrangement lists, or the words themselves beyond the current one.
The accumulators are two integers. The overall bound is $O(\sigma)$, independent
of how long the sentence is.
