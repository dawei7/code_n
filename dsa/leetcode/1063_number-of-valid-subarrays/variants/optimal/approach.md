## General

**Count valid endings for every fixed start**

A subarray beginning at index `i` is valid when `nums[i]` is less than or equal to every later value included in that subarray.

As the right endpoint moves right, validity continues until the first value strictly smaller than `nums[i]`. That smaller value makes the subarray invalid, and every still-longer subarray remains invalid because it continues to contain the same offending value.

Therefore, for each index `i`, the entire problem reduces to finding:

```text
the nearest index j > i such that nums[j] < nums[i]
```

If such an index is `j`, valid right endpoints are `i, i + 1, ..., j - 1`, giving `j - i` valid subarrays starting at `i`. If no smaller value exists, use a virtual boundary `j = n`, and all `n - i` suffix prefixes starting at `i` are valid.

The exact solution finds all of these next-strictly-smaller boundaries with a monotonic stack.

**Initialize every boundary to the virtual end**

The code begins with:

```python
n = len(nums)
right = [n] * n
stk = []
```

`right[i]` will store the first index to the right whose value is strictly smaller than `nums[i]`. It is initialized to `n`, one position beyond the final valid array index.

That default already represents the correct answer for positions having no smaller value to their right. The code only overwrites it when the stack reveals a real boundary.

`stk` stores indices rather than values because the final count needs boundary positions. Values remain available through `nums[index]`.

**Scan from right to left**

The loop is:

```python
for i in range(n - 1, -1, -1):
```

When processing `i`, every position to its right has already been considered. The stack summarizes the only right-side indices that can still be the nearest smaller boundary for some position farther left.

From bottom to top, stack indices move from farther right to nearer right, while their values are strictly increasing. The top is therefore the nearest retained candidate.

**Discard values that are not strictly smaller**

Before selecting a boundary, the code pops:

```python
while stk and nums[stk[-1]] >= nums[i]:
    stk.pop()
```

Any candidate with value greater than or equal to `nums[i]` cannot invalidate a subarray beginning at `i`. The contract allows the leftmost value to be equal to other values, so equality must be removed along with larger values.

Popping is also safe for future positions farther left. The current index `i` is closer to every future left index than the popped index is, and `nums[i]` is less than or equal to the popped value. If a future start needs a smaller boundary and the popped value qualifies, the current value qualifies at least as well and occurs earlier. The popped index can never again be the nearest useful candidate.

This domination argument is what lets the stack forget most indices without losing an answer.

After the loop, either the stack is empty or its top value is strictly smaller than `nums[i]`.

**Why the remaining top is the nearest smaller value**

If the stack is nonempty, the assignment is:

```python
if stk:
    right[i] = stk[-1]
```

The top qualifies because all non-smaller values were popped. It is the nearest qualifying index because stack order places nearer retained indices toward the top.

Could a closer smaller index have been removed earlier? No. An index is removed only when an even closer processed index has a value less than or equal to it. Following that chain of dominations leads to a retained candidate that is at least as close and no larger. If the removed value was strictly below `nums[i]`, its dominating replacement is also strictly below `nums[i]` and appears above any farther candidate. Thus the top is the true first smaller boundary.

If the stack becomes empty, no processed index can be the required smaller value. `right[i]` correctly remains `n`.

**Push the current index for future starts**

After recording its boundary, the solution runs:

```python
stk.append(i)
```

Index `i` is now the nearest processed position for the next iteration. The preceding pop loop has removed every stack value greater than or equal to `nums[i]`, so any remaining top has a strictly smaller value. Appending `i` restores the strictly increasing value order from bottom to top.

The current index may later be popped by an even smaller or equal value to its left. Until then, it is a useful candidate boundary.

**Trace a representative example**

For `nums = [1, 4, 2, 5, 3]`, scan from the right:

- Index four with value three has no right candidate, so its boundary is five.
- Index three with value five sees value three on top, so its boundary is four.
- Index two with value two pops five and three because neither is smaller than two. Its boundary remains five.
- Index one with value four sees value two at index two, so its boundary is two.
- Index zero with value one pops all remaining non-smaller values and keeps boundary five.

The boundary array is `[5, 2, 5, 4, 5]`. Contributions are five, one, three, one, and one, totaling 11.

For the first position, every subarray is valid because one is no larger than any later value. For index one, only the single-element subarray is valid because value two at index two is smaller than four.

**Convert each boundary into a count**

The final line is:

```python
return sum(j - i for i, j in enumerate(right))
```

`enumerate(right)` produces each start index `i` and its stored boundary `j`.

The right endpoints that preserve validity are exactly the indices from `i` through `j - 1`. The number of integers in that inclusive range is `j - i`. The generator computes that contribution for every start, and `sum` adds all contributions.

Every nonempty subarray has one unique left endpoint, so counting valid right endpoints separately for each start neither misses nor double-counts a subarray.

**Why strict inequality is essential**

The invalidating event is a value smaller than the leftmost value, not a value equal to it. For `[2, 2, 2]`, all six nonempty subarrays are valid.

The stack loop uses `>=` when deciding what to pop. Equal values are removed so the search continues past them to a truly smaller value. If it used only `>`, an equal value could be left on top and incorrectly treated as the stopping boundary.

**Why the whole algorithm is correct**

For every index, the monotonic-stack scan finds the nearest strict-smaller value to its right or the virtual endpoint `n` when none exists. Before that boundary, every included value is at least `nums[i]`, so each endpoint creates a valid subarray. At and after the boundary, the strict-smaller value is included, so every such subarray is invalid.

The contribution `right[i] - i` is therefore exact for each start. Summing these disjoint groups yields the total number of valid subarrays.

## Complexity detail

Let `N` be the length of `nums`.

Each index is pushed onto `stk` exactly once. An index can be popped at most once. Although the `while` loop is nested syntactically inside the scan, all pop operations across the complete algorithm total at most `N`. The scan therefore takes `O(N)` amortized time.

Building the final sum also visits `N` boundaries, so total time remains `O(N)`.

`right` stores `N` integers. The stack may also hold `N` indices, for example when values are strictly increasing from left to right in the relevant scan pattern. Auxiliary space is `O(N)`.

These exact bounds match the manifest.

## Alternatives and edge cases

- **Left-to-right monotonic stack:** Push starts while scanning forward. When a strictly smaller value arrives, pop each invalidated start and add the distance to its contribution; after the scan, use `n` for remaining starts. This reaches the same `O(N)` time and space.
- **Quadratic expansion:** For each start, extend right until a smaller value appears. It is simple but takes `O(N^2)` time on non-decreasing input.
- **Segment tree plus searches:** Range minima can help locate a smaller value, but the structure is more complex and typically costs `O(N log N)`, worse than the monotonic stack.
- **One element:** `right[0]` remains one, so the sole single-element subarray contributes one.
- **Strictly increasing array:** No later value is smaller than any start. Every subarray is valid, and the total is `N(N + 1) / 2`.
- **Strictly decreasing array:** The next index is smaller for every start except the last. Only single-element subarrays are valid, so the result is `N`.
- **All values equal:** Equal values are popped by `>=` and never act as boundaries. Every subarray is valid.
- **Duplicate values followed by a smaller value:** The scan looks past all equal values and assigns the later strictly smaller boundary to the appropriate starts.
- **Zero values:** Zero is the minimum allowed value. It cannot have a strictly smaller non-negative value to its right, so every suffix prefix beginning there is valid.
- **Virtual boundary n:** This sentinel is not read from `nums`. It only makes the no-smaller count use the same subtraction formula.
- **Large answer:** The number of subarrays can be quadratic in `N`. Python integers grow as needed, so the sum does not overflow.
- **Stack stores indices:** Storing only values would lose the position needed to compute `j - i`. Indices provide both value access and distance.
- **Input preservation:** The algorithm reads `nums` without modifying it and stores all derived information separately.
