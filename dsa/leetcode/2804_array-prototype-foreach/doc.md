# Array Prototype ForEach

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2804 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/array-prototype-foreach/) |

## Problem Description

### Goal

Add a custom `forEach` method to `Array.prototype` so that every JavaScript array can invoke `array.forEach(callback, context)`. The method must call `callback` once for every array element in index order and must not return a value.

Each callback invocation receives the current element, its numeric index, and the array itself. It must also run with `this` bound to the supplied `context` object. The callback may use these arguments or its context to mutate the same array. Implement the traversal directly rather than delegating to built-in array iteration methods.

### Function Contract

**Inputs**

- `arr`: A valid JSON array containing between $0$ and $10^5$ elements.
- `callback`: The function invoked for each element. In app-local JSON cases, a string names the authored callback behavior.
- `context`: A valid JSON object used as the callback's `this` value.

The native prototype method receives `callback` and `context` directly through `arr.forEach(callback, context)`.

**Return value**

The prototype method returns `undefined`. Its observable result is any callback side effect, including mutations to `arr`; the app-local adapter returns the mutated array for judging.

### Examples

#### Example 1

- **Input:** `arr = [1, 2, 3]`, callback doubles each current value, `context = {"context": true}`
- **Output:** `[2, 4, 6]`
- **Explanation:** The callback replaces each element with twice its previous value.

#### Example 2

- **Input:** `arr = [true, true, false, false]`, callback stores `this`, `context = {"context": false}`
- **Output:** `[{"context": false}, {"context": false}, {"context": false}, {"context": false}]`
- **Explanation:** Every invocation receives the supplied object as its function context.

#### Example 3

- **Input:** `arr = [true, true, false, false]`, callback negates each value, `context = {"context": 5}`
- **Output:** `[false, false, true, true]`
- **Explanation:** The callback visits and negates each Boolean element.
