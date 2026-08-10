## General

**Aggregate every record by its ID**

The result needs one record for each ID appearing in either input, with all values for that ID added together. A map from ID to running total directly represents this requirement.

The exact solution uses `Counter`, a dictionary-like collection whose missing keys start at zero. It iterates through `nums1 + nums2` and performs

`cnt[i] += v`

for each record `[i,v]`. If an ID appears in only one input, its total is that one value. If it appears in both, the second visit adds to the first value.

The uniqueness guarantee within each individual array means an ID appears at most twice across the combined inputs, but the accumulation would remain correct even without that guarantee.

**Why input ordering is not used during aggregation**

Both inputs are already sorted, which would permit a linear two-pointer merge. The checked-in implementation instead concatenates the lists, aggregates through hashing, and sorts the resulting map entries.

Hash aggregation deliberately ignores encounter order. This makes the value-combination logic very simple, but it means output order must be restored afterward.

The expression `nums1 + nums2` creates a new outer list containing references to all pair records. It does not modify either input and does not copy the inner two-element lists themselves.

**Sort the unique result entries**

`cnt.items()` produces one `(id, total)` pair per distinct ID. Calling `sorted` on these pairs uses tuple ordering, whose first comparison component is the ID. Since IDs are unique among the map entries, the first component alone determines their final ascending order.

The result therefore contains:

- every ID from the union of both inputs;
- exactly one record per ID;
- the sum of all associated values;
- records in ascending ID order.

The exact Python expression returns a list of two-element tuples rather than a list of two-element lists. These are equivalent pair sequences for the usual judge serialization, although a caller requiring the annotation's literal mutable `List[List[int]]` shape could convert each tuple to a list.

**Why each total is exact**

Consider any ID $x$. If it is absent from both arrays, the loop never creates a counter entry, so it is correctly absent from the output.

If it appears only in `nums1`, the loop adds its first-array value once. The assumed value from `nums2` is zero, so that stored total is correct. The same reasoning applies symmetrically when it appears only in `nums2`.

If it appears in both, the loop adds both values to the same counter key. Addition is associative, so the encounter order does not matter. The final stored amount is exactly their required sum.

Because a dictionary has one entry per key, duplicate output IDs cannot occur. Sorting changes only order, not keys or totals. This proves all output conditions.

**Trace the sample aggregation**

For

`nums1 = [[1,2],[2,3],[4,5]]`

and

`nums2 = [[1,4],[3,2],[4,1]]`,

the first input creates totals $1\mapsto2$, $2\mapsto3$, and $4\mapsto5$. The second input updates ID $1$ to $6$, creates ID $3$ with $2$, and updates ID $4$ to $6$. Sorting the four items by ID produces pairs `(1,6)`, `(2,3)`, `(3,2)`, and `(4,6)`.

When the arrays have no common IDs, every counter entry receives one value and sorting simply interleaves the two ID sets.

**Why this differs from the manifest summary**

The manifest describes a two-pointer merge with $O(n+m)$ time and constant auxiliary state excluding output. That is a strong way to exploit the already-sorted inputs, but it is not the checked-in source.

The source uses a Counter and then comparison-sorts all distinct IDs. Its conceptual result is the same, but beginners need to understand the actual hash aggregation, concatenation allocation, and sorting cost rather than assuming unseen pointer logic.

## Complexity detail

Let $n=|\texttt{nums1}|$, $m=|\texttt{nums2}|$, and $u$ be the number of distinct IDs across both arrays. Concatenating and scanning the records takes $O(n+m)$ expected time. Counter updates take expected $O(1)$ each. Sorting $u$ item pairs takes $O(u\log u)$ time.

The exact total is $O(n+m+u\log u)$, which is $O((n+m)\log(n+m))$ in the worst case. This differs from the manifest's $O(n+m)$ bound for a two-pointer implementation.

The concatenated outer list and Counter each use $O(n+m)$ worst-case space, and the sorted output uses $O(u)$. Excluding required output, code-accurate auxiliary space is still $O(n+m)$ because of aggregation and concatenation, not the manifest's $O(1)$.

## Alternatives and edge cases

- **Two-pointer merge:** Compare the next ID in each already-sorted input, append the smaller one, and sum on equality. This achieves $O(n+m)$ time and $O(1)$ auxiliary state excluding output.
- **Fixed ID array:** Because IDs are bounded by $1000$, an array of totals can aggregate in linear time and then scan the fixed domain, using constant space relative to input size.
- **Counter plus sorting:** The implemented method is concise and robust even if input order were not sorted, but it gives up the linear merge advantage.
- **No common IDs:** Every input record appears once in the output after sorting.
- **All IDs common:** Every output value is the sum of exactly two records.
- **One array exhausts early:** The Counter approach has no special tail case; all records are simply visited.
- **Positive values:** Totals cannot cancel to zero, so every encountered ID must remain in the output.
- **Input preservation:** List concatenation creates a new outer list and neither original input is changed.
- **Tuple result records:** `sorted(cnt.items())` returns tuples. Convert with a list comprehension if a strict consumer requires inner lists.
- **Manifest distinction:** The optimal two-pointer idea is documented as an alternative, while complexity claims for the exact solution reflect hashing and sorting.
