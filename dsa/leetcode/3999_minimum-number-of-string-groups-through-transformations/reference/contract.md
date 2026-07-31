## Function Contract

**Inputs**

- `words`: An array of nonempty strings containing lowercase English letters.

For one word `w`, its even-index sequence is `w[0], w[2], w[4], ...`, and its odd-index sequence is `w[1], w[3], w[5], ...`. Both sequences include every character of the indicated parity. Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

denote the total number of input characters.

**Return value**

Return an integer equal to the minimum number of groups in a partition where every two strings in the same group are equivalent.
