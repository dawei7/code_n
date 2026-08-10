## General

**Store each mapping inside the list itself**

A dictionary-based clone remembers which new node corresponds to each original. The competitive solution avoids that dictionary by temporarily placing every clone directly after its original:

`A -> A' -> B -> B' -> C -> C'`

During this woven state, the clone of any original node `x` is always `x.next`. That positional rule acts as the original-to-copy mapping while using no input-sized auxiliary container.

The algorithm has three passes:

1. create and weave copied nodes;
2. assign copied random pointers;
3. separate the woven chain into the restored original and the independent copy.

**Pass one: insert a clone after every original**

For original `current`, the code constructs `copied = Node(current.val)`. It saves the original successor in `copied.next`, then changes `current.next` to the clone.

If the original fragment was `current -> successor`, it becomes:

`current -> copied -> successor`

Advancing with `current = copied.next` moves to the saved next original, not back into the clone.

After this pass, every original has exactly one newly allocated neighbor clone. Values match, and the original relative order is still visible by skipping every copied node.

The original list is temporarily modified, but no original `random` pointer changes. That preservation is necessary for the next pass.

**Pass two: translate random pointers in constant time**

The second loop visits only originals by advancing `current.next.next`.

The clone of the current original is `current.next`. If `current.random` points to original node `R`, then the clone of `R` is immediately after it at `current.random.next`. Therefore:

`current.next.random = current.random.next`

recreates the relationship between clones without a dictionary or search.

When the original random pointer is null, the code leaves the copied random pointer at its constructor default `None`.

This positional lookup works for forward pointers, backward pointers, self-pointers, and many pointers sharing one target. For a self-pointer, `current.random` is `current`, so its `.next` is precisely the current clone.

**Pass three: restore and extract**

The woven list still has incorrect `next` links for both outputs. Original nodes point to their clones, and each clone points to the next original.

The code creates a dummy head for the copied chain. At each original `current`:

1. `copied_current.next = current.next` appends the adjacent clone to the copy chain;
2. `current.next = current.next.next` skips that clone and restores the original successor;
3. both traversal pointers advance to their next respective nodes.

On the following iteration, the previous clone’s `next` is overwritten from the next original to the next clone. The last clone was initially inserted before `None`, so the final copied chain ends at `None`.

When the loop finishes, the original list has exactly its initial `next` chain, while `dummy.next` begins a separate chain of clones. All copied random pointers already point to clones from the woven phase.

**Why every deep-copy requirement is met**

Pass one constructs exactly one new node per original and copies its value. Pass two maps every non-null random edge from an original target to the adjacent clone target. Pass three maps every next edge into the clone chain and removes all interleaving.

Every pointer in the returned list ends at a constructed clone or at `None`. No returned `next` or `random` pointer targets an original object.

The original list’s `next` pointers are restored, and its `random` pointers were never changed. Thus the temporary mutation is not observable after successful completion.

The class `Node` is declared at module level as harness structure, while the user algorithm remains inside `Solution`, consistent with the native shape.

## Complexity detail

Let $n$ be the number of original nodes.

Each of the three passes visits every original node once and performs constant work. Three linear passes are still $O(n)$ time.

Apart from the required $n$ cloned output nodes, the algorithm stores a dummy node and a fixed number of pointers. Auxiliary space is $O(1)$, matching the manifest and the source comment.

If output allocation is counted, total newly allocated storage is $O(n)$ because a deep copy inherently requires one new node per input node. The $O(1)$ claim uses the standard convention of excluding the returned output.

## Alternatives and edge cases

- **Two-pass dictionary mapping:** Build the copied `next` chain and an original-to-clone dictionary, then resolve random targets. It avoids mutating the input but needs $O(n)$ auxiliary space.
- **Recursive graph cloning:** Recursively follow both pointers with memoization. It handles cycles but adds $O(n)$ mapping and possible recursion depth.
- **Lazy one-pass mapping:** Create unseen target clones on demand while scanning originals. It works in linear expected time but still stores a dictionary.
- **Empty list:** All three main loops skip; a dummy is created and `dummy.next` returns `None`.
- **One node:** Weaving, optional self-random translation, and separation all work without special branches.
- **Null random pointer:** The freshly constructed clone already has `random = None`, so no assignment is needed.
- **Self-random pointer:** `current.random.next` is the clone immediately beside `current`, correctly creating a clone self-loop.
- **Duplicate values:** Position beside the original, not value, identifies the clone; equal values cannot be confused.
- **Temporary mutation:** If an exception or concurrent reader observes the list between passes, it may see the woven form. This method assumes exclusive, uninterrupted execution until restoration.
- **Restoration order:** Random pointers must be assigned before separation; afterward, `original.random.next` would mean the original target’s next original rather than its clone.
- **Output-space convention:** The method is constant auxiliary space, not zero allocation; constructing the requested copied nodes is unavoidable.
- **Later classes in the file:** `Solution2` and `Solution3` are dictionary-based alternatives with $O(n)$ auxiliary space. They do not change the selected primary class’s interleaving behavior.
