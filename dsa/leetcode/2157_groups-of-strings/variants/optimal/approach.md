## General

**Collapse each letter set into a bitmask**

Represent letters `a` through `z` by the 26 bits of an integer. Word order
then disappears, exactly matching the set-based operations. Multiple words may
produce the same mask, so create one disjoint-set node per distinct mask and
give that node a component weight equal to the mask's frequency.

**Join additions and deletions directly**

Adding or deleting one letter toggles exactly one bit. For every distinct mask,
toggle each of the 26 bit positions and union the two nodes whenever the
resulting mask exists. Addition and deletion are inverse views of the same
edge, so this single check covers both.

**Turn replacements into shared deleted forms**

Two equal-size masks are one replacement apart exactly when deleting one
present bit from each can produce the same intermediate mask. For every
present bit, compute that deleted form. Store the first node seen for each form
and union later nodes that produce it. Identical masks were already collapsed,
which also covers replacement by the same letter.

Each union therefore corresponds to an allowed direct connection. Conversely,
every allowed addition, deletion, or replacement is discovered by one of these
checks. Disjoint-set roots are consequently exactly the required groups.
Tracking root weights during union gives both the group count and largest
group size.

## Complexity detail

Let $n$ be the number of words. The alphabet has the fixed size $26$, so mask
construction and neighbor generation perform $O(n)$ work. Disjoint-set
operations add an inverse-Ackermann factor, giving $O(n\alpha(n))$ time and
$O(n)$ space for distinct masks, deleted forms, parents, and component weights.

## Alternatives and edge cases

- **Compare every pair:** Testing set differences for all word pairs is
  correct but takes $O(n^2)$ time.
- **Generate every replacement:** Trying every absent letter for every present
  letter performs up to $26^2$ lookups per mask; shared deleted forms reduce
  that to a single pass over present bits.
- Different strings such as `"ab"` and `"ba"` have the same letter-set mask
  and must both contribute to the component size.
- A replacement may choose the same letter, so identical masks are connected.
- Connectivity is transitive even when two endpoint words are not directly
  connected.
- Isolated words each contribute one group of size one.
