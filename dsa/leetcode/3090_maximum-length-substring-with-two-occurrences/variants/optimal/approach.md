## General

**A valid range can be maintained instead of rediscovered.** Process `s` from left to right while keeping a window whose character frequencies are all at most two. A fixed table of 26 counts records exactly what is present between the current `left` and `right` boundaries.

**Only the newly added character can violate the rule.** Before extending the window, every stored frequency is valid. Adding `s[right]` changes just one count. If that count becomes three, advance `left`, decrementing counts for the removed characters, until the added character's count returns to two. Other characters cannot become invalid while the window shrinks.

After this repair, the window ending at `right` is the longest valid one with that endpoint. Any earlier left boundary would still contain all three occurrences that forced the repair, whereas moving farther right would only shorten a valid window. Record its length and continue.

The two boundaries never move backward. At each endpoint the maintained range is valid and is the longest valid range ending there; taking the maximum over all endpoints therefore yields the maximum length of any valid substring.

## Complexity detail

Let $n = \lvert s \rvert$. The right boundary visits each character once, and the left boundary removes each character at most once, so the total running time is $O(n)$. The frequency table has exactly 26 entries, independent of $n$, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate every starting position:** Extending a fresh candidate from each index is straightforward but repeats work across overlapping substrings and can take $O(n^2)$ time.
- **Check every complete substring:** Constructing and recounting all substrings adds another factor and can take $O(n^3)$ time.
- **Store only the last occurrence:** One position is insufficient because the window permits two copies; a third occurrence must exclude the oldest of three positions.
- **Shrink when a count reaches two:** Two occurrences are allowed, so shrinking at equality incorrectly discards valid characters.
- A string containing no character more than twice is valid in its entirety.
- A run of identical letters contributes at most two characters to any valid substring.
- The maximum may occur before the final character, so the answer must be updated at every right endpoint.
