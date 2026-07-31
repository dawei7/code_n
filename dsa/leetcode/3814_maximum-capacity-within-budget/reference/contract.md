## Function Contract

**Inputs**

- `costs`: The purchase costs of the machines.
- `capacity`: The corresponding performance capacities; `capacity[i]` belongs to the same machine as `costs[i]`.
- `budget`: The exclusive upper bound on the total purchase cost.

Let $N=\lvert\texttt{costs}\rvert=\lvert\texttt{capacity}\rvert$. A valid choice contains zero, one, or two different indices. For a two-machine choice `{i, j}`, validity requires $i\ne j$ and `costs[i] + costs[j] < budget`; equality with `budget` is not allowed.

**Return value**

Return the maximum sum of capacities among all valid choices. Return `0` if no individual machine costs strictly less than `budget`.
