## General

**Represent each accessed container as a draft state**

For every proxied object or array, keep its original `base`, an initially absent shallow `copy`, its parent draft and parent key, a cache of child drafts, and the proxy itself. A read comes from `copy` after the container changes and otherwise from `base`. Primitive values are returned directly. An object or array value is wrapped lazily and cached, so merely reading a branch does not copy it.

**Propagate the first write to the root**

On the first assignment to a draft, shallow-copy its base. Then recursively mark its parent changed and replace the corresponding slot in the parent's copy with the child's copy. This copies exactly the modified container and the ancestor path needed to make the change reachable from the result. Later writes to an already changed draft reuse its copy.

Each call creates a fresh root draft over the constructor's original object. After the callback, return the root copy if any write occurred; otherwise return the original object. Because writes are directed only to draft copies, the base is never changed. Because each copied child is installed into its copied parent, every requested mutation appears in the returned structure, while untouched branches retain their original references.

## Complexity detail

Let $a$ be the number of container/property accesses that create or consult draft state, and let $c$ be the total number of own properties copied across containers that become modified. One `produce` call takes $O(a+c)$ time and uses $O(a+c)$ auxiliary space for draft states and shallow copies. Unvisited subtrees contribute neither term. The benchmark holds the mutation path constant while growing a large untouched branch, separating structural sharing from full deep cloning.

## Alternatives and edge cases

- **Deep-clone before every callback:** This is functionally correct but copies every untouched branch on every call and scales with the entire input.
- **Mutate then restore:** Temporarily changing the original violates immutability and is unsafe if the callback observes aliases or throws.
- **Record only flat key writes:** A flat log cannot reconnect changes made through nested aliases without tracking parent relationships.
- An empty callback returns the original value because no container needs a copy.
- Root arrays require `slice()` rather than object spread so their array identity and length semantics remain intact.
- Multiple writes to one draft reuse its first shallow copy, and the last value assigned to a key wins.
- Separate `produce` calls must construct fresh draft state over the same original base.
- New keys may receive primitives, while the stated contract excludes deletion, method calls, and object-valued assignments.
