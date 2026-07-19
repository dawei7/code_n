## General
**Parse positions rather than punctuation:** Scan `s` from left to right. A fixed letter becomes a one-choice position. On an opening brace, locate its matching closing brace, split the interior on commas, and store the alternatives as one position.

**Sort choices before expansion:** Sort every brace position's alternatives. Fixed positions are already trivially sorted. This makes the depth-first traversal visit complete words in lexicographic order, so no separate global result sort is necessary.

**Build one character per position:** Backtrack over the parsed positions, appending each available choice and removing it after the recursive call. Reaching position $L$ yields one complete expansion.

Every expansion selects exactly one option from each parsed position, so each generated word is valid. Conversely, every valid independent selection corresponds to one unique root-to-leaf backtracking path and is generated once. At the earliest position where two generated words differ, the traversal exhausts the smaller sorted choice first, proving output order is lexicographic.

## Complexity detail
Parsing takes $O(n)$ time. Producing $R$ strings of length $L$ requires $O(RL)$ time and output space. Parsed groups and the active recursion path use $O(n+L)$ additional storage, which is covered by $O(n+RL)$ total space.

## Alternatives and edge cases
- **Generate then sort globally:** It is correct, but sorting $R$ complete strings adds $O(R\log R)$ comparisons after generation.
- **Quadratic insertion sort:** Sorting expansions by repeated shifting is correct but can take $O(R^2L)$ time when generation order is reversed.
- **Breadth-first Cartesian product:** Expand a list of prefixes group by group. It has the same output-sensitive bound but stores intermediate prefix sets explicitly.
- **No braces:** Return a one-element list containing `s`.
- **Adjacent groups:** Choose independently from each group; no fixed separator is implied.
- **Unsorted alternatives:** Sort them before traversal to guarantee lexicographic output.
- **Fixed prefix or suffix:** Preserve it in every expansion.
