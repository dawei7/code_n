## Function Contract

**Inputs**

- `words`: A nonempty array of equal-length lowercase English strings.

Let $n=\lvert\texttt{words}\rvert$, let $m$ be the common word length, and define the total number of input characters as

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert = nm.
$$

Each pair is determined by two distinct indices with the smaller index first. Equal string values at different indices remain distinct elements and may form a valid pair. A cyclic shift advances every character in one selected string by the same amount modulo 26.

**Return value**

Return an integer equal to the number of index pairs whose two strings can be made equal by uniform cyclic shifts.
