## General
**Store the fully reduced prefix:** Maintain a list as a stack. Before processing the next character, the stack contains the unique fully reduced result for the prefix already read, so no equal adjacent pair exists inside it.

**Resolve the only possible new pair:** Compare the next character with the stack top. If they are equal, pop the top because those two letters form a removable adjacent pair. Otherwise push the character. No other part of the reduced prefix changes, and a pop automatically exposes the earlier stack character for comparison with a later input character.

**Establish the final reduction:** Each input character is pushed at most once and popped at most once. After processing a prefix, the push-or-pop rule produces exactly the result of reducing that prefix: an unequal character extends it, while an equal character cancels its final letter. By induction, the invariant holds for all prefixes. When the scan ends, the stack has no adjacent equal pair and represents a sequence of valid removals from the original string, so its joined contents are the guaranteed unique answer.

## Complexity detail
The scan processes $N$ characters once, and every stack operation is constant time, giving $O(N)$ time. At most $N$ characters remain in the stack, so space is $O(N)$.

## Alternatives and edge cases
- **Repeated string scans:** Find one removable pair, rebuild the string without it, and restart. This is correct but can take $O(N^2)$ time.
- **Regular-expression replacement:** Repeatedly replace every adjacent equal pair until stable. It obscures cascading behavior and may require many full-string passes.
- **In-place write pointer:** Use a mutable character array and treat its written prefix as the stack, achieving the same $O(N)$ time and space bounds.
- **Single character:** No pair exists, so the input is returned unchanged.
- **Complete cancellation:** An even run such as `"aaaa"` reduces to the empty string.
- **Cascading removal:** In `"abba"`, removing `"bb"` exposes `"aa"`, which must also be removed.
- **No duplicates:** A string with no adjacent equal letters remains unchanged.
- **Odd run length:** Repeated cancellation leaves one copy from an odd-length run.
