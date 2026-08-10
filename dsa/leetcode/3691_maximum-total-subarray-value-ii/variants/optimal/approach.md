## General

Unlike the preceding version, the same subarray endpoints cannot be selected twice. There are

$$
\frac{n(n+1)}{2}
$$

distinct nonempty subarrays, far too many to enumerate and sort when $n$ can be $50{,}000$. The algorithm instead organizes them into $n$ monotone sequences and performs a max-heap merge that generates only the largest $k$ values.

The exact source uses a **sparse table** for constant-time range minima and maxima. This is important because the manifest summary says “segment tree,” but that is not the data structure implemented in `solution.py`.

**One monotone sequence for each left endpoint**

Fix a left endpoint $l$ and consider the subarrays:

$$
[l,l], [l,l+1], \ldots, [l,n-1].
$$

Define:

$$
V(l,r)=\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r]).
$$

When $r$ moves one position to the right, the subarray gains an element.

- Its maximum can increase or stay the same; it cannot decrease.
- Its minimum can decrease or stay the same; it cannot increase.

Therefore, $V(l,r)$ is nondecreasing as $r$ increases. For each fixed $l$, the values form one sorted sequence:

$$
V(l,l)\le V(l,l+1)\le\cdots\le V(l,n-1).
$$

Every distinct subarray belongs to exactly one such sequence, identified by its left endpoint.

The problem is now equivalent to finding the sum of the largest $k$ elements across these $n$ sorted sequences. The algorithm reads each sequence backward, beginning with its largest element at $r=n-1$.

**Sparse-table state**

To evaluate $V(l,r)$ quickly, the class `SparseTableRMQ` stores two tables:

- `f_max[i][j]` is the maximum over the length-$2^j$ interval beginning at `i`;
- `f_min[i][j]` is the minimum over the same interval.

Column zero represents intervals of length one:

`f_max[i][0] = data[i]`

`f_min[i][0] = data[i]`

For a higher level $j$, a length-$2^j$ interval is split into two adjacent halves of length $2^{j-1}$. The source combines the previously computed halves:

`f_max[i][j] = max(f_max[i][j - 1], f_max[i + 2^(j-1)][j - 1])`

and analogously uses `min` for `f_min`.

The actual code expresses the power of two with bit shifts. Only starting indices for which the complete interval fits are filled.

The table uses:

`max_log = n.bit_length() + 1`

which allocates a small number of harmless extra columns. Levels whose interval length exceeds $n$ have no valid starting positions and their construction loops are empty.

**Choosing the query block size**

The array `lg` stores:

$$
\texttt{lg}[L]=\lfloor\log_2 L\rfloor.
$$

The recurrence

`lg[i] = lg[i >> 1] + 1`

works because right-shifting a positive integer by one performs floor division by two.

For query interval $[l,r]$, let its length be $L=r-l+1$ and choose $j=\lfloor\log_2L\rfloor$. A block of length $2^j$ fits inside the query. The source uses two such blocks:

- one beginning at $l$;
- one ending at $r$, beginning at $r-2^j+1$.

Together they cover the complete query interval and may overlap. Overlap is safe for minimum and maximum because repeating an element does not change either aggregate. Thus:

`query_max(l, r)`

and

`query_min(l, r)`

each need only two table lookups and one comparison.

**Initializing one candidate per sequence**

For every left endpoint `l`, the largest value in its monotone sequence occurs at `r = n - 1`. The source queries that range and pushes:

`(-val, l, n - 1)`

into `pq`.

Python's heap is a min-heap. Negating `val` makes the most valuable subarray have the smallest first tuple component, so `heappop` behaves like a max-heap.

Coordinates are stored with the value for two reasons:

- `l` identifies which monotone sequence the candidate belongs to;
- `r` identifies the next predecessor to expose after this candidate is selected.

Tuple tie-breaking may compare `l` and `r` when values are equal. Any tied subarray may be chosen first because only the total value matters.

**Extracting the global top $k$**

At every moment, the heap contains the largest not-yet-selected subarray value from each left-endpoint sequence that still has an unselected member.

Initially, this is true because every sequence contributes its last element. Suppose the heap property is true before an extraction. Every unselected subarray lies in one of the sequences, and its value is no greater than that sequence's heap representative. Therefore, the largest heap representative is the largest unselected subarray globally.

The source pops that entry and adds its positive value:

`ans += -val`

If `r > l`, the sequence has another member. Since traversal is backward, the next largest unexposed member is exactly `(l, r - 1)`. Its range value is queried and pushed. If `r == l`, the singleton was the final member and the sequence is exhausted.

Repeating this process $k$ times performs a $k$-way merge of descending sequences. The extracted coordinates are always distinct:

- different sequences have different left endpoints; and
- within one sequence, each right endpoint is exposed once in strictly decreasing order.

Hence the method obeys the distinct-subarray restriction without storing a separate selected-coordinate set.

**Why no larger total is possible**

The heap process emits all subarray values in globally nonincreasing order. After $k$ pops, `ans` is the sum of the $k$ largest values among every distinct subarray.

For any collection of exactly $k$ distinct subarrays, sorting its values cannot make its first value exceed the global largest, its second exceed the global second-largest, and so forth. Its total is therefore no larger than the sum emitted by the heap. The selected heap coordinates attain that sum, making it the maximum possible total.

**A small sequence view**

For `nums = [1, 3, 2]`:

- left endpoint zero gives values $[0,2,2]$;
- left endpoint one gives values $[0,1]$;
- left endpoint two gives value $[0]$.

The heap starts with the last value from each sequence: $2,1,0$. It pops $2$ from the first sequence and exposes that sequence's preceding $2$. The next global pop is also $2$, so for `k = 2` the total is four. These are different coordinates, even though their values tie.

## Complexity detail

Let $n$ be the array length.

The sparse tables contain $O(\log n)$ columns for each of $n$ starting positions. Filling their valid entries takes $O(n\log n)$ time and $O(n\log n)$ space. The `lg` array takes $O(n)$ additional time and space.

Every range-minimum or range-maximum query uses two precomputed blocks and takes $O(1)$ time.

The exact source initializes the heap by calling `heappush` $n$ times, costing $O(n\log n)$. It does not build a list followed by linear-time `heapify`.

Each of the $k$ iterations performs one heap pop and at most one heap push. The heap contains at most one entry per left endpoint, so each operation costs $O(\log n)$. The two range queries for a pushed predecessor cost $O(1)$.

The exact total running time is:

$$
O(n\log n+k\log n)=O((n+k)\log n).
$$

The two sparse tables dominate storage at $O(n\log n)$; `lg` and the heap use $O(n)$.

These are source/manifest mismatches. The manifest claims `O(n + k log n)` time and `O(n)` space and describes segment-tree queries. Those bounds correspond more closely to the editorial's segment-tree alternative, not the checked-in sparse-table source. The exact source has $O(n\log n)$ preprocessing time and space.

## Alternatives and edge cases

- **Enumerate and sort all subarrays:** There are $\Theta(n^2)$ distinct subarrays, so materializing all values is infeasible at the maximum $n$.
- **Segment tree plus heap:** A segment tree uses $O(n)$ space and builds in $O(n)$ time, but each range minimum/maximum query costs $O(\log n)$. This is the manifest-described alternative, not the exact source.
- **Heapify initial candidates:** Building a list of the $n$ terminal candidates and calling `heapify` reduces heap initialization from $O(n\log n)$ to $O(n)$. The checked-in source uses repeated `heappush`.
- **Binary-search a value threshold:** One could try to count subarrays above a range threshold, but efficiently counting max-minus-min constraints is substantially more involved and still needs tie handling for the top-$k$ sum.
- **`k = 1`:** The first heap pop returns the maximum range among all subarrays, which is the global array range.
- **Maximum legal `k`:** When `k=n(n+1)/2`, every sequence is eventually exhausted and every distinct subarray is selected exactly once.
- **One-element array:** The only sequence contains one value zero. The heap pops it, performs no replacement push, and returns zero.
- **All elements equal:** Every range value is zero. Heap tie order is irrelevant, and the total remains zero for any legal $k$.
- **Equal range values:** Distinct subarrays may have identical values. The heap entries retain coordinates, so equal values are still emitted as separate legal choices.
- **Overlapping subarrays:** Different coordinate pairs may overlap freely. The sequence organization is by left endpoint, not by disjointness.
- **Sparse-table overlap:** Query blocks may overlap because minimum and maximum are idempotent. The same technique would not work unchanged for a non-idempotent aggregate such as sum.
