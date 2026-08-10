## General

Unlike the preceding unique-intersection problem, this problem preserves multiplicity. If a value appears three times in one array but only twice in the other, the answer must contain two copies. For each value $x$, the required output count is therefore

$$
\min(\operatorname{count}_{\texttt{nums1}}(x),\operatorname{count}_{\texttt{nums2}}(x)).
$$

The exact solution realizes that formula by treating the occurrences from `nums1` as a limited supply. A `Counter` records how many copies of each value are available from the first array. The loop then reads `nums2` from left to right. Whenever the current value still has positive supply, the solution appends one copy to the answer and consumes one unit from the counter.

**Why a set is no longer enough.**

A set can answer whether a value occurs, but it cannot distinguish one occurrence from ten. For `nums1 = [2, 2]` and `nums2 = [2, 2]`, a set intersection would contain only one `2`, which is too few. The counter preserves the exact quantity available from one side, allowing the scan of the other side to match occurrences one by one.

**Building the available supply.**

`Counter(nums1)` visits all values in `nums1`. For every distinct integer `x`, `cnt[x]` becomes the number of times `x` occurs in that array. The answer begins empty because no occurrences from `nums2` have yet been matched.

The implementation always counts `nums1`. It does not compare the array lengths or swap the inputs. This detail differs from the variant manifest's summary, which says that the shorter array is counted. Counting the shorter input is a useful optimization, but it is not present in the checked-in source and must not be silently attributed to it.

**Consuming matches while scanning the second array.**

For each `x` in `nums2`, the condition `if cnt[x]` asks whether at least one unmatched copy of `x` remains from `nums1`. A `Counter` returns zero for a missing key, so values that never occurred in `nums1` fail the condition. Counts begin nonnegative, and the solution decrements only after a successful match, so a false condition means exactly that no available copy remains.

When the condition is true, `ans.append(x)` records one common occurrence. The following `cnt[x] -= 1` is essential: that specific copy from `nums1` has now been paired with the current copy from `nums2` and cannot be reused. Without the decrement, every later duplicate in `nums2` would also pass whenever `nums1` contained the value at least once, potentially producing too many copies.

For example, take `nums1 = [1, 2, 2, 1]` and `nums2 = [2, 2]`. The counter begins with two available `1`s and two available `2`s. The first scanned `2` is appended and reduces the remaining `2` count to one. The second is also appended and reduces it to zero. The returned answer is `[2, 2]`.

Now change `nums2` to `[2, 2, 2, 2]`. The first two copies consume the two available copies from `nums1`. For the third and fourth copies, `cnt[2]` is zero, so neither is appended. This gives exactly the minimum of the two input frequencies.

**The maintained meaning of the counter.**

Before each loop iteration, `cnt[x]` represents the number of occurrences of `x` in `nums1` that have not yet been paired with processed occurrences from `nums2`. Initially this is true because none of `nums2` has been processed. A nonmatching iteration changes nothing, so the meaning remains true. A matching iteration appends one occurrence and subtracts one available copy, so it also preserves the meaning.

At the end, consider any value `v`. The loop appends `v` once for each encountered copy in `nums2` until either that array runs out of copies or the supply from `nums1` reaches zero. Hence the number appended is exactly the smaller of the two original frequencies. Applying this reasoning independently to every value proves that the complete answer has precisely the required multiset intersection.

**Why output order follows the second array but is not promised.**

Matches are appended during the left-to-right scan of `nums2`, so this particular source returns common occurrences in their encounter order within `nums2`. The contract permits any order, so correctness does not depend on that observation. A caller or test should not require sorted output. The implementation does not mutate either input array; it creates a counter and a new result list.

**Truthiness is safe here.**

Python treats zero as false and a positive integer as true. Because counts are never decremented below zero, `if cnt[x]` is equivalent to `if cnt[x] > 0` throughout this algorithm. The shorter expression would be dangerous only if negative counts were possible, because negative integers are also truthy. The guarded decrement prevents that state.

## Complexity detail

Let $n$ be `len(nums1)`, let $m$ be `len(nums2)`, let $u_1$ be the number of distinct values in `nums1`, and let $r$ be the total length of the returned multiset intersection.

Constructing `Counter(nums1)` takes expected $O(n)$ time. The loop examines all $m$ values in `nums2`; expected hash lookup, append, and decrement costs are constant per iteration. Returning the already-built list is constant work. Total expected running time is therefore $O(n+m)$, matching the manifest's time bound.

The counter stores $u_1$ keys and their remaining counts, so its auxiliary storage is $O(u_1)$, bounded by $O(n)$. Reading a missing key from a `Counter` returns zero rather than requiring a positive stored count for that value, so values unique to `nums2` do not represent useful supply. The answer stores $r$ integers. Including output, total additional storage is $O(u_1+r)$; because $r\le\min(n,m)$, the worst case is $O(n+m)$ only if one uses a loose combined bound, while the more informative expression separates counter state from required output.

If output storage is excluded, the exact source uses $O(u_1)$ auxiliary space. It does not guarantee the manifest's $O(\min(n,m))$ bound because `nums1` is not necessarily the shorter input. If `nums1` has one million distinct values and `nums2` has one value, the counter still stores the million values. A length check and input swap would make the counter use $O(\min(n,m))$ entries, but that optimization belongs to an alternative implementation.

As with ordinary hash-table algorithms, the constant-time operations are expected bounds. Under standard integer hashing they give the intended linear result. The stated value range also limits the universe to integers from `0` through `1000`, so a fixed counting array is possible, although the exact source uses a general `Counter`.

## Alternatives and edge cases

- **Count the shorter array:** Swap the inputs when `nums1` is longer, then run the same counter-and-consumption procedure. Time remains expected $O(n+m)$ while counter storage becomes $O(\min(n,m))$. This matches the manifest summary but is absent from the exact solution.

- **Two pointers on sorted arrays:** When both arrays are already sorted, compare their current values. Advance the smaller side, and append then advance both sides when equal. This takes $O(n+m)$ time and $O(1)$ auxiliary space excluding output, directly answering the first follow-up.

- **Sort unsorted inputs first:** Sorting and then using two pointers costs $O(n\log n+m\log m)$ time. It can reduce hash storage, but in-place sorting mutates inputs and sorting implementations may use additional memory.

- **Fixed frequency array:** Values are restricted to `0` through `1000`, so an array of `1001` counts can replace the hash map. It gives deterministic direct access with bounded storage but relies on this narrow numeric domain.

- **Streaming the disk-backed second array:** Build the counter from `nums1` if it fits in memory, then read `nums2` sequentially in chunks. Each second-array element can be processed once; the complete second array never needs to reside in memory.

- **Neither array fits in memory:** Use external sorting followed by a merge-style scan, or partition both inputs by value ranges or hashes and process matching partitions. The in-memory `Counter` source is not sufficient under that stronger storage restriction.

- **No shared values:** Every lookup is zero, so `ans` remains empty and the method returns `[]`.

- **Unequal duplicate counts:** The decrement stops matching exactly when the first array's supply is exhausted, preventing the larger frequency from leaking into the answer.

- **Zero as a value:** `cnt[0]` is the count associated with key `0`; it is not confused with the dictionary's missing-value behavior. A positive count is truthy, and an exhausted count is false.

- **One-element arrays:** Equal values produce a one-element answer, while unequal values produce an empty answer. No special branch is required.

- **Input order and mutation:** The output happens to follow matching occurrences in `nums2`, and neither input is changed. These are properties of this source, although only the multiset content is required by the contract.

- **Counter entries reaching zero:** The source leaves exhausted keys in the counter with value zero. Removing them could reduce state during the scan, but it is unnecessary for correctness and does not improve the worst-case asymptotic bound.
