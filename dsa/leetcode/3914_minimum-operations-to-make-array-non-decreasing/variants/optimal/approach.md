## General

Consider a boundary between `nums[i]` and `nums[i + 1]`. If the left value exceeds the right by $d=\texttt{nums[i]}-\texttt{nums[i+1]}>0$, the right side must gain at least $d$ more total increment than the left side. An operation can improve this boundary only when its selected subarray begins at `i + 1`; its value `x` then contributes `x` toward that required difference. Because each operation has only one starting boundary, the positive deficits at different boundaries require separate cost. This gives the lower bound

$$
\sum_{i=0}^{n-2} \max(0,\texttt{nums[i]}-\texttt{nums[i+1]}).
$$

That lower bound is attainable. For every positive original drop at boundary `i`, add exactly its difference to the suffix `[i + 1..n - 1]`. A suffix operation changes the difference only across its starting boundary; every later adjacent pair has both elements increased equally. Therefore these suffix operations independently remove all original drops without undoing one another, and their total cost equals the lower bound.

The answer is consequently the sum of all positive adjacent drops. Scan neighboring pairs once and accumulate `left - right` only when `left > right`.

## Complexity detail

The scan visits each adjacent pair once, taking $O(n)$ time. Apart from the running total and the current pair, it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Physically increment each suffix:** Applying the constructive suffix operations to an array proves attainability, but touching every element of every suffix takes $O(n^2)$ time on a decreasing array.
- **Optimize a final array:** Dynamic programming can choose non-decreasing final values and account for range-increment starts, but it stores far more state than the boundary lower bound requires.
- **Already non-decreasing:** No adjacent pair has a positive drop, so the minimum cost is `0`.
- **Equal neighbors:** Equality already satisfies the target relation and contributes nothing.
- **Single element:** There is no adjacent boundary and no operation is needed.
- **Large result:** Up to $n-1$ drops may each approach $10^9$, so fixed-width implementations need a 64-bit accumulator.
- **Cost versus operation count:** One operation with a large `x` costs that full value; combining unit increments does not reduce the total.
