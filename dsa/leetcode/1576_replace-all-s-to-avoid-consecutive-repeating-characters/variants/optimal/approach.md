## General
**Only two neighboring letters can be forbidden**

Process the characters from left to right after copying the string into a mutable list. At a placeholder position `i`, its left neighbor has already been finalized. Its right neighbor is either a fixed letter or another placeholder that will be handled later.

A replacement must differ from both finalized neighboring letters. At most two lowercase letters are forbidden, so trying only `a`, `b`, and `c` always finds an available choice. If the right neighbor is still `?`, it forbids none of these letters at the current step.

**Preserve the invariant while scanning**

After replacing position `i`, every adjacent pair ending at or before `i` is valid. The chosen character differs from the finalized left neighbor, and when the right position is eventually processed, that step will avoid the character just chosen.

Fixed input letters are never modified. Therefore, after the final position is processed, every placeholder has become a lowercase letter and every adjacent pair differs. Joining the mutable characters yields a valid answer.

## Complexity detail
Each of the $N$ positions is inspected once, and at most three candidate letters are tried at a placeholder. The time complexity is $O(N)$.

The mutable character list and returned string use $O(N)$ space. Apart from that representation, the scan uses constant working state.

## Alternatives and edge cases
- **Use the full alphabet:** trying all 26 letters is also linear because the alphabet size is constant, but three candidates are sufficient.
- **Backtracking over replacements:** exploring candidate combinations can find a valid answer but introduces unnecessary exponential branching.
- **Repeated immutable-string rebuilding:** replacing one position with slices creates increasingly large copies and can take $O(N^2)$ time.
- **No placeholders:** return the unchanged string, which already satisfies the guarantee.
- **Single placeholder:** any lowercase letter is valid.
- **Consecutive placeholders:** finalize them left to right so each new letter differs from its replacement neighbor.
- **Placeholder at an endpoint:** only the one existing neighbor restricts its replacement.
- **Same fixed letter around a placeholder:** choose any different letter, such as turning `a?a` into `aba`.
- **Multiple valid answers:** correctness depends on the completion rules, not on matching the example string exactly.
