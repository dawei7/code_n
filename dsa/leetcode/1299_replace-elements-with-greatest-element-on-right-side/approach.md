## General

For every index, the required replacement depends only on elements strictly to its right. A left-to-right scan does not yet know those future values. A right-to-left scan, however, has already seen exactly the suffix needed for the next replacement.

The Optimal solution maintains one number, `mx`, representing the greatest original value strictly to the right of the index currently being processed. It overwrites the input array in place and then updates `mx` to include the original current value for the next iteration.

**Why the scan starts with negative one**

The last element has no elements to its right and must be replaced with `-1`. The code initializes `mx = -1` so that the same assignment used everywhere automatically handles the last index.

The input values are all at least one, so `-1` is smaller than every original value. After the last element is processed, taking a maximum with its positive original value removes the sentinel from future suffix maxima. Even without that ordering fact, the explicit requirement for the last replacement makes `-1` the correct initial answer for the empty right suffix.

**Visiting indices in reverse**

`reversed(range(len(arr)))` produces the indices

$$
n-1,\;n-2,\;\ldots,\;1,\;0.
$$

It does not reverse the array contents. It only determines the order in which positions are visited. This avoids making a reversed copy and ensures that, before index `i` is handled, every index greater than `i` has already contributed its original value to `mx`.

**Saving the original value before overwriting**

Inside the loop, the first operation is

`x = arr[i]`.

The temporary `x` is essential because the next statement, `arr[i] = mx`, destroys the original value at index `i`. That original value must still become a candidate for the suffix maximum used at index `i - 1`.

After saving it, the algorithm writes `mx` into `arr[i]`. At this moment, `mx` summarizes only original elements at indices greater than `i`, so it is exactly the greatest element strictly to the right. It intentionally does not yet include `x`; including the current element would violate the word “right.”

Finally,

`mx = max(mx, x)`

expands the summary to include the original value at index `i`. When the loop moves to `i - 1`, the indices strictly to its right are `i` through `n - 1`, exactly the values now represented by the updated maximum.

Changing the order of these operations would break the solution. If `arr[i]` were overwritten before its original value was saved, that value could never influence earlier positions. If `mx` were updated with `x` before assignment, the replacement at `i` could incorrectly use the element itself.

**A complete trace**

Take `arr = [17,18,5,4,6,1]`.

- Before index $5$, `mx` is $-1$. Save $1$, write $-1$, and update `mx` to $1$.
- Before index $4$, `mx` is $1$, the greatest original value to its right. Save $6$, write $1$, and update `mx` to $6$.
- Before index $3$, save $4$, write the current maximum $6$, and keep `mx` at $6$.
- Before index $2$, save $5$, write $6$, and again keep `mx` at $6$.
- Before index $1$, save $18$, write $6$, and update `mx` to $18$.
- Before index $0$, save $17$, write $18$, and keep `mx` at $18$.

The final array is `[18,6,6,6,1,-1]`.

This trace also demonstrates why already overwritten suffix cells do not cause trouble. The algorithm never reads them to recompute a maximum. Their original information has already been compressed into `mx`.

**The loop fact that guarantees the answer**

Immediately before processing index `i`, `mx` equals the maximum of the original values in positions `i + 1` through `n - 1`. For the last index, this range is empty and `mx = -1` is exactly the required special replacement, so the fact holds at the beginning.

Assuming it holds at some index, assigning `arr[i] = mx` writes the required result there. Saving `x` preserved the original current value. Updating with `max(mx, x)` then produces the maximum over original indices `i` through `n - 1`, which is exactly the set strictly to the right of the next index `i - 1`. Thus, the fact continues to hold as the scan moves left.

By the time the loop ends, every index has received the maximum of its original right suffix, and the final position has received `-1`. Returning `arr` therefore returns the required transformed array.

**Why in-place modification is safe**

Ordinarily, overwriting input while later computations still depend on it can be dangerous. Here, the traversal direction and saved scalar remove that danger. Once position `i` is overwritten, its original value is already in `x` and then folded into `mx`. No later iteration needs to inspect the original suffix array directly.

The function returns the same list object it received, now modified. This matches the requested output, but callers should be aware that their original list does not remain unchanged.

## Complexity detail

Let $n$ be the length of `arr`. `range` and `reversed` provide an iterator over the indices without constructing an $n$-element reversed list. The loop runs exactly once per element.

Each iteration performs one array read, one array write, one maximum comparison, and a constant number of assignments. Therefore, the running time is $O(n)$.

The only additional data are `mx`, `i`, `x`, and iterator state, all constant-sized. The array itself is reused as the output, so auxiliary space is $O(1)$. If an API required preserving the input, copying it for the result would instead require $O(n)$ output storage, but that is not what the exact source does.

The returned array necessarily contains $n$ elements, yet it is the existing input allocation rather than a new auxiliary structure. Complexity analyses normally do not count the required output object as extra working space; here even that output object is reused.

## Alternatives and edge cases

- **Precompute a suffix-maximum array:** A separate array can store the maximum beginning at every position, after which each answer uses the next entry. It is correct and linear-time but uses $O(n)$ extra space when one running maximum is sufficient.
- **Scan to the right for every index:** This direct method is easy to state but repeats comparisons across overlapping suffixes and costs $O(n^2)$ time.
- **Monotonic stack:** A stack is useful for the next greater element, but this task needs the greatest value anywhere to the right. A single suffix maximum is simpler and uses less machinery.
- **Left-to-right traversal:** Without preprocessing, it cannot know future values. Attempting to maintain a prefix maximum solves the opposite problem.
- **Single-element array:** The reverse loop runs once with `mx = -1`, so the only value becomes `-1`.
- **Strictly increasing values:** Each position becomes the original final value, except the final position becomes `-1`, because that last value is the greatest in every earlier right suffix.
- **Strictly decreasing values:** Each position becomes its immediate right neighbor, since that neighbor is the greatest value in the remaining suffix.
- **Duplicate maximum values:** `max` handles ties naturally. The output needs the greatest value, not the position of a unique greatest element.
- **Saving before writing:** Removing `x = arr[i]` or moving it after the overwrite loses original data and gives wrong maxima to earlier indices.
- **Updating after writing:** `mx` must represent a strictly-right suffix during assignment. Updating it with the current value first would allow an element to replace itself.
- **Positive-value constraint:** It makes the `-1` sentinel smaller than all originals. The final-element rule is still explicit, but a generalized problem with arbitrary negative values should reason about the empty suffix separately rather than treating `-1` as a universal mathematical identity.
- **Input mutation visible to callers:** The returned object is `arr` itself. If preserving the caller's list matters outside the problem contract, the method should first copy it, accepting $O(n)$ additional space.
- **No empty-array case:** The contract guarantees at least one element. If an empty list were supplied outside the contract, the loop would do nothing and return an empty list, though the problem does not define a special last element for that case.
