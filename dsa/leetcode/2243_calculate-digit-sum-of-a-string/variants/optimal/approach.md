## General

**Simulate exactly one round at a time**

While the current string is longer than `k`, visit its characters from left to
right in slices of at most `k`. Convert the digits in each slice to integers,
add them, and append the decimal representation of that sum to a fresh list.
Joining the list produces exactly the string specified for the next round:
every input character belongs to one consecutive group, group order is
preserved, and no separator or padding is introduced.

Replacing the current string only after all groups have been processed is
important. It prevents output digits from one group from being consumed during
the same round. When the loop stops, the current length is at most `k`, which
is precisely the required stopping condition, so that current string is the
answer.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ initially. One round takes time proportional to
the current string length. For `k` greater than two, every group produces
fewer than `k` output digits, giving constant-factor contraction. For `k = 2`,
a group can produce two digits, but any such result is between `10` and `18`;
in the next round its two digits sum to one digit. Thus the length contracts by
a constant factor over every pair of rounds. The total number of characters
processed is a geometric series bounded by $O(n)$.

The current and next strings together contain $O(n)$ characters, so auxiliary
space is $O(n)$.

## Alternatives and edge cases

- **Repeated string concatenation:** Appending each group result directly to an immutable string is correct, but can repeatedly copy the growing result and degrade to quadratic time.
- **One global digit sum:** Summing all digits loses the required group boundaries and can produce a different intermediate string and answer.
- **Update in place during a round:** Newly emitted digits must not participate until the next complete round.
- **Initial length at most `k`:** No transformation occurs; return `s` unchanged.
- **Short final group:** Sum all of its available digits even though it contains fewer than `k` characters.
- **Zero-sum groups:** Each becomes exactly one `"0"`, so multiple groups can preserve multiple zero characters.
