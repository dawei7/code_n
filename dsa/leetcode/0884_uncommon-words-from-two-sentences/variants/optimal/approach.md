## General
**Turn the two-sentence definition into one frequency condition**

Split both sentences into words and count them in one shared hash table. A word that appears exactly once across the combined input must occur once in one sentence and zero times in the other. Conversely, every word satisfying the problem's definition has combined frequency one. Thus the original two-part condition is equivalent to selecting entries whose total count equals one.

**Filter the completed frequency table**

After all words have been counted, iterate over the table and return each word with count one. Words shared between the sentences have count at least two, as do words repeated within either sentence, so both kinds are excluded. Since the required output order is unrestricted, the hash table's iteration order does not affect correctness.

## Complexity detail
Splitting, counting, and filtering process $L$ input characters in total, giving $O(L)$ expected time under standard hash-table assumptions. The split words, frequency table, and returned words together require $O(L)$ space in the worst case.

## Alternatives and edge cases
- **Count each word by rescanning both sentences:** This directly checks the definition but can require $O(L^2)$ time when many words are distinct.
- **Maintain two frequency tables:** Counting each sentence separately is also $O(L)$ and mirrors the definition, but one combined table is sufficient because only total frequency one matters.
- **Use sorting:** Sorting all words and scanning equal runs works, but costs $O(L \log L)$ comparison time in the usual model.
- **Repeated within one sentence:** A word occurring twice in `s1` is not uncommon even if it never occurs in `s2`.
- **Present in both sentences:** A word appearing once in each sentence has combined count two and must be excluded.
- **No uncommon words:** Return an empty list when every word is repeated or shared.
- **Arbitrary result order:** Any permutation containing exactly the uncommon words is valid.
