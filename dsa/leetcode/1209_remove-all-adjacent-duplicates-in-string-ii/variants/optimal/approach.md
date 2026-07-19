## General
**Compress the surviving prefix into runs.** Maintain a stack whose entries contain a character and the count of its current adjacent run in the fully reduced prefix processed so far. When the next character differs from the top, push a new run with count one. When it matches, increment the top count.

**Delete at the exact threshold.** As soon as a run count reaches `k`, pop that entry. Nothing larger needs to be stored: reaching `k` means those characters disappear immediately. The run below the popped entry is now exposed, exactly modeling the concatenation caused by a removal. A later character can extend that older run and trigger a cascade without rescanning earlier input.

**Why the stack represents the unique reduction.** Before each new character, the stack expands to the fully reduced form of the processed prefix. Adding one character can affect only its new suffix: it either begins a run, extends the last run, or completes and deletes that run. No earlier internal block can suddenly become removable because it was already reduced. Thus the invariant continues to hold after every character, and expanding the remaining runs after the final character yields the required final string.

## Complexity detail
Each of the $n$ characters is pushed once or merged into the top run, and each stack entry is popped at most once. The processing time is therefore $O(n)$. Reconstructing the answer emits at most $n$ characters and stays within the same bound. The stack can contain $O(n)$ runs.

## Alternatives and edge cases
- **Repeated whole-string scans:** Finding and deleting blocks, then restarting from the beginning, is correct but can take $O(n^2)$ time after many cascades.
- **Rescan the reduced prefix per character:** It preserves correctness but repeats work already summarized by the stack and is quadratic when no characters are removed.
- **Character stack with modulo counts:** Storing each character separately plus its run length also works, but uses more entries than run-length pairs.
- **No removable group:** Every run count remains below `k`, so the original string is returned.
- **Entire string removed:** Popping the last run leaves an empty result.
- **Run longer than `k`:** Every completed group of `k` disappears; the remainder, if any, stays as the new run.
- **Cascade across a deletion:** Equal runs on opposite sides are combined naturally when later processing exposes and extends the older stack top.
- **`k` larger than the string:** No removal is possible.
