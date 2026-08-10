## General

**Encryption is a direct character map**

The constructor receives parallel arrays `keys` and `values`. The statement `dict(zip(keys, values))` builds `self.mp` so each unique key character maps directly to its required two-character code.

The `encrypt` method scans `word1` from left to right. For every character `c`, it first checks membership in `self.mp`. If the character has no mapping, encryption is impossible and the method immediately returns the empty string. Otherwise, it appends `self.mp[c]` to a list. Joining once at the end produces the concatenated ciphertext efficiently.

Because each code has length two, a valid plaintext of length `t` produces ciphertext length `2t`. The order of codes matches the order of plaintext characters.

**Avoid enumerating ambiguous decryptions**

Several different keys may map to the same two-character value. Direct decryption could branch at every ciphertext pair. If many pairs are ambiguous, the number of possible plaintext strings grows exponentially.

The query does not ask to list every possible plaintext. It asks only how many possible plaintexts also occur in the fixed `dictionary`. That allows the work to be reversed: encrypt every dictionary word once during construction, then count equal ciphertexts.

The constructor executes

`self.cnt = Counter(self.encrypt(v) for v in dictionary)`.

For each permitted original word `v`, it calls the same exact encryption procedure used by public requests. `Counter` maps the resulting ciphertext to the number of dictionary words that produce it.

Different dictionary words may collide intentionally. In the example, both `"abcd"` and `"abad"` encrypt to `"eizfeiam"` because `a` and `c` share code `"ei"` in relevant positions. The counter stores frequency two for that ciphertext.

**Decryption becomes one frequency lookup**

The method `decrypt(word2)` returns `self.cnt[word2]`. If the ciphertext was produced by three dictionary words, the result is three. If no dictionary word produced it, `Counter` returns zero for the missing key.

This lookup answers exactly the required question without choosing a reverse mapping for each pair. A dictionary word is a valid decryption of `word2` precisely when encrypting that word produces `word2`:

- if the word decrypts from `word2`, each character's code matches the corresponding two-character block, so re-encryption recreates `word2`;
- if its encryption equals `word2`, each of its characters is one allowed reverse choice for the matching blocks, so it is a possible decryption.

Counting pre-encrypted dictionary words is therefore equivalent to enumerating all possible decryptions and filtering by dictionary membership, but avoids the exponential intermediate set.

**Why dictionary uniqueness and ciphertext collisions coexist**

The dictionary strings themselves are unique, so each permitted original contributes at most one to a frequency. Their encryptions need not be unique because `values` may repeat. The counter deliberately preserves multiplicity after encryption rather than using a set.

Using a set of encrypted dictionary words would be wrong: it could report only whether at least one original exists, losing the number of distinct dictionary strings represented by the same ciphertext.

**Handling an unmapped character**

The general encryption contract says an unmapped plaintext character makes encryption fail. The explicit check returns `''` before joining a partial result.

Public `word1` characters are guaranteed to occur in `keys`, but dictionary words are not separately guaranteed by the listed constraints to use only mapped characters. If a dictionary word is invalid, its generated key is the empty string. Such entries accumulate under `self.cnt['']`. A legal `word2` has even length of at least two, so a decrypt request can never equal `''`; invalid dictionary words therefore do not inflate any legal answer.

**Construction pays for future calls**

The object may receive up to two hundred encrypt and decrypt calls. Preprocessing is especially useful when there are many decrypt calls because it shifts dictionary work to the constructor. Each decryption then performs no branching and no dictionary scan.

The mapping is fixed after initialization, so every later encryption is consistent with the ciphertexts stored during preprocessing. Neither method mutates `self.mp` or `self.cnt`.

**Trace the example mapping**

With `a -> "ei"`, `b -> "zf"`, `c -> "ei"`, and `d -> "am"`, encrypting `"abcd"` appends `"ei"`, `"zf"`, `"ei"`, and `"am"`, producing `"eizfeiam"`.

The same ciphertext can correspond to multiple plaintext combinations because either `a` or `c` can explain an `"ei"` pair. Only two of those combinations occur in the dictionary. Pre-encryption records exactly those two, so lookup returns two without generating the non-dictionary combinations.

## Complexity detail

Let `K` be the number of key mappings, let `D` be the total number of characters across all dictionary words, and let `L` be the plaintext length supplied to one `encrypt` call. Building `self.mp` takes `O(K)` expected time. Encrypting the dictionary during construction processes `D` characters, so constructor time is `O(K + D)`.

One `encrypt` call takes `O(L)` expected time for mapping lookups and `O(L)` time to join the two-character pieces, giving `O(L)` overall.

One `decrypt` call is one counter lookup after hashing `word2`. Under a unit-cost map model it is expected `O(1)` lookup; accounting for string hashing, first-time processing is `O(E)` for ciphertext length `E`. It does not depend on the number of possible reverse plaintexts or dictionary entries.

The mapping uses `O(K)` entries. The counter stores distinct encrypted dictionary strings, whose character content is bounded by `O(D)` because encryption doubles lengths by a constant factor. Constructor temporaries and stored keys therefore use `O(K + D)` space. A single encryption uses `O(L)` output-building space. The manifest's `O(D)` storage treats the bounded alphabet mapping as constant.

## Alternatives and edge cases

- **Backtrack through reverse mappings:** Build code-to-possible-characters lists and enumerate all plaintext combinations for `word2`. This can grow exponentially with the number of ambiguous pairs and wastes work on strings absent from the dictionary.
- **Decrypt every dictionary word per query:** Encrypt each dictionary entry and compare it to `word2` on every call. It is correct but repeats fixed work; preprocessing makes subsequent queries a lookup.
- **Store encrypted dictionary strings in a set:** A set loses collision multiplicity and cannot report how many distinct dictionary words decrypt from one ciphertext.
- **Build one reverse character per code:** Choosing only one key for a repeated value misses other valid plaintexts. Pre-encryption naturally accounts for all dictionary words.
- **Repeated values:** Multiple keys may map to the same code, and their dictionary words correctly increase the same counter entry.
- **Unmapped plaintext character:** `encrypt` immediately returns the empty string rather than a partial ciphertext.
- **Ciphertext absent from preprocessing:** `Counter` returns zero without requiring an explicit membership branch.
- **Repeated decrypt calls:** They reuse the constructor's counter and do not rescan the dictionary.
- **Unique dictionary strings with equal encryption:** Each distinct original contributes one, so the frequency can exceed one.
- **Even ciphertext length:** The contract guarantees legal pair boundaries. Lookup does not need to validate or split the string.
- **Empty encryption key in the counter:** It can arise only from an invalid dictionary word; legal decrypt inputs have length at least two and cannot match it.
- **Input preservation:** The constructor builds new mapping and counter objects; the supplied arrays and dictionary strings are not modified.
