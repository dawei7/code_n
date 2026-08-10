## General

**Exploit the tiny value domain.** Array positions can reach $10^5$, but every value lies from 1 through 100. Instead of extracting and sorting each queried subarray, the algorithm asks which of these 100 possible values occurs inside the query. A fixed-size scan then computes the answer.

**Build one prefix count per value.** `pre_sum[i][j]` is the number of occurrences of value `j` among the first `i` elements of `nums`, covering original indices zero through `i - 1`. Row zero is all zeros. For each later row and each value one through 100, the source copies the previous count and adds one exactly when `nums[i - 1] == j`.

This table costs more memory than a single prefix sum, but it turns an arbitrary range-frequency question into one subtraction. Value zero receives an unused all-zero column because valid values begin at one.

**Convert inclusive queries to half-open ranges.** Query `[l, r]` includes both endpoints. The code stores `left = l` and `right = r + 1`. Frequency of value `j` in that subarray is

`pre_sum[right][j] - pre_sum[left][j]`.

The first term counts values before index `r + 1`; subtracting those before `l` leaves exactly indices `l` through `r`. This half-open convention removes endpoint special cases.

**Only presence matters for distinct-value difference.** The definition forbids choosing two equal values, so multiple occurrences of the same number do not create difference zero. During a query, the algorithm tests whether each frequency is greater than zero but does not use its magnitude. It effectively constructs the sorted set of distinct values without allocating that set.

**Why adjacent distinct values are enough.** Suppose present values in sorted order are `v1 < v2 < ... < vk`. Any nonadjacent pair `va, vb` with at least one value between them has difference larger than one of the adjacent gaps along that interval. Therefore the minimum difference among all distinct pairs occurs between consecutive present values. Scanning possible values in increasing order and remembering only the previous present one covers every candidate gap.

Variable `last` begins at `-1` to mean no value has been seen. On finding present value `j`, the code updates `t` with `j - last` when a previous distinct value exists, then sets `last = j`. `t` starts at infinity.

**Handle a query with only one distinct value.** If all queried elements are equal, the scan finds only one present value and never forms a gap. `t` remains infinity and is replaced with `-1`. A query contains at least two positions by contract, but duplicates alone still yield no valid unequal pair.

**Trace a query.** For values `[4, 5, 2, 2, 7, 10]` over range `[3, 5]`, prefix differences report presence at 2, 7, and 10. The scan computes gaps five and three, retaining three. Duplicate twos are treated as one distinct value, correctly avoiding a zero gap.

**Why every answer is exact.** Prefix differences give exact range frequencies. The ordered value scan visits exactly the distinct values present, and the adjacent-gap theorem proves the smallest visited gap equals the minimum over every unequal pair. If no gap exists, all elements share one value and `-1` is required.

**Inputs remain unchanged.** The table is separate from `nums` and `queries`. Answers are appended in query order, so result index corresponds directly to the input query index.

## Complexity detail

Let $n$ be the number of elements, $q$ the number of queries, and $V=100$ the value-domain size. Building the table processes every element-value pair in $O(nV)$ time. Each query scans all $V$ values, costing $O(qV)$. Total time is $O((n+q)V)$.

The prefix table has $(n+1)(V+1)$ integer entries, so space is $O(nV)$. The output adds $O(q)$ required storage, while per-query scalars are constant. These bounds match the manifest.

With $V$ fixed at 100, this behaves linearly in $n+q$, but retaining $V$ in the notation explains why the technique depends on the bounded values.

## Alternatives and edge cases

- **Sort each queried subarray:** This repeats extraction and sorting, potentially costing far more than the fixed 100-value scan across many queries.
- **Store positions for each value:** Binary-search whether each value has an occurrence in `[l,r]`. This uses $O(n)$ storage but adds logarithmic checks for each of 100 values.
- **Bitsets:** Presence in ranges can be accelerated with specialized bit operations, but prefix counts are straightforward and exact.
- **Duplicate-only range:** One present value leaves no unequal pair, so `-1` is returned.
- **Adjacent numerical values:** A gap of one is the smallest possible positive difference; later scanning cannot improve it, though the exact source continues through 100.
- **Query endpoints:** Adding one to `r` is essential for inclusive input. Omitting it would lose the final array element.
- **Value 100:** The table has 101 value columns, so index 100 is valid.
- **Unused value zero:** It remains zero and is intentionally skipped by loops starting at one.
- **Output order:** Queries are handled sequentially and answers are appended in the same order.
