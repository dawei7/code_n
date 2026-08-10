## General

The input words are written horizontally, but the output reads one character position from every word at a time. Output row zero contains the first character of each word, output row one contains the second character of each word, and so on.

Words can have different lengths. When a word has no character at the current position, a space is required if later words still contribute characters on that row. Spaces at the very end of an output row, however, must be removed.

The exact Optimal solution builds this rectangular view one row at a time and trims only its trailing padding.

**Separating the words**

`words = s.split()` produces the words in their original order. The contract says there is exactly one space between words, but `split()` also safely handles general whitespace and does not include separators in the resulting strings.

Word order must be preserved because each word becomes one output column. Sorting or otherwise rearranging `words` would change the vertical text.

**Determining the number of output rows**

`n = max(len(w) for w in words)` finds the longest word length.

There must be one output row for each character position that exists in at least one word. If the longest word has length `n`, valid positions are zero through `n - 1`. No later row could contain any letter, so exactly `n` rows are needed.

The input contains at least one uppercase word, so `max` always has a length to examine.

**Building one vertical row**

For fixed character position `j`, the comprehension creates one entry per word:

`w[j] if j < len(w) else " "`.

If the word reaches position `j`, its actual letter is used. Otherwise, a space preserves the column so later words remain aligned.

For example, with words `["TO", "BE", "OR", "NOT", "TO", "BE"]` and `j = 2`, only `"NOT"` has a third character. The temporary row is:

`[" ", " ", " ", "T", " ", " "]`.

The three spaces before `T` are meaningful because they identify the empty third-character positions of the earlier words.

**Removing only trailing spaces**

The loop

`while t[-1] == " ": t.pop()`

removes padding after the last real character. It does not remove spaces before or between characters.

At least one word has a character at every `j < n` because `n` is the maximum length. Therefore, trimming cannot empty `t` and `t[-1]` remains safe. It stops when the final entry is a real uppercase letter.

For the preceding temporary row, the two spaces after `T` are popped, leaving `[" ", " ", " ", "T"]`. Joining produces `"   T"`, exactly the required row.

Using `strip()` would be wrong because it would remove leading spaces that preserve column alignment. `rstrip()` could replace the explicit loop, but the exact code performs list pops.

**Joining characters**

`"".join(t)` concatenates the retained single-character entries without adding separators. The result is appended to `ans` in increasing `j` order, so vertical rows appear from top to bottom.

For `"HOW ARE YOU"`:

- position zero gives `H`, `A`, `Y`, producing `"HAY"`;
- position one gives `O`, `R`, `O`, producing `"ORO"`;
- position two gives `W`, `E`, `U`, producing `"WEU"`.

**Why every output character is correct**

For each output row `j` and word column `c`, the comprehension uses `words[c][j]` exactly when it exists. Otherwise, it inserts padding. This exactly transposes the word-character grid.

Trailing padding has no visible column after it and is forbidden by the contract, so the pop loop removes it. Padding before the last real character is necessary and remains. The outer loop visits all and only character positions present in some word.

Thus, every output row contains the correct vertical letters, correct internal or leading spaces, and no trailing spaces.

## Complexity detail

Let $W$ be the number of words, $L$ the maximum word length, and $C$ the number of characters in the input string.

Splitting the string takes $O(C)$ time and stores the word strings. Finding $L$ takes $O(W)$ time.

The outer loop has $L$ iterations. Each builds a $W$-entry temporary list. Across a row, trimming pops at most $W$ entries and joining processes at most $W$ retained entries. Total transformation time is $O(WL)$.

Therefore, total time is $O(C+WL)$. If $P$ denotes the number of positions in the padded word rectangle, $P=WL$, this is the manifest's $O(P)$ once input parsing is included in the same scale.

The output and split words require $O(C+P)$ total representation space in a broad bound. The temporary row uses $O(W)$. The returned vertical strings can contain $O(P)$ characters, so the manifest's $O(P)$ space is appropriate.

## Alternatives and edge cases

- **Use `zip_longest`:** Transpose the words with a space fill value, join each tuple, and apply `rstrip`. It is concise but hides some alignment mechanics.
- **Preallocate a character grid:** It works but stores the full padded rectangle even though rows can be produced one at a time.
- **Use `strip`:** This is incorrect because leading spaces can be meaningful output.
- **Use `rstrip`:** It correctly removes trailing padding and is a simpler equivalent to the pop loop for strings.
- **All words equal length:** No padding is created, and every output row has exactly $W$ letters.
- **One word:** Each character becomes a one-character output string.
- **A longest word in an early column:** Later missing columns create trailing spaces, which are removed.
- **A longest word in a late column:** Earlier short words create leading or internal spaces, which must remain.
- **Safety of `t[-1]`:** Every row below the maximum length contains at least one real character, so trimming never empties the list.
- **Input word order:** It defines output column order and must not change.
- **Uppercase-only guarantee:** A literal space can unambiguously represent padding because spaces do not occur inside words.
