## General

Cells on one bottom-right diagonal move together: increasing both row and column by one stays on the same diagonal. The exact Optimal solution assigns every cell to a diagonal bucket, sorts each bucket in descending order, and then writes values back by popping from the end.

**A constant key for each diagonal**

For cell `(i, j)`, the source uses key:

`m - i + j`.

Moving to `(i + 1, j + 1)` gives:

$$
m-(i+1)+(j+1)=m-i+j,
$$

so the key remains constant along a bottom-right diagonal.

Different parallel diagonals have different values of `j - i` and therefore different shifted keys. Adding `m` makes every used index positive, allowing a list of buckets instead of a dictionary.

`g` has `m + n` lists. Its index zero is unused, while all actual keys fit from one through `m+n-1`.

The extreme keys make that range concrete. The bottom-left cell `(m - 1, 0)` has key one. The top-right cell `(0, n - 1)` has key `m + n - 1`. Every other cell lies between them. This proves both that the allocation is large enough and that no negative indexing accidentally addresses a bucket from the end of the Python list.

**Collecting matrix values**

The nested loops visit every matrix cell in row-major order. `g[m - i + j].append(x)` places its value in the matching diagonal bucket.

At this stage, the matrix remains unchanged, and all $mn$ values are stored exactly once across the buckets.

**Why buckets are sorted in reverse**

Each bucket executes `e.sort(reverse=True)`, placing its largest value first and smallest value last.

The write-back phase uses `pop()`, which removes the final list element in constant amortized time. Because the final element is currently smallest, successive pops yield ascending values.

If buckets were sorted in ordinary ascending order, popping from the end would produce descending diagonals. Removing from index zero would preserve ascending order but cost linear time per removal because Python must shift remaining list elements.

**Write-back order along a diagonal**

The second row-major traversal encounters cells of any one diagonal from top-left to bottom-right. For example, `(0,0)` is encountered before `(1,1)`, which is before `(2,2)`.

The first cell receives the smallest bucket value, the next receives the next smallest, and so on. Therefore, each diagonal becomes ascending in its required direction.

Interleaving visits from different diagonals does not matter because every diagonal has an independent bucket and pop sequence.

Row-major order really does preserve direction within one diagonal. If two cells share a diagonal and the second lies below-right of the first, its row index is larger. The outer row loop therefore cannot encounter it earlier. That ordering fact is what connects “pop values from smallest upward” to “write a diagonal from top-left toward bottom-right.”

**A small diagonal example**

Suppose one diagonal originally contains values `[3,2,1]` from top-left to bottom-right. Its bucket sorts to `[3,2,1]` in reverse order.

The first write-back pop returns one, the second returns two, and the third returns three. The diagonal becomes `[1,2,3]`.

**Why every cell is correct**

The key proof shows that a bucket contains exactly one whole diagonal and no cells from another. Sorting orders precisely that diagonal's multiset.

Write-back visits diagonal positions in top-left-to-bottom-right order and assigns successive smallest remaining values. Every original cell contributes once and every pop consumes once, so no value is lost or duplicated.

The source modifies `mat` in place and returns the same matrix object.

Notice that bucket positions are not stored. They are unnecessary because the second traversal recomputes the same key from each cell's coordinates. Collection records only the multiset of values, while matrix traversal itself supplies the correct destination order.

## Complexity detail

Let $m$ and $n$ be matrix dimensions and $L=\min(m,n)$, the maximum diagonal length.

Collection and write-back each visit $mn$ cells, taking $O(mn)$ time.

If diagonal lengths are $d_1,d_2,\ldots$, sorting costs:

$$
\sum_k O(d_k\log d_k)
\leq O(mn\log L),
$$

because every $d_k \leq L$ and their sum is $mn$. Total time is $O(mn\log L)$.

Buckets collectively store all $mn$ values, requiring $O(mn)$ auxiliary space, matching the manifest. The list of $m+n$ bucket objects is lower-order relative to the matrix cell count for nonempty dimensions.

Python's sort may use temporary memory, but total remains within $O(mn)$.

## Alternatives and edge cases

- **Min-heaps by diagonal:** Heapify each bucket and pop minima during write-back. It has the same broad time bound but more per-pop overhead.
- **Sort one diagonal at a time:** This reduces auxiliary storage to $O(L)$ while preserving $O(mn\log L)$ time.
- **Counting sort:** Values lie from 1 through 100, so frequency counting can achieve linear matrix time under the bounded value range.
- **Ascending bucket plus front removal:** It is logically correct but inefficient in Python because removing index zero shifts the list.
- **One row:** Every diagonal has length one, so the matrix is unchanged.
- **One column:** Likewise, every diagonal contains one cell.
- **Duplicate values:** Sorting and popping preserve their multiplicity.
- **Unused bucket zero:** The shifted key never uses it; this wastes only one empty list.
- **Input mutation:** The same matrix is overwritten and returned.
- **Key choice:** `j - i` would also identify diagonals but needs a dictionary or offset for negative values.
- **Reverse sort:** It is paired deliberately with end-pop to emit ascending values.
