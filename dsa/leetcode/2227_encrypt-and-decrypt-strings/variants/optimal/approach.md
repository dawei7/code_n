## General

**Reverse the direction of the repeated question**

A literal decryption branches whenever several keys share the same two-character value. Exploring those branches can create exponentially many candidate plaintexts, even though only dictionary words may contribute to the answer. Instead, process the finite dictionary once in the forward direction.

Build the direct character-to-value map, encrypt every dictionary word, and count how many words produce each nonempty ciphertext. Distinct dictionary words may deliberately increment the same counter entry. Words containing an unmapped character cannot encrypt successfully and therefore cannot match any valid nonempty decryption query.

**Answer operations from the prepared index**

Encryption maps each character and concatenates the resulting two-character strings. A missing key makes the whole operation return `""`.

Decryption now asks exactly for the stored frequency of `word2`. Every counted dictionary word is a valid decryption because its forward encryption equals `word2`; conversely, every permitted plaintext that can produce `word2` was processed during construction and incremented that same entry. The lookup therefore returns precisely the required number without enumerating ambiguous reverse mappings.

## Complexity detail

Let $D$ be the total number of dictionary characters and $Q$ the total number of characters passed to later method calls. Constructing the encrypted-frequency index takes $O(D)$ time. Across the operation sequence, encryption and hashing queried ciphertexts take expected $O(Q)$ time, for $O(D+Q)$ total expected time.

The direct map has at most 26 entries. Stored ciphertext keys contain at most twice the dictionary's total character count, so auxiliary space is $O(D)$.

## Alternatives and edge cases

- **Backtrack through reverse mappings:** This can enumerate exponentially many plaintext combinations before discovering that most are absent from the dictionary.
- **Scan the dictionary on every decryption:** Forward-encrypting every dictionary word per query is correct but repeats $O(D)$ work.
- **Trie-guided reverse search:** A dictionary trie can prune impossible plaintext prefixes, but preprocessing exact encrypted frequencies is simpler and gives direct lookups.
- **Colliding values:** Different keys may map to the same two-character value, and all matching dictionary words must be counted.
- **Unmapped dictionary character:** Such a word encrypts to `""` and cannot match a valid nonempty `word2`.
- **Unknown ciphertext block:** No dictionary encryption has that ciphertext, so decryption returns zero.
- **Repeated queries:** Lookup operations do not mutate the prepared frequency table.
