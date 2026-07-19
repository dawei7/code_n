## General
**Track the currently open pairs.** Scan `s` from left to right with a counter `depth`. An opening parenthesis begins one more enclosing pair, so increment `depth` when `(` is encountered. A closing parenthesis ends the innermost active pair, so decrement `depth` when `)` is encountered. Digits and operators do not affect nesting.

**Record a new maximum after opening.** Immediately after processing `(`, `depth` equals the number of parenthesis pairs that contain the next position. Compare it with `maximum` at that moment. Updating before a later closing parenthesis ensures that even the innermost level of a run such as `((()))` is observed.

The validity guarantee means `depth` never becomes negative and returns to zero after the scan. Every possible nesting level begins at an opening parenthesis, so examining `depth` after every opening observes the global maximum. Conversely, the counter counts only unmatched openings, so no recorded value can exceed the true nesting depth.

## Complexity detail
The scan examines each of the $n$ characters once, giving $O(n)$ time. The two integer counters use $O(1)$ auxiliary space; no explicit stack is needed because the task asks only for the number of active pairs, not their positions or contents.

## Alternatives and edge cases
- **Explicit stack:** Pushing each `(` and popping for each `)` also finds the maximum stack size, but it uses $O(n)$ space for information that a counter already captures.
- **Repeated prefix counting:** Counting opens and closes again for every prefix is correct, but rescans characters and takes $O(n^2)$ time.
- A string containing no parentheses has maximum depth zero.
- Adjacent groups such as `()()` each return to depth zero; their depths are not added together.
- A run of opening parentheses may establish the maximum before any digit or operator appears.
- Because `s` is guaranteed valid, the algorithm does not need separate rejection logic for unmatched parentheses.
