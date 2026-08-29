## General

**Translate the formula directly into array lookups**

The required value at answer index $i$ is `nums[nums[i]]`. There are two lookups in that expression. The first lookup, `nums[i]`, produces another valid index. The second lookup uses that result to obtain the value that belongs in the answer. The permutation guarantee is what makes this safe: every element of `nums` is between $0$ and $N-1$, so every value can be used as an index into the same length-$N$ array.

The exact solution expresses this operation with the list comprehension `[nums[num] for num in nums]`. Although the comprehension does not explicitly mention an index `i`, it performs precisely the operation in the definition. Iterating `for num in nums` visits the values `nums[0]`, `nums[1]`, and so on in their original order. During the iteration for position $i$, the variable `num` therefore equals `nums[i]`. Appending `nums[num]` consequently appends `nums[nums[i]]`. Because the iteration order is the original array order, that appended value becomes answer element $i$.

For `nums = [0, 2, 1, 5, 3, 4]`, consider the values encountered by the comprehension:

| Answer position | Current `num` | Value appended, `nums[num]` |
|---:|---:|---:|
| 0 | 0 | `nums[0] = 0` |
| 1 | 2 | `nums[2] = 1` |
| 2 | 1 | `nums[1] = 2` |
| 3 | 5 | `nums[5] = 4` |
| 4 | 3 | `nums[3] = 5` |
| 5 | 4 | `nums[4] = 3` |

The resulting list is `[0, 1, 2, 4, 5, 3]`. It is useful to distinguish the role of a value from its numeric appearance here. A value such as `5` is not copied directly to the answer. It is first interpreted as an address, and the value stored at that address is copied.

**Why a new list is the natural fit for this solution**

Every required lookup must observe the original permutation. If the algorithm overwrote `nums[i]` with its answer too early, a later lookup might read that new answer rather than the original value and produce the wrong result. The comprehension avoids that dependency completely. Python evaluates every lookup from the unchanged input list while building a separate output list. Only after all elements have been evaluated is that new list returned.

This also means the function has no surprising mutation side effect. A caller that still holds a reference to `nums` sees the original permutation after the method returns. That behavior is often easier to reason about than an encoding-based in-place method, even though the problem includes an optional follow-up asking about constant auxiliary memory.

**Why the construction is correct**

Fix any answer index $i$ from $0$ through $N-1$. When the comprehension reaches its $i$-th iteration, Python supplies the $i$-th input element to `num`, so `num = nums[i]`. The expression in front of `for` is then evaluated as `nums[num] = nums[nums[i]]`. That value is appended as the $i$-th output element because a list comprehension preserves iteration order. Thus the returned list satisfies the required equation at this arbitrary index. Since the same reasoning applies to every valid $i$, all answer elements are correct.

No special branching is necessary for fixed points or cycles in the permutation. If `nums[i] = i`, the two-level lookup simply returns `nums[i]`. If several indices form a cycle, each answer position independently follows exactly two edges of that cycle. The algorithm never needs to discover or traverse a whole cycle.

## Complexity detail

Let $N$ be `len(nums)`.

The comprehension performs exactly $N$ iterations. Each iteration reads one already supplied value and performs one constant-time Python list indexing operation. Constructing the returned list therefore takes $O(N)$ time.

The returned list contains $N$ integers, so the solution allocates $O(N)$ space for the answer. Apart from that required output, the comprehension needs only a constant amount of scalar state for the current value and iteration machinery. If a convention excludes returned output from auxiliary-space accounting, the auxiliary space is $O(1)$; the manifest records $O(N)$ because the concrete implementation does allocate a distinct length-$N$ result.

The nested appearance of `nums[nums[i]]` does not imply quadratic time. It is two direct array accesses, not one loop inside another. Likewise, permutation cycles do not increase the work: the code never chases indices repeatedly.

## Alternatives and edge cases

- **In-place quotient-and-remainder encoding:** Because every original value is in $[0,N-1]$, one can temporarily store both the old and new values in each integer, usually with a base of $N$, then decode in a second pass. That meets the follow-up's $O(1)$ auxiliary-memory target but mutates the input and requires careful use of remainders whenever a previously encoded cell is read.
- **Explicit indexed loop:** Initializing an answer list and assigning `ans[i] = nums[nums[i]]` is equivalent to the comprehension. It may be more familiar to a beginner, but it has the same $O(N)$ time and $O(N)$ returned-space costs.
- **Accidental in-place overwrite:** Simply assigning `nums[i] = nums[nums[i]]` from left to right is unsafe. A later position may depend on an original value that was already replaced. It is only correct with an encoding technique or another way to preserve old values.
- **Single-element permutation:** The only possible input is `[0]`. The lookup is `nums[nums[0]] = nums[0]`, so the method correctly returns `[0]`.
- **Fixed points:** An index with `nums[i] = i` maps to its own value. It needs no special treatment.
- **Long permutation cycles:** A cycle of any length is harmless because each result follows exactly two indexed links from the unchanged input.
- **Index safety:** The solution relies on the stated zero-based permutation contract. If arbitrary negative or out-of-range integers were allowed, Python indexing semantics could produce an unintended value or raise an error; such inputs are outside the problem.
- **Input preservation:** The exact solution returns a new list and leaves `nums` untouched. This is a behavioral advantage over the constant-extra-memory follow-up technique.
