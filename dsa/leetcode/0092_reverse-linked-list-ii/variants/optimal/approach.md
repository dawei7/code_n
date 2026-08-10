## General

The task is to reverse node links only inside the inclusive one-based interval `[left, right]`. Nodes before that interval must still lead into it, and the original first node of the interval must lead to the suffix afterward. The selected solution performs those three jobs in one forward pass:

1. find the node immediately before the interval;
2. reverse exactly `right - left + 1` links; and
3. reconnect both interval boundaries.

It changes pointers rather than swapping node values, so the node objects themselves appear in reversed order as the contract intends.

**Why a dummy node simplifies the left boundary**

`dummy = ListNode(0, head)` creates a temporary node before the real head. The pointer `pre` advances `left - 1` times from `dummy`. It therefore ends at the node immediately before position `left`.

This description remains true when `left == 1`: zero advances leave `pre` at `dummy`, which is indeed the predecessor of the real first node. Without a dummy, reversing from position one would require a separate branch because no real predecessor exists and the list's head changes. The dummy turns both cases into the same pointer operation.

After the walk, the code saves

- `p = pre`: the predecessor before the segment; and
- `q = pre.next`: the original first segment node.

These identities matter after reversal. `p` must be connected to the new first segment node, while `q` becomes the last segment node and must be connected to the untouched suffix.

**Meaning of the reversal pointers**

The assignment `cur = q` begins at position `left`. During the reversal loop:

- `pre` points to the already reversed part immediately to the left of `cur`;
- `cur` is the next segment node whose link must be reversed; and
- `t` temporarily preserves the unreversed successor of `cur`.

Each iteration executes these conceptual steps:

1. Save `cur.next` in `t`. This is essential because changing `cur.next` would otherwise destroy the only forward path to the remaining nodes.
2. Set `cur.next = pre`, reversing one link.
3. Move `pre` to `cur`, making the processed node the front of the reversed portion.
4. Move `cur` to `t`, the next unprocessed node.

The loop runs exactly

$$
k=\texttt{right}-\texttt{left}+1
$$

times, once per node in the inclusive segment. When it ends, `pre` points to the original node at `right`, now the front of the reversed segment. `cur` points to the node at `right + 1`, or to `None` when the reversed segment reaches the list tail.

**Why the temporary link to `p` is safe**

Unlike a whole-list reversal often initialized with `pre = None`, this code begins with `pre` equal to the node before the segment. Consequently the first reversed node, `q`, temporarily points backward to `p`. Later iterations form the desired reversed chain in front of `q`.

At that intermediate moment, `p.next` still points forward to `q`, so there is a temporary two-node cycle between `p` and `q`. The algorithm does not traverse through `p.next` during the loop; it uses its saved local pointers. After the loop, both boundary assignments remove the cycle and establish the final structure:

- `p.next = pre` connects the prefix to the new segment head; and
- `q.next = cur` connects the new segment tail to the suffix.

The order of those final assignments is safe because `p`, `pre`, `q`, and `cur` were all saved independently. No still-needed node becomes unreachable.

**Trace for `[1,2,3,4,5]`, `left = 2`, `right = 4`**

After one advance from `dummy`, `p` is node `1`; `q` and `cur` are node `2`.

1. Reverse node `2` toward node `1`. `pre` becomes `2`, and `cur` becomes `3`.
2. Reverse node `3` toward node `2`. The reversed portion is `3 -> 2 -> 1`; `cur` becomes `4`.
3. Reverse node `4` toward node `3`. `pre` is `4`, and `cur` is `5`.

The internal chain currently points `4 -> 3 -> 2 -> 1`, while node `1` still points to `2`. Setting `p.next = pre` changes node `1` to point to `4`. Setting `q.next = cur` changes node `2` to point to `5`. The result is `1 -> 4 -> 3 -> 2 -> 5`.

**Early return**

If the list has one node or `left == right`, no link needs to change. Returning immediately avoids constructing a dummy and entering a loop. The nonempty-list constraint makes `head.next` safe to access. Even without the early return, the general reversal could handle a one-node interval, but avoiding unnecessary temporary rewiring is clearer.

## Complexity detail

Let $n$ be the number of list nodes and $k=\texttt{right}-\texttt{left}+1$ the segment length. Locating the predecessor takes `left - 1` pointer advances, and reversing takes $k$ iterations. Their sum is at most $n$, so time is $O(n)$. More precisely, the method stops immediately after position `right` and costs $O(\texttt{right})$; the conventional whole-input upper bound is $O(n)$.

The algorithm allocates one dummy node and uses a fixed number of node references and counters. It creates no array, map, or recursion stack, so auxiliary space is $O(1)$. The original nodes are reused; the dummy is not part of the returned list.

## Alternatives and edge cases

- **Head-insertion reversal:** Keep the node before the segment fixed and repeatedly remove the node after the segment's original first node, inserting it immediately after the predecessor. It also runs in one pass with $O(1)$ space, but its repeated four-link choreography can be less intuitive initially.
- **Recursive reversal:** Recursion can reverse the chosen range or simulate a backward pointer, but it uses $O(n)$ stack space and can be harder to reconnect correctly.
- **Value swapping:** Swapping `val` fields from the ends inward may reproduce the displayed values, but it does not reverse node identity and can violate expectations when external references point to nodes.
- **Interval starts at the head:** The dummy ensures `p` exists. After reconnection, `dummy.next` is the new real head.
- **Interval ends at the tail:** After the loop, `cur` is `None`; assigning `q.next = None` correctly terminates the list.
- **One-node interval:** The early return preserves every link. This includes a one-node list and any case where `left == right`.
- **Whole-list reversal:** Both boundary cases occur together. `p` is the dummy and `cur` becomes `None`, so the returned `dummy.next` is the old tail and the old head terminates the list.
- **Save before overwriting:** Replacing `cur.next` before preserving it would lose the unprocessed suffix. The temporary `t` is required, not cosmetic.
- **Valid positions are guaranteed:** The loops rely on `1 <= left <= right <= n`. No behavior for an out-of-range interval needs to be invented.
