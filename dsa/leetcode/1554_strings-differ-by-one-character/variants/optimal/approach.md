## General

**Remove one position to create a comparison signature**

Two equal-length strings differ in exactly one position `i` if all characters except position `i` are equal and their characters at `i` are different.

The source replaces one character at a time with the marker `*`. For word `word` and index `i`, it builds:

`word[:i] + "*" + word[i + 1:]`.

This wildcard signature preserves the position of the removed character and every other character.

If two words produce the same signature, they agree at every non-wildcard position. Because the marker occurs at the same location in the identical signatures, the only position where they can differ is that wildcard position.

**Why distinct input strings make the collision exact**

Matching signatures prove the two words differ in at most one character. They might have differed in zero characters if duplicate words were allowed.

The contract says all input strings are unique. Therefore, two different words cannot have the same removed character as well as the same remaining characters. A signature collision between processed words consequently proves their wildcard characters differ, giving Hamming distance exactly one.

This distinctness guarantee is an essential part of the proof, not merely a data-cleanliness detail.

**Store signatures from earlier words**

Set `s` contains every wildcard signature generated for words already processed, plus earlier positions of the current word.

For each new signature `t`, the source first tests membership. If it already exists, a qualifying pair has been found and the method returns true immediately.

Otherwise, it adds `t` and continues. If all word-position combinations finish without a collision, no two strings differ by exactly one character.

**Why different wildcard positions do not cause false matches**

The `*` remains inside the signature. A signature made by replacing index zero has its marker at index zero, while one made by replacing index one has it at index one.

Because original words contain only lowercase English letters and never `*`, signatures with markers at different positions cannot be equal. Every collision therefore compares removal at the same index.

**Tracing the first example**

For `"abcd"`, replacing index one creates `"a*cd"`, which is stored.

When `"aacd"` is processed, replacing index one creates the same `"a*cd"`. The original words agree at indices zero, two, and three, while their index-one characters are `b` and `a`. The method returns true.

By contrast, `"abcd"` and `"acbd"` differ at positions one and two. Replacing only one position leaves the other mismatch visible, so none of their corresponding signatures collide.

**Why generating every position is complete**

Suppose two strings differ exactly at index `i`. When each word's loop reaches `i`, both replace that sole differing character with the same marker. Every other position was already equal, so their signatures are identical.

The later-processed word finds the earlier signature in the set and returns true.

Conversely, as shown above, a collision implies agreement everywhere except the wildcard and distinctness implies disagreement there. The method therefore has neither false negatives nor false positives.

**The exact cost of Python slicing**

Conceptually, there are $Q\ell$ signatures for $Q$ words of length $\ell$. An ideal rolling-hash or mutable-signature implementation could process each in constant additional work after preprocessing.

The exact stored Python source is different: `word[:i]` and `word[i+1:]` copy substrings, concatenation creates another string, and hashing a newly created signature examines its characters. Building one signature costs $O(\ell)$ time.

This implementation remains practical because $\ell \le 20$ and the total number of source characters is bounded, but its exact complexity should not be confused with the idealized manifest bound.

**Early termination**

As soon as one collision appears, the existential question is answered. The method avoids generating signatures for remaining positions or words.

Worst-case analysis still considers inputs with no qualifying pair, where every signature is created and stored.

## Complexity detail

Let $Q$ be word count and $\ell$ their common length. There are $Q\ell$ loop iterations.

With literal Python slicing, concatenation, and hashing of each fresh length-$\ell$ string, one iteration costs $O(\ell)$. Exact worst-case time is therefore $O(Q\ell^2)$, rather than the manifest's idealized $O(Q\ell)$.

The set can hold $O(Q\ell)$ signature strings, each of length $\ell$. Counting stored characters gives $O(Q\ell^2)$ memory in the exact implementation. If fixed-length signatures are treated as atomic or rolling hashes are used, the manifest's $O(Q\ell)$ storage description applies.

The small upper bound $\ell \le 20$ makes the extra factor a limited constant in this dataset, but it remains real in an asymptotic explanation.

## Alternatives and edge cases

- **Rolling hash per omitted position:** It can build signatures in $O(1)$ per position after preprocessing, realizing expected $O(Q\ell)$ time with collision safeguards.
- **Compare every pair of words:** Direct Hamming comparisons cost $O(Q^2\ell)$.
- **Sort wildcard signatures:** It can detect equal neighbors but requires materializing and sorting all signatures.
- **Duplicate words:** They would create collisions despite Hamming distance zero, but uniqueness excludes them.
- **One-character words:** Every word produces `"*"`; any two distinct one-letter words correctly differ by one.
- **One word only:** No signature can match one from another word, so the result is false.
- **Difference at first position:** Replacing index zero makes matching suffixes collide.
- **Difference at last position:** Replacing the final index makes matching prefixes collide.
- **Two differences:** Replacing one leaves the other mismatch, preventing collision.
- **Wildcard safety:** `*` is outside the lowercase input alphabet and cannot be confused with source data.
- **Equal lengths:** They ensure signatures align position by position and retain the same length.
- **Early return:** The first proven pair is sufficient; no pair identities need to be returned.
- **Hash-set behavior:** Membership is expected constant time after the signature is built, subject to normal hash-table assumptions.
