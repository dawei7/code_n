## General

Only adjacent drops obstruct non-decreasing order. For a pair $(a,b)$ with $a>b$, the right element and everything after it need a net increase of at least $a-b$ relative to the left element.

The source sums every positive adjacent drop:

$$
\sum_{i=0}^{n-2}
\max(\texttt{nums}[i]-\texttt{nums}[i+1],0).
$$

This is not merely a heuristic. The sum is both a lower bound on the cost of every possible operation plan and the cost of a concrete plan using suffix increments.

**What an operation does across array boundaries**

Consider the boundary between indices $i$ and $i+1$. Adding $x$ to a subarray can affect the difference between those two positions in only three ways:

- if the subarray contains both positions, both rise by $x$ and their difference is unchanged;
- if it contains neither, the difference is unchanged;
- if it begins at $i+1$, the right side gains $x$ relative to the left and the drop is reduced by $x$;
- if it ends at $i$, the left side gains $x$ relative to the right and the drop becomes worse by $x$.

An operation can help a particular drop boundary only when its left endpoint is exactly $i+1$.

Most importantly, one contiguous operation has only one left endpoint. Its cost $x$ can provide a positive relative increase across at most one boundary.

**The lower bound from every original drop**

Suppose

$$
d_i=\texttt{nums}[i]-\texttt{nums}[i+1]>0.
$$

To make the final pair non-decreasing, the total increments applied to index $i+1$ must exceed the total increments applied to index $i$ by at least $d_i$. Only operations starting at $i+1$ contribute positively to that relative amount. The sum of their $x$ values must therefore be at least $d_i$.

Different boundaries require operations with different start indices. A single operation cannot supply its same cost as a positive start contribution to two boundaries. Summing the independent requirements gives:

$$
\text{total operation cost}
\ge
\sum_{i:\,\texttt{nums}[i]>\texttt{nums}[i+1]}
\left(\texttt{nums}[i]-\texttt{nums}[i+1]\right).
$$

This is exactly the quantity returned by the source.

**A construction that reaches the bound**

For every boundary $i$ with positive drop $d_i$, perform one operation on suffix

$$
[i+1,n-1]
$$

with increment $x=d_i$.

The operation contributes $d_i$ to the total cost and raises the right side of boundary $i$ relative to its left side by exactly the required amount.

Why do these suffix operations not break another boundary? A suffix starting before a later boundary contains both endpoints of that later boundary and raises them equally. A suffix starting after an earlier boundary does not include either endpoint of that earlier boundary. Only the suffix beginning at $i+1$ changes the relative increment across boundary $i$.

Let $z_j$ be the total added to position $j$ by all these suffix operations:

$$
z_j=\sum_{t<j}\max(\texttt{nums}[t]-\texttt{nums}[t+1],0).
$$

Across boundary $i$:

$$
z_{i+1}-z_i
=
\max(\texttt{nums}[i]-\texttt{nums}[i+1],0).
$$

If the original pair drops, this difference exactly cancels the drop. If it does not drop, the difference is zero and its existing non-decreasing order remains.

Thus the constructed final array is non-decreasing and costs exactly the lower bound. The bound is therefore the true minimum.

**Example with overlapping suffixes**

For `nums = [3,3,2,1]`, positive drops are:

$$
\max(3-3,0)=0,
$$

$$
\max(3-2,0)=1,
$$

and

$$
\max(2-1,0)=1.
$$

The sum is two.

One construction:

1. Add 1 to suffix indices 2 through 3, producing `[3,3,3,2]`.
2. Add 1 to suffix index 3, producing `[3,3,3,3]`.

The total cost is $1+1=2$, matching the source.

For `[5,1,2,3]`, only the first boundary drops, by four. Adding 4 to suffix `[1,3]` gives `[5,5,6,7]` in one operation with total cost four.

**Why the number of operations is irrelevant**

The objective minimizes the sum of chosen $x$ values, not the operation count. An increment $x=5$ costs the same total as five identical unit-increment operations.

The proof reasons in units of increment cost. Grouping several units into one operation or splitting them does not change the objective, so the suffix construction may use one operation per positive drop without claiming that this is the fewest number of operations.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. `pairwise(nums)` generates the $N-1$ adjacent pairs lazily. The generator computes one subtraction, maximum, and addition per pair.

Time complexity is

$$
O(N).
$$

The source does not construct the final array or store the drops. The generator and running sum use

$$
O(1)
$$

auxiliary space.

The input is not modified. Python integers safely accumulate a total that may exceed one individual array value.

For $N=1$, there are no adjacent pairs. Summing the empty generator returns zero, correctly recognizing that a singleton is already non-decreasing.

## Alternatives and edge cases

- **Simulate the suffix construction:** Actually modifying every suffix proves feasibility but can cost $O(N^2)$; only the summed drop values are needed for the answer.
- **Raise each element to the previous final value:** A left-to-right greedy can compute final values, but counting element increments individually overcharges because one subarray operation raises many elements for one cost.
- **Count operations instead of total \(x\):** This solves a different objective; one large increment and many unit increments have different operation counts but identical requested cost.
- **Already non-decreasing array:** Every adjacent difference is nonpositive, so the sum is zero.
- **Equal neighbors:** They create no drop and require no cost.
- **Several consecutive drops:** Each boundary contributes independently, and nested suffix operations achieve their sum.
- **A later rise:** Suffix increments preserve the existing difference at boundaries where no operation starts, so a rise is not damaged.
- **Single element:** The empty adjacent-pair sum is zero.
- **Large values:** Differences up to $10^9-1$ and their total are handled exactly by Python integers.
- **Positive \(x\) requirement:** Zero-drop boundaries simply receive no operation; every constructed operation has strictly positive $d_i$.
- **Required helper:** Standalone execution needs `pairwise` from Python's `itertools` module.
- **Input preservation:** The source evaluates differences without changing `nums`.
