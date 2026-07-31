## General

Wrap the root in a `Proxy`, but do not recursively process its descendants up front. The proxy's `get` trap returns primitives unchanged and lazily wraps an object or array only when that child is actually read. A `WeakMap` caches one proxy per original container, preserving repeated-access identity and avoiding duplicate wrappers.

**Reject mutations at the container where they occur**

The `set`, `deleteProperty`, and `defineProperty` traps throw a string selected from the target's type. Object targets use `Error Modifying: key`; array targets use `Error Modifying Index: index`. The trap throws even when the proposed value equals the current one, because the contract rejects the attempt itself.

For arrays, the `get` trap recognizes the seven specified mutating method names and returns a function that immediately throws `Error Calling Method: name`. It does not invoke the real method, so the target remains untouched. Other reads use `Reflect.get` and are recursively protected when their value is another container. Because every path exposed to the caller is proxied and every mutation route is intercepted before reaching its target, neither the root nor any nested original value can change.

## Complexity detail

Creating the root immutable view takes $O(1)$ time. Each property access, rejection, or method interception takes $O(1)$ expected time. If $p$ distinct containers are reached, cached proxy state uses $O(p)$ space; untouched subtrees require no work or proxy allocation. The benchmark grows an untouched branch while performing the same root assignment, contrasting lazy wrapping with a correct eager recursive wrapper.

## Alternatives and edge cases

- **Deep freeze:** Recursively freezing the input eagerly traverses everything, changes the original objects' extensibility, and does not produce the required string errors.
- **Eager recursive proxies:** Wrapping a copied version of every nested container can enforce the contract but spends time and space on untouched branches.
- **Root-only proxy:** Protecting just the root allows writes through a nested object or array and is therefore insufficient.
- Assigning the existing value still counts as a forbidden modification.
- Array indexes use the index-specific error, while mutating methods use the method-specific error.
- Non-mutating reads and `Object.keys` must retain ordinary behavior.
- Throw the required string literal directly rather than constructing an `Error`.
- Cache nested proxies so repeated reads of the same container return the same protected identity.
