## General

Let $n$ be the length of `nums`, let $m=\max(\texttt{nums})$, and let the modulus be $M=10^9+7$.

**One chosen value determines both arrays**

At index $i$, choosing `arr1[i] = v` forces `arr2[i] = nums[i] - v`. Non-negativity restricts $v$ to the interval from $0$ through `nums[i]`. It is therefore enough to count valid sequences of values for `arr1`; `arr2` is then unique.

Suppose the previous `arr1` value is $u$ and the current value is $v$. The first array requires $u \le v$. The second array requires

$$
\texttt{nums[i-1]}-u \ge \texttt{nums[i]}-v,
$$

which rearranges to $u \le v-(\texttt{nums[i]}-\texttt{nums[i-1]})$. Combining both upper bounds gives

$$
u \le v-\max(0,\texttt{nums[i]}-\texttt{nums[i-1]}).
$$

**Dynamic programming with prefix sums**

Store in `ways[v]` the number of valid prefixes whose last `arr1` value is $v$. Initially every value from $0$ through `nums[0]` forms one valid length-one prefix.

For each later index, build prefix sums of the previous row. For a current value $v$, the derived bound identifies a contiguous predecessor range starting at zero, so one prefix lookup yields the sum of all legal `ways[u]`. Values below the required increase have no predecessor and retain zero ways. Reduce every sum modulo $M$.

The state meaning is true initially. During a transition, the predecessor bound is exactly the conjunction of the two monotonicity conditions, so the prefix sum includes every valid extension once and excludes every invalid extension. By induction, the final states count precisely all valid `arr1` arrays, and hence all monotonic pairs. Summing the last row produces the answer.

## Complexity detail

Each of the $n$ positions uses at most $m+1$ states. Building a prefix row and then filling the next row both take $O(m)$ time, for $O(nm)$ total time. Only the previous and current rows plus one prefix array are retained, so auxiliary space is $O(m)$.

## Alternatives and edge cases

- **Direct dynamic-programming transition:** Summing all predecessors separately for every current value is correct but costs $O(nm^2)$ time.
- **Enumerate both arrays:** Once `arr1` is known, `arr2` is fixed; constructing both during search adds no freedom and grows exponentially with $n$.
- **Combinatorial shortcut for constant input:** A flat `nums` array admits a stars-and-bars count, but that formula does not handle changes between adjacent values.
- A length-one input has `nums[0] + 1` valid decompositions.
- A steep rise in `nums` forces `arr1` to increase enough that `arr2` does not increase.
- A decrease in `nums` adds no extra lower bound beyond `arr1` being non-decreasing.
- Some positive input profiles have zero valid pairs.
- DP values must be reduced modulo $10^9+7$ throughout, not only after unbounded accumulation.
