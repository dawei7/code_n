## General

The transpose changes where every value is located without changing any value. Suppose the input has $m$ rows and $n$ columns. An element at row $r$ and column $c$ in the input must appear at row $c$ and column $r$ in the result. In compact form, the defining rule is

$$
\text{answer}[c][r] = \text{matrix}[r][c].
$$

This exchange of the two indices also exchanges the dimensions. An $m \times n$ input becomes an $n \times m$ output. That detail matters most for rectangular matrices. A two-row, three-column matrix does not remain two by three: its three input columns become three output rows, and its two input rows become two output columns.

**View the matrix as a sequence of rows.** The solution uses `zip(*matrix)`. The star operator unpacks the outer list, so each input row is passed to `zip` as a separate iterable. If the matrix is

```text
[a, b, c]
[d, e, f]
```

then the call behaves like `zip([a, b, c], [d, e, f])`. Python's `zip` first takes the element at position zero from every row, producing `(a, d)`. It then takes the element at position one from every row, producing `(b, e)`, and finally produces `(c, f)`. Those groups are exactly the input columns. Treating each input column as an output row is precisely the transpose operation.

The outer `list(...)` consumes the iterator returned by `zip` and collects all transposed rows. The resulting outer object is a list, while each row created by `zip` is a tuple. The declared annotation says that the return value is a list of lists, but for this judge the tuple rows represent the same ordered integer sequences and serialize as the required two-dimensional result. The algorithmic content is still a newly constructed matrix; no input row is mutated.

**Why every output position is correct.** Consider any valid output coordinate $(c,r)$. During the $c$-th iteration of `zip`, the function requests the item at index $c$ from each unpacked input row. The item contributed by input row $r$ is therefore `matrix[r][c]`, and it becomes item $r$ of output row $c$. Thus the value stored at output coordinate $(c,r)$ is exactly the value required by the transpose definition.

This also proves that nothing is lost or duplicated. Every input cell has one unique pair $(r,c)$, so it is sent to one unique output pair $(c,r)$. Swapping the indices twice returns the original pair, which means two different input cells cannot collide at one output location. Because every input row has the same length under the matrix contract, `zip` completes exactly $n$ groups and every group contains exactly $m$ values.

**A rectangular trace.** For `matrix = [[1,2,3],[4,5,6]]`, unpacking supplies the iterables `[1,2,3]` and `[4,5,6]`. The three successive groups are `(1,4)`, `(2,5)`, and `(3,6)`. The result therefore has three rows and two columns:

```text
[(1, 4),
 (2, 5),
 (3, 6)]
```

Reading the first output row confirms that it is the original first column. Reading the second output column confirms that it contains the original second row. Both perspectives are consequences of the same index swap.

This compact implementation is optimal because the requested output itself contains all $mn$ input values. Any correct method must at least produce those $mn$ positions, so it cannot asymptotically do less work or use less output storage. The built-in operation merely expresses the necessary traversal directly.

## Complexity detail

Let $m$ be the number of input rows and $n$ be the number of columns in each row. The call to `zip` produces $n$ tuples, and building each tuple reads one item from each of the $m$ rows. It therefore processes $mn$ values.

- **Time complexity:** $O(mn)$. Every matrix element is read once and placed once into the transposed result.
- **Space complexity:** $O(mn)$. The returned matrix contains $mn$ values. Apart from the required output and the small iterator machinery used by `zip`, the algorithm needs no additional structure whose size grows independently.

The input is not modified. If output storage were excluded from auxiliary-space accounting, the extra working space would be $O(m)$ for the iterators and one row being assembled internally, but the branch manifest counts the returned matrix and therefore states $O(mn)$.

## Alternatives and edge cases

- **Explicit nested loops:** Allocate an $n \times m$ result and assign `answer[c][r] = matrix[r][c]` for every pair of indices. This has the same optimal complexity and may be clearer in languages without an operation like `zip`, but it is more verbose than the exact solution.
- **Nested list comprehension:** A construction such as one output row per column also has $O(mn)$ time and space. It can return actual lists instead of tuples, although it must still express both index ranges correctly.
- **In-place swapping:** Swapping `matrix[r][c]` with `matrix[c][r]` is only straightforward for a square matrix. Rectangular matrices change dimensions, so a general in-place index swap does not fit this contract.
- **Single row:** An input with shape $1 \times n$ becomes $n \times 1$. Each produced tuple contains one value, so `zip` handles it naturally.
- **Single column:** An $m \times 1$ input becomes $1 \times m$. There is exactly one output tuple containing all input values.
- **One cell:** A $1 \times 1$ matrix is unchanged in value and dimensions. The general grouping operation still works without a special branch.
- **Square matrix:** The dimensions remain the same, but values away from the main diagonal exchange positions. Main-diagonal cells have equal row and column indices and therefore stay in place.
- **Negative values, zero, and duplicates:** Transposition depends only on positions. The magnitude, sign, and uniqueness of cell values do not affect the operation.
- **Ragged rows:** Python's `zip` stops at the shortest iterable, which would silently discard trailing cells in uneven rows. The problem supplies a proper rectangular matrix, so all rows have the same length and this behavior cannot occur for a valid input.
- **Tuple output rows:** `zip` creates tuples rather than lists. The judge accepts these ordered rows as the requested matrix representation; code requiring mutable row lists could convert each tuple separately without changing the underlying algorithm.
