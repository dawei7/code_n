## General

The exact solution uses the strict-increasing guarantee in a counting argument. It concatenates all three arrays, counts every value, and then scans `arr1` in its original increasing order. A value is returned exactly when its total count is three.

**Why a total count of three means one occurrence in every array**

Every input array is strictly increasing. Therefore, a value can occur at most once in `arr1`, at most once in `arr2`, and at most once in `arr3`.

Across all three arrays, the maximum possible total frequency of any value is consequently three. Reaching three is possible only through one occurrence from each array. A value appearing in only one or two arrays has total count one or two.

This equivalence would fail if duplicates were allowed within an array. Three copies in `arr1` alone could falsely imitate membership in all arrays. The strict-order contract is therefore essential to this implementation.

**Build the combined counter**

`arr1 + arr2 + arr3` constructs one list containing all occurrences from the three inputs. `Counter(...)` then maps each distinct integer to its total frequency in that combined sequence.

For the first example, values one and five each appear once in every input, so their counter entries are three. Values such as two or three appear in only two arrays, so their entries are two.

The concatenation is not merely conceptual in Python. The `+` operations allocate new list storage before the counter is built. That exact memory behavior matters when describing complexity.

**Use `arr1` to produce sorted output**

The result comprehension is:

`[x for x in arr1 if cnt[x] == 3]`.

Any common value must occur in `arr1`, so scanning only that array cannot miss an answer. Because `arr1` is strictly increasing, selected values are emitted in increasing order automatically.

There is no need to sort counter keys. Hash-map iteration order is irrelevant because the output order comes from `arr1`.

There is also no need to deduplicate the result. Strict increase guarantees that `arr1` itself contains each candidate once.

**Following the example**

For `arr1 = [1, 2, 3, 4, 5]`, the comprehension examines candidates in that order. The counter count for one is three, so one is included. Counts for two, three, and four are below three, so they are skipped. Five has count three and is included. The returned list is `[1, 5]`.

If there is no common element, no scanned value has count three and the comprehension naturally produces an empty list.

**Why the result is exact**

If the method includes `x`, its combined count is three. Since each array can contribute at most one, all three arrays must contain it. Every output value is valid.

Conversely, if `x` belongs to all three arrays, it contributes exactly three combined occurrences. It also appears during the `arr1` scan, passes the condition, and is included. Every common value is returned.

Finally, `arr1`’s ordering proves the output is sorted. These three facts establish membership, completeness, and order.

## Complexity detail

Let $N=n_1+n_2+n_3$ be the total number of input elements.

List concatenation copies $O(N)$ references. Building the counter scans the combined list in expected $O(N)$ time. The result scan takes $O(n_1)$ expected time for hash lookups. Total expected time complexity is $O(N)$.

The exact implementation uses $O(N)$ temporary space for concatenation. The counter stores $O(u)$ entries for $u$ distinct values, with $u\leq N$. The returned result can contain at most $\min(n_1,n_2,n_3)$ values. Thus auxiliary space is $O(N)$, not $O(1)$ for this exact code, even though a three-pointer alternative can achieve constant auxiliary space.

Python evaluates chained list additions by creating an intermediate list for `arr1 + arr2` and then the final combined list. Peak storage remains $O(N)$.

## Alternatives and edge cases

- **Three pointers:** Compare the current values, advance a pointer that is too small, and advance all three on equality. This uses $O(1)$ auxiliary space and $O(N)$ time.
- **Set intersection:** Convert each array to a set and intersect them, then sort. This is concise but uses linear extra storage and does not exploit sorted traversal.
- **Binary search:** Test each value of the shortest array in the other two arrays. This uses little extra space but costs logarithmic searches.
- **One common value:** It appears once in each array, reaches count three, and is returned once.
- **No intersection:** The comprehension returns `[]`.
- **Different array lengths:** Counting is independent of length; all that matters is one occurrence from each.
- **Strict increase:** It simultaneously prevents false count-three results and guarantees sorted, duplicate-free output.
- **Bounded values:** A fixed frequency array could replace the counter because values are at most 2000.
- **Hashing complexity:** Counter construction and lookups use the standard expected $O(1)$ hash-table model.
- **Allocated concatenation:** Using `Counter(chain(arr1, arr2, arr3))` could avoid the combined list, but that is not the stored implementation.
