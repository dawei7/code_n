## General
**Build the cheapest shape for a proposed peak**

Fix a candidate target value $p$. To minimize the total array sum, values on each side should decrease by exactly one per step until reaching one, then remain one. Any larger neighbor would consume extra budget without helping the target, while any faster decrease would violate the adjacent-difference bound.

**Sum each slope arithmetically**

For a side of length $\ell$, the values begin at $p-1$. If the descending sequence remains positive across the whole side, sum its $\ell$ terms as an arithmetic progression. Otherwise sum $p-1,p-2,\ldots,1$ and add one for each remaining position. Adding both sides and the peak gives the minimum sum required for $p$ in constant time.

**Binary-search the last feasible peak**

If peak $p$ is feasible, every smaller positive peak is also feasible. If $p$ exceeds the budget, every larger peak does as well. Binary-search this monotone predicate over $[1,\texttt{maxSum}]$, retaining the largest candidate whose minimum required sum does not exceed `maxSum`.

The constructed mountain proves sufficiency because it is itself a valid array whenever its sum fits. Its pointwise-minimal slopes prove necessity because every valid array with peak $p$ must spend at least that much. The final feasible binary-search boundary is therefore exactly the maximum possible target value.

## Complexity detail
Each feasibility check uses a constant number of arithmetic operations. Binary search performs $O(\log\texttt{maxSum})$ checks, so total time is $O(\log\texttt{maxSum})$. Only scalar bounds and sums are stored, requiring $O(1)$ space.

## Alternatives and edge cases
- **Construct the candidate array:** Explicitly filling both slopes takes $O(n)$ per check and is impossible when $n$ approaches $10^9$.
- **Increment the peak one at a time:** It is correct but may require $O(\texttt{maxSum})$ feasibility steps.
- **Target at an edge:** One side has length zero and contributes no sum.
- **Slope reaches one early:** Remaining positions contribute one each; they must not be treated as zeros.
- **Slope never reaches one:** Sum exactly the required number of descending terms rather than the full sequence to one.
- **Minimum budget:** When `maxSum == n`, every element must be one and the answer is `1`.
- **Single position:** The peak equals `maxSum`.
