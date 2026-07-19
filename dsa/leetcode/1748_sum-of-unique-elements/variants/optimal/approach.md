## General
**Count occurrences in the bounded value domain**

Create a frequency array indexed by possible values. Because every element is in the fixed range from $1$ through $100$, each input value directly selects one counter. Scan `nums` once and increment the corresponding counter.

**Make uniqueness depend on the final count**

A value contributes precisely when its completed frequency equals one. After counting, inspect the possible values and add the index of every counter equal to one. Repeated values are excluded even if their first occurrence initially looked unique.

**Use the contract to keep storage constant**

The frequency array always has 101 entries, independent of $n$. This is constant auxiliary space under the stated bounds, while still giving direct and unambiguous frequency information.

## Complexity detail
Counting all $n$ elements takes $O(n)$ time. Inspecting the fixed 100-value domain adds $O(100)$ work, so the total remains $O(n)$. The 101 counters use $O(100)=O(1)$ auxiliary space because the value range is fixed by the contract.

## Alternatives and edge cases
- **Hash map:** Counting only encountered values is also $O(n)$ time, but uses $O(u)$ space for $u$ distinct values instead of exploiting the bounded domain.
- **Incremental unique sum:** Add a value on its first occurrence and subtract it on its second; later occurrences make no change. This avoids the final domain scan but needs careful state transitions.
- **Repeated full scans:** Calling a linear count operation for every element is correct but takes $O(n^2)$ time.
- **No unique values:** The result is zero when every value appears at least twice.
- **All values unique:** Every array element contributes to the result.
- **More than two occurrences:** A value contributes nothing whether it appears twice or many times.
- **Boundary values:** Values `1` and `100` are valid and require correctly sized frequency storage.
