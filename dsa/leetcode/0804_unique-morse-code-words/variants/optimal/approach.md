## General
**Map letters by alphabet index**

Store the 26 prescribed Morse codes in alphabet order. For each character, subtract the code point of `a` to select its Morse fragment. Concatenate the fragments for a word without separators, exactly matching the transformation rule.

**Deduplicate complete transformations**

Insert every completed Morse string into a hash set. Equal transformations collapse to one entry even when they came from different spellings; unequal strings occupy distinct entries. The final set size is therefore exactly the requested count.

Every character is replaced by its unique prescribed fragment in its original order, so the constructed string is the word's required transformation. Set membership identifies equality of those entire strings and no other property, making the number of stored keys precisely the number of distinct transformations.

## Complexity detail
Let `c` be the total number of letters across all words. Each letter contributes a constant-length Morse fragment, so constructing and hashing all transformations takes $O(c)$ expected time. The set and its stored transformation strings use $O(c)$ space in the worst case.

## Alternatives and edge cases
- **Sort transformations:** Build all encoded strings, sort them, and count adjacent changes; this uses $O(c + w \log w)$ time for `w` words.
- **Compare against a list:** Linearly checking every prior distinct transformation is correct but can require $O(w^2)$ comparisons.
- **Trie of dots and dashes:** A trie can share prefixes but is unnecessary when hashing complete strings is direct.
- **Duplicate input words:** They necessarily produce one shared transformation and do not increase the count.
- **Different words may collide:** Letter boundaries are omitted, so strings such as `a` and `et` can encode identically.
- **Single word:** Exactly one transformation exists.
- **No separators:** Adding delimiters between letter codes would change the required equivalence relation.
