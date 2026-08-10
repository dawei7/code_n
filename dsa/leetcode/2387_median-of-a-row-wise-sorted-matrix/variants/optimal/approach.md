## General

**Search the value instead of flattening the matrix**

The matrix contains $N=mn$ values and $N$ is odd. The median is the element with one-based sorted rank:

$$
\frac{N+1}{2}.
$$

Flattening and sorting all cells would take at least $O(N)$ time just to read them, violating the requested sub-$O(mn)$ direction. The row-wise sorted property instead lets us ask efficiently: for a candidate value $x$, how many matrix entries are at most $x$?

That count is monotone in $x$. Once it reaches the median rank, it never decreases. Binary search can locate the smallest value where it reaches that threshold.

**Count values at or below one candidate**

For one sorted row, `bisect_right(row, x)` returns the insertion position after all occurrences of `x`. That position equals the number of row values less than or equal to `x`.

The helper sums this quantity across rows:

```python
def count(x):
    return sum(bisect_right(row, x) for row in grid)
```

Duplicates are handled correctly. If a row contains several copies of `x`, `bisect_right` places the insertion point after every copy, so all contribute to the rank count.

Each row search is logarithmic rather than scanning its elements.

**Calculate the target rank**

The code uses:

```python
target = (m * n + 1) >> 1
```

Right shift by one divides a nonnegative integer by two with floor. Because $mn$ is odd, this equals $(mn+1)/2$, the one-based median position.

For nine values, the target is five: the median is the smallest value with at least five matrix entries at or below it.

**Use keyed `bisect_left` on the answer domain**

All values lie between one and $10^6$. The searched sequence is `range(10**6 + 1)`, representing candidate values zero through one million.

The call:

```python
bisect_left(range(10**6 + 1), target, key=count)
```

uses a subtle Python API. The `key` function is applied to elements of the searched range, so comparisons use `count(candidate)`. It is not applied to `target`. `bisect_left` finds the first range position whose key is not less than `target`—the first candidate with `count(candidate) >= target`.

Because each range element equals its index, the insertion index returned by `bisect_left` is also the candidate value itself.

Including zero is harmless even though matrix values begin at one: `count(0) = 0`, so zero cannot meet a positive target.

**Why the first qualifying value is the median**

Let the globally sorted multiset be $a_1\le a_2\le\cdots\le a_N$, and let $r=(N+1)/2$.

For every $x<a_r$, fewer than $r$ elements are at most $x$, so `count(x) < target`. At $x=a_r$, at least the first $r$ elements are at most $x$, so `count(x) >= target`. Therefore, $a_r$ is exactly the smallest qualifying value.

The count predicate is monotone because increasing $x$ cannot cause any previously counted element to become uncounted. Keyed binary search returns this boundary, so it returns the median.

**Trace the first example**

Across the rows `[1,1,2]`, `[2,3,3]`, and `[1,3,4]`, there are nine values and target rank five.

For candidate one, the three `bisect_right` results sum to three. This is below five. For candidate two, the results count five entries: three ones and two twos. Two is the first candidate meeting the target, so the algorithm returns two.

**Why the search is below full matrix scanning per probe**

The helper does inspect every row, but it searches within each row logarithmically. It never visits all $n$ entries in a row. The outer binary search needs only logarithmically many candidate probes over the fixed value range.

The `range` object is lazy and compact; it does not allocate one million integers.

## Complexity detail

Let $V=10^6+1$ be the searched value-domain size. One `count` call performs $m$ binary searches of $O(\log n)$ each, for $O(m\log n)$ time. `bisect_left` makes $O(\log V)$ key evaluations. Total time is:

$$
O(m\log n\log V).
$$

The generator inside `sum`, scalar variables, and lazy `range` use $O(1)$ auxiliary space. `bisect_right` is iterative and does not allocate per-row copies. This matches the manifest.

The fixed domain could be narrowed to the minimum first element and maximum last element across rows, reducing constants without changing asymptotic reasoning.

## Alternatives and edge cases

- **Flatten and sort:** It is simple but takes $O(mn\log(mn))$ time and $O(mn)$ space, violating the intended sublinear-in-cells search.
- **Heap merge of rows:** A $k$-way merge can find the median in $O(mn\log m)$ worst-case work and still processes about half the cells.
- **Narrow value bounds:** Search from `min(row[0])` to `max(row[-1])` instead of the full constraint domain for fewer probes.
- **Single row:** The method still works, though direct indexing at the middle would be simpler.
- **Single column:** Each row search is constant-size, and value binary search finds the middle across rows.
- **Duplicate median values:** `bisect_right` counts all copies, while “first count reaching target” returns the correct repeated value.
- **Minimum possible median:** Candidate zero fails, and candidate one can be returned.
- **Maximum possible median:** The inclusive range contains `10**6`, so the upper boundary is searchable.
- **Key semantics:** `count` applies to range candidates, not to `target`; misunderstanding this changes the search meaning.
- **Odd element count:** It gives one unambiguous middle rank, as guaranteed by odd `m` and `n`.
