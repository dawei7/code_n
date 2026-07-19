## General
**Keep the best value for each next sign**

After processing a prefix, let `plus` be the best sum of a subsequence with an odd number of chosen elements, so its last element received a plus sign. Let `minus` be the best sum with an even number of chosen elements, including the empty subsequence with sum zero.

For each `value`, either skip it or append it. Appending to an even-length subsequence adds `value`, producing an odd length; appending to an odd-length subsequence subtracts `value`, producing an even length:

$$
\begin{aligned}
\textit{nextPlus} &= \max(\textit{plus},\ \textit{minus} + \textit{value}),\\
\textit{nextMinus} &= \max(\textit{minus},\ \textit{plus} - \textit{value}).
\end{aligned}
$$

Both transitions must read the previous states, not a state already updated for the same element, because a source element may be selected at most once.

**Why the two states are sufficient**

Future choices depend only on whether the next selected element receives a plus or minus sign and on the best sum available for that parity. Any smaller sum with the same parity can never lead to a better continuation, so it may be discarded. The transitions consider both possibilities—skip or select—for every element, and therefore preserve the optimum for each parity by induction over the prefix. The answer is `plus`, because all values are positive and an optimal non-empty subsequence can end after an added element.

## Complexity detail
Each of the $N$ values performs two constant-time state transitions, giving $O(N)$ time. Four scalar state values are sufficient, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **All-predecessor dynamic programming:** Store plus/minus states ending at every index and inspect all earlier indices for transitions; this is correct but takes $O(N^2)$ time and $O(N)$ space.
- **Greedy rise accumulation:** The answer can also be expressed through positive adjacent gains, but the two-state DP exposes the subsequence parity directly and generalizes more clearly.
- **One element:** The only useful choice adds that value, so it is the answer.
- **Strictly increasing input:** Selecting only the final, largest value is optimal.
- **Strictly decreasing input:** Alternating high and low selections can capture multiple gains.
- **Equal values:** Subtracting and re-adding the same value contributes zero, so duplicates need not be selected.
