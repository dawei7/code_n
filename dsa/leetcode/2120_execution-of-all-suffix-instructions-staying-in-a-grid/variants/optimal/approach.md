## General

**Simulate each independent suffix**

Map each instruction to its row and column change. For every starting index
`start`, reset `row` and `column` to `startPos`, then scan instructions from
`s[start]` toward the end.

Apply the next displacement tentatively. If the new coordinate is outside
$[0,n-1]$ in either dimension, stop that suffix without increasing its count.
Otherwise the move is executable, so increment the count and continue. Append
the final count before resetting for the next starting index.

For a fixed suffix, the maintained coordinate is exactly the robot's position
after the counted instructions because each accepted move applies its stated
unit displacement. The scan stops precisely when the next move would leave the
grid or when no instruction remains, matching the two stopping rules.
Repeating this from the original position for every index therefore produces
each required answer independently.

## Complexity detail

Suffix $i$ contains $m-i$ instructions. In the worst case all remain inside
the grid, so the total number examined is
$\sum_{i=0}^{m-1}(m-i)=O(m^2)$. The returned list uses $O(m)$ space; excluding
that required output, the simulation uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recompute every candidate endpoint:** For each suffix and possible length,
  replay the suffix from its beginning to check the endpoint. This is correct
  but repeats prefixes and takes $O(m^3)$ time.
- **Prefix displacement range queries:** Represent movements as prefix
  coordinates and search for the first prefix leaving the translated row or
  column bounds. Segment-tree or offline structures can improve asymptotic
  time, but add substantial machinery beyond the bounded $m \le 500$ contract.
- A move that would leave the grid contributes zero and ends that suffix.
- Every suffix resets to `startPos`; positions reached by earlier suffix runs
  do not carry over.
- A one-cell grid rejects every movement instruction.
- If every remaining move stays inside, the answer equals the suffix length.
