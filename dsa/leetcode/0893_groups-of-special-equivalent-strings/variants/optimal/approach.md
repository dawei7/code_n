## General

Allowed swaps never move a character from an even index to an odd index or from an odd index to an even index. Within the even positions, however, any two characters may be swapped, and repeated swaps can create any permutation of those characters. The same is independently true for odd positions.

Therefore a string's special-equivalence class is completely determined by two multisets:

- the characters at indices $0,2,4,\ldots$;
- the characters at indices $1,3,5,\ldots$.

Two strings are special-equivalent exactly when both corresponding multisets match.

**Build a canonical signature.** For each word:

- `word[::2]` extracts even-indexed characters.
- `word[1::2]` extracts odd-indexed characters.
- Each extracted sequence is sorted independently.
- The two sorted lists are concatenated and joined into one string.

Sorting removes the irrelevant order within a parity class while preserving character multiplicities. For example, even characters `['z','x']` and `['x','z']` both normalize to `['x','z']`.

Although the two pieces are concatenated without an explicit separator, all input words have the same length. The even part therefore always occupies exactly $\lceil L/2\rceil$ positions in every signature, and the odd part occupies exactly $\lfloor L/2\rfloor$. The boundary is implicit and cannot shift between words.

**Why equal signatures imply equivalence.** If signatures match, the even-index multisets match and the odd-index multisets match. Any permutation of a finite set of positions can be produced by swaps within those positions. Rearrange the first word's even characters to match the second word's even positions, and independently rearrange its odd characters to match the second's odd positions. Both operations are allowed, so the first word can become the second.

**Why equivalence implies equal signatures.** Every allowed move swaps two positions of the same parity. It therefore preserves the multiset of even characters and the multiset of odd characters. Any number of moves preserves both. If one word can become another, their two parity multisets must have been identical, and sorting them produces identical signatures.

These two directions prove that signature equality is exactly special equivalence, not merely a necessary approximation.

The set comprehension builds one signature per input word and inserts it into `s`. Equal signatures collapse to one set entry, while different equivalence classes remain distinct. Since equivalence is transitive, each unique signature corresponds to one maximal group. Returning `len(s)` therefore gives the group count without explicitly storing lists of group members.

For `zzxy`, even indices contain `z` and `x`, while odd indices contain `z` and `y`. The signature normalizes those to even `xz` followed by odd `yz`. Word `xyzz` has even `x,z` and odd `y,z`, giving the same signature. Word `zzyx` has different parity multisets and therefore a different signature.

The approach focuses on what moves preserve—parity-specific character counts—rather than simulating swap sequences. That turns a potentially large reachability search into direct classification.

## Complexity detail

Let $N$ be the number of words and $L$ their common length. The exact code sorts about $L/2$ characters twice per word.

- **Time complexity of the exact comparison-sort implementation:** $O(NL\log L)$ in a general comparison model.
- **Manifest time interpretation:** Because $L\le20$ and the alphabet is fixed, sorting cost is bounded by a small constant factor and is summarized as $O(NL)$ for this constrained problem.
- **Space complexity:** $O(NL)$ for all distinct signature strings in the worst case, plus $O(L)$ temporary sliced and sorted character data per word. With bounded $L$, the manifest abbreviates this as $O(N)$.

A 26-count signature for each parity would achieve literal $O(NL)$ time without sorting.

## Alternatives and edge cases

- **Two frequency arrays:** Count 26 letters separately at even and odd indices. This gives an $O(L)$ signature and avoids sorting.
- **Simulate allowed swaps:** Exploring permutations is factorial and unnecessary because parity multisets fully characterize reachability.
- **Sort the whole word:** This loses the distinction between even and odd positions and can merge strings that are not special-equivalent.
- **Compare only even positions:** Odd-position character counts are independently invariant and must also match.
- **One-character words:** The odd multiset is empty. Groups are determined solely by the one even character.
- **Two-character words:** Each parity contains one fixed position, so no nontrivial swap is possible; only identical words group together.
- **Odd word length:** The even side has one more position than the odd side. The fixed signature boundary preserves that fact.
- **Repeated characters:** Sorting or counting retains multiplicity, which is necessary for equivalence.
- **Duplicate words:** They generate the same signature and belong to the same group.
- **All words equivalent:** The set has one entry and the result is one.
- **Every signature distinct:** Each word forms its own maximal group.
- **Same-length guarantee:** It makes delimiter-free signature concatenation unambiguous. Mixed lengths would need the length or a separator in the key.
- **Maximal group wording:** Equivalence classes are automatically maximal sets under an equivalence relation; counting unique signatures counts those classes.
