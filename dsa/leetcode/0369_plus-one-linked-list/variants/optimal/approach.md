## General

Ordinary addition starts at the least significant digit, but this linked list starts at the most significant digit and has no backward links. Reversing the list or using recursion would make the final digit easy to reach, but the exact solution finds the one position where carry propagation must stop.

When adding one to a decimal number, only its trailing run of nines creates a carry. The rightmost digit below nine increases by one, and every digit after it becomes zero. For example:

```text
1 -> 2 -> 3 -> 9 -> 9
          becomes
1 -> 2 -> 4 -> 0 -> 0
```

The source locates that rightmost non-nine digit in one forward scan, then performs the required mutations in a second forward scan over only its suffix.

**Why a dummy leading zero is added.**

`dummy = ListNode(0, head)` places a zero-valued node before the original head. It gives the algorithm a guaranteed digit that is not nine, even when every real digit is nine.

Without this sentinel, input `[9,9,9]` has no existing non-nine digit to increment. Its result needs a new leading one: `[1,0,0,0]`. With the dummy, the same general procedure increments the dummy from zero to one and zeroes all real nodes.

For inputs that do not overflow to a new digit, the dummy remains zero and is omitted from the returned list. This removes the need for a separate all-nines branch.

**Finding the carry-stopping digit.**

Variable `target` begins at `dummy`. The loop walks the original list from left to right. Every time it sees a value other than nine, it replaces `target` with that node.

After the scan, `target` is the rightmost real digit below nine, if one exists. Otherwise it is still the dummy. Every real node after `target` must be a nine. If some later digit were not nine, the loop would have updated `target` to that later node.

This last observation is the invariant that makes the second phase safe. The source does not check whether suffix digits equal nine before turning them into zero, because their position after the rightmost non-nine proves that they do.

**Applying the addition.**

`target.val += 1` performs the only nonzero digit increment.

- If `target` holds `0` through `8`, adding one produces `1` through `9` with no carry beyond that node.
- `target` can never hold nine by construction.
- If `target` is the dummy, it changes from zero to one and represents a new leading digit.

The code then moves `target` to `target.next` and walks to the end, assigning zero to every node. Those nodes were the trailing nines whose `9 + 1` behavior produces zero while carrying left.

**A trace without a long carry.**

For `[1,2,3]`, the scan updates `target` at every node because none is nine. It finishes at the tail holding `3`. Incrementing produces `4`; `target.next` is null, so the zeroing loop does nothing. The dummy is still zero, and the returned list is its next node: `[1,2,4]`.

**A trace with a partial carry.**

For `[1,2,9,9]`, `target` first moves to `1`, then to `2`, and remains there for both nines. The source increments `2` to `3`, moves into the suffix, and changes both nines to zero. The result is `[1,3,0,0]`.

**A trace with a new leading digit.**

For `[9,9]`, no real node updates `target`, so it remains the dummy. Incrementing gives dummy value one, and the suffix walk zeroes both original nodes. Because `dummy.val` is now truthy, the method returns the dummy itself, producing `[1,0,0]`.

**Choosing the returned head.**

The final expression is `dummy if dummy.val else dummy.next`.

If all original digits were nine, dummy value is one and it must become the new head. Otherwise dummy remains zero and is only an implementation sentinel; returning `dummy.next` preserves the original head node.

The constraints exclude leading zeros except for the number zero, so a non-all-nine input never legitimately needs the dummy in its numerical representation. Input `[0]` updates the real node from zero to one and returns that original node.

**Why the result is numerically correct.**

Let the original decimal representation consist of a prefix ending at the rightmost non-nine digit, followed by $r$ trailing nines. Adding one leaves every digit before that target unchanged, increases the target by one, and changes each of the $r$ nines to zero. This is exactly standard base-ten carry propagation.

If no real non-nine digit exists, the entire number is $10^n-1$; changing the dummy to one and all $n$ real digits to zero produces $10^n$. Therefore the same mutation rule is correct in every case.

The method changes node values in place and may return one newly allocated leading node. It does not allocate a replacement node for every digit and does not convert the list into an integer, so there is no integer-overflow concern.

## Complexity detail

Let $n$ be the number of original nodes. The first loop visits all $n$ nodes. The second loop visits only nodes after the selected target, at most $n$ nodes. Total running time is $O(n)$.

Only one dummy node and a constant number of pointer variables are allocated, so auxiliary space is $O(1)$. The returned structure reuses all original nodes, adding the dummy only when a new leading digit is required. This matches the manifest.

The input list is mutated. If callers require the original number to remain unchanged, a copy would be necessary and would increase additional space to $O(n)$.

## Alternatives and edge cases

- **Reverse the linked list:** Reverse, add one from the new head with ordinary carry, then reverse back. This is $O(n)$ time and $O(1)$ space but performs more pointer mutation and requires careful restoration.

- **Recursive addition from the tail:** Recurse to the end, propagate a carry while unwinding, and add a new head if needed. It is concise but uses $O(n)$ call-stack space.

- **Store nodes in an array or stack:** Gather node references, process them backward, and stop when carry disappears. This is straightforward but uses $O(n)$ auxiliary space.

- **Convert to an integer:** Parse all digits, add one, and rebuild the list. Besides unnecessary allocation, this can overflow fixed-width numeric types for long lists.

- **Last digit below nine:** The target is the tail; only that digit changes and the suffix pass is empty.

- **Trailing run of nines:** Exactly that suffix becomes zero, while the closest earlier non-nine digit increases.

- **All nines:** The sentinel becomes the new leading one and every original node becomes zero.

- **Single zero:** The real node is the rightmost non-nine, changes to one, and the dummy is discarded.

- **A digit becomes nine:** Incrementing an `8` to `9` is valid and creates no further carry. Only an original `9` would propagate, and `target` is never nine.

- **Original head identity:** Except for the all-nines case, the returned head is the original head and only some node values change.

- **Platform node type:** `ListNode` is provided by the execution environment; the solution constructs only the sentinel through that interface.
