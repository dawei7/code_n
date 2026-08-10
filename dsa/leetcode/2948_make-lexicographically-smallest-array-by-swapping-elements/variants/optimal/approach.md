## General

Two values may be swapped directly when their difference is at most `limit`. Repeated operations make reachability transitive: if value $a$ can swap through $b$ and $b$ through $c$, occurrences carrying these values belong to one connected component and can be rearranged among that component's indices.

The source identifies these components after sorting values.

**Sort values together with original indices**

`arr = sorted(zip(nums, range(n)))`

creates pairs `(value, original_index)` ordered first by value. Keeping indices attached records where each component's values are allowed to end.

In sorted value order, start group at `i` and extend `j` while

`arr[j][0] - arr[j - 1][0] <= limit`.

If the gap between consecutive sorted values is small enough, those two occurrences can swap directly and connect their surrounding chains.

If the gap is greater than `limit`, no value on the lower side can swap with a value on the upper side: every cross-gap difference is at least that consecutive gap. The connected component ends.

**Why an entire chain can be permuted**

Within one group, consecutive sorted values are connected by allowed swaps. A connected graph's items can be permuted among its vertices using swaps along paths. Even if the smallest and largest values differ by more than `limit` and cannot swap directly, intermediate values can transport them through the component.

Thus the group values may be assigned arbitrarily to the original indices belonging to that group, while values cannot cross a group boundary.

**Lexicographically minimize each component**

For `arr[i:j]`, values are already sorted increasingly. The source extracts and sorts their original indices:

`idx = sorted(k for _, k in arr[i:j])`.

It then zips the increasing indices with the increasing value pairs and writes

`ans[k] = x`.

This places the smallest available component value at the earliest component index, the next smallest at the next index, and so on.

Lexicographic order gives absolute priority to the earliest position. Any assignment placing a larger component value at an earlier index while a smaller one occupies a later index can be improved by swapping those two values. Repeating this exchange yields the sorted-to-sorted assignment.

Components do not share reachable indices or values, so optimizing each independently produces the global lexicographically smallest array.


Every output assignment stays within a connected swap component, so it is reachable through allowed operations. No value is lost or duplicated because each sorted occurrence is zipped to exactly one group index.

For optimality, consider the first output index where another reachable array differs. Both arrays must draw from the same component at that index. The source assigns the smallest component value not already used at earlier component indices, so the other array cannot place a smaller value there. Therefore no reachable array is lexicographically smaller.

Duplicates are handled as separate `(value,index)` pairs. Their ordering among themselves is irrelevant, but multiplicity is preserved.

## Complexity detail

Sorting $n$ value-index pairs takes $O(n\log n)$. Across groups, sorting their index lists costs at most $O(n\log n)$ in total. Group scans and assignments are linear. Overall time is $O(n\log n)$.

`arr`, `ans`, and temporary index lists use $O(n)$ space. Temporary lists are per group, so their peak total remains linear.

The source returns a new array and does not modify `nums`.

## Alternatives and edge cases

- **Union-find over all value pairs:** Connecting every directly swappable pair is quadratic. Sorted consecutive gaps reveal the same components efficiently.
- **Map values to group queues:** Another method groups sorted values and pops the smallest group value while scanning original indices.
- **Sort the entire array blindly:** Incorrect when a gap greater than `limit` separates unreachable components.
- **Large endpoint difference inside a group:** It is still reachable through a chain of intermediate values.
- **Gap exactly equal to limit:** It connects groups because swaps allow `<= limit`.
- **Duplicate values:** Difference zero always connects them, and each occurrence remains represented.
- **One component:** The whole output is globally sorted.
- **Every gap too large:** Each component has one item and the output equals the input.
- **Index sorting:** Sorting only values is insufficient; smallest values must go to earliest reachable original positions.
- **Reachability versus one operation:** The solution relies on unlimited swaps and transitive component connectivity.
- **Why only consecutive sorted gaps matter:** If every neighboring pair along an interval is connected, the entire interval is one component. If one neighboring gap breaks, all cross-gap pairs differ by even more and no hidden edge can reconnect it.
- **Component indices need not be adjacent:** Swaps may choose any two array indices; connectivity depends on current values, so one component can occupy scattered original positions.
- **Assignment exchange proof:** If two component indices $p<q$ receive values $u>v$, exchanging them makes the first changed position smaller and therefore strictly improves lexicographic order.
- **Returned array is fresh:** Writing into `ans` preserves the original input while ensuring each index is assigned exactly once by its component.
