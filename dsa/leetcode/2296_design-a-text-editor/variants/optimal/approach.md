## General

**Split the document at the cursor**

Keep one stack for characters to the left of the cursor in normal order and
one stack for characters to its right in reverse order. The cursor is the
boundary between them. Appending inserted text to the left stack places it
exactly at that boundary and advances the cursor past it.

Backspace removes up to `k` items from the end of the left stack. Moving left
pops characters from the left stack and pushes them onto the right stack;
moving right performs the reverse transfer. These operations stop when `k`
characters have moved or the source stack is empty, so the cursor never leaves
the document.

After a move, the requested context is simply the last at most ten characters
of the left stack. At all times, concatenating the left stack with the reverse
of the right stack reconstructs the full text, and the length of the left
stack is the cursor position. Every method preserves this representation,
which proves that its edits, movement bounds, and returned context match the
contract.

## Complexity detail

Let $q$ be the number of calls, $L$ the maximum text length, and $W$ the total
number of characters inserted, actually deleted, or actually moved across the
cursor. Each character-stack action is constant time, and each context result
examines at most ten characters, giving $O(W+q)$ total time. The two stacks
together store the current text in $O(L)$ space.

## Alternatives and edge cases

- **Single contiguous character array:** Inserting or deleting near the beginning requires shifting the suffix and can make a long trace quadratic.
- **Two strings with slicing:** This is concise, but repeated middle edits copy growing prefixes or suffixes.
- **Doubly linked list:** Cursor-local edits and moves meet the target bounds, but node-per-character overhead is higher than two stacks.
- **Delete past the start:** Remove only the entire left stack and return that smaller count.
- **Move past either end:** Stop at the boundary rather than storing an invalid cursor position.
- **Insertion in the middle:** Existing right-side characters remain after the inserted text.
- **Ten-character window:** Movement returns only the closest ten left characters, not the whole prefix.
- **Empty left context:** A cursor at position zero returns `""`.
- **Right-stack orientation:** Its last element must be the next character to the right so a right move restores characters in document order.
