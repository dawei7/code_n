## Function Contract

**Inputs**

- `words`: A nonempty array of lowercase English strings.

A candidate uses two distinct indices $i<j$. The candidate is valid only when `words[i] != words[j]`, and its distance is $j-i+1$, not merely the index difference.

**Return value**

Return the maximum distance among all valid pairs, or `0` when no unequal pair exists.
