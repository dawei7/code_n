## General

**Represent the cursor as a boundary between two stacks**

The editor stores characters left of the cursor in `self.left` and characters right of the cursor in `self.right`.

`left` is in ordinary text order: its last element is the character immediately left of the cursor. `right` is stored in reverse proximity order: its last element is the character immediately right of the cursor.

If `left=["a","b"]` and `right=["e","d","c"]`, the visible text is `"abcde"` with the cursor between `b` and `c`. The reverse representation makes both characters adjacent to the cursor available through constant-time list `pop`.

**Add text at the cursor**

New text belongs immediately left of the cursor, in its original order. `self.left.extend(list(text))` converts the string to characters and appends them.

The right stack is untouched, so its text remains after the insertion. The cursor ends after the new characters because their final character becomes the new top of `left`.

For text `"xy"` inserted between `"ab"` and `"cde"`, `left` becomes `["a","b","x","y"]` and the represented document becomes `"abxycde"`.

**Delete only what exists on the left**

Backspace can remove at most `len(self.left)` characters. The assignment

`k = min(k, len(self.left))`

clamps the request to the number actually available.

The loop pops exactly `k` characters from `left`. Each pop removes the character immediately before the cursor, so repeated pops match backspace order. The right side and cursor-relative suffix are unchanged.

Returning the clamped `k` gives the actual deletion count.

**Move the cursor left**

Moving left once transfers the character immediately left of the cursor to become the character immediately right. The operation

`self.right.append(self.left.pop())`

does exactly that.

Repeating it `k` times reverses the transferred block inside `right` in precisely the representation required for later right moves. The request is clamped to `len(left)`, so the cursor never passes the beginning.

**Move the cursor right**

The inverse transfer pops the immediate-right character from `right` and appends it to `left`:

`self.left.append(self.right.pop())`.

Clamping to `len(right)` prevents movement beyond the end. Since the two operations are inverses, moving left and then right by the same feasible amount restores the state.

**Return the required left context**

Both cursor movement methods return

`''.join(self.left[-10:])`.

The slice selects the last ten left-side characters, or all of them when fewer than ten exist. Joining restores natural text order because `left` itself is stored in natural order.

If the cursor is at the beginning, the slice is empty and the method returns `""`.

**Trace the sample's central movement**

After adding `"leetcode"` and deleting four characters, `left` represents `"leet"`. Adding `"practice"` makes it `"leetpractice"`.

Moving left eight times transfers `e,c,i,t,c,a,r,p` into `right` in pop order. The left side becomes `"leet"`, and the right stack's top is `p`, the immediate next character. Returning the last ten left characters gives `"leet"`.

Moving right later pops from that reversed stack, restoring `p,r,a,c,t,i` in correct document order.

**Why the representation invariant is preserved**

Initialization represents an empty document with both stacks empty. Adding appends text to the left side without changing right text. Deleting removes a suffix of left text. Cursor moves transfer exactly one boundary character while preserving the concatenation of `left` and reversed `right`.

Every method therefore preserves both the full document content and the cursor boundary semantics. Its return value is derived from the exact left stack required by the contract.

## Complexity detail

Let `W` be added text length and `q` the requested movement or deletion count after clamping.

`addText` takes `O(W)` time; the exact source also creates `list(text)` of size `W` before extension. Delete and cursor movement take `O(q)` time because each affected character is popped or transferred once. Creating the returned context touches at most ten characters, `O(1)`.

Across the editor's lifetime, the two persistent stacks contain exactly the current document's `L` characters, using `O(L)` space. An add call temporarily allocates `O(W)` for `list(text)`.

## Alternatives and edge cases

- **One string plus cursor index:** Inserting or deleting in the middle of an immutable string can copy `O(L)` characters per operation.
- **Doubly linked list:** It supports cursor-local edits but retrieving the last ten characters requires backward traversal and more per-character object overhead.
- **Rope or balanced tree:** It helps with much larger block operations, but two stacks directly meet the `O(k)` follow-up.
- **Extend directly from the string:** `left.extend(text)` would avoid the temporary `list(text)` while preserving behavior.
- **Delete beyond the beginning:** Clamping deletes all left characters and returns their actual count.
- **Move left beyond the beginning:** All left characters transfer and the cursor stops at zero.
- **Move right beyond the end:** All right characters transfer and the cursor stops at document length.
- **Empty left context:** Cursor methods return the empty string.
- **More than ten left characters:** Only the last ten are returned; editor content is not truncated.
- **Add while right text exists:** New characters enter between left and right stacks, exactly at the cursor.
- **Delete while right text exists:** Only the left stack changes.
- **Persistent mutation:** Method calls update the editor object for all later calls.
