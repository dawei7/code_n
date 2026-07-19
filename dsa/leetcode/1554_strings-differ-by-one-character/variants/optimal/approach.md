## General
**Represent a word with one position removed**

Two words differ only at index `i` exactly when removing the character at `i` leaves identical strings and the removed characters differ. Encode every word with two polynomial rolling hashes. Precompute the power belonging to each position, so subtracting that character's weighted contribution produces a masked signature in constant time.

Using two fixed-width moduli makes accidental signature matches extremely rare. On a matching pair of hash signatures, compare the actual prefixes and suffixes before accepting, so a hash collision can never produce a false positive.

**Process one character column at a time**

For a fixed index, map each masked signature to the word indices already seen in that column. If a prior word has the same verified remaining characters but a different removed character, return `true`.

Discard the map before moving to the next column. Retaining signatures for every word-position pair would require $O(q\ell)$ stored entries and can exceed the platform memory limit; column-wise processing holds only $O(q)$ signatures at once.

**Why every valid pair is found**

Suppose two words differ exactly at index `i`. Their masked representations for that column are identical, their removed characters differ, and exact verification succeeds when the later word is processed. Conversely, any accepted pair matches before and after `i` and differs at `i`, so its Hamming distance is exactly one.

## Complexity detail
Encoding all words and scanning all $q\ell$ word-position pairs takes expected $O(q\ell)$ time. Exact verification occurs only for matching double-hash signatures; under normal hashing assumptions it adds negligible work, while preserving deterministic correctness. The Accepted column-wise implementation uses only $O(q+\ell)$ space, which is within the required $O(q\ell)$ bound; the independent prefix/suffix-ID formulation stores $O(q\ell)$ state.

## Alternatives and edge cases
- **Prefix/suffix trie-state identifiers:** assign canonical IDs to every prefix and reversed suffix, then use the pair of IDs as a collision-free masked signature in $O(q\ell)$ time, at the cost of $O(q\ell)$ storage.
- **Wildcard strings:** replace each position with a marker and hash the resulting string; materializing every pattern takes $O(q\ell^2)$ character work.
- **Compare every pair:** directly count differing positions for all pairs in $O(q^2\ell)$ time.
- Width-one strings qualify whenever the dictionary contains two distinct strings.
- A difference at the first or final character is handled like any interior index.
- Strings differing at two positions must not be accepted.
- The input strings are distinct, so an equal duplicate pair is outside the source contract.
- Column identity matters: removing different positions cannot form a valid comparison.
- A single dictionary word cannot form a pair.
