## General

**Measure the remaining change at every position.** Define $d_i = \texttt{target[i]} - \texttt{nums[i]}$. A positive value needs increment operations, a negative value needs decrement operations, and its magnitude is the number of unit layers that must cover that position.

At the first position, all $\lvert d_0\rvert$ layers must begin there. For every later position, compare its demand with the previous demand:

- If $d_{i-1}$ and $d_i$ have the same nonzero sign, up to $\min(\lvert d_{i-1}\rvert, \lvert d_i\rvert)$ existing layers can extend across the boundary. Only an increase of the magnitude starts new operations, contributing $\max(0, \lvert d_i\rvert - \lvert d_{i-1}\rvert)$.
- If their signs differ, or the previous demand is zero, no earlier operation has the direction needed at position $i$. All $\lvert d_i\rvert$ layers must start anew.

This gives a left-to-right scan that stores only the previous difference and the accumulated answer.

**Why this count is minimal.** At each boundary, every newly required layer counted above must start at or after that boundary: extending an opposite-direction layer would move an element away from its target, and there are not enough same-direction layers on the left to cover a magnitude increase. This is a lower bound on any solution. It is attainable by extending every reusable same-direction layer and starting exactly the counted number of additional intervals. Thus the sum is both achievable and unavoidable.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each pair of corresponding elements is examined once, so the running time is $O(n)$. The scan keeps a constant number of integers and uses $O(1)$ auxiliary space.

The returned count can exceed 32-bit range because both $n$ and an individual difference can be large; the mathematical answer should be accumulated in a wide integer type.

## Alternatives and edge cases

- **Simulate unit-height interval layers:** Repeatedly finding and applying a shared layer is correct but can take $O(n^2)$ time on a strictly increasing difference run.
- **Monotonic-stack decomposition:** A stack can organize rising and falling layers, but the adjacent-difference observation yields the same count with less state.
- Equal adjacent differences reuse every active layer and add no operation.
- A decrease in magnitude with the same sign ends some intervals but starts none.
- A zero difference breaks all active layers; a later nonzero demand starts fresh.
- A sign change prevents sharing because one operation has only one direction.
- Arrays that are already equal require zero operations.
- A one-element array needs exactly the absolute difference of its two values.
