## General

For index $i$, only elements to its right are eligible. Scanning from right to left turns that positional condition into a maintained data set: before processing $i$, store exactly the values from indices $i+1$ through $n-1$.

The source separates those suffix values by parity into two ordered multisets. It queries the multiset of the opposite parity for the number of values strictly smaller than `nums[i]`, then inserts the current value for use by earlier indices.

**Why two ordered collections match the conditions**

The score requires both:

$$
\texttt{nums}[j]<\texttt{nums}[i]
$$

and opposite parity.

The list `sl` contains two `SortedList` objects:

- `sl[0]` stores even suffix values;
- `sl[1]` stores odd suffix values.

Keeping the parity classes separate means a query never has to inspect or subtract same-parity values. Keeping each class sorted means the strict value threshold can be answered with binary search.

These are multisets rather than ordinary sets. If the same qualifying value occurs at several different suffix indices, every index must contribute separately. `SortedList` retains duplicate entries, so its rank counts their multiplicity.

**The suffix invariant**

The loop runs through

$$
i=n-1,n-2,\ldots,0.
$$

Immediately before computing `ans[i]`:

- `sl[0]` contains every even value `nums[j]` with $j>i$;
- `sl[1]` contains every odd value `nums[j]` with $j>i$; and
- neither structure contains `nums[i]` or any value to its left.

At $i=n-1$, both structures are empty, matching the empty suffix. After answering index $i$, the source inserts `nums[i]` into its own parity structure. This establishes the invariant for the next iteration at $i-1$.

The order “query first, insert second” is essential. Inserting first could allow the current index to count itself when the value test permitted it in a modified problem; more generally, it would violate the exact $j>i$ interpretation.

**Selecting the opposite parity**

The low bit

$$
\texttt{nums}[i]\mathbin{\&}1
$$

is 0 for an even value and 1 for an odd value. XOR with 1 flips that bit:

$$
(\texttt{nums}[i]\mathbin{\&}1)\mathbin{\hat{}}1.
$$

Thus:

- current even parity 0 becomes index 1, selecting odd suffix values;
- current odd parity 1 becomes index 0, selecting even suffix values.

The source writes `nums[i] & 1 ^ 1`. Under Python operator precedence, `&` binds before `^`, so this evaluates as `(nums[i] & 1) ^ 1`.

For insertion, `nums[i] & 1` chooses the current value's own parity list.

**Why \(bisect\_left\) returns the exact score**

In a sorted multiset, `bisect_left(x)` returns the first index at which `x` could be inserted while keeping the order. Every entry before that index is strictly less than $x$, and every entry from that index onward is at least $x$.

Therefore

```text
sl[opposite_parity].bisect_left(nums[i])
```

equals the number of stored suffix values that are:

1. opposite in parity, because only that multiset is queried;
2. strictly smaller, because equal values lie at or after the left insertion point; and
3. to the right, because of the suffix invariant.

Those are exactly the three requirements in the score definition.

**A trace**

For `nums = [5, 2, 4, 1, 3]`, scan from the end:

- At value 3, both multisets are empty, so the score is 0; insert 3 into the odd list.
- At value 1, the even list is empty, so the score is 0; insert 1 into the odd list.
- At value 4, query odd values smaller than 4. Both 1 and 3 qualify, giving 2; insert 4 into the even list.
- At value 2, query odd values smaller than 2. Only 1 qualifies, giving 1; insert 2 into the even list.
- At value 5, query even values smaller than 5. Both 2 and 4 qualify, giving 2.

The returned array is `[2, 1, 2, 0, 0]`.

**Why every qualifying index is counted once**

Fix $i$. Every $j>i$ has already been inserted exactly once into the structure matching `nums[j]`'s parity. If its parity differs from `nums[i]`, it lies in the queried multiset; otherwise it lies in the unqueried one. Within the queried multiset, its rank position is before `nums[i]` exactly when its value is strictly smaller.

Thus every qualifying suffix index contributes one stored occurrence before the insertion point, and no non-qualifying index contributes. The rank is the exact score.

## Complexity detail

Let $N$ be the array length. The loop processes every index once. Each iteration performs one ordered-multiset rank query and one insertion.

Under the `SortedList` interface's logarithmic ordered-search and insertion model, each operation costs $O(\log N)$, giving total time

$$
O(N\log N).
$$

The two multisets together contain exactly the already-processed values and eventually store all $N$ inputs. The answer array also contains $N$ integers. Total space is

$$
O(N).
$$

This matches the asymptotic manifest bounds, but not its stated implementation. The manifest describes coordinate compression with one Fenwick tree per parity. The checked-in Python source performs no compression and constructs two `SortedList` objects. The explanation and dependency requirements must follow the actual source.

The magnitude of values up to $10^9$ does not affect tree height or list rank complexity; operations depend on the number of stored elements.

## Alternatives and edge cases

- **Coordinate-compressed Fenwick trees:** This is the method described by the manifest and also achieves $O(N\log N)$ time and $O(N)$ space, but it is not the checked-in implementation.
- **Merge-sort counting:** A divide-and-conquer method can count cross-half qualifying pairs, though parity filtering complicates the merge bookkeeping.
- **Quadratic suffix scan:** Checking every pair directly is $O(N^2)$ and too slow for $N=10^5$.
- **Equal values:** `bisect_left` excludes them, correctly enforcing strict `<` rather than `<=`.
- **Duplicate smaller values:** Every duplicate occupies its own multiset entry and contributes once for its distinct index.
- **Last index:** No values lie to its right, so both structures are empty and its score is zero.
- **All values same parity:** The opposite-parity multiset is empty at every query, so every answer is zero.
- **All values equal:** Equal values are not strictly smaller even when parity could differ; in fact equal integers also share parity, so no pair qualifies.
- **Expression precedence:** `nums[i] & 1 ^ 1` relies on Python parsing `&` before `^`; explicit parentheses would make the intent clearer.
- **Query-before-insert order:** This preserves the strict right-side condition $j>i$.
- **External dependency:** `SortedList` is generally supplied by the `sortedcontainers` package and must be available in the execution environment.
- **Input preservation:** The source reads `nums` without sorting or changing it.
