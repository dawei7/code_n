## Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers.

Let $n=\lvert\texttt{nums}\rvert$. Each score is based only on positions $j$ with $i<j<n$. Equal values never qualify because the comparison is strict, even if a later value were otherwise eligible. Parity is determined by divisibility by $2$.

**Return value**

Return an integer array `answer` of length $n$, where `answer[i]` counts the indices $j$ to the right of $i$ for which `nums[j] < nums[i]` and exactly one of `nums[i]` and `nums[j]` is even.
