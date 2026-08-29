## General

**Copy the ordinary chain before resolving arbitrary links**

Each original node has two pointers with different structure. `next` forms the ordinary linear list, so it can be copied in one sequential pass. `random` may point forward, backward, to the same node, or to `None`, so a random target’s clone cannot always be found by following the copy chain from the current position.

The selected source solves that lookup problem with dictionary `d`:

`original node -> copied node`

It uses two passes. The first creates every copied node in `next` order and fills the mapping. The second uses the complete mapping to assign `random` pointers.

This separation is beginner-friendly because no copied random pointer is assigned before all possible targets exist.

**First pass: build brand-new nodes and the copied `next` chain**

`dummy` is an extra node before the copied head, and `tail` points to the last copied node created so far. The dummy avoids special logic for the first real node.

For each original `cur`, the loop:

1. constructs `Node(cur.val)`;
2. attaches it after `tail`;
3. moves `tail` to that new node;
4. records `d[cur] = node`;
5. advances through the original `next` pointer.

After processing the first `k` originals, the chain beginning at `dummy.next` contains exactly `k` new nodes in the same order, with the same values. The dictionary maps each of those originals to its corresponding copy.

The code never inserts an original node into the copied chain. Every real copied node comes from a constructor call. This establishes the identity independence required for a deep copy.

Appending in original `next` order automatically reconstructs all `next` relationships. The final copied `tail.next` remains `None` because newly constructed nodes begin without a next target.

**Second pass: translate every random target**

Once the first pass finishes, every original list node is a key in `d`. The code returns to `head` and visits the original list again.

For an original `cur` with a non-null random pointer, `d[cur.random]` is the unique clone of the target. Assigning that object to `d[cur].random` reproduces the relationship entirely within the copied list.

If `cur.random` is `None`, the clone receives `None`.

This handles every direction:

- a forward random pointer works because the target clone was created during the complete first pass;
- a backward pointer finds an earlier mapping;
- a self-pointer makes the cloned node point to itself;
- several originals pointing to one target all reuse the same target clone.

Looking up by original object identity is important. Values are not guaranteed unique, so a value-to-copy map could merge different nodes that happen to store the same integer.

**Why the result is a deep copy**

There is exactly one constructed node for each original because the first loop walks the `next` chain once and constructs once per position. The mapping records that one-to-one correspondence.

Copied values match by construction. Copied `next` relationships match because nodes are appended in the same sequence. Copied `random` relationships match because each original target is translated through `d`.

No copied pointer references an original. The copied `next` pointers were connected only to newly constructed nodes, and copied `random` pointers are dictionary values, which are also newly constructed nodes. Therefore, later mutation of either list does not alter the other list’s nodes or links.

Returning `dummy.next` skips the artificial helper node and returns the clone corresponding to the original head.

For an empty input, neither pass executes and `dummy.next` is `None`, producing the correct empty copied list.

**Why this is not the constant-space method**

Although the variant manifest declares `O(1)` space, this exact source stores one dictionary entry per original node. The mapping is essential to its second pass and grows linearly with the list. It is a valid linear-time deep copy, but its actual auxiliary space is $O(n)$.

The constant-space technique in the local editorial temporarily interleaves each clone directly after its original. This source does not perform that weaving.

## Complexity detail

Let $n$ be the number of list nodes.

The first pass visits all $n$ nodes once. The second pass visits them once more, and each dictionary access is expected $O(1)$. Total expected time is $O(n)$.

The dictionary contains $n$ mappings, so auxiliary space is $O(n)$. The dummy node and traversal pointers use $O(1)$ additional space.

The returned list itself necessarily occupies $O(n)$ space because the task requires $n$ new nodes. Even when output allocation is excluded from auxiliary complexity, the dictionary remains $O(n)$. Therefore, the selected source does not meet the manifest’s stated $O(1)$ auxiliary bound; counting output and work together is also $O(n)$.

## Alternatives and edge cases

- **Interleave clones with originals:** Insert each clone immediately after its original, derive a random target clone through `original.random.next`, then separate both lists. It achieves $O(1)$ auxiliary space but temporarily mutates the input.
- **Recursive graph copy:** Treat `next` and `random` as graph edges and memoize original-to-clone nodes. It is elegant but uses $O(n)$ mapping and call-stack space.
- **One-pass dictionary cloning:** Lazily create clones for `next` and `random` targets as they are encountered. It still uses $O(n)$ space and has more cases than the selected two-pass form.
- **Empty list:** The dummy is allocated, both loops are skipped, and `None` is returned.
- **Single node with null random:** One independent node is returned with both pointers null.
- **Self-random pointer:** `d[cur.random]` equals `d[cur]`, reproducing the self-loop in the copied list.
- **Duplicate values:** Object-keyed mapping distinguishes nodes even when `val` fields are equal.
- **Many pointers to one node:** Every lookup returns the same target clone, preserving shared identity.
- **Platform type:** `Node` is shown in the quoted template block because the native harness supplies it. The selected method relies on its constructor accepting the value and defaulting links to null.
- **Manifest mismatch:** Describing this exact implementation as $O(1)$ auxiliary space would be incorrect; the dictionary is input-sized.
