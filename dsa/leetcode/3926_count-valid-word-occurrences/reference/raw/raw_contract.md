## Function Contract

**Inputs**

- `chunks`: The ordered string pieces that are concatenated directly to form `s`.
- `queries`: Valid word strings whose complete-word occurrence counts are requested.

Let

$$
C = \sum_{x \in \texttt{chunks}} \lvert x \rvert
\quad\text{and}\quad
Q = \sum_{q \in \texttt{queries}} \lvert q \rvert.
$$

Hyphen classification uses neighboring characters in the fully concatenated `s`, including neighbors that originated in different chunks.

**Return value**

Return an integer array `ans` with `ans[i]` equal to the number of maximal words in `s` that exactly equal `queries[i]`.
