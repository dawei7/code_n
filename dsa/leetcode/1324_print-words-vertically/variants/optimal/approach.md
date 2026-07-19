## General
**Transpose the padded words**

Split `s` into its words and find $L$. For each character position `row` from 0 through `L - 1`, visit the words from left to right. Append `word[row]` when that position exists; otherwise append a space as a placeholder for the shorter column.

After the row is assembled, remove only its trailing spaces and append it to the answer. Padding during construction preserves the exact columns of any later visible characters, while `rstrip` enforces the output rule. Iterating every possible character position of the longest word produces exactly the required number and order of rows.

## Complexity detail
The nested loops inspect all $P=wL$ cells. Splitting the sentence and finding $L$ are bounded by the input length and do not exceed this work. The temporary row buffers and returned strings contain at most $P$ characters, so auxiliary output construction space is $O(P)$.

## Alternatives and edge cases
- **Pad then transpose:** Explicitly right-pad every word to length $L$ before transposing is simple but materializes another full $P$-character rectangle.
- **Repeated string concatenation:** Extending immutable row strings one character at a time can repeatedly copy prefixes; a character list plus one join avoids that overhead.
- **One word:** Return its characters as one-character strings.
- **Equal-length words:** No padding or trimming is needed.
- **Short middle word:** Its spaces inside a row must remain when a later column has a character.
- **Trailing short words:** Their absent characters become trailing spaces and must be removed.
