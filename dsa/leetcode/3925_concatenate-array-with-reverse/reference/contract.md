## Function Contract

**Inputs**

- `nums`: The integer array whose forward and reversed orders must be concatenated.

Let $n$ be `nums.length`.

**Return value**

Return a new array `ans` of length $2n$ satisfying

$$
\texttt{ans}[i] = \texttt{nums}[i]
\quad\text{and}\quad
\texttt{ans}[i+n] = \texttt{nums}[n-i-1]
$$

for every $0 \le i < n$.
