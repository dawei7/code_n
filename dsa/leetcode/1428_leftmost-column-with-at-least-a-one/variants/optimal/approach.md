## General

**Reduce the matrix problem to one boundary search per row**

Each row is sorted in non-decreasing order and contains only zero and one. Therefore, every row has one of these forms:

```text
0 0 0 1 1 1
0 0 0 0 0 0
1 1 1 1 1 1
```

The row's useful fact is the boundary where ones begin. If each row's first-one column is known, the answer for the whole matrix is the minimum of those columns.

Directly reading every cell could use as many as $mn$ calls to the hidden API and exceed the 1,000-call limit. Binary search uses sortedness to locate each row boundary with only logarithmically many calls.

**Read only dimensions through the interface**

```python
m, n = binaryMatrix.dimensions()
```

obtains the row and column counts. The solution never attempts to inspect a backing matrix. Every cell value is obtained through `binaryMatrix.get`, respecting the contract.

The code initializes:

```python
ans = n
```

Valid column indices range from zero through $n-1$, so $n$ is a convenient sentinel meaning no one has been found yet.

**Use `bisect_left` over a virtual list of column indices**

For each row `i`:

```python
j = bisect_left(
    range(n),
    1,
    key=lambda k: binaryMatrix.get(i, k)
)
```

`range(n)` behaves as the sorted sequence of candidate column indices from zero to $n-1$. The `key` function transforms a candidate column `k` into the hidden row value at `(i,k)`.

Python's `bisect_left` looks for the earliest position at which target 1 could be inserted while preserving order in the transformed values. Because a row's transformed sequence is some zeros followed by some ones, that insertion position is exactly the first-one column.

The key is applied to elements of `range(n)`, not to target 1. Each key evaluation makes one `binaryMatrix.get(i,k)` call. Binary search discards roughly half the candidate columns after each call.

**What happens for every row shape**

- If a row begins with one, the earliest insertion position is zero.
- If it has zeros followed by ones, the returned position is the first one.
- If it is all zeros, target one belongs just past the row, so `bisect_left` returns `n`.

Thus the same call handles a missing one without an extra final API request.

**Combine row results**

`ans = min(ans, j)` retains the smallest boundary found across all processed rows. An all-zero row returns `n` and cannot worsen an already-valid answer. A row beginning with one makes `ans` zero, the smallest possible column, although the exact implementation continues processing remaining rows.

At the end:

```python
return -1 if ans >= n else ans
```

converts the sentinel to the required -1. Under normal results, `ans` cannot exceed `n`, so `>=` safely covers the no-one state.

**Trace a small matrix**

For:

```text
[0, 0, 1, 1]
[0, 1, 1, 1]
[0, 0, 0, 0]
```

the three binary searches return 2, 1, and 4. The running minimum changes from sentinel 4 to 2, then 1, and remains 1 after the all-zero row. Column one is correctly returned.

**Why binary search is valid through an API**

Binary search does not require direct array access. It requires only the ability to ask for a value at a chosen index. `binaryMatrix.get` provides exactly that. The hidden implementation of the matrix is irrelevant as long as the documented method returns the requested cell.

**Why the algorithm is correct**

Within a sorted binary row, all columns before the first one contain zero and every column at or after it contains one. `bisect_left` returns that boundary, or `n` when the one region is empty. Therefore, `j` is correct for every row.

The leftmost matrix column containing a one is precisely the minimum first-one boundary over all rows with a one. The running minimum computes that value, and the sentinel conversion handles the case where no row has one.

**Why the API-call budget is respected**

A binary search over $n$ columns uses $O(\log n)$ calls. Across $m$ rows, the solution makes $O(m\log n)$ calls. With both dimensions at most 100, this is roughly at most 700 key probes, below the 1,000-call limit.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Each of $m$ calls to `bisect_left` performs $O(\log n)$ key evaluations, so the exact stored implementation takes $O(m\log n)$ time and API calls. `range(n)` is a compact range object, and the algorithm stores only dimensions, indices, and the answer sentinel, giving $O(1)$ auxiliary space.

The manifest advertises $O(m+n)$ time. That bound corresponds to the staircase method that begins at the top-right cell and moves only left or down. The exact source instead performs independent row binary searches, so $O(m\log n)$ is the accurate bound for this file.

## Alternatives and edge cases

- **Top-right staircase:** At a one, move left; at a zero, move down. It makes at most $m+n$ API calls and realizes the manifest's advertised time with $O(1)$ space.
- **Linear scan of every row:** Stop at each row's first one. It is correct but can make $mn$ calls and violate the judge limit.
- **Manual row binary search:** Track low and high bounds explicitly. It has the same $O(m\log n)$ behavior as `bisect_left` and may be more portable across Python versions.
- **Narrow searches using current answer:** Once column `ans` is known, later rows need search only to its left. This can reduce calls in practice.
- **All-zero matrix:** Every search returns `n`, the sentinel survives, and the function returns -1.
- **A one in column zero:** The row search returns zero, which is globally optimal.
- **One row:** The method reduces to finding that row's first one.
- **One column:** Each search determines whether its only value is zero or one.
- **API restriction:** The solution reads dimensions once and every cell only through `get`.
- **Call-cap accounting:** The exact constraints make independent binary search safe even though the staircase approach is asymptotically better.
