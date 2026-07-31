## General

**Separate physical storage from logical orientation.** Store the result's characters in a deque and keep a Boolean flag indicating whether its logical order is reversed. A `%` only toggles this flag. In normal orientation, a letter is appended at the right and `*` removes from the right; in reversed orientation, those same logical-end operations use the left side instead. Each of these operations is constant-time.

**Duplication preserves the physical pattern.** If the deque is in normal orientation, doubling its physical sequence clearly appends the logical string to itself. If it is reversed, the logical string is the reverse of the physical sequence. Doubling the physical sequence and then reading it backward still yields two consecutive copies of that reversed logical string. Therefore `#` can snapshot the deque and extend it with the same physical sequence without inspecting the orientation.

At every step, reading the deque according to the flag equals the result defined by all processed input characters: the endpoint rules implement logical append and removal, toggling reverses the view, and physical doubling duplicates either view. Join the deque once at the end, using reverse iteration only when the flag is set.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and let $L$ be the final output length. Letters add one stored character, successful `*` operations remove one, and every `#` copies exactly as many characters as it adds. Across the whole run, all duplication work is bounded by the total net growth plus at most $n$ removed characters, so processing takes $O(n+L)$ time. The final join also costs $O(L)$. The deque and returned string use $O(L)$ auxiliary storage apart from the unavoidable output.

## Alternatives and edge cases

- **Reverse the materialized string for every `%`:** This is simple but can repeatedly copy a large unchanged result, taking $O(nL)$ time in the worst case.
- **Append duplicated characters one by one to an immutable string:** Repeatedly copying a growing prefix can take $O(L^2)$ time.
- **Leading or excessive `*`:** Removing from an empty result has no effect.
- **`#` on an empty result:** Duplicating the empty string leaves it empty.
- **`%` on an empty or one-character result:** The orientation may toggle, but the visible string is unchanged.
- **Several `%` operations:** Two consecutive reversals cancel because the orientation flag toggles twice.
- **Append while reversed:** The new letter belongs at the deque's physical left, which is the logical end.
- **Duplicate while reversed:** Copy the physical deque in the same order; do not reverse the snapshot.
- **Exponential output growth:** Repeated `#` operations can make $L$ much larger than $n$, so complexity must include the output length.
