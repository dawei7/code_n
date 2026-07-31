## General

**Interpret a partition as sign choices**

The first element of every part is added. Inside a part, signs alternate, so
an element may be subtracted only when the preceding element was added; after
a subtraction, the next element must be added. Starting a new part also adds
its first element. Thus the partition problem is equivalent to choosing signs
for the array under two rules: `nums[0]` is added, and no two consecutive
elements may both be subtracted.

**Keep the two possible signs of the current element**

After processing a prefix, let `added` be the greatest total among valid sign
choices whose last value was added, and let `subtracted` be the greatest total
whose last value was subtracted. For the next `value`:

- Adding it is legal after either state, so the new `added` is
  `max(added, subtracted) + value`.
- Subtracting it is legal only after an added value, so the new `subtracted`
  is `added - value`.

Initialize `added = nums[0]` and make `subtracted` unreachable. Each update
therefore considers every legal continuation and nothing forbidden. By
induction, both states are optimal for their stated ending sign after every
prefix, and the larger final state is the maximum total cost of a valid
partition.

## Complexity detail

Each of the $n$ values is processed once with constant work, giving $O(n)$
time. Only the two DP totals are retained, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **DP array:** Storing both states for every prefix follows the same
  recurrence and takes $O(n)$ time, but uses unnecessary $O(n)$ space.
- **Try every final subarray:** A prefix DP that enumerates every possible
  start of the last part is correct but costs $O(n^2)$ time.
- A one-element array has only one possible part, so its value is returned
  even when that value is negative.
- Consecutive negative values cannot both be subtracted; a split or an added
  occurrence must separate those choices.
- All-positive input is optimally split wherever subtraction would reduce the
  total, including into singletons when appropriate.
- The answer can exceed 32-bit range because both $n$ and the value magnitude
  are large.
