## General

**Find the first place where order fails**

An array is non-decreasing when every adjacent pair satisfies `nums[i] <= nums[i + 1]`. The outer loop scans from left to right until it finds the first inversion:

`a = nums[i] > nums[i + 1] = b`.

If no inversion exists, the array is already valid and using zero modifications satisfies “at most one,” so the method returns `True`.

Once the first inversion is found, any successful one-element repair must change one of its two elements. Changing any unrelated position would leave `a > b` untouched. The exact solution therefore tests the two meaningful repair directions and then returns immediately.

**The helper verifies the entire array**

`is_sorted(nums)` uses `pairwise` to generate every adjacent pair and `all` to verify `a <= b` for all of them.

The helper short-circuits at the first failed comparison. It allocates no list of pairs; `pairwise` and the generator expression produce values lazily.

Checking the entire array after a candidate modification is simple and robust. It automatically catches:

- a new inversion created with the element before the changed position;
- a new inversion created with the element after it;
- a separate original inversion farther to the right.

**First candidate: lower the left value**

For inversion `a > b`, changing the left element requires its new value to be at most `b`. The code chooses the canonical value `b`:

`nums[i] = b`.

Why is testing exactly `b` enough? It is the largest value that fixes the current pair. A larger choice would not fix `a > b`. A smaller choice would only make it harder to remain at least as large as the previous neighbor. Therefore:

- if setting the left element to `b` preserves global order, a valid repair exists;
- if it violates the previous boundary, no still-smaller value could repair that boundary.

The helper checks the complete array. If sorted, return `True` immediately.

For `[4, 2, 3]`, lowering four to two gives `[2, 2, 3]`, which is non-decreasing.

**Second candidate: raise the right value**

If lowering the left element fails, the code executes:

`nums[i] = nums[i + 1] = a`.

This chained assignment restores `nums[i]` to its original value `a` and changes the right element from `b` to `a`. Operationally, only the right member of the original array is modified.

Any repair that changes the right element must raise it to at least `a`. Choosing exactly `a` is the smallest such value, so it is easiest to keep no larger than the following neighbor. If this smallest legal raise still creates a right-side inversion, no larger value could do better.

The method returns the result of one final global sortedness check.

**Why the two canonical values cover all possibilities**

At the first inversion, a one-change solution has only two structural choices.

If it changes the left value, that value must be no greater than `b`. Setting it to the maximum allowed value `b` is best for satisfying the preceding relation. Thus any viable left-side repair implies the tested repair is viable.

If it changes the right value, that value must be at least `a`. Setting it to the minimum allowed value `a` is best for satisfying the following relation. Thus any viable right-side repair implies the tested repair is viable.

If neither canonical modification makes the entire array sorted, no other single value or position can succeed.

**A case where neighboring context matters**

Consider `[3, 4, 2, 3]`. The first inversion is four followed by two.

- Lowering four to two gives `[3, 2, 2, 3]`, creating an inversion with the previous three.
- Restoring four and raising two to four gives `[3, 4, 4, 3]`, leaving an inversion with the final three.

Both choices fail, so the answer is `False`. Merely counting the original visible inversion would not be sufficient; the repair must fit both sides.

**Why the first inversion is sufficient**

The prefix before the first inversion is already non-decreasing by definition. Any one-element solution must fix this inversion by changing one of its endpoints. The two tests explore both endpoint choices and use a full scan to validate the prefix boundary and every suffix relation.

No later inversion needs separate branching. If one remains after a candidate change, the helper rejects that candidate because repairing it would require a second modification.

**Input mutation is observable**

The exact solution changes `nums` in place while testing:

- a successful left-lowering return leaves that modification in the list;
- the right-raising path leaves the right value changed whether the final answer is true or false.

The problem asks only for a Boolean and permits this in the judge. A caller that requires input preservation should work on a copy or restore both values before returning.

## Complexity detail

Let `N` be the array length.

The outer scan examines at most `N - 1` adjacent pairs. After the first inversion, `is_sorted` runs once for the left candidate and, only if that fails, once for the right candidate. Each verification is `O(N)`. A constant number of linear scans gives total time `O(N)`.

The implementation uses scalar variables and lazy iterators whose size does not grow with `N`, so auxiliary space is `O(1)`. The input is modified in place; that mutation does not allocate an additional array.

Although the source may traverse portions of the array up to three times, constant factors do not change the linear bound.

## Alternatives and edge cases

- **Single-pass greedy repair:** At the first inversion, inspect the previous neighbor to decide immediately whether to lower the left value or raise the right, then continue scanning for a second inversion. This avoids full rescans while retaining `O(N)` time and `O(1)` space.

- **Try modifications on a copy:** Preserves the caller's input but uses `O(N)` additional space.

- **Count inversions only:** This is insufficient because repairing one inversion can create another with an adjacent element, as in `[3, 4, 2, 3]`.

- **Sort and compare:** Sorting changes many positions and costs `O(N log N)`. It does not directly prove that one element modification is enough.

- **One-element array:** There are no adjacent pairs, so it is already non-decreasing.

- **Two-element inversion:** Either endpoint can be changed to the other, so the first candidate succeeds.

- **Equal adjacent values:** Equality is allowed. The violation condition must be `>`, not `>=`.

- **Inversion at index zero:** Lowering the first value has no preceding boundary to violate and will fix that pair; later order is still checked.

- **Inversion at the final pair:** Raising the last value has no following boundary, while lowering the left value may or may not fit the prefix.

- **Multiple separated inversions:** Neither one-element candidate can remove all of them, and the global helper returns `False`.

- **Negative values:** Only ordering matters, so signs require no special handling.

- **Successful left candidate:** The method returns before restoring `nums[i]`, leaving the list modified.

- **Failed final candidate:** The exact code also leaves the right element raised on a `False` return. This side effect should be documented for non-judge callers.

- **At most one modification:** An already sorted array correctly returns `True` without changing anything.
