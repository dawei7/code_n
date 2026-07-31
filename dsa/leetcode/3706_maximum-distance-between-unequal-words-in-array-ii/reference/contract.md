## Function Contract

**Inputs**

- `words`: An array of lowercase English words.

For a valid pair, the indices satisfy $0\le i<j<\lvert\texttt{words}\rvert$ and `words[i] != words[j]`. Distance counts both endpoints, so adjacent unequal words have distance $2$, not $1$.

**Return value**

Return the maximum value of $j-i+1$ among all valid pairs. If every entry is equal—or the array has only one entry—return `0`.
