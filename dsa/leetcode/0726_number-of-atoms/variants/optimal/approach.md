## General
**Read multipliers before the units they affect**

Scan the formula from right to left. A run of digits is then encountered before the atom or closing parenthesis it multiplies. Parse the entire run in reverse place-value order and store it as the pending factor; when no digits precede a unit in the reverse scan, its factor is one.

**Track cumulative group multiplication**

Keep a stack whose top is the product of all multipliers for the currently active nested groups. On `)`, push the current product times the pending factor and reset that factor. On the matching `(`, pop. Thus every atom can be added directly to one global frequency map without constructing and repeatedly merging a map for each group.

**Recover complete atom names backward**

When a letter is reached, move left across all lowercase letters until the required uppercase first letter is found. That slice is one atom name. Add `pending factor * active group product` to its total, reset the pending factor, and continue before the uppercase character.

**Why every multiplier is applied exactly once**

Formula grammar places an optional number immediately after exactly one atom or parenthesized group. The reverse scan stores that number until it reaches that unit. Group factors stay on the multiplier stack precisely between their closing and opening parentheses, so they multiply exactly the enclosed atoms. Each atom occurrence is visited once and contributes through all and only its enclosing groups.

**Build the canonical output**

Sort the distinct atom names lexicographically. Append each name and append its decimal total only when the total is greater than one. This produces the unique required representation rather than preserving formula order.

## Complexity detail
Let `n` be the formula length, `A` the number of distinct atom names, and `d` the maximum parenthesis depth. Parsing consumes every character once for $O(n)$ time, and sorting the names costs $O(A \log A)$, for $O(n + A \log A)$ total time. The count map and multiplier stack use $O(A + d)$ space.

## Alternatives and edge cases
- **Stack of frequency maps:** push a new counter for each group and merge it into its parent on `)`; it is intuitive but deeply nested groups with many atoms can trigger repeated $O(A)$ merges and quadratic worst-case work.
- **Recursive descent:** parse a group into a returned counter; it mirrors the grammar, but merging returned counters has the same repeated-work risk unless counts are accumulated with a carried multiplier.
- **Expand repeated groups:** materialize every multiplied atom occurrence; numeric counts can make the expansion far larger than the input.
- **Implicit count:** an atom or group without following digits has multiplier one.
- **Multi-digit count:** all consecutive digits form one number, not separate factors.
- **Atom boundary:** an uppercase letter begins a name and its following lowercase letters belong to that same name.
- **Nested multiplication:** multiply all enclosing group factors, not merely the nearest one.
- **Count of one:** omit the numeral from the returned string.
- **Output order:** sort by the complete atom name, not by first character or appearance order.
