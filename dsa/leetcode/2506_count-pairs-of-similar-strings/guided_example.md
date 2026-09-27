# Guided Example: Count Pairs Of Similar Strings

Two words are similar when they consist of the same characters. Nothing is said
about how often each character occurs or in what order, so the relation only
looks at the **set** of characters a word uses. This lesson derives the whole
solution from that observation: similarity is an equivalence relation, the
equivalence classes are exactly the distinct character sets, and the answer is a
sum of counts of pairs inside each class. The representative instance below is
small enough to enumerate every pair by hand and confirm the count.

## 1. Similarity is an equivalence relation

Write $S(w)$ for the set of characters occurring in a word $w$. The definition
says

$$
w \sim w' \quad \Longleftrightarrow \quad S(w) = S(w').
$$

Equality of sets is reflexive, symmetric and transitive, so $\sim$ is an
equivalence relation on the array of words. Every equivalence relation partitions
its domain into disjoint classes, which gives the structural plan:

1. compute the class of each word, i.e. its character set;
2. group the words by class;
3. count how many index pairs each class contains;
4. add those counts, because a pair can belong to exactly one class.

The final step is where disjointness is used: since no word lies in two classes,
no pair is counted twice, and no pair inside a class is missed.

| Property of a word | Does it affect similarity? | Reason |
|:---|:---:|:---|
| the set of characters used | yes | this is the definition of the class |
| how many times a character repeats | no | only membership in the set matters |
| the order of the characters | no | a set has no order |
| the length of the word | no, except that it bounds the set size | a longer word can repeat characters without changing its set |
| the position of the word in the array | no | it identifies the element of the pair, not the class |

## 2. A signature for a character set

Because the alphabet is exactly the 26 lowercase English letters, a character
set can be encoded as a 26-bit integer. Number the letters from 0 for `a` to 25
for `z`, and define the signature of a word as

$$
m(w) = \sum_{c \in S(w)} 2^{\,p(c)},
$$

where $p(c)$ is the letter's position. The sum runs over the *set* $S(w)$, so a
repeated letter is added only once. Two words are similar exactly when their
signatures are equal, because two subsets of a 26-element universe with the same
indicator vector are the same subset. The signature is therefore a faithful
representative of the class, and it is a machine word rather than a data
structure, which makes class lookup a constant-time operation.

| Word | Character set $S(w)$ | Positions of the letters | Signature $m(w)$ |
|:---|:---|:---|:---:|
| `aba` | a, b | 0, 1 | 3 |
| `aabb` | a, b | 0, 1 | 3 |
| `abcd` | a, b, c, d | 0, 1, 2, 3 | 15 |
| `bac` | a, b, c | 0, 1, 2 | 7 |
| `aabc` | a, b, c | 0, 1, 2 | 7 |

## 3. The representative instance and its classes

Take the first official example,
`words = ["aba", "aabb", "abcd", "bac", "aabc"]`, and group the five words by the
signature computed above.

| Signature | Character set | Member indices | Words | Class size $k$ |
|:---:|:---|:---|:---|:---:|
| 3 | a, b | 0, 1 | `aba`, `aabb` | 2 |
| 7 | a, b, c | 3, 4 | `bac`, `aabc` | 2 |
| 15 | a, b, c, d | 2 | `abcd` | 1 |

Three classes appear, two of them with two members each. The signature-15 class
is a singleton and can never produce a pair, which is worth noticing: a class of
size one contributes nothing and must not be counted.

## 4. Counting pairs inside one class

Inside a class of size $k$, every unordered pair of distinct indices is a valid
pair, so the class contributes the binomial coefficient

$$
\binom{k}{2} = \frac{k (k-1)}{2}.
$$

The formula counts unordered pairs because a pair $(i,j)$ is required to satisfy
$i < j$; ordering the two indices by position is a convention, not a choice.
Applying the formula class by class and summing gives the answer.

| Class (character set) | Size $k$ | $\binom{k}{2}$ | Pairs it contributes |
|:---|:---:|:---:|:---|
| a, b | 2 | 1 | (0, 1) |
| a, b, c | 2 | 1 | (3, 4) |
| a, b, c, d | 1 | 0 | none |

Concretely, the only two qualifying pairs are indices 0 with 1, whose words use
a and b, and indices 3 with 4, whose words use a, b and c. Every other pair
differs in its character set, so the total is $1 + 1 = 2$, which is the required
output.

## 5. Incremental counting and its invariant

The same total can be accumulated while the words are read one at a time, without
ever storing the classes' member lists. Keep a count of how many words of each
signature have been seen so far. When a new word arrives with signature $m$:

- the pairs it forms with the words already counted are exactly the pairs
  $(j, i)$ with $j < i$, and there are as many of them as the current count for
  $m$;
- add that count to the answer, then increment the count for $m$.

The invariant is that after processing the first $t$ words, the answer equals the
number of similar pairs whose larger index is at most $t - 1$, and the counter
for each signature equals the number of processed words with that signature.
Each pair is charged exactly once, at the moment its second index is processed,
which is why no pair is double-counted and none is lost. Processing a word of a
brand-new signature adds nothing, since its counter was zero.

| Step $t$ | Word | Signature $m$ | Counter for $m$ before | Pairs added | Answer after | Counter for $m$ after |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | `aba` | 3 | 0 | 0 | 0 | 1 |
| 2 | `aabb` | 3 | 1 | 1 | 1 | 2 |
| 3 | `abcd` | 15 | 0 | 0 | 1 | 1 |
| 4 | `bac` | 7 | 0 | 0 | 1 | 1 |
| 5 | `aabc` | 7 | 1 | 1 | 2 | 2 |

The final answer is $2$, matching the class-by-class computation. The two
methods cannot disagree: the incremental sum over the array equals
$\sum_m \binom{\text{count}(m)}{2}$, because each class contributes its own
triangular number one step at a time.

## 6. Correctness of the signature and the count

**The signature is lossless for similarity.** Two words are similar if and only
if their character sets are equal, and a character set over a fixed 26-letter
alphabet is uniquely determined by which of the 26 bits are set. Hence
$m(w) = m(w')$ exactly when $w \sim w'$. No information needed for the decision
is discarded: multiplicity is irrelevant by the definition, and order is
irrelevant because a set has no order. When a repeated letter is encountered the
corresponding bit is already set, so the signature is unchanged, which is the
formal reason `a` and `aaaa` share a class.

**The total counts each pair exactly once.** The classes partition the array, so
the pairs partition into per-class pairs. Within a class of size $k$ there are
exactly $k(k-1)/2$ pairs with distinct indices and $i < j$; summing over classes
therefore counts every similar pair once and no dissimilar pair at all. The
incremental form reaches the same number by a telescoping argument, charging each
pair at the later of its two indices, so the two computations are equal rather
than merely similar.

**The pair count is a function of class sizes only.** The identity of the words
inside a class never enters the arithmetic; only how many there are. That is why
the answer for the instance with three words all using a and b is
$\binom{3}{2} = 3$, regardless of the fact that the three words have different
lengths.

## 7. Traps the instance exposes

| Situation | Naive expectation | What actually happens |
|:---|:---|:---|
| `a`, `aa`, `aaaa`, `b` | the different lengths make the first three dissimilar | all three use only the letter a, so they form $\binom{3}{2} = 3$ pairs, and the single b adds none |
| `abc`, `cba`, `bac`, `abd` | order matters, so only anagram-adjacent pairs count | the three permutations are one class giving 3 pairs; `abd` is its own class |
| Two identical words in the array | they are the same element and cannot form a pair | array positions are distinct, so a pair $(i,j)$ is well defined even when the words are equal |
| A class of size one | it contributes one pair with itself | $k(k-1)/2$ with $k = 1$ is 0; never add $k$ pairs instead of $\binom{k}{2}$ |
| Two different classes | a word might match across classes | classes are disjoint by construction, so cross-class pairs can never be similar |
| A word of length 100 | its signature needs more bits or a bigger counter | length does not increase the signature; at most 26 bits are ever set, and repeats are absorbed |
| The whole alphabet | a 26-letter mask might overflow | a 26-bit value is bounded by $2^{26} - 1$, comfortably inside a machine word |
| Counting unordered pairs | the ordered count might be wanted | the contract asks for $i < j$, so each unordered pair is counted once, not twice |

Two authored checks confirm these points. For
`words = ["ab", "ba", "aab", "xy", "yx", "z"]` the classes are a-b with three
members, x-y with two, and z alone, giving $3 + 1 + 0 = 4$. And for three words
that each use all 26 letters — in forward order, in reverse order, and doubled —
the class has three members and the answer is $\binom{3}{2} = 3$, since order and
multiplicity are both ignored.

## 8. Complexity: time and auxiliary space

Let $n$ be the number of words and let

$$
L = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

be the total number of characters in the input.

**Time.** Building a signature inspects every character of a word once and sets
one bit per character, so the cost is linear in the word's length; over the whole
array this is $O(L)$. Each pair-count step performs one lookup and one increment
in the signature table, costing $O(1)$ expected time under hashing, or $O(1)$
worst case if the table is indexed directly by the 26-bit signature. The total is
$O(L + n)$, which is linear in the input and optimal, since every character must
be read at least once to know the character set.

**Auxiliary space.** The only storage beyond the answer is the table of counts.
It holds at most one entry per distinct signature, so its size is bounded by the
number of distinct character sets, which is at most $2^{26}$ but in practice at
most $n$; the bound needed here is $O(n)$, and each entry is a single integer.
The signature itself is one machine word, and no word's characters are ever
stored. Total auxiliary space is therefore $O(n)$ with a very small constant, or
$O(1)$ if the counts are kept in a fixed array indexed by the 26-bit signature.

| Strategy | Time | Auxiliary space | Trade-off |
|:---|:---:|:---:|:---|
| Signature table with incremental pair counting | $O(L + n)$ | $O(n)$ | intended method; one pass, and every pair is charged exactly once |
| Group the words by sorted distinct characters, then sum binomials | $O(L \log \sigma + n)$ | $O(L)$ | equivalent grouping with an extra factor from sorting each word's distinct letters, where $\sigma \le 26$ |
| Compare every pair of words directly | $O(n^{2} \cdot \sigma)$ | $O(1)$ | trivially correct and fine for $n \le 100$, but quadratic and slow to scale |
| Compare sorted words for equality | $O(L \log \sigma + n \log n)$ | $O(L)$ | sorting destroys the distinction the problem ignores, so it must sort the deduplicated letters, not the word |
| Union-find over words sharing characters | $O(L + n \alpha(n))$ | $O(n)$ | overkill here and easy to get wrong: transitivity of the character sets must not be confused with connectivity between words |
