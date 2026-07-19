## General
**View the sentence as one cyclic character stream**

Join the words with spaces and add one trailing space. Let `position` count characters consumed from infinitely repeated copies of this stream. At the start of each row, `position % L` identifies the next sentence character, where `L` is the cyclic string length.

**Advance by a full row, then restore a word boundary**

Tentatively add `cols`. If the next cyclic character is a space, consume it and begin the next row after that separator. Otherwise move backward until the character just before `position` is a space. This discards the partial word that cannot fit, retreating by at most the maximum word length `w`.

**Detect repeated row-start states**

The next row transition depends only on `position % L`. Store the row number and absolute position the first time each offset appears. When it repeats, the intervening rows and consumed characters form a deterministic cycle; skip as many whole copies of that cycle as the remaining screen height permits.

**Why the character count gives complete sentences**

Every accepted advance ends immediately after a whole word and its separator, so the consumed cyclic stream exactly represents legal placements. One complete stream length corresponds to one sentence. Therefore `floor(position / L)` after all rows is precisely the number of complete repetitions.

## Complexity detail
At most $\min(r,L)$ distinct row-start offsets are processed before rows finish or a cycle repeats. Each boundary correction retreats at most `w` characters, for $O(\min(r,L)w)$ time. The state map and cyclic sentence text use $O(L)$ space.

## Alternatives and edge cases
- **Place words directly on every row:** is simple but may examine $O(rc)$ short words when both dimensions are large.
- **Precompute a transition for every starting word:** gives $O(s + r)$ row simulation after transition construction, where `s` is sentence word count.
- **Build each rendered row as text:** wastes memory because only the next word index and completed count matter.
- A word that exactly reaches the final column fits.
- Words may not be split between rows.
- A one-word sentence can complete several times on one row.
- Spaces exist only between placed words, never before the first word of a row.
