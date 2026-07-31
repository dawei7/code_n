## General

**Identify boundaries that rotations cannot repair**

A rotation never moves a value across a block boundary. A cut before position $b$ can therefore occur in a successful partition only when every value on its left is no greater than every value on its right:

$$
\max(\texttt{nums}[0:b]) \le \min(\texttt{nums}[b:n]).
$$

This condition also suffices to give the two sides their correct places in the globally sorted array. Compute every such good cut in linear time from prefix maxima and suffix minima. A candidate length $k$ is rejected immediately if any proper multiple of $k$ is not a good cut.

**Recognize a sortable circular block**

View one fixed block as a circle, including the edge from its last value back to its first. A block is a cyclic rotation of a non-decreasing sequence exactly when this circle has at most one strict descent.

If a rotation is sorted, all its adjacent edges are non-decreasing and the only possible circular descent is the wrap from its maximum back to its minimum. Conversely, if the circle has one descent, starting immediately after that edge visits every value in non-decreasing order. If it has no strict descent, going all the way around forces all values to be equal, so every rotation is already non-decreasing.

**Enumerate only possible lengths**

Generate the divisors of $n$ in paired form up to $\sqrt n$. For each divisor $k$, first verify its required cuts and then count circular descents inside every block of length $k$. Add $k$ precisely when all cuts and blocks pass.

The two tests are jointly sufficient: every block can be rotated into its own sorted order, and every boundary places the entire left prefix no later than the entire right suffix. Concatenating those rotated blocks is therefore globally non-decreasing. They are also necessary because successful rotations preserve every block's values and circular order.

## Complexity detail

Let $D$ be the number of positive divisors of $n$. Prefix/suffix preprocessing takes $O(n)$ time. Every divisor examines at most $n$ cuts and circular edges, so all candidates take $O(nD)$ time; the $O(\sqrt n)$ divisor enumeration is dominated by that bound. The cut and suffix arrays use $O(n)$ space, while the divisor list uses $O(D) \subseteq O(n)$ space.

The benchmark defines size as the length $N$ of a strictly descending array. The accepted method performs its linear preprocessing and divisor checks, while a correct direct method that materializes all $k$ rotations of a length-$k$ block performs $\Theta(N^2)$ list work for the divisor $k=N$.

## Alternatives and edge cases

- **Materialize every cyclic rotation:** Comparing each rotated block with its sorted form is straightforward, but a block of length $k$ costs $O(k^2)$ and the full-length divisor makes the method quadratic.
- **Sort and compare block multisets:** Sorting establishes which values belong in each block, but it still needs a separate circular-order check and adds avoidable $O(n\log n)$ work per candidate in a direct implementation.
- **Rolling hashes for rotations:** String-matching-style hashes can locate a sorted block inside two copies of itself, but collision handling and repeated block sorting make this more complicated than counting strict descents.
- **Length one:** Singleton blocks never change anything, so $k=1$ is sortable exactly when the original array is already non-decreasing.
- **One full block:** For $k=n$, there are no proper block boundaries; the entire answer depends on whether the array has at most one circular descent.
- **Equal values:** Equality is not a descent, and a good boundary deliberately permits the same value on both sides.
- **Already sorted input:** Every divisor is sortable without rotating any block, so all divisors contribute to the answer.
