## General

Each column can be optimized independently because an operation changes one cell and no condition compares cells from different columns. Fix a column and scan it from top to bottom while remembering the final value chosen for the preceding row.

Suppose the current original value is $x$ and the adjusted value above it is $p$. The current cell must finish at least at $p+1$, and increments cannot reduce $x$. Its smallest legal final value is therefore $\max(x,p+1)$. Add the difference between this value and $x$ to the answer, then carry the chosen value forward as the new predecessor.

This smallest legal choice is optimal at every row. Any valid solution must pay at least the same increment for the current cell. Choosing a larger value cannot help any later row; it only raises the lower bound that the next cell must exceed. Inductively, the scan gives every cell the least value compatible with the already-minimal prefix, so its column cost is minimal. Summing these independent minima gives the minimum for the entire matrix.

The implementation stores the adjusted predecessor instead of modifying `grid`. This preserves the caller's matrix while retaining exactly the state needed for the next comparison.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Every one of the $mn$ cells is examined once, so the running time is $O(mn)$. Apart from loop indices, the accumulated answer, and one predecessor value, the algorithm allocates no input-dependent storage, so its auxiliary space is $O(1)$.

The benchmark fixes one column and defines `size` as $m$. Its legal 12-, 24-, and 48-row tiers span 4x and contain only zeros, forcing the final column to become $0,1,\ldots,m-1$. The accepted method remains linear in $m$. A correct slower simulation performs each unit increment separately, requiring $1+2+\cdots+(m-1)=\Theta(m^2)$ loop iterations and failing only the scaling verdict.

## Alternatives and edge cases

- **Mutate the matrix in place:** Writing each adjusted value into `grid` makes the next comparison convenient and keeps $O(1)$ auxiliary space, but it unnecessarily changes the caller's input.
- **Simulate each increment:** Repeatedly add 1 until the inequality holds. This is correct, but its time depends on the answer and becomes quadratic on a flat column.
- **Process rows independently:** Comparing only original adjacent values is incorrect because an incremented predecessor may force a larger cascade farther down the column.
- **Single row:** Every column is already strictly increasing because there is no adjacent pair to violate the condition.
- **Already increasing column:** Every chosen value equals its original value and contributes zero operations.
- **Equal or decreasing values:** The current cell must become exactly one greater than the adjusted predecessor, not merely one greater than its own original value.
- **Independent columns:** Carry a separate predecessor while scanning each column; no adjustment in one column affects another.
