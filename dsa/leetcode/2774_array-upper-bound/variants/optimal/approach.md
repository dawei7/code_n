## General

**Search for a boundary, not merely for an equal element**

The array is sorted in ascending order and may contain duplicates. An ordinary binary search that returns as soon as it sees `target` could return any occurrence. The required answer is the last occurrence.

The exact method instead searches for the first index whose value is strictly greater than `target`. Once that upper boundary is known, the position immediately before it is the last value less than or equal to `target`. A final equality check decides whether that position is actually a target occurrence.

This boundary formulation handles duplicates without maintaining a separate “best match seen so far” variable.

**Use a half-open search interval**

`left` starts at zero and `right` starts at `this.length`, one position beyond the last valid array index. The active search interval is `[left, right)`: it includes `left` but excludes `right`.

Allowing `right` to equal the length is important. If every array value is at most `target`, then the first value greater than `target` does not exist inside the array; its insertion boundary is naturally `this.length`.

The loop continues while `left < right`. The midpoint

`Math.floor((left + right) / 2)`

is always a valid index in the nonempty half-open interval.

**The boundary invariant**

The search maintains two facts:

- every index strictly before `left` contains a value less than or equal to `target`;
- every index at or after `right`, when it is an actual array index, contains a value greater than `target`.

Initially both regions are empty, so the statements are trivially true.

At `middle`:

- If `this[middle] <= target`, then sorted order implies every index through `middle` also has a value at most `target`. None can be the first greater value, so set `left = middle + 1`.
- Otherwise `this[middle] > target`. The boundary could be `middle` or somewhere earlier, so set `right = middle` rather than discarding `middle`.

Each update preserves the invariant and strictly shortens the interval.

**What termination means**

When `left == right`, no unknown position remains. The invariant says all earlier positions are at most `target` and all later positions are greater. Thus `left` is exactly the first index containing a value greater than `target`, or the array length if there is no such value.

The code sets `candidate = left - 1`. If any target exists, all copies are consecutive in a sorted array, and the final copy must be immediately before the first greater value. Therefore `candidate` is the only possible answer.

However, `candidate` could contain a smaller value when the target is absent. The return expression checks both:

- `candidate >= 0`, so there is a preceding array element;
- `this[candidate] === target`, so that element is an exact match.

Only then does it return the index; otherwise it returns `-1`.

**A duplicate walkthrough**

For `[3, 4, 6, 6, 6, 6, 7]` with target 6, the predicate “value is at most 6” is true through index five and false from index six onward. Binary search narrows to boundary six. The candidate is five, and the equality check succeeds, so the result is the last 6.

For `[1, 4, 5]` with target 2, the first value greater than 2 is at index one. Candidate zero contains 1 rather than 2, so the method returns `-1`.

For target 5 in `[3, 4, 5]`, every element is at most the target. The boundary becomes three, candidate becomes two, and the final value matches.

**Why strict and non-strict comparisons are placed this way**

The condition `this[middle] <= target` deliberately sends equal values to the discarded left region. That forces the search to continue to the right of every duplicate. Using `< target` instead would find the first value greater than or equal to the target, which is the lower bound and points to the first occurrence rather than the last.

Likewise, when a value is greater, assigning `right = middle` keeps that position as a possible boundary. Using `middle - 1` would mix closed-interval rules into a half-open search and could skip the answer.

**Prototype method behavior**

The implementation assigns the function to `Array.prototype.upperBound`. Therefore any ordinary array inherits the method, and `this` inside the function is the receiving array. The algorithm allocates no copy and does not modify array contents.

Its correctness assumes `this` is sorted ascending according to the same numerical comparisons used by `<=` and `===`. That sortedness is part of the problem contract.

## Complexity detail

Let `n` be the array length. Each iteration reduces the remaining interval to at most about half its previous size. After `O(log n)` iterations, `left` equals `right`. Each iteration performs constant work, and the final validation is constant time. Total time is `O(log n)`.

Only `left`, `right`, `middle`, and `candidate` are stored. Auxiliary space is `O(1)`. The search is iterative, so there is no recursion stack, and the input array is not copied.

`Math.floor((left + right) / 2)` uses JavaScript number arithmetic rather than a bitwise shift. At the stated length of at most `10^4` either is safe, but avoiding bitwise conversion also avoids imposing a signed 32-bit interpretation on indices in more general use.

## Alternatives and edge cases

- **Linear scan:** Remembering the last matching index is simple but costs `O(n)` and ignores the sorted-order opportunity.
- **Built-in `lastIndexOf`:** It has the desired equality behavior but also scans linearly.
- **Stop at the first equality:** Ordinary binary search may return a middle duplicate rather than the last occurrence.
- **Search for the lower bound:** The first value greater than or equal to target identifies the first occurrence, not the last. Upper bound minus one is the needed boundary.
- **Target smaller than every element:** The upper boundary is zero, candidate is `-1`, and the guard returns `-1` without indexing as a match.
- **Target larger than every element:** The boundary is `n`. The last index is checked and returned only if it equals the target; otherwise absence is reported.
- **All elements equal target:** The boundary advances to `n` and candidate `n - 1` is the correct last occurrence.
- **One-element array:** The method returns zero for a match and `-1` otherwise.
- **Duplicates at the end:** The half-open interval allows the boundary to be `n`, so the last duplicate is found correctly.
- **Target between two values:** Candidate is the smaller neighbor, but the final strict equality check prevents a false match.
- **Empty array outside the stated constraint:** The loop is skipped, candidate is `-1`, and the method still returns `-1` safely.
- **Unsorted receiver:** The monotonic boundary invariant fails, so results are unspecified; sorted ascending order is essential.
- **`NaN` values or target:** JavaScript comparisons with `NaN` are not a normal numerical order. Such values are outside the stated sorted-number contract.
- **Prototype modification:** Adding methods globally can affect enumeration in unrelated code, but the challenge explicitly requests an Array prototype enhancement.
