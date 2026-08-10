## General

**Reverse the vowel subsequence while leaving every other position fixed.**

Imagine extracting only the vowels from left to right. If they are

$$
v_0,v_1,\ldots,v_{q-1},
$$

then the output must place $v_{q-1}$ into the original position of $v_0$, place $v_{q-2}$ into the position of $v_1$, and so on. Every consonant, digit, space, or punctuation character must remain at its original index.

Two pointers can find these mirrored vowel occurrences directly. The left pointer searches for the earliest unprocessed vowel, and the right pointer searches for the latest unprocessed vowel. Swapping them performs exactly one pair in the reversed vowel order.

**Make a mutable character buffer.**

Python strings cannot be changed at individual indices. The source therefore creates `cs = list(s)`, a mutable list containing the same characters in the same order.

All pointer searches and swaps operate on `cs`. At the end, `''.join(cs)` combines the final characters into the required new string. The original input string remains immutable, which is appropriate because this function's contract returns a string rather than requiring mutation of a character-array argument.

The conversion and final join do not alter character content. They only provide a representation in which swapping positions is possible.

**Recognize both lowercase and uppercase vowels.**

The string `vowels = "aeiouAEIOU"` lists all ten accepted vowel characters. Testing `cs[i] not in vowels` asks whether the current character is absent from that fixed collection.

Case is preserved. An uppercase `A` is recognized as a vowel but remains uppercase when moved; the algorithm swaps complete characters and never normalizes them. Printable ASCII characters not in this list are treated as non-vowels.

Because the membership collection always has length ten, each membership check is constant time in asymptotic analysis. A set could also provide constant expected membership, but is unnecessary for such a fixed tiny group.

**Find the next vowel from the left.**

The outer loop runs while `i < j`. Its first inner loop advances `i` while `cs[i]` is not a vowel.

Every skipped character is a non-vowel. It must stay at the same position in the output, and the algorithm never writes to that index. Once `i` stops, either the pointers have met or crossed, or `cs[i]` is the leftmost remaining vowel.

The repeated `i < j` guard prevents the search from moving beyond the right pointer or accessing outside the unresolved interval.

**Find the next vowel from the right.**

The second inner loop similarly decrements `j` while `cs[j]` is not a vowel. Skipped right-side non-vowels remain untouched. When it stops with `i < j`, `cs[j]` is the rightmost remaining vowel.

Both searches are required before swapping. If only the left pointer skipped consonants, a vowel could be exchanged with a right-side non-vowel and incorrectly move that non-vowel from its fixed position.

**Swap a mirrored vowel pair and move inward.**

After both searches, the source checks `if i < j` again. If true, both positions hold vowels and are distinct. Tuple assignment swaps them safely, then `i` increments and `j` decrements so the same occurrences are not processed again.

The swapped left position now holds the latest remaining vowel, which is exactly its final reversed-vowel value. The swapped right position holds the earliest remaining vowel, also its final value.

If the searches make the pointers meet, at most one unpaired vowel remains. A middle vowel maps to itself in the reversed vowel sequence, so no swap is needed.

**Walk through `IceCreAm`.**

The vowels in occurrence order are `I`, `e`, `e`, and `A`.

- The initial pointers find `I` at the far left and `A` near the right. Swapping them places `A` first and `I` last among vowel positions.
- The pointers move inward. The searches skip non-vowels until they find the two `e` occurrences.
- Swapping equal `e` characters leaves the visible buffer unchanged but correctly processes that mirrored pair.

Joining the buffer yields `AceCreIm`. All characters such as `c`, `C`, `r`, and `m` remain at their original indices.

**The loop invariant.**

Before each outer iteration:

- every vowel occurrence strictly left of `i` already contains its final reversed-vowel character;
- every vowel occurrence strictly right of `j` already contains its final reversed-vowel character;
- non-vowel positions are unchanged;
- only vowel occurrences between `i` and `j` may still need reversal.

The invariant is initially true because nothing has been processed. The searches skip only non-vowels, preserving them. The swap pairs the outermost unresolved vowels and puts both in final positions. Moving inward then preserves the invariant.

When the loop ends, zero or one unresolved vowel remains. Zero means all pairs are finished; one maps to itself. Therefore all vowel occurrences appear in reverse order and all non-vowels remain fixed.

**Why no character is lost or duplicated.**

Each operation is a swap, so `cs` always contains exactly the original multiset of characters. Every vowel occurrence belongs to one outermost pair or is the unique middle occurrence. The pointers move monotonically and never revisit a completed pair. The final join uses every buffer position exactly once.

## Complexity detail

Let $n$ be `len(s)`. Converting the string to `cs` takes $O(n)$ time. Although the code contains inner loops inside an outer loop, `i` only moves right and `j` only moves left. Across the entire execution, each pointer advances through at most $n$ positions, so all searching and swapping is $O(n)$ total. Joining the result is another $O(n)$ operation. Overall time complexity is $O(n)$.

The mutable character list contains $n$ entries, so auxiliary space is $O(n)$. The pointer variables and fixed vowel string use $O(1)$ additional space. This matches the source and manifest.

## Alternatives and edge cases

- **Collect vowel indices or values first:** Store every vowel, reverse that list, and write values back into vowel positions. This is easy to structure but uses additional space proportional to the number of vowels on top of the mutable output buffer.

- **Use a vowel set:** Replacing the ten-character string with a set makes membership expected $O(1)$, but asymptotic behavior is unchanged because the current membership scan has a fixed bound of ten.

- **Repeated string concatenation:** Building the result one character at a time can become quadratic in languages with immutable strings. The list buffer plus one final join avoids that cost.

- **No vowels:** Both searches eventually make the pointers meet, no swap occurs, and the original string is returned unchanged.

- **One vowel:** It is the middle of the vowel sequence and maps to itself; the pointers do not swap it with a non-vowel.

- **Two vowels:** The searches locate them and perform exactly one swap, regardless of how many non-vowels lie between.

- **Mixed case:** Uppercase and lowercase forms are both recognized, and their original case travels with the character.

- **Repeated equal vowels:** Swapping equal characters has no visible effect but is correct and still advances both pointers.

- **Printable nonletters:** Digits, spaces, and punctuation are absent from `vowels`, so the searches skip them and their indices remain unchanged.
