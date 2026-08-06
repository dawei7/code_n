## Description

Implement an `ImmutableHelper` class for JSON arrays and objects. Its constructor receives an original immutable value. The class exposes `produce(mutator)`, which gives `mutator` a proxied view of that original value. The callback may appear to assign primitive values anywhere in the view, but none of those assignments may alter the original.

After the callback finishes, `produce` returns a value reflecting exactly that callback's assignments. Separate calls always begin from the constructor's original value, not from a prior result. Unchanged branches should be reused rather than cloning the full JSON structure; only modified containers and the ancestor path needed to reconnect them should be copied.

The callback always returns `undefined`. It only accesses existing keys, never deletes keys or calls methods on proxied objects, and never assigns an object as a new value. The source JSON can be large, and there may be many calls to `produce`.
