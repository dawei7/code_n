## General

**Simulate the specification directly**

The problem defines a sequence of insertion operations. At step $i$, value `nums[i]` must be inserted at position `index[i]` in the current target list. Python's `list.insert(position, value)` has exactly those semantics: existing elements at that position and to its right shift one place, and the new value occupies the requested index.

The solution begins with `target = []`. `zip(nums, index)` pairs corresponding entries as `(x, i)` from left to right. For every pair, `target.insert(i, x)` performs the required operation. Returning `target` after the loop therefore mirrors the statement without needing any transformed representation.

**What insertion means at each boundary**

If `i == 0`, the new value becomes the first element and all current values shift right.

If `i == len(target)`, the value is appended at the end and no existing value shifts.

For an index strictly inside the list, the prefix before `i` remains unchanged, the new value occupies `i`, and the old suffix begins at `i+1`.

The guarantee `0 <= index[i] <= i` makes every operation valid. Before step $i$ under zero-based indexing, exactly $i$ values have already been inserted, so the current target length is $i$. The allowed range is precisely zero through the current length.

**Following the first example**

The first three pairs insert 0 at zero, 1 at one, and 2 at two, producing `[0,1,2]`. The fourth pair inserts 3 at index two. The old value 2 shifts right, producing `[0,1,3,2]`. The final pair inserts 4 at index one. Values 1, 3, and 2 shift, yielding `[0,4,1,3,2]`.

No value is overwritten. Insertion increases list length by one, unlike assignment such as `target[i] = x`, which would replace an existing value and fail when the list is initially empty.

**The loop invariant**

After processing the first $r$ pairs, `target` is exactly the array produced by applying the first $r$ specified insertions in order, and its length is $r$.

The invariant is true initially for zero operations and an empty list. For the next pair, `insert` places the requested value at the requested current index while preserving the relative order of all previous values on either side. That is exactly the next rule, so the invariant remains true and length increases by one. After every pair has been processed, the invariant states that `target` is the required final array.

**Why processing order cannot change**

Insertions affect the positions of earlier values, so the operations are not commutative. Processing pairs from right to left or sorting by target index would describe a different sequence. `zip` preserves array order and ensures each `nums` value uses the index from the same position.

For example, inserting 3 at index two before earlier elements exist would be invalid even though that same insertion is valid at its intended fourth step. The time at which an index is applied is part of the problem.

**Why the direct approach is appropriate**

The maximum length is only 100, so the cost of shifting list elements is small. A more advanced indexed sequence could make insertions asymptotically faster, but it would add substantial complexity for no practical benefit under these constraints. The exact solution is concise because the language's list operation already embodies the requested behavior.

## Complexity detail

Let $n$ be the number of pairs. Python lists are contiguous arrays. Inserting near the front of a current length-$i$ list can shift $i$ elements, costing $O(i)$. Across all steps, the worst-case total is

$$
\sum_{i=0}^{n-1}O(i)=O(n^2).
$$

Appending cases may be amortized $O(1)$, but worst-case input can repeatedly insert at zero. The returned target stores $n$ values, so space is $O(n)$. Apart from the required result list and temporary loop references, auxiliary scalar space is $O(1)$. These bounds match the manifest.

## Alternatives and edge cases

- **Linked list:** Finding the requested index costs $O(i)$ even if insertion itself is constant after locating it, so total time remains quadratic and Python implementation becomes more complex.
- **Balanced indexed tree:** An order-statistics tree can support insertions in $O(\log n)$, but it is excessive for $n\le100$ and not built into Python's standard list.
- **Reverse placement with free slots:** Process operations backward and locate the appropriate empty position using a Fenwick tree. This can reach $O(n\log n)$ but requires a nontrivial inversion argument.
- **Assignment instead of insertion:** It overwrites rather than shifts and cannot build the specified sequence.
- **Index zero:** Every current element shifts right and the new value becomes first.
- **Index equal to current length:** `insert` behaves like append.
- **Repeated values:** Values need not be unique; positions and operation order distinguish occurrences.
- **Single pair:** The guaranteed index is zero, producing the one-element result.
- **All indices increasing:** Every operation appends, giving linear practical behavior.
- **All indices zero:** Every operation shifts the full current list, realizing the quadratic worst case and reversing arrival order.
- **Equal input lengths:** The contract guarantees `zip` does not silently drop an unmatched tail.
- **Input mutation:** Neither `nums` nor `index` is changed; only the new `target` list is modified.
