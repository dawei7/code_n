## Function Contract

`solve(nums, k) -> int`

Let $n=\lvert\texttt{nums}\rvert$ and let $M=10^9+7$.

**Inputs**

- `nums`: A nonempty array of positive resource requirements, processed in index order.
- `k`: The positive number of resource units initially available and added by every operation.

Before processing element `i`, one or more operations may be performed only when the current resource is less than `nums[i]`. If the operation being performed is the $j$-th operation overall, it costs $j$. Processing the element then decreases the resource by `nums[i]`.

**Output**

Return the minimum total cost of all operations needed to process every element, reduced modulo $M$.
