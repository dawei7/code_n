## General

Every row is sorted in ascending order, so each row can be searched independently with binary search. The exact solution takes this direct route: it visits the rows from top to bottom, asks where `target` would be inserted in each row, and immediately returns `True` if that position already contains `target`.

The matrix also has sorted columns, but this particular implementation does not use that second property. Ignoring a useful property may leave a stronger algorithm available, yet it does not harm correctness: if every row is searched correctly, every matrix cell belongs to one of those searched rows.

**What `bisect_left` tells us**

For a sorted row, `bisect_left(row, target)` returns the smallest index `j` such that `row[j] >= target`. If no element is at least `target`, it returns `len(row)`.

That position divides the row into two parts:

- every index smaller than `j` contains a value strictly less than `target`;
- if `j` is inside the row, `row[j]` is the first value greater than or equal to `target`.

This characterization makes the membership test simple. If `j` equals the row length, every value in the row is smaller than the target, so the target is absent. If `j` is valid but `row[j] > target`, the earlier values are too small and this first not-smaller value is already too large, so the target is again absent. The only remaining possibility is `row[j] == target`, which proves that the target occurs.

The code expresses those two necessary conditions together:

```text
j is a valid column index AND row[j] equals target
```

The bounds check must come before indexing because Python's short-circuit `and` avoids evaluating `row[j]` when `j` is just past the final element.

**Why the leftmost occurrence is enough**

The statement says rows are ascending, which permits equal neighboring values unless strictness is stated separately. Even if a target appeared multiple times in one row, `bisect_left` would point to its first occurrence. Since the function only needs a Boolean answer, finding any occurrence is sufficient. There is no need to count duplicates or search farther right.

**A row-by-row trace**

Use the matrix

```text
[
  [ 1,  4,  7, 11, 15],
  [ 2,  5,  8, 12, 19],
  [ 3,  6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

and `target = 5`.

- In the first row, the insertion point is index `2`, where the value is `7`. Everything before it is less than `5`, and `7` is greater than `5`, so that row cannot contain the target.
- In the second row, the insertion point is index `1`, and `row[1]` is `5`. The function returns `True` immediately.

For `target = 20`, every row produces either an insertion point at its end or a valid position holding a value greater than `20`. No equality is found, so the loop finishes and the function returns `False`.

**Why searching all rows is correct**

Consider one arbitrary row. The binary-search property above proves that the equality test returns `True` exactly when that row contains `target`. The outer loop applies this complete membership test to every row. If any row contains the target, the corresponding iteration finds it and returns `True`. Conversely, the function returns `True` only after directly comparing a matrix value with the target, so it cannot produce a false positive. If the loop ends, every row has been shown not to contain the target; because the matrix is the union of its rows, the target is absent from the entire matrix, and returning `False` is correct.

**Rectangular shape and the bounds check**

The source checks `j < len(matrix[0])` rather than `j < len(row)`. The problem guarantees an $m\times n$ rectangular matrix, so all rows have the same length and these quantities are equal. Under that contract the check is correct. For a ragged list of lists, it could be unsafe or inaccurate, but ragged input is outside the allowed domain.

The constraints also guarantee at least one row and at least one column. That is why reading `matrix[0]` requires no empty-matrix guard in this exact implementation.

**Relationship to the globally stronger staircase search**

The manifest describes a top-right walk that eliminates a whole row or column after each comparison. That is a different algorithm from the protected Python source. The actual source performs `bisect_left` once per row. Its explanation and complexity must therefore be based on row-wise binary search, even though the column ordering enables a better worst-case bound for many matrix shapes.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Binary search in one row takes $O(\log n)$ comparisons. In the worst case, the target is absent or appears only in the last searched row, so all $m$ rows are processed. The resulting worst-case time complexity is

$$
O(m\log n).
$$

An early match can reduce the actual work. If the target is found in row `r` using zero-based indexing, only `r + 1` binary searches occur, but asymptotic worst-case analysis must still allow all rows.

`bisect_left` searches by indices and does not create a copy of the row. The loop stores only the current row reference and insertion index, so auxiliary space is $O(1)$. No recursion is used. The input is read-only, and the function returns a Boolean rather than building output proportional to the matrix.

The manifest's $O(m+n)$ time bound belongs to staircase search, not to this implementation. Depending on the matrix dimensions, $O(m\log n)$ may be better or worse than $O(m+n)$: for example, binary searching a small number of very wide rows can be attractive, while staircase search is stronger for a roughly square matrix.

## Alternatives and edge cases

- **Top-right staircase search:** Start at `(0, n - 1)`. If the current value is too large, move left; if it is too small, move down. Each comparison eliminates one column or row, giving $O(m+n)$ time and $O(1)$ space while using both sorting guarantees. This is the algorithm summarized in the manifest, but it is not the exact source being explained.
- **Bottom-left staircase search:** The symmetric version moves up when the value is too large and right when it is too small. It has the same $O(m+n)$ bound.
- **Scan every cell:** A full scan is correct without any ordering assumptions but costs $O(mn)$ time and wastes the row-sorted structure.
- **Binary search every row:** This is the implemented strategy. It is easy to justify and especially reasonable when $m$ is small relative to $n$, but it does not benefit from column ordering.
- **Target smaller than a row's first value:** `bisect_left` returns `0`; the equality comparison fails, correctly proving that row contains no target.
- **Target larger than a row's last value:** `bisect_left` returns `n`; short-circuit evaluation prevents an out-of-range access.
- **Duplicate values:** `bisect_left` selects the first matching position. Since only existence matters, duplicates require no further work.
- **One row:** The method reduces to one ordinary binary search and takes $O(\log n)$ time.
- **One column:** It performs one constant-size binary search per row, giving $O(m)$ time. A binary search down the sorted column could instead take $O(\log m)$, but the source does not choose that orientation dynamically.
- **One cell:** The insertion position is either `0`, leading to the direct equality test, or `1`, leading safely to `False`.
- **Ragged or empty matrices:** The source relies on the documented nonempty rectangular $m\times n$ contract. Supporting arbitrary Python nested lists would require checking emptiness and comparing `j` with each individual `len(row)`.
