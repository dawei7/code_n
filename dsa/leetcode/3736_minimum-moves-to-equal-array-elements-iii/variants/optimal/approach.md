## General

Let $M = \max(\texttt{nums})$. Because a move can only increase an element, the final common value cannot be smaller than $M$. Choosing $M$ itself is feasible, so each value $x$ needs exactly $M-x$ moves.

Adding those independent deficits gives

$$
\sum_{x \in \texttt{nums}} (M-x).
$$

This total is minimal. Any common target greater than $M$ would add the same positive extra distance to every element, while a smaller target cannot be reached from the current maximum. The implementation therefore finds $M$ once and accumulates every deficit to it.

## Complexity detail

Finding the maximum and summing the deficits each scan the $n$ values once, so the running time is $O(n)$. Apart from scalar totals, the method allocates no storage that grows with the input, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort before choosing the target:** The last sorted value is the maximum, but sorting raises the running time to $O(n\log n)$ and is unnecessary.
- **Simulate individual moves:** Incrementing values one move at a time eventually reaches the same result but can take time proportional to the numeric answer rather than the array length.
- **Repeated maximum searches:** Recomputing the maximum for every element is correct but takes $O(n^2)$ time; one shared maximum is sufficient.
- **Already equal values:** Every deficit is zero, so the answer is `0` even though no array change is needed.
- **Single-element array:** Its sole value is already the common target, so the answer is also `0`.
