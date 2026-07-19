## General
**Reduce the array to its remaining signed gap**

First sum `nums`. Only the difference between that total and `goal` matters after this point: the individual existing values cannot be changed. Let

$$
D = \left\lvert \texttt{goal} - \sum_{x \in \texttt{nums}} x \right\rvert.
$$

The sign tells whether added values must increase or decrease the sum, while $D$ is the magnitude they must collectively supply.

**Derive an unavoidable lower bound**

One added element can change the sum toward the goal by at most `limit`. Therefore $k$ added elements can cover at most $k\cdot\texttt{limit}$ units of the gap. Any valid answer must satisfy

$$
k \ge \left\lceil \frac{D}{\texttt{limit}} \right\rceil.
$$

This proves that fewer elements cannot work.

**Show that the lower bound is attainable**

Use values with magnitude `limit` and the required sign until less than `limit` of the gap remains. If the remainder is nonzero, one final value equal to that signed remainder completes the sum and still satisfies the bound. When $D=0$, no value is needed.

Thus the lower bound is always constructible, making the minimum count $\lceil D/\texttt{limit}\rceil$. Integer arithmetic computes it as `(D + limit - 1) // limit`.

## Complexity detail
Computing the current sum scans all $n$ values once, taking $O(n)$ time. The difference and ceiling division take constant additional time. Only scalar totals are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Repeatedly append maximal values:** Simulating each addition reaches the same answer but may take up to the returned count rather than computing it directly.
- **Dynamic programming over sums:** This treats the added values like a subset-sum problem, but arbitrary bounded integers make the simple magnitude bound exact; DP is unnecessary and potentially enormous.
- **Already at the goal:** When $D=0$, the ceiling is zero and no element should be appended.
- **Nondivisible gap:** A positive remainder requires one final partial-magnitude value.
- **Negative correction:** The same absolute-gap formula applies; only the conceptual sign of the constructed values changes.
- **Unit limit:** Each addition changes the sum by at most one, so the answer equals $D$.
- **Large totals:** Summing up to $10^5$ values of magnitude $10^6$ can exceed 32-bit range, so fixed-width implementations need a sufficiently wide integer type.
