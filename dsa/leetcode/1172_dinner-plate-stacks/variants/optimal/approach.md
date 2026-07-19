## General
**Separate the two ordering requirements.** Store each stack as a list inside an outer list. The outer list preserves stack indices and makes its final element the rightmost represented stack. A min-heap of non-full indices independently exposes the leftmost place where a push is allowed.

**Maintain the heap lazily.** Before a push, discard heap entries that now lie beyond the trimmed outer list or refer to a full stack. If no valid index remains, append a new empty stack and put its index into the heap. Push onto the heap's smallest-index stack, then remove that heap entry if the stack has reached `capacity`. A stack that changes from full to non-full during removal is inserted into the heap.

**Trim only the unused right boundary.** `popAtStack(index)` rejects an absent or empty stack; otherwise it removes that stack's top value and records newly available space when necessary. It then drops empty stacks only from the end of the outer list. Heap entries for those removed indices may remain temporarily, but the next push recognizes them as stale. `pop()` trims the same empty suffix and delegates to the current final stack, which is exactly the rightmost non-empty one.

The heap minimum therefore always yields the leftmost usable stack after stale entries are removed, and the trimmed list's last stack always yields the rightmost available value. These are precisely the two required choices.

## Complexity detail
Each heap insertion or removal costs $O(\log s)$. Every stack trimmed from the right was previously created, so all trimming across $m$ operations costs $O(m)$ in total. Consequently the full operation sequence takes $O(m\log s)$ time. The stacks hold $v$ values, while the outer list and heap use $O(s)$ metadata, for $O(v+s)$ space.

## Alternatives and edge cases
- **Scan stacks from the left on every push:** This is simple and correct, but a long run of full stacks makes one insertion $O(s)$ and the complete sequence quadratic.
- **Track only the rightmost stack:** That supports `pop()` but cannot find the leftmost hole created by `popAtStack` efficiently.
- **Capacity one:** Every push fills its stack immediately, and any successful removal empties one; the same heap and trimming rules still apply.
- **Hole in the middle:** Removing from a non-final stack must make its index available without renumbering any later stack.
- **Absent or empty index:** `popAtStack` returns `-1` and changes no state.
- **Empty suffix:** Several trailing empty stacks can be trimmed together, but empty stacks between non-empty ones must retain their indices.
- **Completely empty structure:** `pop()` returns `-1`, and the next push creates stack `0` again.
