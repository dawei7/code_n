## General

**Count in how many rows each value appears**

An integer belongs to the intersection exactly when it appears in every row of `nums`. The constraints provide a crucial guarantee: values inside each individual row are distinct.

Because of that guarantee, every occurrence of value `x` comes from a different row. If its total occurrence count equals `len(nums)`, then it appeared once in every row. If the count is smaller, at least one row omitted it.

The solution uses `cnt = [0] * 1001` because every value lies from one through one thousand. Array index `x` directly stores the number of rows containing `x`.

**Process every input value once**

The nested loops visit every row and every integer in that row:

`cnt[x] += 1`.

No per-row set is needed because duplicates within a row are forbidden. That condition prevents one row from contributing two or more to the same value's count.

Let `q = len(nums)`. After all rows:

- if `cnt[x] == q`, `x` occurs in all `q` rows;
- if `cnt[x] < q`, it is absent from at least one;
- `cnt[x] > q` cannot occur under the distinct-within-row guarantee.

**Build sorted output without a separate sort**

The return comprehension enumerates `cnt` from index zero through one thousand:

`[x for x, v in enumerate(cnt) if v == len(nums)]`.

Enumeration visits numeric indices in increasing order, so selected values are automatically ascending. No output sort is required.

Index zero is outside the allowed input value range. Its count stays zero, and since `nums` has at least one row, it cannot satisfy the equality. Keeping slot zero simplifies direct indexing without affecting output.

**Why every returned value is common**

Suppose `x` is returned. Its count equals the number of rows. Each row can contribute at most one occurrence, and there are exactly that many rows. Therefore, every row must have contributed once. `x` is present in each array.

**Why every common value is returned**

If `x` appears in every row, each row contributes one during the nested scan. Its final count is exactly `len(nums)`. The comprehension visits index `x`, sees that equality, and includes it.

The two directions prove the output is exactly the set intersection. Increasing enumeration order proves the ordering requirement independently.

**Trace the sample**

For rows `[3,1,2,4,5]`, `[1,2,3,4]`, and `[3,4,5,6]`, values three and four are incremented once in each row and finish with count three. Values one, two, and five finish below three, and six appears once. The scan returns indices three and four.

For disjoint rows, no counter reaches the row count and the comprehension returns an empty list.

**The one-row case**

When `nums` has one row, every value in that row receives count one, equal to `len(nums)`. The result is simply that row's values sorted ascending, which is exactly the intersection of a single collection.

**Exact implementation versus manifest summary**

The manifest describes maintaining a set intersection and gives space in terms of total input size. The stored Python solution instead exploits the bounded value domain with a fixed 1001-entry counting array.

Both methods are correct, but this approach does not construct row sets or repeatedly intersect them. Its output ordering comes from scanning the numeric universe.

**Why the uniqueness guarantee matters**

If a row could contain duplicate `x` values, total occurrence count would no longer equal number of containing rows. For example, two copies in one row could compensate for absence in another. The exact method is correct because the contract explicitly rules out this case.

The input arrays are only read and remain unchanged.

## Complexity detail

Let

$$
T = \sum_i \lvert \texttt{nums}[i] \rvert
$$

be the total number of input values, and let `U = 1001` be the counter length. Counting takes `O(T)` time and scanning the counter takes `O(U)`, for `O(T + U)` total time.

The counter uses `O(U)` space. Since `U` is a fixed constraint bound, this is `O(1)` with respect to input size; expressing the value universe explicitly is more informative.

The returned list contains `r` common values and naturally requires `O(r)` output space.

## Alternatives and edge cases

- **Repeated set intersection:** Convert rows to sets and intersect them. It is general and matches the manifest summary but uses hash structures instead of the bounded domain.
- **Sort every row and use pointers:** This avoids hashing but costs sorting time and requires more complicated multi-row coordination.
- **Count raw occurrences when duplicates are allowed:** That would be incorrect without first deduplicating each row; this solution relies on the stated uniqueness guarantee.
- **Single row:** All its values are returned in ascending order.
- **No common value:** No count reaches the row total, producing `[]`.
- **All rows identical:** Every row value reaches the required count.
- **Value one or one thousand:** Both map to valid counter endpoints.
- **Unused index zero:** It remains unselected because row count is positive.
- **Input rows unsorted:** Counting ignores their order; final index enumeration supplies sorting.
- **Different row lengths:** Only presence in every row matters, not row size.
- **Output distinctness:** Each numeric index is considered once, so no duplicate can appear.
- **Input preservation:** No row is sorted or mutated.
