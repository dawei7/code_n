## General

**Check capacity before constructing rows**

An $m$-by-$n$ array contains exactly $mn$ cells. The task requires using every original element exactly once, so construction is possible if and only if

`m * n == len(original)`.

If the values differ, the source returns an empty list immediately. Too many and too few elements are both impossible.

**Partition the input into consecutive row slices**

When the length matches, row zero must contain indices zero through $n-1$, row one indices $n$ through $2n-1$, and so forth.

The comprehension iterates start index `i` over

`range(0, m * n, n)`.

These starts are zero, $n$, $2n$, and so on through $(m-1)n$, exactly one per row.

For each start, slice `original[i : i + n]` copies the next $n$ elements into one row.

**Why there are exactly `m` rows**

The range spans total length $mn$ in steps of $n$. Since $n$ is positive, it produces

$$
\frac{mn}{n}=m
$$

start indices. Every produced slice has length $n$ because the feasibility check guarantees its upper boundary does not run past a partial final row.

**Why every element is used once**

Adjacent row slices are

$$
[0,n),[n,2n),\ldots,[(m-1)n,mn).
$$

They are disjoint and their union is every valid original index. Slicing preserves order within each interval, and the comprehension preserves row order.

No element is omitted, repeated, or reordered relative to row-major construction.

It is useful to connect this interval view to an arbitrary element. Take original index $q$, where $0\le q<mn$. Integer division gives its unique row number `q // n`, and the remainder gives its unique column number `q % n`. The slice for row `q // n` begins at `(q // n) * n` and includes exactly the indices whose quotient by $n$ is that row number. Therefore it includes $q$ once. No other slice can include $q$ because different rows have disjoint quotient ranges.

**Trace the standard example**

For `original=[1,2,3,4]`, $m=2$, and $n=2$, the starts are zero and two. The slices are `original[0:2]`, giving `[1,2]`, and `original[2:4]`, giving `[3,4]`.

For $m=1,n=3$, the range has only start zero and the one slice contains the entire input.

**Why slicing creates independent rows**

Each Python list slice produces a new list. Rows do not alias one another, and changing a returned row later does not mutate `original`.

The elements themselves are integers and need no deep copying. The outer comprehension creates the matrix list holding the row lists.

This independence matters in Python. An expression such as `[[0] * n] * m` would repeat references to the same inner list, so changing one apparent row would change every row. Here each slice expression is evaluated separately for a different interval, and each evaluation constructs a distinct list object. The result has the same values as the flat array without the shared-row aliasing trap.

**Why the method is correct**

On an invalid length, no matrix with the required dimensions can use exactly all elements, so empty is required.

On a valid length, the start progression and slices form precisely the row-major partition specified by the problem. The output has correct dimensions, values, and order.

The feasibility test is both necessary and sufficient. It is necessary because a rectangular matrix with fixed positive dimensions has no way to gain or lose cells. It is sufficient because, once the counts agree, the consecutive partition described above always exists; the values themselves impose no additional restrictions. They may repeat, be negative, or appear in any order, and slicing treats them uniformly.

**Direct slicing versus coordinate arithmetic**

An alternative can allocate a matrix and place original index $q$ at row `q // n` and column `q % n`. Slicing packages the same quotient/remainder grouping into a shorter operation while preserving the same linear copying cost.

## Complexity detail

Let $L=\texttt{len(original)}$. On valid input, the slices collectively copy exactly $L=mn$ elements, so time is $O(L)$. The comprehension creates $m$ row objects.

The returned matrix stores $O(L)$ element references, matching the manifest's space bound. Excluding required output, only comprehension and slice construction state is used; peak construction storage is still tied to the output rows. Invalid input returns in $O(1)$ time and space.

Although there are $m$ slice operations, their total copying work is not $O(mL)$. Every slice has length $n$, so the combined work is $m\cdot n=L$. The range object itself is compact and does not allocate a list containing all start indices.

## Alternatives and edge cases

- **Nested row/column loops:** Explicitly fill a preallocated matrix; same $O(L)$ time and output space.
- **`divmod` mapping:** Map each flat index to row and column, useful when slicing is unavailable.
- **Iterator chunking:** Consume $n$ elements per row; must still validate the exact total.
- **Too many original elements:** Return empty rather than discard extras.
- **Too few original elements:** Return empty rather than create a short final row.
- **One row:** One slice contains all elements when $n=L$.
- **One column:** Each length-one slice becomes a separate row.
- **$m=n=1$:** Valid only for a one-element original.
- **Positive dimensions:** Guarantee the range step `n` is nonzero.
- **Independent rows:** Slicing prevents shared-row aliasing.
- **Input preservation:** Slices copy row lists and do not modify `original`.
- **Order:** The output follows original row-major order exactly.
