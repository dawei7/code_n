## General

**What the expected arrangement means**

The students currently stand in the order recorded by `heights`. The school wants them arranged in non-decreasing height order. Non-decreasing means that every height is at least the height immediately before it. Equal heights are allowed, so a sequence such as `[1, 1, 3, 3, 7]` is correctly ordered.

The task does not ask us to move the students or report the correct arrangement. It asks for the number of indices whose current height differs from the height that belongs at that index in the expected arrangement.

That distinction matters. Suppose the current sequence is `[1, 2, 1]`. Its expected sequence is `[1, 1, 2]`. Index zero already contains the expected value. Indices one and two do not, so the answer is two. We compare the two sequences position by position; we do not merely ask whether the input contains the right collection of heights, because it obviously does.

The expected height sequence is determined uniquely by sorting all values into non-decreasing order. Duplicate heights do not create ambiguity for this problem. Two students of the same height may exchange identities, but the value placed at each index remains the same. Since the answer depends only on heights, not student identities, a sorted list of height values is exactly the reference sequence we need.

**Build the reference sequence without changing the input**

The first line is:

```python
expected = sorted(heights)
```

Python's `sorted` function reads every value from `heights` and returns a new list whose values are in ascending, and therefore non-decreasing, order. The original `heights` list remains unchanged.

Keeping both lists is essential to this implementation. `heights` represents what we actually observe, while `expected` represents what should be at every position. If the code instead called `heights.sort()` and did not first preserve the original order, it would lose the very information it needs to find mismatches. After an in-place sort, comparing the list with itself would incorrectly produce zero for every input.

For example, with `heights = [1, 1, 4, 2, 1, 3]`, sorting produces `expected = [1, 1, 1, 2, 3, 4]`. This one operation does all of the ordering work. The remaining task is a linear positional comparison.

**Align corresponding indices**

The expression `zip(heights, expected)` produces pairs in matching index order. Its first pair contains `heights[0]` and `expected[0]`, its second pair contains the two values at index one, and so on.

Normally, `zip` stops when its shorter input is exhausted. That behavior cannot hide any value here because `expected` was created by sorting `heights`. Sorting neither inserts nor removes elements, so the two lists always have exactly the same length. Consequently, `zip` visits every valid index exactly once.

For the example above, the aligned pairs are:

```text
(1, 1), (1, 1), (4, 1), (2, 2), (1, 3), (3, 4)
```

The first, second, and fourth pairs match. The third, fifth, and sixth pairs differ. Therefore the correct answer is three.

**Turn each comparison into one contribution**

For each aligned pair, the generator evaluates `a != b`. The result is a Boolean value:

- `False` when the current height already equals the expected height.
- `True` when the two values differ and this index must be counted.

In Python, Boolean values participate in integer addition: `False` contributes zero and `True` contributes one. Therefore:

```python
sum(a != b for a, b in zip(heights, expected))
```

adds exactly one for every mismatching index and nothing for every matching index. The generator supplies comparisons to `sum` one at a time, so it does not build a separate list of Boolean results.

The `return` statement immediately gives this total as the answer. No explicit counter or indexed loop is necessary because the generator and `sum` express the same counting process directly.

**Why this produces the correct count**

Sorting `heights` produces a sequence containing exactly the original multiset of values in non-decreasing order. That is precisely the expected sequence defined by the problem.

Now consider any index `i`. The aligned comparison for that index is true exactly when `heights[i]` is different from `expected[i]`. According to the problem, that is exactly the condition under which index `i` must contribute one to the answer. If the values are equal, the comparison is false and the index correctly contributes zero.

The two lists have equal length, so every index is considered once. No index is duplicated, skipped, or compared with the wrong expected position. Summing all of these zero-or-one contributions therefore equals the number of indices at which the current and expected sequences differ.

Notice that this reasoning does not depend on all heights being distinct. If several students share a height, the sorted reference contains the same number of copies of that height. A position holding the correct height is counted as correct even if one imagines a different same-height student standing there. This matches the value-based contract.

**Why sorting is a natural direct solution**

The phrase "expected order" suggests constructing that order explicitly. Once the sorted copy exists, the definition of the answer becomes a simple comparison. This keeps the implementation short and makes its correctness easy to inspect.

The constraints also make comparison sorting entirely practical. Even though a counting method can use the small height range to improve the asymptotic bound, the exact solution is already fast for the allowed input sizes. Its main conceptual advantage is that it mirrors the problem statement: construct the expected sequence, compare it with the current sequence, and count differences.

## Complexity detail

Let `N` be the number of students.

Creating `expected` with Python's comparison sort takes `O(N log N)` time in the general case. The subsequent `zip` traversal performs `N` constant-time comparisons, so it takes `O(N)` time. The sorting term dominates, giving the exact implementation a total time complexity of `O(N log N)`.

The new sorted list stores `N` height values, which requires `O(N)` auxiliary space. The generator used by `sum` is lazy and needs only constant additional state. Python's sorting machinery can also use temporary working memory, but this does not change the overall `O(N)` auxiliary-space bound.

The variant manifest states `O(N + H)` time and `O(H)` space, where `H` is the range of possible height values. Those bounds describe the counting-sort optimization, not the exact comparison-sorting source shown here. Because every height is between one and 100, a frequency array can record how often each height occurs. Scanning that small array in increasing-height order reconstructs the expected values while directly comparing them with the original sequence. That method takes `O(N + H)` time and `O(H)` space.

When `H = 100` is treated as a fixed problem constant, the counting method is effectively linear in `N`. It is the optimal asymptotic approach under the stated bounded-height contract. The current code instead favors the directness of `sorted`, so its honest exact bounds remain `O(N log N)` time and `O(N)` space.

## Alternatives and edge cases

- **Frequency counting for the manifest target:** Allocate counts for all heights from one through `H`, then visit height values in increasing order. Each stored occurrence represents the next expected height. Compare it with the next position of the original list and count a mismatch when they differ. This avoids comparison sorting and achieves `O(N + H)` time with `O(H)` space.
- **Counting without materializing the expected list:** A frequency array does not need to expand into a second list. Keep an index into `heights` and compare it against each height value repeated according to its frequency. This retains the same optimal bounds and saves the separate `O(N)` reference list.
- **In-place sorting after making a copy:** One could copy the original list and sort either copy in place. This is equivalent in purpose to `sorted` but more verbose. Sorting the only copy of the original order is incorrect because it destroys the baseline needed for comparison.
- **Manual mismatch loop:** An explicit counter and loop over indices produce the same answer as `sum(a != b for a, b in zip(heights, expected))`. That form may be useful while learning, but it does not improve the complexity.
- **Bubble sort:** Repeated neighboring swaps can construct the expected sequence, but its `O(N^2)` time is worse than both comparison sorting and frequency counting. The small input limit may allow it to finish, yet it ignores the stronger structure of the height range.
- **Already sorted input:** When `heights` is already non-decreasing, `expected` equals it at every index. Every comparison is false, so the sum correctly returns zero.
- **One student:** A one-element list is necessarily non-decreasing. The single aligned pair matches and the result is zero.
- **All heights equal:** Sorting does not change the sequence. Student identities are irrelevant because every position contains the same height, so the result is zero.
- **Reverse order:** A descending input usually creates many mismatches, but a middle value in an odd-length list may remain at the same index after sorting. The algorithm compares positions rather than assuming every element must be counted.
- **Duplicate heights:** Repeated values are retained with their exact frequencies. The method counts only value mismatches and does not incorrectly distinguish students who have equal heights.
- **Values at the limits:** Heights of one and 100 are ordinary sortable values. A counting implementation must size and index its frequency storage carefully enough to include both endpoints.
- **No required output ordering beyond the count:** The function returns one integer, so no reconstruction or reporting of mismatching indices is necessary.
