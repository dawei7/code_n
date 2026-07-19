## General
**Express the final load as a prefix transition**

Let `dp[i]` be the minimum travel count after delivering the first `i` boxes and returning to storage. A final load that begins at index `j` and ends just before `i` is legal exactly when $i-j \le \texttt{maxBoxes}$ and its prefix-sum weight does not exceed `maxWeight`.

Create `changes[k]` for box index `k`: the number of adjacent destination changes from box 0 through box `k`, with `changes[0] = 0`. The loaded segment from `j` through `i-1` crosses `changes[i - 1] - changes[j]` port boundaries. It also needs one movement from storage to its first port and one back to storage, so

$$
\texttt{dp[i]} = \texttt{changes[i-1]} + 2
  + \min_j\left(\texttt{dp[j]} - \texttt{changes[j]}\right)
$$

over all capacity-feasible starts `j`. Subtracting `changes[j]` correctly excludes the boundary between box `j - 1` and the new load's first box; the ship returned to storage at that split.

**Turn feasibility into a sliding interval**

As `i` increases, legal starts form a contiguous suffix of earlier indices. A start falls out forever once the box count is too large. Because every weight is positive, it also falls out forever once the prefix-weight difference exceeds `maxWeight`. Remove such indices from the front of a deque.

**Keep only undominated transition values**

Among feasible starts, the recurrence needs the minimum `dp[j] - changes[j]`. Store candidate indices in non-decreasing order of that value. Before appending a new index, remove candidates from the back while their value is at least the new value: they can never be preferable, and they expire no later because they are older. The deque front is therefore the best legal start for the next state.

Every possible schedule ends with some capacity-feasible consecutive load, so the recurrence considers its preceding optimal prefix. Conversely, combining a recorded prefix schedule with any feasible transition constructs a legal schedule whose added travel is counted exactly. The deque removes only expired starts or starts dominated in both value and lifetime, so its front preserves the recurrence minimum. Induction over `i` proves `dp[n]` is optimal.

## Complexity detail
Prefix arrays and DP states take $O(n)$ space. Each candidate index enters the deque once, leaves its front at most once, and leaves its back at most once. All prefix and transition work is therefore $O(n)$ time, with $O(n)$ auxiliary space overall.

## Alternatives and edge cases
- **Quadratic dynamic programming:** scan every feasible start for every prefix; it uses the same recurrence but takes $O(n^2)$ time when capacities allow long batches.
- **Segment tree or heap:** range-minimum or lazy-expiration structures can evaluate transitions in $O(n \log n)$ time, but the feasible interval's monotone movement permits a linear deque.
- **Greedily fill every load:** maximizing each batch size can miss a better split at a port-run boundary and is not generally optimal.
- **Repeated destination:** consecutive boxes for the same port add weight and box count but no port-to-port movement.
- **Both limits apply:** a candidate start must satisfy the box-count and weight constraints simultaneously.
- **Single box:** its only schedule moves storage to its port and back, for a result of two.
- **Final return:** the last batch must return to storage just like every earlier batch.
