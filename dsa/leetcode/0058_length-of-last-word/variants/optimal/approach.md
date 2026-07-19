## General
**Ignore only the trailing-space suffix**

Move an index left past all trailing spaces. Once a non-space character is reached, the last word has been located. Count backward until a space or the beginning of the string. No earlier character can affect this maximal final non-space run.

**Two backward phases match the definition directly**

The first phase establishes that the index points to the final character of the last word. During the second phase, `length` equals the number of consecutive word characters already crossed from right to left. Encountering a space or passing index zero completes exactly that maximal sequence.

**Trace trailing and internal spaces**

For `"fly me to moon  "`, skip the two final spaces, then visit `n`, `o`, `o`, and `m`. The next character is a space, so the answer is 4.

**The maximal non-space suffix is the last word**

Trailing spaces belong to no word, so skipping them cannot remove any character from the answer. The first remaining character from the right is the final character of the last word.

Continuing left until a space or the string boundary visits exactly that word's maximal contiguous non-space run—no earlier word can cross the delimiter. The number of visited characters is therefore precisely the last word's length.

## Complexity detail
In the worst case the scan visits every character once, for $O(n)$ time. It uses one index and one counter, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Split the whole string:** is concise but creates a list and substrings requiring $O(n)$ additional space.
- **Strip then search backward:** may allocate a trimmed copy depending on the language.
- **Scan left-to-right:** can reset a current length after spaces and is also $O(n)$ time and $O(1)$ space, but reads irrelevant prefixes even when the last word is short.
- A string containing one word reaches the beginning rather than a separating space. Multiple consecutive internal spaces are irrelevant because counting stops at the first one before the last word.
- The contract guarantees at least one word, so the initial skip cannot run past the whole string; a broader API should define that all-space case explicitly.
