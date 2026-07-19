## General
**Treat the current result as a stack**

Scan the input from left to right while storing the characters that have survived so far. Only the newest survivor can form a newly exposed invalid pair with the next input character. If the stack is empty or the two characters are not opposite-case versions of the same letter, push the new character.

**Cancel exactly when the boundary is invalid**

When the stack top and current character are different as characters but equal after case normalization, they form a removable pair. Pop the stack top and do not push the current character. This also exposes the previous survivor, allowing a later input character to trigger a chain of cancellations without rescanning the prefix.

After every step, the stack is the fully reduced result of the prefix processed so far. A push preserves goodness because the new boundary is valid; a pop removes the only new invalid boundary, and the remaining stack was already good. Thus, after the final character, the stack is good and represents a legal sequence of removals. Since the contract guarantees a unique final result, joining the stack returns exactly that result.

## Complexity detail
Each of the $n$ characters is pushed at most once and popped at most once. Every comparison and stack operation is constant time, so the scan takes $O(n)$ time. In the worst case no pair cancels, and the stack stores all $n$ characters, requiring $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Repeated search and splice:** finding one bad pair, deleting it, and restarting is straightforward, but repeated scans and string rebuilding can take $O(n^2)$ time.
- **Recursive reduction:** recursion can mirror the cancellation process, but it adds call-stack overhead and can still rescan unchanged text unless it carries explicit stack state.
- A single character is already good.
- The entire string may cancel, so an empty answer is valid.
- Equal adjacent characters with the same case, such as `"aa"`, do not cancel.
- Different letters never cancel merely because their cases differ, so `"aB"` remains unchanged.
- Removing one pair can expose another invalid pair across the removed boundary.
- Either order, lowercase-uppercase or uppercase-lowercase, must be recognized.
