## Description

You are given an array of strings `words`. For any string `s`, form `E` from all characters at even indices, in their original order, and form `O` from all characters at odd indices. A transformation independently cyclically shifts `E` and `O` to the right by any numbers of positions, including zero, then places their characters back into the corresponding even and odd positions of `s`.

Two strings are equivalent when one can become the other through a single transformation. Partition `words` into as few groups as possible. Every input string must belong to exactly one group, and every pair of strings placed in the same group must be equivalent. Return the minimum possible number of groups.
