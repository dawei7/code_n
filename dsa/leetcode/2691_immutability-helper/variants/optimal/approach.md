## General

**Provide mutation syntax without mutating the base**

`ImmutableHelper` stores the original JSON object in `this.obj`. Each call to `produce` gives the mutator a proxy that appears writable, but writes are redirected into lazily created shallow copies.

The key optimization is structural sharing. A small edit deep in the object should copy only:

- the container that directly changes;
- every ancestor container needed to connect that changed container back to the root.

Unchanged sibling objects and arrays remain shared with the original because they are immutable from the mutator's perspective.

**Create fresh draft state for every production**

Each `produce` call creates a root state whose `base` is `this.obj`.

A state stores:

- `base`, the original container represented by this draft node;
- `copy`, initially `null` and later a shallow writable copy;
- `parent` and `parentKey`, which locate this node inside its parent;
- `children`, a map caching draft states for accessed nested containers;
- `proxy`, the object exposed to mutator code.

These states belong only to the current call. A later `produce` begins again from the same original object, so previous produced changes do not accumulate.

**Read from the base until a copy exists**

The proxy's `get` trap chooses:

`state.copy === null ? state.base : state.copy`.

Before any write to that container, reads come directly from the immutable base. After its first write, reads come from the copy and therefore observe the mutator's changes.

This distinction is essential for code such as `proxy.val = proxy.val + 1`: the right side reads the current value, and the later read sees the assigned value.

**Return primitives directly and proxy nested containers**

If the retrieved value is `null` or not an object, the `get` trap returns it directly. Numbers, strings, and Booleans cannot contain deeper JSON edits.

For an object or array, the trap looks for a cached child state under that property. If none exists, it creates one with the current state as parent and the property as `parentKey`.

Returning `child.proxy` lets apparently ordinary nested syntax such as `proxy.obj.val.x = 20` trigger the same lazy behavior at every level.

**Why child proxies are cached**

Repeatedly reading the same nested property should represent the same draft state.

Without caching, two variables referring to `proxy.obj` could receive independent proxies and independent copies, making writes through one invisible through the other.

`children` reuses the state while its `base` still matches the current nested value. The base check protects against a property whose referenced container changes, although the contract rules out assigning new object values.

**Copy on the first write**

The `set` trap calls `markChanged(state)` before assigning into `state.copy`.

If a copy already exists, `markChanged` returns immediately. Otherwise it shallow-copies the base:

- arrays use `value.slice()`;
- objects use spread syntax `{ ...value }`.

A shallow copy duplicates the container but keeps references to nested children. That is intentional: deeper children are copied only if they themselves are changed.

**Propagate change status to the root**

If a newly copied state has a parent, `markChanged` recursively ensures the parent also has a copy. It then installs the child's copy into:

`state.parent.copy[state.parentKey]`.

For a deep write, this recursion copies the changed container, then each ancestor on the path to the root. As recursion unwinds, every parent copy is linked to the already copied child.

The final root copy is therefore a complete object graph containing the edit while still sharing untouched branches.

**Trace one deep mutation**

Suppose the base is conceptually `{user: {score: 10}, theme: {dark: true}}` and the mutator assigns `proxy.user.score = 11`.

Reading `user` creates a child draft but no copy. Setting `score` creates a shallow copy of the user object.

Propagation then creates a shallow copy of the root and replaces its `user` reference with the copied user. The `theme` reference is left shared because that branch was never modified.

The original root still points to the original user whose score remains 10.

**Several writes reuse copies**

After a state has `copy !== null`, later writes modify that same copy. Ancestors already reference it, so they do not need to be copied or relinked again.

If a different child changes later, its first copy propagates upward. An ancestor whose copy already exists simply keeps it, and the propagation then replaces the appropriate sibling property with the new child copy.

This gives one shallow copy per changed container, not one per assignment.

**Return the original when nothing changed**

After `mutator(root.proxy)` finishes, the method checks the root state's copy.

If it remains `null`, no set trap occurred anywhere, because every descendant change would have propagated a copy to the root. The method returns `this.obj` itself.

Reusing the same identity for a no-op production is safe and avoids an unnecessary full clone.

**Why the original remains unchanged**

Every assignment is performed only after a shallow copy exists, and it targets `state.copy` rather than `state.base`.

Nested writes copy and relink their entire ancestor path before mutation becomes observable at the produced root. No set operation is ever forwarded to a base object.

Therefore the returned graph reflects all writes while the constructor's original graph retains its previous values.

## Complexity detail

Let $a$ measure draft property accesses and created proxy states, and let $c$ be the total number of array elements and object properties copied across containers that become changed. Proxy/map work is expected $O(a)$, while shallow copying costs $O(c)$. Total time is $O(a+c)$.

States and child maps use $O(a)$ space, and changed shallow copies use $O(c)$. Total additional space is $O(a+c)$. Unchanged subtrees are shared instead of copied, which is the central savings over a deep clone.

## Alternatives and edge cases

- **Deep-clone before every mutator:** Simple and correct, but copies the entire object even for one small edit or no edit.
- **Mutate then restore the original:** Fragile in the presence of exceptions and aliases, and it violates immutability during execution.
- **Eagerly proxy and clone every node:** Preserves behavior but loses lazy work proportional to actual access and change.
- **No writes:** Returns the exact original object reference.
- **Top-level write:** Copies only the root container.
- **Deep write:** Copies the changed container and each ancestor path, while sharing siblings.
- **Multiple writes to one container:** Reuse its first shallow copy.
- **Arrays:** `slice` preserves element order and length while creating a writable container copy.
- **New primitive key:** The set trap adds it to the copied object without touching the base.
- **Null and primitives:** Returned directly because no deeper mutation is possible.
- **Repeated `produce` calls:** Each starts from `this.obj`, so results are independent.
- **Contract restrictions:** Deletion, mutating array methods, and assigning new object values are intentionally outside the supported mutator behavior.
