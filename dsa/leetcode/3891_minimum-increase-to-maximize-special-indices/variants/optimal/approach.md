## General

**Price each possible peak independently**

For an interior index $i$, define

$$
c_i=\max\left(0,\max(\texttt{nums[i-1]},\texttt{nums[i+1]})+1-\texttt{nums[i]}\right).
$$

This is exactly the number of increments needed to make $i$ special while leaving its neighbors unchanged. Increasing an unselected neighbor cannot help: it can only raise the threshold that a selected peak must exceed. Consequently, once a nonadjacent set of peak indices is chosen, its minimum cost is the sum of the corresponding $c_i$ values.

**Characterize every maximum-size peak set**

Adjacent indices cannot both be special, because each would have to be strictly greater than the other. The $n-2$ interior indices therefore form a path from which no two adjacent positions may be selected. Its maximum independent-set size is

$$
\left\lfloor\frac{n-1}{2}\right\rfloor.
$$

When $n$ is odd, the interior path has odd length and there is only one maximum-size choice: indices $1,3,5,\ldots,n-2$. Summing their costs gives the answer directly.

When $n$ is even, let $k=(n-2)/2$. Every maximum-size choice contains $k$ indices and has one of these forms for a split $t$ from $0$ through $k$:

$$
\{1,3,\ldots,2t-1\}\;\cup\;\{2t+2,2t+4,\ldots,2k\}.
$$

The set starts with an odd-index prefix and finishes with an even-index suffix; either part may be empty. This exhausts the possibilities because $k$ nonadjacent selections use $2k-1$ positions of a path with length $2k$, leaving exactly one unit of slack at a boundary or between two selections.

**Sweep the phase switch**

Start at $t=0$, whose chosen indices are all even interiors, and sum their costs. Advancing from split $t-1$ to split $t$ replaces index $2t$ with index $2t-1$, so update the running cost by adding $c_{2t-1}-c_{2t}$. The smallest running value over all $k+1$ splits is the optimum.

Each examined set has the maximum possible number of nonadjacent interior indices. Its summed local costs are both sufficient, by incrementing only those selected indices, and necessary, because each selected value must strictly exceed its unchanged neighbors. Taking the minimum over the complete parity characterization therefore gives the requested lexicographic optimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Computing the forced odd-index sum or sweeping the even-length split choices visits $O(n)$ indices and takes $O(n)$ time. The algorithm retains only running totals and loop indices, so it uses $O(1)$ auxiliary space.

The benchmark defines size as the array length and uses equal-valued arrays, for which every maximum-size configuration is legal and has the same nonzero cost. The sweep remains linear. A correct method that separately reconstructs and sums all $\Theta(n)$ maximum-size configurations performs $\Theta(n^2)$ work on these tiers.

## Alternatives and edge cases

- **Cardinality dynamic programming:** Tracking the minimum cost for every prefix and every selected-count target is correct, but its $\Theta(n^2)$ state transitions are unnecessary because maximum-cardinality sets have the parity-switch structure above.
- **Prefix and suffix sums:** Precomputing odd-prefix and even-suffix costs also evaluates every split in $O(n)$ time, but uses $O(n)$ auxiliary space instead of a single running total.
- **Already-special index:** Its local cost is zero and must stay eligible; no operation is needed merely because it is selected.
- **Strict comparison:** Matching the larger neighbor is insufficient. The selected value must reach one more than that neighbor, which is why the formula contains `+ 1`.
- **Endpoints:** Indices $0$ and $n-1$ cannot be selected, but they determine the local costs of indices $1$ and $n-2$.
- **Parity:** Odd $n$ has one maximum configuration, while even $n$ requires checking every possible phase switch rather than only the all-odd and all-even choices.
- **Changing non-peaks:** Increasing an unselected element never lowers any chosen peak's cost and can only make neighboring peak conditions harder.
- **Large totals:** A single local cost can reach $10^9$, and there can be nearly $5\times10^4$ selected indices, so fixed-width implementations need a 64-bit integer for the answer.
