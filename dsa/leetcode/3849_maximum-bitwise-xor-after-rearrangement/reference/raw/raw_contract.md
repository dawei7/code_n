## Function Contract

**Inputs**

- `s`: A binary string whose character positions cannot be changed.
- `t`: A binary string whose complete multiset of characters may be rearranged.

The two strings have the same length $N$. A valid arrangement uses every character of `t` exactly once. XOR is applied at corresponding positions, producing another binary string of length $N$.

Because every candidate result has the same length, comparing the represented integers is equivalent to comparing the result strings lexicographically, with `'1'` greater than `'0'`.

**Return value**

Return the length-$N$ binary string representing the maximum possible XOR value.
