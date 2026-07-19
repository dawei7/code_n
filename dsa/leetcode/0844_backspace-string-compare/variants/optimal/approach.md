## General
**Read only characters that survive**

Scan a string from right to left with a skip counter. Encountering `#` increases the number of earlier letters that must be erased. Encountering a letter while the counter is positive consumes one pending backspace and decreases the counter. The first letter reached with a zero counter is the next character visible in the final text.

Maintain one reverse index and skip counter for each input. Repeatedly advance each side to its next surviving character. If only one side has a character, the edited lengths differ. If both do but their letters differ, the final texts differ. If both indices pass the beginning together, every surviving character matched and the result is `true`.

A skipped letter is erased by one `#` to its right, while a returned letter has no unmatched backspace to erase it. Thus each helper step identifies the exact next character of the fully edited text in reverse order. Comparing those characters proves the result without ever materializing either edited string.

## Complexity detail
Each index moves only left and never revisits a position, so the combined time is $O(\lvert s \rvert+\lvert t \rvert)$. Four integer variables hold the indices and skip counts, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Build with stacks:** Processing each string left to right and popping on `#` is simple and linear, but stores up to $O(\lvert s \rvert+\lvert t \rvert)$ characters.
- **Repeated immutable rebuilding:** Appending or slicing a newly allocated string after every keystroke can copy the accumulated text repeatedly and take quadratic time.
- **Leading backspaces:** Any number of `#` characters before a surviving letter simply exhausts against empty text.
- **More backspaces than letters:** Excess pending skips disappear when the index passes the start; they do not create characters or errors.
- **Different raw strings:** Different keystroke sequences may still reduce to the same final text.
- **Empty final texts:** Both inputs can become empty even though neither input string is empty.
