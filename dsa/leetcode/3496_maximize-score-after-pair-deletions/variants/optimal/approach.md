## General

Every allowed operation removes elements only from the two ends, so the elements not yet deleted always form one contiguous interval of the original array. The number of operations is fixed: $\lfloor(n-1)/2\rfloor$. Consequently, one element survives when $n$ is odd and two elements survive when $n$ is even.

The score equals the sum of all input values minus the sum of the final survivors. Maximizing the score is therefore equivalent to minimizing that remainder.

When $n$ is odd, any original element can be the lone survivor. To leave index $i$, exactly $i$ elements must disappear on its left and $n-i-1$ on its right. These counts have the same parity: remove boundary pairs from one side when both are even, or first remove one element from each side and then remove same-side pairs when both are odd. Thus the cheapest possible remainder is the minimum array value.

When $n$ is even, the survivors must be adjacent because the remaining interval is contiguous. Conversely, every adjacent pair can survive by the same parity construction applied to the counts outside that pair. The cheapest remainder is therefore the minimum sum of consecutive elements. One scan obtains the total and the appropriate minimum.

## Complexity detail

Let $n$ be the length of `nums`. Summing the array and finding either its minimum element or its minimum adjacent-pair sum takes $O(n)$ time. Only scalar accumulators are needed, so auxiliary space is $O(1)$.

Reading all $n$ input values is necessary because changing any unexamined value can change the total or the minimum survivor, giving an $\Omega(n)$ lower bound. The linear method is therefore asymptotically optimal. The benchmark varies $n$ and contrasts this scan with a correct interval dynamic program that explores $\Theta(n^2)$ reachable remainders.

## Alternatives and edge cases

- **Interval dynamic programming:** Recursing over the three possible deletions is correct with memoization but creates $O(n^2)$ interval states and storage.
- **Always take the locally largest removable pair:** A large immediate score can force an expensive remainder, so local deletion value is not a safe greedy criterion.
- **Sort the array:** Sorting loses adjacency, which is essential when an even-length array must leave two consecutive original elements.
- **One or two elements:** No operation is permitted, so the score is zero regardless of their values.
- **Odd length:** Exactly one element remains, and any position is reachable.
- **Even length:** Exactly two adjacent elements remain; a non-adjacent pair cannot be the final interval.
- **Negative values:** Removing a negative value lowers the score, so it can be advantageous to preserve the most negative reachable remainder.
- **Tied minima:** Any cheapest element or adjacent pair yields the same optimal score.
