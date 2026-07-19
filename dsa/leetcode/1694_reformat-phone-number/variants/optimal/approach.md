## General
**Separate cleanup from block decisions**

Scan `number` once and retain only digits. Spaces and dashes carry no information after cleanup, so this produces the exact sequence that must appear in the answer. Keeping cleanup independent also prevents original separator positions from accidentally influencing the new grouping.

**Reserve a legal final suffix**

Maintain an index into the clean digits. While more than four digits remain, append the next three as a block and advance the index by three. Stopping at four or fewer is the crucial rule: consuming another triple from a four-digit suffix would strand one digit, which is forbidden.

At the stopping point, the contract guarantees at least two digits remain. A suffix of two or three is appended as one block. A suffix of four is split at its midpoint into two two-digit blocks. Joining the accumulated blocks with dashes produces exactly one separator between blocks and none at either end.

Every emitted three-digit prefix is required because more than four digits remained at that moment. The final case analysis is exhaustive over the only possible suffix lengths, and each branch creates only blocks of length two or three. Since cleanup and slicing preserve order and consume each digit exactly once, the result satisfies every formatting rule.

## Complexity detail
The cleanup scan examines the $N$ input characters once, and block construction copies each retained digit a constant number of times, for $O(N)$ time. The clean digit string, block list, and returned string together use $O(N)$ space.

## Alternatives and edge cases
- **Regular-expression cleanup:** replacing spaces and dashes and then applying the same suffix logic is also linear, but a direct character filter avoids regex machinery.
- **Always take triples greedily:** doing so when exactly four digits remain creates a forbidden one-digit final block.
- **Repeated immutable-string concatenation:** prepending or appending blocks one at a time may copy an increasing prefix repeatedly; collecting blocks and joining once avoids quadratic copying.
- **Two digits:** return one two-digit block with no dash.
- **Three digits:** return one three-digit block with no dash.
- **Four digits:** return exactly two two-digit blocks.
- **Original separators:** leading, trailing, adjacent, or mixed spaces and dashes are all discarded uniformly.
