## General
**Represent only the equality pattern of a string**

Scan a string from left to right and assign each newly encountered letter the next small identifier. Repeated letters reuse their first identifier. For example, both `abb` and `mee` normalize to `(0, 1, 1)`, whereas `abc` becomes `(0, 1, 2)`.

**Compare each word with the pattern's signature**

Compute the canonical signature of `pattern` once. A word matches exactly when its signature is identical, so retain those words and ignore the others.

Equal signatures mean that any two positions hold the same letter in the pattern exactly when they hold the same letter in the word. Mapping each pattern letter to the word letter at its first occurrence is therefore consistent and injective, hence bijective on the letters used. Conversely, any valid letter permutation preserves every equality and inequality relation between positions, so it must produce the same signature.

## Complexity detail
Computing one signature costs $O(L)$ time, and it is done for the pattern and all $N$ words, giving $O(NL)$ time. A signature and its temporary letter map use $O(L)$ space. The returned list can hold $N$ word references, so total additional storage including the result container is $O(N+L)$.

## Alternatives and edge cases
- **Maintain forward and reverse maps:** Checking both `pattern -> word` and `word -> pattern` mappings directly is also $O(NL)$ and makes the bijection explicit.
- **Compare every pair of positions:** Testing whether equality agrees for all index pairs is correct but costs $O(NL^2)$ time.
- **Check only a forward map:** This is insufficient because two pattern letters could incorrectly map to the same word letter.
- **All letters distinct:** A word matches only when all of its letters are also distinct.
- **All letters equal:** A matching word must repeat one letter at every position.
- **One-character pattern:** Every one-character word matches because any single used letter can be mapped bijectively.
- **Duplicate input words:** Each matching occurrence belongs in the returned list; normalization does not deduplicate the input.
