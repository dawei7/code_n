## General

**Build one lookup level for each precedence rule**

A query can match in three increasingly permissive ways: exact spelling, case-insensitive spelling, or case-insensitive spelling after treating every vowel as interchangeable.

The first successful rule must win. The solution preprocesses `wordlist` into one structure for each rule, then checks queries in that same order.

**Exact matches**

Set `s = set(wordlist)` contains original spellings.

For query `q`, `q in s` tests exact characters and capitalization. If present, the method appends `q` itself and immediately continues.

Returning the query is correct because exact equality means it is identical to the wordlist spelling.

**Case-insensitive matches**

Dictionary `low` maps lowercase spelling to the first original word with that spelling.

During preprocessing, `low.setdefault(t, w)` inserts `w` only when lowercase key `t` has not appeared. Later capitalization variants do not overwrite it, preserving the required first match.

After exact matching fails, the query is lowercased. If it exists in `low`, the stored original spelling is returned.

**Vowel-error normalization**

Helper `f(w)` scans a lowercase word. Every vowel in `"aeiou"` becomes `"*"`, while consonants remain unchanged.

For example, `"kite"` and `"keto"` both become `"k*t*"`. Word `"keet"` becomes `"k**t"` and does not match because vowel positions and length differ.

Dictionary `pat` maps each normalized pattern to the first original word producing it. `setdefault` again preserves wordlist priority.

After exact and lowercase checks fail, the lowercased query is normalized and looked up in `pat`.

**Why one wildcard symbol is sufficient**

The vowel-error rule allows each vowel position to change independently to any vowel. Replacing all vowels with one marker removes vowel identity while preserving word length, consonants, and which positions are vowels.

Two normalized strings are equal exactly when they differ only by vowel choices and capitalization under this rule.

The marker `*` cannot collide with input because words contain only English letters.

**Why precedence is exact**

The query loop uses `continue` after each successful level.

Exact matching occurs before lowercasing, so it cannot be replaced by an earlier differently capitalized entry. A lowercase match occurs before vowel normalization, so exact letters up to case beat a looser vowel match.

Only if both fail does the pattern dictionary apply. If that fails, an empty string is appended.

**Trace**

With `wordlist = ["KiTe", "kite", "hare", "Hare"]`:

- Exact set contains all four spellings.
- Lowercase key `"kite"` maps to first entry `"KiTe"`.
- Pattern `"k*t*"` also maps to `"KiTe"`.

Query `"kite"` is exact and returns `"kite"`.

Query `"Kite"` is not exact but lowercases to `"kite"`, so it returns `"KiTe"`.

Query `"keti"` misses the lowercase map but normalizes to `"k*t*"`, so it returns `"KiTe"`.


Each key captures precisely one required equivalence relation. Set membership recognizes exact equality. Lowercase keys recognize capitalization-only differences. Normalized keys recognize capitalization and vowel substitutions while preserving everything else.

The query checks these relations in required precedence order, and preprocessing retains the first wordlist representative for non-exact ties. Therefore, each returned correction is exactly specified.

**Why preprocessing pays off**

Without maps, each query might rescan every wordlist entry under all three rules. Preprocessing computes canonical keys once, so each query performs only a constant number of expected-time lookups plus work proportional to its own length.

**Why pattern equality has no false positives**

Suppose two lowercase words produce the same pattern. Every consonant position must contain the same literal consonant because consonants are copied unchanged. Every wildcard position must contain a vowel in both words. Pattern length is also identical.

Therefore, the words differ only in which vowel occupies a vowel position, exactly the permitted error. Conversely, words related by permitted vowel substitutions clearly produce the same pattern. The normalization is both necessary and sufficient.

**Why original spellings are stored as values**

Dictionary keys are normalized for matching, but the required answer must preserve capitalization from `wordlist`. Storing `w` as the dictionary value lets the algorithm return the source spelling directly.

If the normalized key itself were returned, answers would be lowercase or contain wildcard symbols and would violate the output contract.

**One output per query**

Every query follows exactly one chain of precedence checks and appends exactly one string. Each success continues immediately, and the final empty-string branch covers failure. The length and ordering of `ans` therefore match `queries` one-for-one.

## Complexity detail

Let `S` be total characters across `wordlist` and `queries`.

Preprocessing lowercases and normalizes each word once. Query handling lowercases and may normalize each query once. Hash operations are expected constant time aside from key construction, so expected time is `O(S)`.

The set, two maps, and output store `O(S)` total character content or references, so space is `O(S)`.

## Alternatives and edge cases

- **Scan wordlist per query:** Direct but can require quadratic total content work.
- **Regular expressions:** They add overhead; canonical pattern keys are simpler.
- **Overwrite dictionary keys:** This would return the last match instead of the first. `setdefault` is essential.
- **Exact match with a later spelling:** Exact membership returns the identical query.
- **Capitalization tie:** The first wordlist spelling is retained.
- **Vowel-pattern tie:** The first matching wordlist entry is retained.
- **Different lengths:** Patterns differ and cannot match.
- **Missing or extra vowel:** Positions are preserved, so insertions and deletions do not match.
- **Uppercase vowels:** Lowercasing occurs before normalization.
- **No match:** The output contains an empty string.
