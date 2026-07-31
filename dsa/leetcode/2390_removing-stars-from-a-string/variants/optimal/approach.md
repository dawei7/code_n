## General

Scan the string from left to right and store letters that have not yet been removed. Their order in the buffer matches their order in the processed prefix.

When a letter appears, append it. When a star appears, remove the buffer's final letter. That final letter is exactly the closest non-star character to the star's left that has survived earlier operations. The input guarantee ensures the buffer is nonempty at every pop.

After processing any prefix, the buffer equals the unique result of applying all stars in that prefix. Appending a letter preserves the claim, while a star removes the required nearest surviving letter. By induction, once the full input has been processed, joining the buffer gives exactly the final star-free string.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Every character causes one constant-time append or pop, and joining the survivors is linear, so total time is $O(n)$. The stack and returned string use $O(n)$ space.

## Alternatives and edge cases

- **Repeated backward search:** Marking removed positions and scanning left from every star to find the next surviving letter can take $O(n^2)$ time.
- **Right-to-left counter:** Scan backward, count stars waiting to delete letters, and retain letters only when no deletion is pending. This is also $O(n)$.
- **Consecutive stars:** Each star pops one more surviving letter; it does not attempt to delete another star.
- **All letters removed:** Joining an empty stack correctly returns the empty string.
- **No stars:** Every letter is appended and the original string is returned unchanged.
- **Legality guarantee:** No defensive behavior for a star without a preceding unmatched letter is required.
