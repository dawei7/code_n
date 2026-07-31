## General

Read `s` from left to right and use one bit for each lowercase English letter.
For a character `ch`, its bit position is `ord(ch) - ord("a")`. If that bit is
already set, the current position is the character's second occurrence, so
return `ch`. Otherwise, set the bit and continue.

**Why the first detected repeat is the answer**

The scan processes indices in strictly increasing order. Before visiting an
index, the mask records exactly the letters that appeared at earlier indices.
Therefore, the first character whose bit is already set is precisely the
character with the earliest second occurrence. Returning immediately is safe:
every unprocessed character has a later index and cannot have an earlier
second occurrence.

The contract guarantees a repeated letter, so the scan must return. Because
there are only 26 lowercase letters, the first repeat is encountered by the
27th inspected character at the latest.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Each inspected character performs a constant
number of bit operations, so the worst-case time is $O(n)$. The integer mask
contains exactly 26 possible flags and therefore uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Set of encountered letters:** A set gives the same $O(n)$ time and, over
  the fixed lowercase alphabet, $O(1)$ space; the bitmask makes that fixed
  bound explicit.
- **Repeated prefix search:** Checking every earlier position for each new
  character is correct but takes $O(n^2)$ time in the general string model.
- **Immediate duplicate:** For a string such as `"aa"`, the second character
  is returned without inspecting anything later.
- **Several repeated letters:** First-occurrence order is irrelevant; only the
  earliest second occurrence determines the answer.
- **Guaranteed repetition:** No fallback value is needed for a valid input.
