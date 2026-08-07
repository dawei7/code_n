## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $n = \texttt{nums.length}$, let $V = \max(\texttt{nums})$, and define $N = \max(n,V)$.

At any moment, position `a` may be assigned the current value at position `b` exactly when `nums[a] % nums[b] == 0`. Operations are optional and may be repeated.

**Return value**

Return the minimum possible sum of all array elements. The result may exceed the range of a 32-bit signed integer.
