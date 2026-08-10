## General

**Use the counter to represent which phase the scan is in**

The loop iterates over `reversed(s)`, so characters arrive from right to left. `length == 0` initially means the scan has not yet entered the final word. A positive `length` means it is currently traversing that word.

This lets one loop perform both required phases: ignore trailing spaces, count non-space characters, then stop at the separator before the word.

**Trailing spaces do not trigger termination**

When the current character is a space, the code checks `if length`. If `length` is still zero, no word character has been seen, so this space belongs to the trailing suffix and the loop continues.

Breaking on the first reversed space unconditionally would be wrong for inputs such as `"moon  "`: it would return zero before reaching `moon`. The counter distinguishes trailing spaces from the separator that follows the word in reverse order.

**Count every character in the final word**

Whenever the reversed character is not a space, `length += 1`. Under the input alphabet guarantee, every such character is an English letter and belongs to the current word.

Once at least one letter has been counted, the next space lies immediately before the final word in forward order. The word is maximal, so no earlier character belongs to it, and the loop breaks. The accumulated count is returned.

If the final word begins at index 0, no separating space exists. The reversed iterator becomes exhausted, and the complete word length is returned without executing `break`.

**Trace the phases**

For `"Hello World   "`, the first three reversed characters are spaces and leave `length` at zero. The next five characters spell `World` backward and increase the counter to 5. The following space finds a positive counter and terminates the scan. Characters from `Hello` are never examined.

For `"a"`, the sole character increments the counter to 1, the iterator ends, and 1 is returned. For `"a    "`, all trailing spaces are ignored first and the same final count is reached.

**Correctness invariant**

Before the first non-space character, every inspected character is a trailing space and `length` remains zero. After entering the word, `length` equals the number of consecutive non-space characters inspected from the string's rightmost non-space position.

The first space encountered in this second phase is exactly the word's left boundary. Stopping there makes the count equal to the length of the final maximal non-space substring. If no such boundary exists, exhaustion proves the substring reaches index 0. These cases cover every valid input.

**`reversed(s)` does not reverse-copy the string**

In Python, `reversed` obtains a reverse iterator over the existing sequence. It stores an index and yields characters on demand; it does not construct `s[::-1]`. The source can therefore scan backward with constant auxiliary space.

**Why stopping early cannot miss part of the word**

Once counting has begun, every character seen since the rightmost letter has been non-space. The first following space in reverse order is immediately before that consecutive run in forward order. By the definition of a word as a maximal non-space substring, characters on the far side of that space belong either to another word or to additional separators. Neither can extend the last word across a space. Breaking at that exact boundary is therefore final, and continuing toward the beginning could only waste work.

**The unused alternative class**

`Solution2` in the same file calls `strip().split(" ")`, creating new string/list data proportional to the input. The harness selects class `Solution`, whose reverse iterator and counter are the behavior described here.

## Complexity detail

The scan examines trailing spaces plus final-word characters and, when present, one separating space. In the worst case this is all $n$ characters, so time is $O(n)$. Early `break` often avoids inspecting most of the prefix.

The counter, loop character, and reverse iterator use constant state. No token list or reversed string is materialized, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Two explicit indices:** First skip trailing spaces, then move left across the word and subtract boundaries. It makes the two phases visually explicit.
- **Forward constant-space scan:** Track the current word length and preserve it whenever a word ends. It handles the task but cannot skip the irrelevant prefix.
- **Built-in stripping and splitting:** It is concise but uses $O(n)$ temporary storage and may create many unused earlier words.
- **No trailing space:** Counting begins on the first loop iteration.
- **Many trailing spaces:** `length == 0` prevents them from ending the scan.
- **No preceding separator:** Iterator exhaustion returns the full-string word length.
- **Multiple earlier spaces:** The method stops at the first separator before the final word, so earlier spacing is irrelevant.
- **At least one word:** This guarantee ensures the final result is positive for valid input.
- **All-spaces input outside the contract:** Every character is ignored and zero is returned.
- **Input unchanged:** Strings are immutable, and reverse iteration performs no mutation or copy.
