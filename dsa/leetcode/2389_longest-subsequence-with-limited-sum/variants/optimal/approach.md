## General

**For a fixed length, choose the cheapest elements**

The question asks for the maximum number of elements whose sum stays within a budget. All values are positive. If we want a subsequence of length $r$, the smallest possible sum is obtained by taking the $r$ smallest array values.

Original positions do not prevent this choice. Any set of selected indices, when read in increasing index order, forms a subsequence. Sorting is used only to determine which values are cheapest; those values always correspond to some valid index set in the original array.

This observation converts an enormous collection of possible subsequences into one minimum sum for every possible length.

**Sort values and build minimum-length costs**

The code sorts `nums` in non-decreasing order. It then uses `accumulate(nums)` to create:

```text
s[0] = smallest value
s[1] = sum of two smallest values
s[2] = sum of three smallest values
...
```

Thus, `s[r - 1]` is the minimum sum achievable by any length-$r$ subsequence.

Because every input number is positive, prefix sums are strictly increasing. Taking one additional value always raises the required budget.

**Why the sorted prefix is a lower bound**

Let sorted values be $a_1\le a_2\le\cdots\le a_n$. Consider any selection of $r$ values. Its smallest selected value is at least $a_1$, its second-smallest is at least $a_2$, and so on. Therefore, its sum is at least:

$$
a_1+a_2+\cdots+a_r.
$$

The prefix consisting of those exact $r$ smallest values achieves equality. Hence, this prefix sum is both a lower bound for all length-$r$ subsequences and an achievable cost.

It follows that a length $r$ is feasible for query budget $q$ exactly when `s[r - 1] <= q`.

**Binary-search the largest feasible length**

For each query `q`, the exact solution calls:

```python
bisect_right(s, q)
```

`bisect_right` returns the insertion position after every prefix sum less than or equal to `q`. That position is also the number of affordable prefix sums and therefore the largest feasible subsequence length.

If even `s[0]` is greater than `q`, the insertion position is zero, representing the empty subsequence. If `q` covers `s[-1]`, it returns `n`, meaning all elements fit.

Using the right insertion boundary is important because equality is allowed. A prefix sum exactly equal to the query must count as feasible.

**Trace the first example**

Sorting `[4, 5, 2, 1]` produces `[1, 2, 4, 5]`, and prefix sums are `[1, 3, 7, 12]`.

- For query `3`, two prefix sums are at most three, so the maximum length is two.
- For query `10`, `1, 3, 7` fit but `12` does not, so the length is three.
- For query `21`, all four prefix sums fit, so the length is four.

The actual subsequence for length three need not appear in sorted order in the original array. Choosing original values `4, 2, 1` at their original indices yields a valid subsequence with the same affordable cardinality. Only existence and maximum size are requested.

**Why each answer is optimal**

Suppose `bisect_right` returns $r$. Then the sum of the $r$ smallest values is at most $q$, so those corresponding original elements form an achievable subsequence of length $r$.

If $r<n$, the sum of the $r+1$ smallest values is greater than $q$. Every other selection of $r+1$ values has at least that sum, so no longer subsequence can fit. Therefore, $r$ is exactly the maximum size.

Queries are independent. Reusing the same sorted prefix array is valid because answering one query does not consume elements or change `nums`.

**Input mutation**

`nums.sort()` modifies the caller-provided list. The algorithm no longer needs original order after establishing that any chosen index set can be read as a subsequence. If preserving input is required externally, use `sorted(nums)` instead at the cost of an explicit copy.

## Complexity detail

Let $n$ be the number of values and $m$ the number of queries. Sorting takes $O(n\log n)$ time. Building prefix sums takes $O(n)$.

Each `bisect_right` search takes $O(\log n)$ time, so all queries take $O(m\log n)$. Total time is $O(n\log n+m\log n)$.

The prefix-sum list uses $O(n)$ space, and the returned answer list uses $O(m)$. The manifest reports $O(n)$ auxiliary space for preprocessing, conventionally excluding required output. Python's in-place sort may also use implementation-dependent temporary memory.

## Alternatives and edge cases

- **Sort queries offline:** Process budgets in ascending order while advancing one prefix pointer. This answers all queries in $O(n\log n+m\log m)$ time and can avoid one binary search per query.
- **Scan prefixes for each query:** Correct but takes $O(mn)$ time in the worst case.
- **Do not sort:** Original prefix sums do not represent cheapest cardinalities; an expensive early value might be skipped in a subsequence.
- **Budget below the minimum value:** `bisect_right` returns zero, correctly choosing the empty subsequence.
- **Budget equals a prefix sum:** The right boundary includes it, because sums may be less than or equal to the query.
- **Budget covers all values:** The answer is `n`.
- **Duplicate values:** Prefix sums remain increasing because values are positive, and duplicates pose no special problem.
- **All values positive:** This guarantee makes longer sorted prefixes strictly more expensive; zeros or negatives would require adjusted reasoning.
- **Repeated queries:** Each produces the same binary-search result independently.
- **Input mutation:** Sorting changes `nums` order even though the returned result depends only on its multiset.
