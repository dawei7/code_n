## General

Pascal's triangle is built row by row. Every row begins and ends with one. Each interior value is the sum of the two adjacent values above it: the previous row's value one position to the left and the value at the same position.

The selected solution expresses that rule compactly with `pairwise(f[-1])`. Adjacent pairs from the most recently completed row generate every interior value of the next row.

**How rows and indices are related**

Using zero-based row indices, row $i$ contains $i+1$ values. Its boundary positions zero and $i$ are one. For an interior position $j$,

$$
P(i,j)=P(i-1,j-1)+P(i-1,j).
$$

The two terms exist because an interior position has a number above-left and a number above-right. At a boundary, only one of those positions would be inside the prior row, so the boundary is supplied directly as one.

This recurrence is also the binomial-coefficient identity

$$
\binom{i}{j}
=
\binom{i-1}{j-1}
+
\binom{i-1}{j},
$$

but knowing combinations is not required to implement or verify the construction.

**Why starting with `[[1]]` is valid**

The contract guarantees `numRows >= 1`, so the output always contains the first row. The source initializes `f = [[1]]` and only needs to generate the remaining `numRows - 1` rows.

If `numRows` is one, `range(numRows - 1)` is empty and the initial triangle is returned immediately. This directly matches the second Reference example.

The implementation does not support zero according to the usual extended version of the problem: it would return `[[1]]` rather than `[]`. That behavior is outside the stated positive-input contract, but it is important not to claim broader support than the exact source provides.

**How `pairwise` creates the interior**

For a sequence `[x0, x1, x2, ...]`, `pairwise` yields `(x0, x1)`, then `(x1, x2)`, and so on. The list comprehension computes `a + b` for each adjacent pair.

If the previous row is `[1, 3, 3, 1]`, its pairs are `(1, 3)`, `(3, 3)`, and `(3, 1)`. Their sums are `[4, 6, 4]`. Placing one before and after them creates `[1, 4, 6, 4, 1]`.

The first row `[1]` contains no adjacent pair. `pairwise([1])` is empty, so the middle list is empty and `[1] + [] + [1]` correctly produces the second row `[1, 1]`.

**Why every generated row is correct**

Assume `f[-1]` is the correct current final row. The comprehension enumerates every adjacent pair exactly once, from left to right. Those pairs correspond one-for-one with the next row's interior positions.

Each resulting sum is therefore the required above-left plus above-right value. Adding the two boundary ones completes the row, and `f.append(g)` preserves it as the next output row.

The initial row is correct. Repeating the argument for each loop iteration proves that every appended row is correct and appears in top-to-bottom order. The loop runs exactly one fewer time than the requested row count, so no extra row is produced.

**Tracing all five rows**

The state begins as:

`[[1]]`.

No adjacent sums exist in the first row, so the next row is `[1, 1]`. Its one adjacent pair sums to two, producing `[1, 2, 1]`.

Pairs from `[1, 2, 1]` sum to three and three, producing `[1, 3, 3, 1]`. The next adjacent sums are four, six, and four, producing `[1, 4, 6, 4, 1]`.

After four iterations, `f` contains exactly five rows and matches the Reference output.

**Why earlier rows remain unchanged**

Every `g` is a newly created list. The source reads `f[-1]` but never mutates it, so rows already stored in the output remain stable.

The concatenations also create new lists rather than aliasing a previous row. Even if callers later mutate one returned row, the other rows are distinct list objects.

**Exact source dependencies**

The annotation `List[List[int]]` requires `List` to be defined when the function is declared, unless annotation evaluation is postponed by the environment. The file has no `from typing import List`.

It also calls `pairwise` without `from itertools import pairwise`. For `numRows > 1`, a standalone execution therefore raises `NameError` unless the harness injects that symbol. `itertools.pairwise` requires Python 3.10 or newer; on earlier versions, `zip(row, row[1:])` is a compatible alternative.

## Complexity detail

Let $R$ equal `numRows`. The algorithm creates

$$
1+2+\cdots+R=\frac{R(R+1)}{2}
$$

output values. Each interior addition and boundary placement takes constant time, so total time is $\Theta(R^2)$, conventionally written $O(R^2)$.

The returned triangle contains the same triangular number of integers, requiring $\Theta(R^2)$ output space. This matches the manifest's $O(\text{numRows}^2)$ space statement when output storage is included.

Beyond the retained output, constructing the newest row and intermediate concatenation lists can use $O(R)$ transient space. The newest `g` becomes part of the output, while temporary middle or partial lists are released. Thus auxiliary space excluding output is $O(R)$ for this exact Python expression, not strictly $O(1)$.

At the constraint maximum of thirty rows, values and output are small, but the asymptotic derivation remains quadratic.

## Alternatives and edge cases

- **Explicit nested loops:** Allocate each row, set its boundary ones, and calculate interiors from the previous row. It avoids the `pairwise` dependency and makes indices visible.
- **In-place single-row update:** Useful when only one row is requested, but this problem must return all rows, so the full quadratic output still has to be retained.
- **Binomial multiplicative formula:** Generate each row with consecutive combination values. It avoids looking at the previous row but needs careful exact integer arithmetic.
- **`zip(row, row[1:])`:** Replaces `pairwise` on older Python versions, though `row[1:]` creates a slice unless an iterator-based form is used.
- **One requested row:** Returns the initialized `[[1]]` without evaluating `pairwise`.
- **Zero rows outside the contract:** The exact source incorrectly returns one row; an explicit zero check would be needed for that extended input.
- **Boundary values:** They are always one and must not be calculated by indexing outside the previous row.
- **First transition:** A one-element row has no adjacent pairs, which correctly gives `[1, 1]`.
- **Distinct row objects:** Every appended row must be newly allocated; repeating the same mutable list reference would corrupt prior rows.
- **Missing imports:** Both `List` and `pairwise` need to be available in a standalone environment.
- **Python version:** `itertools.pairwise` is unavailable before Python 3.10.
- **Output space:** Returning every row inherently requires $\Omega(R^2)$ stored integers.
- **Integer size:** Python handles Pascal values without overflow; other languages should choose a type appropriate to the maximum row.
- **Input maximum:** With $R\le30$, the central coefficients fit comfortably within common integer ranges used by typical platforms.
