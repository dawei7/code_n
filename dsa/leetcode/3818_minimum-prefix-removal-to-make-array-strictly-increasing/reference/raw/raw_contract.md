## Function Contract

**Inputs**

- `nums`: A non-empty array of integers.

Let $N=\lvert\texttt{nums}\rvert$. Removing a prefix of length $k$ leaves `nums[k:]`; $k=0$ denotes the empty prefix. A remaining array is strictly increasing exactly when every adjacent pair satisfies `nums[j] < nums[j + 1]` within that suffix. Equal neighbors do not satisfy the condition.

A solution always exists: removing the first $N-1$ elements leaves one element, which is strictly increasing. Therefore the minimum answer lies between $0$ and $N-1$ inclusive.

**Return value**

Return the smallest prefix length whose removal leaves a strictly increasing array.
