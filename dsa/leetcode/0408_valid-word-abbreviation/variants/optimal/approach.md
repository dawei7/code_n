## General
**Keep one pointer in each string**

Let `word_index` mark the next unconsumed word character and `abbr_index` the next abbreviation token. A letter token must equal `word[word_index]`; if so, advance both pointers by one.

**Parse an entire numeric token before skipping**

When the abbreviation character is a digit, reject immediately if it is zero because that would be a forbidden leading zero. Accumulate all consecutive digits into one number, then advance only the word pointer by that skip length.

**Reject as soon as the word boundary is crossed**

After a skip, a word index greater than its length proves the abbreviation asks for nonexistent characters. At the end, both pointers must be exhausted: leftover word characters mean the abbreviation is too short, while the abbreviation loop already prevents leftover unmatched tokens.

**Why the scan matches abbreviation semantics exactly**

Each letter consumes exactly one equal word character, and each number consumes exactly its parsed positive count without inspecting those characters. These are the only token types. The pointers preserve source order, so reaching both ends witnesses a complete expansion equal to the word; every rejection corresponds to a violated rule.

## Complexity detail
Each of the `w` word positions is advanced over at most once, and each of the `a` abbreviation characters is parsed once, for $O(w + a)$ time. Numeric accumulators and pointers use $O(1)$ space.

## Alternatives and edge cases
- **Expand skipped positions into wildcard text:** can validate afterward but allocates $O(w)$ additional storage.
- **Consume strings through front slicing:** is logically correct but repeatedly copies suffixes and can take $O((w + a)^2)$ time.
- **Recursive token matching:** adds call-stack state even though every token has a deterministic effect.
- A number consisting of several digits is one skip count.
- Any numeric token beginning with zero is invalid.
- A skip may end exactly at the word boundary.
- Skipping beyond the word length is invalid.
