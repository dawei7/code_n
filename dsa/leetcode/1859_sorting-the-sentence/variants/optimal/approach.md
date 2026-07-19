## General
Split `s` at its spaces. The final character of each resulting token is its
original 1-based position, while every earlier character belongs to the word.
Because there are at most nine words, one decimal digit always contains the
entire position.

Allocate nine result slots. For each token, convert its final digit to a
zero-based index and store `token[:-1]` in that slot. If the sentence contains
$m$ tokens, the contract guarantees that positions $1$ through $m$ occur
exactly once, so those first $m$ slots become the original word sequence.
Joining them with single spaces restores precisely the requested sentence.

## Complexity detail
Splitting, slicing the marked words, and joining the answer process $O(S)$
characters in total. The result slots, split tokens, and returned string store
$O(S)$ characters. The fixed nine-element slot array itself is $O(1)$.

## Alternatives and edge cases
- **Sort marked words by their suffix:** sorting the tokens by the final digit
  is concise, but it adds comparison work that direct indexed placement does
  not need.
- **Repeated search by position:** scanning all tokens once for each expected
  digit reconstructs the same answer but performs redundant searches.
- A one-word sentence still carries the suffix `1`; remove it and return the
  remaining word without adding spaces.
- Uppercase and lowercase letters are word content and must be preserved
  exactly.
- The position is always one digit because the contract permits at most nine
  words; stripping more trailing characters would corrupt the word.
