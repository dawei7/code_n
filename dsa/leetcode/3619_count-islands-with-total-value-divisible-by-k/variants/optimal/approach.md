## General

Scan every matrix position. When a positive cell has not yet been visited, it begins one new island traversal. Push it onto an explicit stack and negate its value immediately. Negation distinguishes discovered land from both undiscovered positive land and zero-valued water, preventing duplicate pushes without allocating a separate visited matrix.

Pop cells until the stack is empty. Add each original positive value to the component total modulo `k`; because visited values are stored negated, subtract the stored value. Examine only the four horizontal and vertical neighbors, marking and pushing each positive neighbor. Once the stack empties, the traversal has reached every cell in that maximal island and no cell outside it. Increment the answer exactly when the accumulated residue is zero.

Each positive cell is assigned to the first traversal that discovers it and is then non-positive forever. Thus no island is split or counted twice. Modulo accumulation is sufficient because a sum is divisible by `k` exactly when its residue is zero. The app adapter returns zero directly for an all-water matrix before scanning individual cells.

## Complexity detail

Let the matrix have $m$ rows and $n$ columns. Every cell is scanned once, and every land cell is pushed and popped once while checking four neighbors, giving $O(mn)$ time. The explicit stack can contain $O(mn)$ cells in the worst case, so auxiliary space is $O(mn)$. The grid itself is modified in place to store visitation state.

The benchmark uses one all-land island of $S=mn$ cells. The accepted traversal visits it once. A calibrated correct alternative starts a fresh flood fill from every land cell and counts the component only from its lexicographically smallest coordinate, performing $O(S^2)$ work.

## Alternatives and edge cases

- **Separate visited matrix:** It preserves the input and has the same asymptotic bounds, but requires another $O(mn)$ Boolean structure.
- **Recursive depth-first search:** It is concise but an island of up to $10^5$ cells can exceed the language recursion limit.
- **Repeated flood fills:** Recomputing a component from each of its cells is correct with careful canonical counting but can take $O((mn)^2)$ time.
- **Diagonal contact:** Diagonal neighbors belong to separate islands unless a horizontal or vertical path connects them.
- **All water:** There are no islands, so return `0`.
- **`k = 1`:** Every positive island total is divisible, so count all islands.
- **Single-cell island:** Count it exactly when that cell value is divisible by `k`.
- **Large component sum:** Accumulating only the residue avoids unnecessary growth and preserves divisibility.
