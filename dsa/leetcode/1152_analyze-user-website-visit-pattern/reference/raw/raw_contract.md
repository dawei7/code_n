## Function Contract

**Inputs**

- `username`: A list of lowercase user names, one for each visit record.
- `timestamp`: A list of visit times aligned with `username`.
- `website`: A list of lowercase website names aligned with the other two lists.

All three lists have the same length $m$. Each complete visit tuple is unique, but individual timestamp values are not promised to be unique. Chronological pattern order therefore requires three strictly increasing visit times.

For a user $u$ with $\ell_u$ records, define the total number of candidate visit triples by

$$
C = \sum_u \binom{\ell_u}{3}.
$$

The input guarantees that at least one user has visited at least three websites.

**Return value**

- A list containing the three website names of the maximum-score pattern, with lexicographic order resolving a score tie.
