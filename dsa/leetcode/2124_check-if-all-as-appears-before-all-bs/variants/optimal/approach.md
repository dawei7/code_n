## General

**A violation creates an adjacent `ba` boundary**

A valid string has the form `a...ab...b`: once the first `b` appears, no later
position may contain `a`. If this rule is violated, consider the first `a`
that occurs after some `b`. Its immediately preceding run must begin after a
`b`, so somewhere before that `a` the adjacent substring `ba` occurs.

Conversely, any adjacent `ba` directly places an `a` after a `b` and violates
the required global order. The condition is therefore equivalent to the
absence of `ba`, which can be checked in one scan.

## Complexity detail

Searching the $n$-character string for a fixed two-character pattern takes
$O(n)$ time. The check uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Track whether a b has appeared:** Scan characters and reject an `a` after
  setting a `seen_b` flag. This is the same $O(n)$ time and $O(1)$ space.
- **Compare every a-b pair:** Check that each `a` index is smaller than every
  `b` index. This is correct but may take $O(n^2)$ time.
- A string containing only `a` is valid because there is no `b`.
- A string containing only `b` is valid because there is no `a`.
- The shortest invalid string is `ba`.
- One late `a` after a long b-block is sufficient to make the answer false.
