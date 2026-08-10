## General

**Find group boundaries during one forward traversal**

The competitive implementation lets `cur` visit each original node in order. A counter named `length` records the current position modulo `k`:

```python
length = (length + 1) % k
```

Whenever the value becomes zero, `cur` is the $k$th node of a complete group and that group is reversed immediately. If traversal ends while the counter is nonzero, the remaining nodes never trigger reversal and therefore stay in their original order.

This avoids a separate look-ahead scan for each group while still refusing to reverse an incomplete suffix.

**Maintain a predecessor before the active group**

The source creates a dummy before `head` and initializes

```python
cur, cur_dummy = head, dummy
```

`cur` is the traversal pointer. `cur_dummy` is the node immediately before the current not-yet-reversed group. For the first group it is the dummy; after a group is reversed, it becomes that group's new tail, which is exactly the predecessor of the next group.

The fixed `dummy` remains the return anchor because the first reversal may change the real head.

**Save the traversal successor before reversal changes links**

At the top of every outer iteration, the source records

```python
next_cur = cur.next
```

When `cur` completes a group, the helper will reverse links inside that group, including links used to reach `cur`. Saving the original successor first ensures the outer traversal can continue at the first node after the group. The iteration ends with `cur = next_cur`, regardless of whether a reversal occurred.

Without this saved reference, advancing through a reversed `cur.next` could walk backward into the group or skip the suffix.

**Call the helper with half-open boundaries**

On a complete group, the invocation is

```python
self.reverse(cur_dummy, cur.next)
```

`begin = cur_dummy` is the node before the group, and `end = cur.next` is the first node after it. The helper reverses nodes strictly between those boundary references, leaving `end` itself untouched. This half-open interval representation handles a final complete group because `end` may be `None`.

Before the helper call, the source also saves

```python
next_dummy = cur_dummy.next
```

This is the original first node of the group. Reversal will turn it into the group's tail, so assigning `cur_dummy = next_dummy` afterward prepares the predecessor for the next group.

**Reverse by repeatedly moving the second node to the front**

Inside `reverse`, `first = begin.next` stays fixed as the original first node and eventual group tail. `cur = first.next` starts at the second group node. Each loop iteration performs:

```python
first.next = cur.next
cur.next = begin.next
begin.next = cur
cur = first.next
```

The first assignment removes `cur` from immediately after `first`. The next two insert it immediately after `begin`, at the front of the partially reversed group. Finally, `first.next` now names the next node still awaiting movement, so `cur` advances there.

For `1 -> 2 -> 3` between boundaries, moving `2` to the front gives `2 -> 1 -> 3`; moving `3` gives `3 -> 2 -> 1`. Throughout, `first` remains node `1`, and its `next` link eventually points to `end`. The helper stops when `cur == end`, so it never moves a node outside the group.

**Trace `[1, 2, 3, 4, 5]` with `k = 2`**

The counter is one at node `1` and returns to zero at node `2`. `next_cur` saves node `3`; `next_dummy` saves node `1`. Reversing between the dummy and node `3` produces `2 -> 1`, and `cur_dummy` becomes node `1`.

Traversal resumes from saved node `3`. The counter reaches zero at node `4`; node `5` is saved as the exclusive end. Reversal produces `4 -> 3`, and the processed chain is `2 -> 1 -> 4 -> 3 -> 5`. The final node `5` leaves the counter at one, so no helper call occurs and it remains unchanged.

**Why the algorithm is correct**

Before each outer step, every completed group before `cur_dummy` is correctly reversed, `cur_dummy` precedes the current group, and `cur` follows original forward order within the unprocessed suffix. A zero modulo counter occurs exactly on every $k$th node after the previous boundary. The helper then reverses exactly that complete half-open group and reconnects it to both boundaries. The saved original first node becomes the next `cur_dummy`, and `next_cur` resumes at the untouched suffix.

If traversal ends without another zero, fewer than `k` nodes have accumulated since the last boundary and none of their links were changed. Thus all complete groups and only complete groups are reversed.

## Complexity detail

Let $n$ be the number of nodes.

- **Time complexity: $O(n)$.** The outer traversal visits every node once. For each complete group, the helper moves `k - 1` nodes once. Across disjoint groups that helper work totals at most $n$, giving linear overall work.
- **Auxiliary space: $O(1)$.** The source uses a dummy node, a modulo counter, and a constant number of pointers. The helper is iterative and its calls do not nest. Original nodes form the output.

Unlike approaches that count ahead and then reverse, this implementation does not scan complete-group nodes twice before mutation, though both designs remain $O(n)$.

## Alternatives and edge cases

- **Probe, detach, and reverse:** First verify `k` nodes, detach the group, reverse it as an ordinary list, and reconnect. It is often easier for beginners to audit and has the same asymptotic bounds.
- **Recursive suffix processing:** It can be concise but uses $O(n/k)$ stack space.
- **Stack of `k` node references:** Pop nodes to reverse each group, but the additional memory is $O(k)$ rather than constant.
- **`k = 1`:** The modulo counter is always zero, but the helper's `cur` equals `end`, so it performs no link moves and the list remains unchanged.
- **`k = n`:** The helper is called once with `end = None` and reverses the whole chain.
- **Incomplete suffix:** Its counter never returns to zero, so no link in it changes.
- **Exact multiple of `k`:** The final helper uses `None` as the exclusive end and reconnects the new group tail to `None`.
- **Duplicate values:** Reversal is positional; values are never compared or modified.
- **`next_cur` timing:** It must be saved before the helper because internal links cease to follow original traversal order afterward.
- **`next_dummy` meaning:** It is saved before reversal because the original group head becomes its tail and the next group's predecessor.
- **Input mutation:** The function rewires the supplied nodes in place and returns a potentially different head.
- **Positive `k` guarantee:** Modulo by zero would fail, but the contract guarantees $k\ge1$.
