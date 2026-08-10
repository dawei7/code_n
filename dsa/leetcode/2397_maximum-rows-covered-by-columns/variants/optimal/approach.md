## General

**Represent each row's required columns as bits**

A row is covered when every column containing one in that row has been selected. With at most twelve columns, a single integer can represent both a row's requirements and a selected-column set.

Bit `j` corresponds to column `j`. For each row, the code generates `1 << j` only where the cell value is one and combines those bits using bitwise OR:

```python
reduce(or_, (1 << j for j, x in enumerate(row) if x), 0)
```

The initial value zero handles an all-zero row. Its resulting mask is zero, meaning it requires no selected column.

**Enumerate selected-column masks**

For `n` columns, integers zero through `2^n - 1` encode every possible subset. The loop:

```python
for mask in range(1 << len(matrix[0])):
```

therefore considers every column selection once.

The problem requires exactly `numSelect` distinct columns. `mask.bit_count()` gives the number of set bits, so masks with the wrong cardinality are skipped. A bitmask cannot select the same column twice; distinctness is automatic.

**Test whether one row is covered**

Let row requirement mask be `x` and selected mask be `mask`. Bitwise `x & mask` retains required bits that are also selected. The row is covered exactly when:

```python
(x & mask) == x
```

Equality means every one bit of `x` survives, so all required columns belong to the selection. Extra selected columns do not matter.

For an all-zero row, `x = 0`. Then `0 & mask == 0` for every selection, correctly treating the row as always covered.

The expression is Boolean, and Python's `sum` counts true values as one:

```python
t = sum((x & mask) == x for x in rows)
```

`t` is therefore the number of rows covered by this exact-size selection.

**Keep the best selection value**

The algorithm updates `ans = max(ans, t)` for every eligible mask. It does not need to remember which columns achieved the maximum because the question asks only for the number of covered rows.

If several selections tie, retaining the same count is sufficient.

Selecting an additional column can never make a previously covered row uncovered, because coverage asks only whether all required bits are present. Nevertheless, the algorithm cannot simply select every column: the contract requires exactly `numSelect` choices. The bit-count filter enforces that global resource limit while each subset test checks the row-local requirement.

**Trace the first example**

Rows `[0,0,0]`, `[1,0,1]`, `[0,1,1]`, and `[0,0,1]` become masks:

```text
000
101
110
100
```

Here bit-display orientation is conceptual; bit `0` represents column zero. Selecting columns zero and two gives mask `101`. Requirement `000` is a subset, `101` is a subset, `110` is not because its column-one bit is missing, and `100` is a subset. Three rows are covered.

**Why exhaustive mask evaluation is correct**

Every legal choice of exactly `numSelect` columns corresponds to one unique integer with those bits set. The enumeration reaches it, and the subset tests count exactly its covered rows.

Conversely, every evaluated mask passing the bit-count filter corresponds to a legal selection of exactly that many distinct columns. Thus, the algorithm evaluates all and only feasible selections. Taking the maximum of their exact coverage counts returns the global optimum.

**Exact complexity versus the manifest description**

The manifest describes evaluating exact-size combinations and gives a combination-based term. The source does not generate combinations directly; it loops over all $2^n$ masks and filters by bit count.

Only $\binom{n}{k}$ masks trigger the $m$ row tests, where $k=\texttt{numSelect}$, but all $2^n$ masks still pay the cardinality check. This difference is small for $n\le12$ but should be represented accurately.

## Complexity detail

Let $m$ be the row count, $n$ the column count, and $k$ the number selected. Building all row masks examines $mn$ cells, taking $O(mn)$ time.

The mask loop performs $2^n$ bit-count checks. Exactly $\binom{n}{k}$ masks scan all $m$ row masks. Exact time is:

$$
O\left(mn+2^n+m\binom{n}{k}\right).
$$

With $n\le12$, this exhaustive search is practical.

The `rows` list stores $m$ integers, so auxiliary space is $O(m)$. Generators and scalar masks use constant additional space.

## Alternatives and edge cases

- **Generate only combinations:** Iterating `combinations(range(n), k)` avoids checking the other $2^n-\binom{n}{k}$ masks and aligns more closely with the manifest formula.
- **Backtracking with pruning:** Build selections one column at a time and bound remaining coverage. It can help larger domains but is unnecessary for twelve columns.
- **All-zero row:** Its zero mask is a subset of every selection and is always counted.
- **`numSelect = n`:** Only the all-bits mask qualifies, and every row is covered.
- **One selected column:** Only rows whose one bits are all in that column, plus zero rows, count.
- **Row with more than `numSelect` ones:** It can never be covered, and every subset test fails.
- **Duplicate row masks:** They are separate matrix rows and each contributes independently to `t`.
- **Extra selected zeros:** Selecting a column where a row has zero never harms coverage.
- **Bit orientation:** Only consistent mapping matters; bit `j` is used for column `j` everywhere.
