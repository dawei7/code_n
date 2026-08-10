## General

**Stable means contained inside one non-decreasing run**

A subarray has no inversion exactly when its elements are non-decreasing. If every adjacent pair satisfies `nums[t] <= nums[t+1]`, transitivity prevents any earlier element from exceeding a later one. Conversely, an adjacent decrease is itself an inversion.

Therefore `nums` splits into maximal non-decreasing runs. A stable subarray must lie entirely inside one run, and every subarray inside one run is stable.

A run of length `k` contains

$$
1+2+\cdots+k=\frac{k(k+1)}2
$$

nonempty subarrays.

**Record run starts and prefix totals**

The scan keeps `l` as the current run's start. A run ends at `r` when `r` is the final array index or `nums[r] > nums[r+1]`.

At each end, `seg` receives the run start `l`. The array `s` receives a cumulative total after adding that run's triangular count. With `s[0]=0`, `s[t]` equals the total stable-subarray counts of complete runs with indices below `t`.

Run starts are strictly increasing, enabling binary search for the runs touched by a query.

**Separate a query into left partial, full middle, and right partial runs**

For query `[l,r]`, `bisect_right(seg,l)` gives `i`, the first run start strictly greater than `l`. Thus `l` lies in run `i-1`.

`bisect_right(seg,r)-1` gives `j`, the run containing `r`.

If `i>j`, no new run begins after `l` and at or before `r`. Both endpoints are in the same non-decreasing run. Every subarray inside the query segment is stable, so a query length `k=r-l+1` contributes `k(k+1)/2`.

Otherwise the query crosses at least one run boundary:

- `a=seg[i]-l` is the number of queried positions in the left endpoint's partial run.
- `b=r-seg[j]+1` is the number in the right endpoint's partial run.
- Runs with indices `i` through `j-1` lie fully inside the query.

The answer is

$$
\frac{a(a+1)}2
+(s[j]-s[i])
+\frac{b(b+1)}2.
$$

The prefix difference selects exactly the full middle runs because `s[t]` totals runs before `t`.

When the query crosses one boundary and `j=i`, there are no full middle runs; `s[j]-s[i]=0`, leaving the two partial triangles.

**Why cross-boundary subarrays are excluded**

Every boundary stored in `seg` follows an adjacent decrease. A subarray crossing that boundary contains the decreasing adjacent pair and is not stable. Therefore stable subarrays inside a query partition cleanly by maximal run, and summing per-run triangles neither misses nor double-counts any candidate.

For `nums=[3,1,2]`, runs are `[3]` and `[1,2]`. Query `[0,2]` contributes one from the first run and three from the second, totaling four. No subarray crossing from three to one is stable.

For equal values such as `[2,2]`, the strict break test `x>next` does not split the run, correctly allowing the length-two non-decreasing subarray.

As an indexing check, suppose run starts are `[0,3,7]` and a query is `[1,8]`. Then `i=1` points to start three, while `j=2` identifies the run beginning at seven. The left partial has positions one and two, the right partial has seven and eight, and `s[2]-s[1]` contributes the complete run beginning at three.

## Complexity detail

Let `n` be the array length and `q` the number of queries. Preprocessing scans once and uses $O(n)$ time.

Each query performs two `bisect_right` calls on up to `n` run starts, so the exact source takes $O(\log n)$ time per query. Total actual time is

$$
O(n+q\log n).
$$

This contradicts the manifest's $O(n+q)$ claim and its statement of constant-time queries. Achieving that bound would require a direct per-position run-index table or another constant-time locator, which the source does not build.

`seg` and `s` each use $O(n)$ space in the worst case, while the output uses $O(q)$. Auxiliary preprocessing space is $O(n)$, or $O(n+q)$ including the returned list.

## Alternatives and edge cases

- **Enumerate all subarrays per query:** This can require $O(qn^2)$ work. Run decomposition aggregates them.
- **Scan runs inside every query:** Prefix totals remove work proportional to the number of crossed runs.
- **Assume “no inversion” only means no adjacent decrease:** For a sequence, adjacent non-decreasing order is equivalent to no inversion by transitivity.
- **Split on equal neighbors:** Equality is allowed, so only a strict decrease ends a run.
- **Single-index query:** It lies in one run and returns one.
- **Query inside one run:** The entire query triangle is valid.
- **Query starts or ends at a run boundary:** The bisect conventions assign endpoints to the correct run and yield positive partial lengths.
- **Every adjacent pair decreases:** Every run has length one, so each query answer is just its number of elements.
- **Entire array non-decreasing:** `seg` has one start, and every query uses the single-run branch.
- **Manifest mismatch:** Binary search operations must appear in the actual runtime bound.
- **Large counts:** A length-$10^5$ run has about five billion subarrays, requiring 64-bit arithmetic outside Python.
