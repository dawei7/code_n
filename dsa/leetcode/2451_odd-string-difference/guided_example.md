# Guided Example: Odd String Difference

## 1. The Instance We Will Trace

We work through one input from beginning to end:

- **Input:** `words = ["adc", "wzy", "abc"]`
- **Required output:** `"abc"`

Every word has the same length, all words but one share a common *difference integer array*, and we must return the word whose array is the odd one out. This instance is worth tracing because the two majority words, `"adc"` and `"wzy"`, share no letter at all, yet they must be recognized as identical in the only sense the problem cares about. A method that compares letters, or that treats the alphabet position of a letter as meaningful, is refuted here even though it would survive simpler inputs.

## 2. Difference Arrays: What Actually Identifies a Word

Fix the alphabet positions $\pi(\texttt{'a'}) = 0$, $\pi(\texttt{'b'}) = 1$, $\dots$, $\pi(\texttt{'z'}) = 25$. For a word $w$ of length $m$, its **difference integer array** has length $m-1$ and is defined componentwise by

$$
D(w)[j] = \pi(w[j+1]) - \pi(w[j]), \qquad 0 \le j \le m-2 .
$$

The subtraction is directed, so a descending step contributes a negative component. Applying the definition to our three words:

| word $w$ | positions $\pi(w[0]), \pi(w[1]), \pi(w[2])$ | adjacent subtractions | difference array $D(w)$ |
|---|---|---|---|
| `"adc"` | $0,\; 3,\; 2$ | $3-0,\; 2-3$ | $(3,\; -1)$ |
| `"wzy"` | $22,\; 25,\; 24$ | $25-22,\; 24-25$ | $(3,\; -1)$ |
| `"abc"` | $0,\; 1,\; 2$ | $1-0,\; 2-1$ | $(1,\; 1)$ |

The table exposes the structural fact the whole exercise rests on: `"adc"` and `"wzy"` are **alphabet translations** of each other. Adding the constant $22$ to each position of `"adc"` produces `"wzy"`, and because a constant shifts both terms of every subtraction, it cancels:

$$
\bigl(\pi(w[j+1]) + \delta\bigr) - \bigl(\pi(w[j]) + \delta\bigr) = \pi(w[j+1]) - \pi(w[j]).
$$

Hence $D$ is invariant under uniform translation of a word, provided the translated letters remain inside the alphabet. The letters themselves are therefore *not* the identity of a word in this problem; the difference array is. Only the differences of the positions carry information, and the absolute position of the first letter carries none.

## 3. The State: A Partition of Words by Signature

The quantity we maintain is a partition of the words seen so far, keyed by the difference array used as a *signature*. Concretely, the state is a mapping from a signature to the list of words that produced it. A signature must be usable as a lookup key, so it is held as an immutable ordered sequence of integers whose equality is decided component by component; two signatures are the same key exactly when they agree in every one of their $m-1$ positions.

The processing rule is uniform and needs no case analysis: read a word, compute its difference array, and append the word to the list stored under that signature.

| step | word read | signature produced | state after the insertion |
|---|---|---|---|
| 1 | `"adc"` | $(3, -1)$ | $\{(3,-1) \mapsto [\texttt{"adc"}]\}$ |
| 2 | `"wzy"` | $(3, -1)$ | $\{(3,-1) \mapsto [\texttt{"adc"}, \texttt{"wzy"}]\}$ |
| 3 | `"abc"` | $(1, 1)$ | $\{(3,-1) \mapsto [\texttt{"adc"}, \texttt{"wzy"}],\ (1,1) \mapsto [\texttt{"abc"}]\}$ |

Reading off the finished partition:

| signature | member words | class size | role in this instance |
|---|---|---|---|
| $(3, -1)$ | `"adc"`, `"wzy"` | $2$ | the shared (majority) array |
| $(1, 1)$ | `"abc"` | $1$ | the singleton class, and the answer |

The output step is now mechanical: among the classes, find the one holding exactly one word and return that word. Here the singleton holds `"abc"`, which agrees with the authored expected output for this input.

## 4. Why the Singleton Class Must Be the Odd Word

**Partition invariant.** After the first $t$ words have been read, the mapping's classes are exactly the equivalence classes of the first $t$ words under the relation "has the same difference array", and every one of those $t$ words occurs in exactly one list.

*Proof by induction on $t$.* For $t = 0$ the mapping is empty and the claim is vacuous. Assume it holds after $t-1$ words. When the $t$-th word arrives, its stored signature is computed by the same subtraction rule that defines $D$, so it is a key that genuinely represents $D(w_t)$, not an approximation. Appending $w_t$ to that key's list puts it in the class of words with signature $D(w_t)$ and in no other class, and touching no other list leaves every earlier word's membership unchanged. The classes are therefore still disjoint and still cover all $t$ words.

Because equal signatures mean equal difference arrays and distinct keys mean a disagreement in at least one component, no two different arrays are ever merged. A hash collision cannot corrupt the answer: a collision only forces a full component comparison, which distinguishes two different arrays.

**Existence and uniqueness.** The statement guarantees that all words share one difference array except one. So among $p$ words there are exactly two distinct signatures: one carried by a single word, and one carried by the remaining $p-1$ words. Since $p \ge 3$, the majority class has at least two members and is never confused with the singleton. The scanning rule therefore finds exactly one candidate — it cannot find none, and it cannot find two — so the word it returns is precisely the unique word whose difference array differs from all the others. This gives both soundness (the returned word really is odd) and completeness (no other word can be odd).

## 5. Boundaries and Traps This Problem Sets

| situation | concrete instance | outcome and the trap it exposes |
|---|---|---|
| Shortest words, $m = 2$ | `["ab", "bc", "ac"]` | Signatures are $(1), (1), (2)$; the singleton is `"ac"`. A one-component signature still partitions correctly, so no special case for $m = 2$ is needed. |
| Negative differences | `["cba", "abc", "dcb", "edc"]` | `"cba"`, `"dcb"`, `"edc"` all give $(-1,-1)$; `"abc"` gives $(1,1)$. Replacing differences by absolute values would fuse descending and ascending patterns and destroy the answer. |
| Translation invariance | `"adc"` versus `"wzy"` | Different letters, identical difference array. Comparing letter values instead of differences rejects a valid majority word. |
| Outlier in the first position | `["ace", "abc", "bcd"]` | `"ace"` gives $(2,2)$ while `"abc"` and `"bcd"` both give $(1,1)$, so the majority signature is not known until the second word is read. Any shortcut that assumes the first word is the majority is wrong here. |
| Repeated majority word | `["aaa", "bob", "ccc", "ddd"]` | $(0,0)$ has three members and `"bob"` alone gives $(13,-13)$. Duplicate *text* is irrelevant; membership is decided by signature. |
| Reference example `"acb"` | `"acb"` | Differences $(2, -1)$ demonstrate that a signature is not necessarily sorted or non-negative. |
| Several odd words | not permitted by the statement | The selection rule must rely on the guarantee. If two singleton classes existed the answer would be ambiguous, and the guarantee is what makes "the class of size one" well defined. |
| Equal-length guarantee | any input | Every signature has arity $m-1$, so component-by-component comparison always aligns like with like. Unequal lengths would need padding or a different relation. |
| Longest words, $m = 20$ | 20-letter words | Signatures have $19$ components; only the constant factor changes, not the method. |

## 6. Alternative Methods and Their Trade-offs

| method | time | auxiliary space | trade-off |
|---|---|---|---|
| Signature mapping (the approach derived above) | $O(pm)$ | $O(p + m)$ here | One uniform pass, no case analysis; needs an immutable multi-component key. |
| Infer the shared signature from the first three words, then find the word that disagrees | $O(pm)$ | $O(m)$ | Uses the pigeonhole fact that two of three words share the majority signature, so storage for the shared key is small; but it must handle the case where one of the first three *is* the outlier, which adds branching. |
| Translate every word to its first letter (store $\pi(w[j]) - \pi(w[0])$) | $O(pm)$ | $O(p + m)$ | This is the prefix sum of the difference array, so it induces the same partition; it is a re-encoding, not a different algorithm, and it makes the translation invariance explicit. |
| Normalize each word modulo the alphabet size | $O(pm)$ | $O(p + m)$ | Modular normalization survives wrapping letters, but the problem's differences are ordinary integers, so wrapping would merge patterns the statement keeps distinct. |
| Compare every pair of words componentwise | $O(p^2 m)$ | $O(m)$ | Correct but quadratic; it also has to decide which word of a disagreeing pair is the odd one, using a third word as a reference. |
| Sort the words by signature and group equal neighbours | $O(pm \log p)$ | $O(p)$ | Sorting costs more than needed; the guarantee bounds the number of classes at two, so no ordering information is required. |

## 7. Complexity Derivation

Let $p$ be the number of words and $m$ their common length, so each difference array has $m-1$ components.

- **Signature construction.** Reading one word touches its $m$ letters and performs $m-1$ subtractions, so one signature costs $O(m)$. Over all words this is $O(pm)$.
- **Key hashing and insertion.** Building the hash of an $(m-1)$-component signature reads all components, which is again $O(m)$ per word, hence $O(pm)$ in total. Expected constant-time lookup follows from the hashing, with a full component comparison only on a collision.
- **Selecting the answer.** The statement permits at most two distinct signatures, so the final scan inspects at most two classes and returns a single stored word: $O(1)$.

Combining, the expected running time is $\Theta(pm)$.

For space, the mapping is the only state that grows. Its key set contains at most two signatures under the guarantee, each of length $m-1$, which is $O(m)$; the word lists across all classes together hold exactly $p$ references to words already present in the input, which is $O(p)$. Signature construction itself needs only $O(m)$ transient storage for the signature currently being built. Auxiliary space is therefore $O(p + m)$ — not $O(pm)$ as it would be if every signature were distinct. With $p \le 100$ and $m \le 20$ the whole computation is far below any practical limit, but the derivation shows exactly which quantity dominates each term.
