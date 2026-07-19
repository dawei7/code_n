## General
**Measure the needed supply of each letter.** Keep an array of 26 balances. For every aligned pair of characters, increment the entry for the character from `s` and decrement the entry for the character from `t`. After the scan, a positive balance for a letter is exactly the number of additional copies that `t` needs, while a negative balance represents copies that `t` has in excess.

Because the strings have equal length, the total positive balance equals the magnitude of the total negative balance. One replacement can remove one surplus character and supply one missing character at the same time. Therefore the sum of all positive balances is both achievable and a lower bound: every missing copy must be created, and exactly that many replacements can pair all deficits with all surpluses.

## Complexity detail
The paired scan takes $O(n)$ time. Summing the 26 positive balances takes constant time. The balance array always contains 26 integers, so auxiliary space is $O(1)$ with respect to $n$.

## Alternatives and edge cases
- **Two frequency maps:** Separate counters for `s` and `t` also give $O(n)$ time, but one difference array states the needed replacements more directly.
- **Repeated search and removal:** Matching each character of `s` against a mutable list of `t` is correct but can require $O(n^2)$ time.
- **Already anagrams:** Every balance is zero, so no replacement is needed even when the character orders differ.
- **Completely different strings:** Every position may need replacement, making the answer $n$.
- **Repeated letters:** Multiplicity, not mere membership, determines the deficit.
