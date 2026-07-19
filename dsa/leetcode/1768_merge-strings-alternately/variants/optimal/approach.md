## General
**Alternate through the shared prefix**

Let `shared` be the smaller input length. For every index below `shared`, append `word1[index]` and then `word2[index]` to a character buffer. This directly enforces both the alternating order and the requirement that `word1` contributes first.

**Append both possible suffixes**

At index `shared`, at least one input has no characters left. Append `word1[shared:]` and then `word2[shared:]`; one slice is empty, while the other is exactly the required leftover suffix. This avoids a separate branch for which word is longer.

**Join once after all characters are placed**

Every index below `shared` contributes one character from each word in the required order. Every later index belongs to only the longer word and retains its original order in the appended suffix. Thus each input character appears exactly once in its prescribed output position. Joining the buffer once constructs that sequence without repeatedly copying an expanding immutable string.

## Complexity detail
The paired loop handles $2\min(A,B)$ characters, and the two suffixes contain the remaining $\lvert A-B\rvert$ characters. Joining writes the $A+B$ output characters once, so total time is $O(A+B)$. The character buffer and returned string require $O(A+B)$ space.

## Alternatives and edge cases
- **Two independent pointers:** Advancing a pointer for each word inside one loop is equally valid, but requires two boundary checks per iteration.
- **Repeated string concatenation:** Adding one character to an immutable result repeatedly can copy the existing prefix and degrade to $O((A+B)^2)$ time.
- **`zip_longest`:** A fill sentinel can express the alternation compactly, but it must be removed carefully and adds machinery unnecessary for two short suffixes.
- **Equal lengths:** Both suffixes are empty after the alternating loop.
- **Longer `word1`:** Only `word1[shared:]` contributes trailing characters.
- **Longer `word2`:** Only `word2[shared:]` contributes trailing characters.
- **Single-character inputs:** The result still starts with the character from `word1`.
- **Repeated letters:** Characters are placed by position; equality between values does not change the ordering.
