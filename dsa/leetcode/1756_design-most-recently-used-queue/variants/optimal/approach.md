## General

**Store the logical queue directly in a Python list**

The exact implementation represents the current MRU queue as `self.q`. Its constructor creates:

`list(range(1, n + 1))`.

`range(1, n + 1)` produces the required values one through `n`, and converting it to a list stores them in queue order. List index zero is the first logical queue position, while the problem's `k` is one-indexed.

This representation makes the class state easy to understand: at every moment, reading `self.q` from left to right gives exactly the current queue from first to last.

**Translate one-indexed k to a list index**

`fetch(k)` first reads:

`ans = self.q[k - 1]`.

Subtracting one converts the requested position into Python's zero-based index. The constraints guarantee `1 <= k <= n`, and every fetch removes one value then appends it again, so queue length always remains `n`. The lookup is therefore valid for every legal call.

Saving the value in `ans` before deletion is necessary. Once the list entry is removed, `self.q[k - 1]` refers to the next shifted value or may be past the end when `k == n`.

**Remove exactly one list element**

The source deletes the selected position with:

`self.q[k - 1 : k] = []`.

The slice starts at `k - 1` and stops before `k`, so it contains exactly one element. Assigning the empty list to that slice replaces the one-element region with nothing, which removes it.

This is behaviorally equivalent to `self.q.pop(k - 1)`, except that the exact source has already read the value separately. All elements after the removed position shift one index to the left so the list remains contiguous and preserves their relative order.

Elements before the fetched position are unchanged. Elements after it remain in their original order. Those facts match the queue operation, which removes only the selected value rather than rearranging unrelated values.

**Append the fetched value as most recently used**

`self.q.append(ans)` adds the saved value after every remaining element. Appending makes it the final queue entry, which is precisely the required “move to the end” behavior.

The method returns `ans` after the state update. Thus the caller receives the value that occupied the requested position before it was moved.

For queue `[1,2,3,4,5,6,7,8]` and `fetch(3)`, `ans` becomes three. Deleting the slice at index two leaves `[1,2,4,5,6,7,8]`. Appending three gives `[1,2,4,5,6,7,8,3]`, exactly matching the example.

**Why repeated fetches use the updated order**

`self.q` is instance state, so it persists between method calls. A later `fetch` indexes the already-modified list, not the original one-to-`n` order.

After the example's first fetch, requesting position five reads value six from the current queue. Removing and appending it produces `[1,2,4,5,7,8,3,6]`. This demonstrates that `k` always refers to current rank, not to a permanent value label or original index.

**Fetching the final element**

When `k == n`, `ans` is already the final value. The deletion removes it and `append` immediately places it back at the end. The observable order is unchanged, and the correct value is returned.

The implementation does not add a special case because the general remove-and-append sequence is still valid. It performs some unnecessary work in this case, but simplicity and correctness are preserved.

**Class invariant and correctness**

Immediately after construction, `self.q` contains each integer from one through `n` exactly once in the specified order.

Assume the list matches the logical queue before a fetch. Reading index `k - 1` obtains the logical $k$-th element. Replacing its one-element slice with empty removes exactly that occurrence and keeps every other element's relative order. Appending the saved value places it after all others.

Therefore the updated list is exactly the queue obtained by moving its $k$-th element to the end, it still contains every original value once, and the returned value is correct. By induction, this remains true across all fetch calls.

## Complexity detail

Construction creates and stores $n$ integers, taking $O(n)$ time and $O(n)$ state space.

For `fetch(k)`, reading `self.q[k - 1]` is $O(1)$. Deleting a middle slice shifts the elements after it and costs $O(n-k)$, which is $O(n)$ in the worst case. Appending is amortized $O(1)$. Therefore the exact implementation's fetch time is $O(n)$ worst case, not the manifest's stated $O(\sqrt n)$.

The list always holds exactly $n$ queue values, so class storage is $O(n)$. A fetch uses only the scalar `ans` in addition to the list, giving $O(1)$ per-call auxiliary space. Python's internal list resizing may reserve spare capacity but remains $O(n)$.

Achieving the manifest's $O(\sqrt n)$ fetch bound would require a bucketed square-root decomposition or another order-statistics structure. That optimization is described by the local editorial but is not implemented in the exact `solution.py`.

## Alternatives and edge cases

- **Square-root decomposition:** Store roughly $\sqrt n$ buckets and rebalance after removal, obtaining about $O(\sqrt n)$ work per fetch with $O(n)$ storage.
- **Fenwick or segment tree:** Track occupied historical positions and locate the $k$-th active value by order statistics, supporting polylogarithmic updates and lookup with extra implementation complexity.
- **Balanced indexed sequence:** A suitable order-statistics tree can remove by rank and append efficiently, but Python's standard library has no direct built-in type.
- **Linked list alone:** Removal is constant time once a node is known, but locating the $k$-th node still takes $O(n)$.
- **List pop:** `pop(k - 1)` would express the same exact list behavior more compactly and retain the same worst-case shifting cost.
- **First position:** Every remaining element shifts left, producing the worst deletion work.
- **Last position:** The order is unchanged after remove-and-append, though the method still executes both operations.
- **Single-element queue:** Every legal fetch removes and restores the sole value, returning one.
- **Repeated same k:** Each call uses the newly updated queue order, so it may return different values.
- **Value versus position:** `k` is a current one-based rank, not the integer label to search for.
- **Queue length invariant:** One deletion followed by one append keeps length exactly `n`.
- **Uniqueness invariant:** The selected value is removed before being appended, so no duplicate is introduced.
- **At most 2000 fetches:** The list solution fits the small official constraints even though it does not satisfy the follow-up complexity.
- **Input n:** The constructor stores its derived range but does not need to retain `n` separately.
