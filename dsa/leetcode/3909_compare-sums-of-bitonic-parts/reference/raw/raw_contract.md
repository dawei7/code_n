## Function Contract

**Inputs**

- `nums`: A bitonic integer array that is strictly increasing up to one peak and strictly decreasing after it.

Let $p$ be the unique peak index. Strict increase means `nums[i] < nums[i + 1]` for every $0\le i<p$, while strict decrease means `nums[i] > nums[i + 1]` for every $p\le i<n-1$. Define the two inclusive sums as

$$
A=\sum_{i=0}^{p}\texttt{nums[i]}
\qquad\text{and}\qquad
B=\sum_{i=p}^{n-1}\texttt{nums[i]}.
$$

The peak value `nums[p]` appears once in each sum.

**Return value**

Return `0` if $A>B$, return `1` if $B>A$, and return `-1` if $A=B$.
