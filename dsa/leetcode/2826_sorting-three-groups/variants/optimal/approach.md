## General

Removing elements while preserving the others' order means choosing a subsequence. A non-decreasing subsequence is already a valid final array, and deleting every element outside it costs `len(nums) - kept_length`. Minimizing deletions is therefore equivalent to maximizing the length of a non-decreasing subsequence.

Only three values can appear, so store `longest[0]`, `longest[1]`, and `longest[2]`, where `longest[v - 1]` is the greatest length of a non-decreasing subsequence in the processed prefix that ends with value $v$.

When the current value is $v$, it may extend any retained subsequence ending in a value at most $v$, or start a new subsequence. Thus its new state is one plus the maximum among the states for $1$ through $v$. States ending in the other values remain unchanged because skipping the current element is always permitted.

**Why one state per ending value is sufficient**

Among two subsequences ending in the same value, only the longer one can be better for every future extension: both accept exactly the same future values. Keeping the maximum length therefore loses no useful choice.

After each processed prefix, every state is attainable by construction. Conversely, take any non-decreasing subsequence in that prefix and inspect its last value $v$. Removing that last value leaves a valid subsequence ending at most at $v$, which the previous states represent with at least the same prefix length. The transition therefore represents every attainable extension. By induction, the maximum final state is exactly the longest non-decreasing subsequence length, and subtracting it from $n$ gives the minimum deletions.

## Complexity detail

Let $n$ be the length of `nums`. Each value updates one state using at most three entries, so the total time is $O(n)$. The three-state array has fixed size and uses $O(1)$ auxiliary space.

The benchmark repeats descending triples. This implementation still performs constant work per element, whereas the conventional index-based longest-subsequence dynamic program compares each position with every earlier position and grows quadratically.

## Alternatives and edge cases

- **Index-based subsequence dynamic programming:** Store the best subsequence length ending at every index and inspect all earlier positions. It is correct but takes $O(n^2)$ time and $O(n)$ space.
- **Patience sorting with upper bound:** Computing the longest non-decreasing subsequence using binary search takes $O(n \log n)$ time and $O(n)$ space, but the alphabet of three values permits the simpler linear constant-state method.
- **Enumerate group boundaries:** Try every split between the `1`, `2`, and `3` regions and count retained values. A direct pair of boundaries takes $O(n^3)$ without prefix counts or $O(n^2)$ with them.
- **Deletion semantics:** An operation removes an element; it never changes its value or moves it elsewhere.
- **Equal values:** Repeated equal values may all be retained because the target order is non-decreasing, not strictly increasing.
- **Missing groups:** A valid result may contain only one or two of the three values.
- **Singleton or sorted input:** The full array is already non-decreasing, so the answer is zero.
