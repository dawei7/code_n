## General
**Each character has exactly two semantic choices**

At position `i`, either preserve `word[i]` as a literal or abbreviate it. These independent binary choices give $2^{n}$ choice masks, matching the number of required outputs, so enumerating all `n`-bit masks generates the result without searching invalid candidates.

The delicate part is representing consecutive abbreviated positions. While reading one mask, carry a pending count rather than appending a number immediately. A set bit increments that count. A clear bit first appends the pending count when it is nonzero, then appends the current character and resets the count.

**Flush a pending run only when its boundary is known**

Suppose the choices for `word` abbreviate `w` and `o`, preserve `r`, then abbreviate `d`. The first two branches carry count two. Preserving `r` flushes `"2"` before `r`; reaching the end flushes the final `"1"`, producing `"2r1"`.

Delaying the number prevents adjacent numeric tokens such as `"11r1"`. Every maximal run of abbreviated positions is emitted once as its total length, which is the canonical generalized-abbreviation form.

**Choice masks are a bijection with abbreviations**

Every mask selects one subset of positions to abbreviate. Pending-count flushing converts each maximal selected run to its length and preserves every unselected character, so the constructed string is valid.

Conversely, any generalized abbreviation uniquely identifies which source positions its numeric runs replace and which positions its literal characters preserve. Those choices define exactly one mask. Different masks cannot produce the same canonical abbreviation, so all $2^{n}$ valid results appear exactly once.

## Complexity detail
There are $2^{n}$ masks, and converting one mask can inspect and materialize $O(n)$ characters, giving $O(n 2^n)$ total time and output space. The pieces for the current abbreviation use $O(n)$ auxiliary space beyond the returned list.

## Alternatives and edge cases
- **Backtracking with a pending count:** also achieves $O(n 2^n)$ time and avoids materializing invalid candidates.
- **Emit a separate number for every abbreviated character and normalize later:** creates duplicate noncanonical candidates and can grow substantially faster than the required output.
- **Choose arbitrary substring lengths recursively:** must prevent adjacent abbreviation blocks or it generates the same abbreviation through several partitions.
- Repeated source letters do not merge; they occupy distinct positions. A one-character word has exactly its literal form and `"1"`.
