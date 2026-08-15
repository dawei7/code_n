# Immutability Helper

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2691 |
| Difficulty | Hard |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/immutability-helper/) |

## Problem Description

### Goal

Implement an `ImmutableHelper` class for JSON arrays and objects. Its constructor receives an original immutable value. The class exposes `produce(mutator)`, which gives `mutator` a proxied view of that original value. The callback may appear to assign primitive values anywhere in the view, but none of those assignments may alter the original.

After the callback finishes, `produce` returns a value reflecting exactly that callback's assignments. Separate calls always begin from the constructor's original value, not from a prior result. Unchanged branches should be reused rather than cloning the full JSON structure; only modified containers and the ancestor path needed to reconnect them should be copied.

The callback always returns `undefined`. It only accesses existing keys, never deletes keys or calls methods on proxied objects, and never assigns an object as a new value. The source JSON can be large, and there may be many calls to `produce`.

### Function Contract

**Inputs**

- `obj`: The original JSON object or array. Its serialized length is between 2 and $4\cdot 10^5$.
- `mutations`: The app-local adapter's list of independent mutation batches. Each assignment has a non-empty `path` of existing container keys followed by the target key, plus a primitive `value` to store. Native LeetCode receives the equivalent behavior as mutator callback functions.

**Return value**

The native class returns one structurally shared immutable result per `produce` call. The app-local `solve(obj, mutations)` returns the result of every independent batch in order, while leaving `obj` unchanged.

### Examples

#### Example 1

- **Input:** `obj = {"val":10}` with independent assignments of `11` and `9` to `val`.
- **Output:** `[{"val":11},{"val":9}]`

#### Example 2

- **Input:** `obj = {"arr":[1,2,3]}` with one batch setting `arr[0]` to `5` and adding `newVal = 7`.
- **Output:** `[{"arr":[5,2,3],"newVal":7}]`

#### Example 3

- **Input:** `obj = {"obj":{"val":{"x":10,"y":20}}}` with one batch swapping the two leaf values.
- **Output:** `[{"obj":{"val":{"x":20,"y":10}}}]`
