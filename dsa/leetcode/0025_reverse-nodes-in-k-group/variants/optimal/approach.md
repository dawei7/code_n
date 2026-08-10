## General

**Verify a complete group before changing any link**

The final suffix must remain unchanged when it contains fewer than `k` nodes. Reversing first and discovering the shortage afterward would require undoing work. The selected implementation instead starts each iteration with `pre`, the node immediately before the candidate group, and advances a probe `cur` exactly `k` times.

```python
cur = pre
for _ in range(k):
    cur = cur.next
    if cur is None:
        return dummy.next
```

If `cur` becomes `None`, fewer than `k` nodes follow `pre`. No link in this candidate suffix has been changed, so returning immediately preserves it exactly. If all steps succeed, `cur` is the last node of a complete group.

**Use a dummy predecessor for the first group**

The outer setup is

```python
dummy = pre = ListNode(next=head)
```

`dummy` stays fixed before the returned list. `pre` moves and always denotes the predecessor of the next possible group. This makes the first group identical to later groups: after reversal, its new head is assigned to `pre.next`. The caller receives `dummy.next`, which automatically reflects a changed real head.

The dummy's value is irrelevant and it is not returned as a real node.

**Save both outside connections, then detach exactly $k$ nodes**

After the probe succeeds, three references describe the local structure:

```python
node = pre.next
nxt = cur.next
```

`node` is the original first node of the group. It will become the group's tail after reversal. `cur` is the original final node and will become the new group head. `nxt` is the first node after the group, possibly `None`.

The assignment

```python
cur.next = None
```

temporarily separates the group from the unprocessed suffix. Detachment gives the helper an ordinary null-terminated list containing exactly the intended `k` nodes. Saving `nxt` first is mandatory; otherwise the suffix reference would be lost.

**Reverse the detached list by front insertion**

The nested `reverse` helper builds a reversed chain behind another temporary dummy. For each node `cur`, it saves `cur.next`, inserts `cur` at the front of the reversed prefix, and continues from the saved successor:

```python
nxt = cur.next
cur.next = dummy.next
dummy.next = cur
cur = nxt
```

The helper invariant is that `dummy.next` heads the reversal of all nodes already consumed, while `cur` heads the untouched remainder of the detached group. Moving `cur` to the front extends the reversed prefix by one without losing the remainder. When `cur` becomes `None`, every detached node appears once in reverse order.

No values are modified and no replacement output nodes are created. The helper's dummy is only an anchor.

**Reconnect the reversed group on both sides**

The outer method installs the helper's returned head with

```python
pre.next = reverse(node)
```

The original first node `node` is now the reversed group's final node. The source restores the right connection with

```python
node.next = nxt
```

and then sets `pre = node`. This last update reestablishes the outer invariant: `pre` is the tail of all processed groups and sits immediately before the next unprocessed candidate.

Both reconnections are necessary. Omitting `pre.next` would leave the processed prefix pointing at the old group head; omitting `node.next` would lose the rest of the list.

**Trace `[1, 2, 3, 4, 5]` with `k = 2`**

Initially `pre` is the dummy. The probe reaches node `2`, so `node = 1` and `nxt = 3`. Detaching after `2` creates group `1 -> 2`; the helper returns `2 -> 1`. Reconnection produces `dummy -> 2 -> 1 -> 3 -> 4 -> 5`, and `pre` becomes node `1`.

The next probe reaches node `4`. The group `3 -> 4` is detached, reversed, and reconnected as `4 -> 3`; `pre` becomes node `3`. A final probe can advance to node `5` but its second step reaches `None`. The method returns without touching node `5`, yielding `[2, 1, 4, 3, 5]`.

For `k = 3`, the first complete group becomes `3 -> 2 -> 1`. Only two nodes remain, so the early return preserves `4 -> 5`.

**Why every complete group is reversed exactly once**

Before each iteration, the chain through `pre` consists of correctly reversed complete groups, and the suffix after `pre` is still in original order. A failed probe changes nothing and proves the whole remaining suffix is incomplete. A successful probe isolates exactly the next `k` nodes, the helper reverses exactly those nodes, and the reconnections extend the processed prefix without altering later nodes. Moving `pre` to the new group tail restores the invariant. Therefore termination returns every complete group reversed and the sole incomplete suffix unchanged.

The `while pre` condition is effectively open-ended because `pre` always names a real dummy or processed tail. Normal termination occurs through the failed-probe return. The final `return dummy.next` is a defensive fallback.

## Complexity detail

Let $n$ be the list length.

- **Time complexity: $O(n)$.** Each complete group is scanned once for `k` nodes and reversed once for `k` nodes, at most two visits per node. The final incomplete suffix is probed once. Thus the total is bounded by a constant multiple of $n$.
- **Auxiliary space: $O(1)$.** Both loops are iterative. The method keeps a fixed number of node references and one temporary dummy inside the currently executing helper. Helpers do not nest, so their dummy nodes do not accumulate. The returned chain reuses the original nodes.

The input limit of 5,000 nodes does not affect stack depth because no recursion is used.

## Alternatives and edge cases

- **Recursive group processing:** Reverse one group and recursively process the suffix. It is natural but uses $O(n/k)$ call-stack frames and misses the constant-space follow-up.
- **Reverse then restore an incomplete group:** It avoids a separate probe but adds delicate rollback logic; verifying first is easier to reason about.
- **Array of node references:** Reverse each complete slice in the array and relink, but this costs $O(n)$ extra memory.
- **`k = 1`:** Every one-node group is detached, unchanged by reversal, and reconnected; the list values and node order remain the same.
- **`k = n`:** The probe validates the entire list and the helper reverses it once.
- **Length divisible by `k`:** After the final group, the next probe immediately reaches `None` and returns the fully processed list.
- **Incomplete final suffix:** Detection happens before detachment, so every link in that suffix remains original.
- **Node values:** Values and duplicates are irrelevant; only positions and links determine groups.
- **Input mutation:** Original `next` pointers are rewritten. Callers must use the returned head.
- **Saved suffix:** `nxt` must be captured before `cur.next = None`; changing that order loses access to the remainder.
- **Valid positive `k`:** The contract excludes zero. With `k = 0`, the probe would not advance and the pointer logic would not represent a meaningful group.
