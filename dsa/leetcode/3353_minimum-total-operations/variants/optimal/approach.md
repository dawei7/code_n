## General

An operation on a prefix ending at index $i$ changes `nums[i]` but leaves `nums[i + 1]` untouched. Therefore it changes exactly one adjacent difference at that right boundary; differences strictly inside the prefix remain unchanged because both endpoints receive the same addition.

The final element can only be included by choosing the whole array. Such an operation shifts every value equally and cannot help make unequal values equal, so the final common value may be regarded as fixed at `nums[n - 1]`.

Now work conceptually from right to left. If `nums[i] = nums[i + 1]`, those positions already have the same offset from the fixed suffix and no operation should end at $i$. If they differ, at least one operation must end at $i$, because operations ending elsewhere cannot alter their difference. One operation with adjustment `nums[i + 1] - nums[i]` makes that boundary equal without disturbing any boundary to its right.

Thus every unequal adjacent pair contributes exactly one necessary and sufficient operation. Counting those pairs gives the minimum directly; the operations need not be simulated.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm inspects each of the $n-1$ adjacent pairs once, taking $O(n)$ time and $O(1)$ auxiliary space.

The benchmark size is $n$. Strictly increasing inputs make every boundary require an operation. The optimal scan stays linear, while explicitly applying each right-to-left adjustment to all elements of its prefix performs $1+2+\cdots+(n-1)=\Theta(n^2)$ updates.

## Alternatives and edge cases

- **Explicit right-to-left simulation:** Applying the necessary adjustment to each prefix is correct, but physically updating the elements repeats work and takes $O(n^2)$ time.
- **Track the current suffix target:** A right-to-left scan can maintain the desired value and increment whenever the next original value differs; this is equivalent to counting unequal adjacent pairs.
- **Whole-array operations:** Adding a value to every element preserves all adjacent differences, so it never reduces the number of required operations.
- **Single element:** There are no adjacent boundaries, and the answer is zero.
- **Repeated runs:** A constant run contributes nothing internally; only a transition from one value to another contributes an operation.
- **Large or negative values:** Only equality comparisons are needed, so the magnitude and sign of an adjustment cannot cause arithmetic issues.
