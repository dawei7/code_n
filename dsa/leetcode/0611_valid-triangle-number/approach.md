## General

The input asks for triplets of *indices*, so equal numeric values at different positions represent different choices. Sorting the array makes triangle validity easy to count in batches.

After sorting, choose indices:

$$
i<j<k
$$

so:

$$
\texttt{nums}[i]\le\texttt{nums}[j]\le\texttt{nums}[k].
$$

For nonnegative lengths, the only triangle inequality that can fail is:

$$
\texttt{nums}[i]+\texttt{nums}[j]>\texttt{nums}[k].
$$

The other two sums each include the largest side and are automatically at least as large as the remaining smaller side, becoming strict for positive valid choices. A zero side cannot pass the decisive inequality with sorted nonnegative values.

**Fixing the two smaller-side indices**

The nested loops enumerate every pair $i<j$. The third index must lie in suffix `j + 1` through the end.

Because the suffix is sorted, all values strictly below:

```python
nums[i] + nums[j]
```

are valid largest sides. Once a value is greater than or equal to the sum, it and all later values are invalid.

**Finding the boundary with binary search**

`bisect_left(nums, target, lo=j + 1)` returns the first index in the suffix whose value is greater than or equal to `target`. Call this insertion index $p$.

Then:

- valid third indices are $j+1,j+2,\ldots,p-1$;
- the last valid index is $k=p-1$;
- their count is

$$
(p-1)-(j+1)+1=p-j-1=k-j.
$$

That is exactly what the source adds:

```python
k = bisect_left(...) - 1
ans += k - j
```

If no suffix value is valid, `bisect_left` returns `j + 1`, so `k = j` and the contribution is zero. If every suffix value is valid, it returns `n`, so `k = n - 1` and every available third index is counted.

**Strict inequality and duplicate values**

Using `bisect_left` for the sum excludes values equal to the sum. Such triples are degenerate and must not count. A right-biased search would incorrectly include equality if used without adjustment.

Duplicates remain separate positions after sorting. For `[2,2,3,4]`, choosing the first 2 with 3 and 4 and choosing the second 2 with 3 and 4 are two different index triplets. The loops visit both $i$ positions and count both, as required.

Sorting mutates `nums` in place. The result depends only on the multiset of values, so this does not affect correctness, but callers that need original order would require a copy.

**Why the algorithm is correct**

Every index triplet corresponds to exactly one sorted-index ordering $i<j<k$ and is considered under its unique pair $(i,j)$. For that pair, binary search identifies exactly the contiguous suffix prefix whose values satisfy the strict triangle inequality. Thus, every counted index forms a triangle.

Conversely, any valid triplet has its largest sorted index $k$ satisfying `nums[k] < nums[i] + nums[j]`. Therefore, $k$ lies before the binary-search boundary and is included in the contribution for pair $(i,j)$. No triplet is counted twice because its two smaller indices uniquely determine the loop iteration and its largest index contributes one position in that batch.

Summing all pair contributions yields exactly the number of valid triplets.

**Example**

For sorted `[2,2,3,4]`:

- pair indices $(0,1)$ has sum 4; only value 3 is below it, contributing one;
- $(0,2)$ has sum 5; value 4 contributes one;
- $(1,2)$ likewise contributes one;
- other pairs have no later third index.

Total is three.

## Complexity detail

Let $n$ be array length. Sorting costs $O(n\log n)$. There are $\Theta(n^2)$ pairs $(i,j)$, and the exact source performs an $O(\log n)$ binary search for every pair. Therefore, its actual worst-case time is:

$$
O(n^2\log n),
$$

not the manifest’s $O(n^2)$.

The editorial’s moving-$k$ linear scan reuses a monotonically advancing boundary across $j$ values for each fixed $i$ and achieves $O(n^2)$ time. That optimization is not present in the exact protected source.

Python’s in-place Timsort can use $O(n)$ temporary space in the worst case, matching the manifest’s $O(n)$ space. Loop variables and binary search use constant additional state.

## Alternatives and edge cases

- **Two-pointer largest-side scan:** Fix largest index $k$, move left/right pointers, and when a pair works count all positions between them. Achieves $O(n^2)$ after sorting.
- **Monotone third pointer:** For fixed $i$, advance `k` as `j` increases rather than binary-searching from scratch. Also $O(n^2)$.
- **Brute-force triples:** Tests all $\binom n3$ choices in $O(n^3)$ time.
- **Zero lengths:** Cannot participate in a nondegenerate triangle; the strict inequality naturally contributes zero.
- **Equality:** `a+b=c` is excluded by `bisect_left` at the first value equal to the sum.
- **Duplicates:** Counted by index multiplicity, not deduplicated by value.
- **Fewer than three values:** Loops contribute nothing and return zero.
- **All equal positive values:** Every index triplet is valid and counted.
- **Input mutation:** `nums.sort()` changes caller-visible order.
- **Nonnegative constraint:** Supports reducing three inequalities to the smallest-two sum versus largest.
- **Boundary with no valid `k`:** Contribution formula becomes zero, not negative.
- **Boundary beyond array:** `bisect_left` returns `n`, correctly counting the full suffix.
- **Complexity fidelity:** Binary search inside both loops adds a logarithmic factor; do not describe this exact implementation as $O(n^2)$.
