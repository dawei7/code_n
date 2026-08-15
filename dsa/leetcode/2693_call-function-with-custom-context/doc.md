# Call Function with Custom Context

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2693 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [call-function-with-custom-context](https://leetcode.com/problems/call-function-with-custom-context/) |

## Problem Description

### Goal

Extend every JavaScript function with a `callPolyfill` method. Its first argument is a non-null object that must become the function's `this` context. Any remaining arguments must be forwarded to the function in their original order, and the polyfill must return exactly what the function returns.

For example, an ordinary call to a function that reads `this.item` has no supplied object context and may therefore observe `undefined`. Calling the same function through `callPolyfill({ item: "salad" }, ...)` must make that object available as `this` for the duration of the invocation.

The implementation may not use the built-in `Function.call` method.

### Function Contract

**Inputs**

- `context`: The non-null object to use as `this`.
- `args`: Zero or more values to pass as the function's positional arguments.

The method is invoked on the function itself as `fn.callPolyfill(context, ...args)`. Including `context`, the input argument list contains between $1$ and $100$ values. The serialized context contains between $2$ and $10^5$ characters.

**Return value**

Return the value produced by invoking `fn` once with `context` as `this` and the supplied additional arguments in order.

### Examples

#### Example 1

- **Input:** `fn = function add(b) { return this.a + b; }`, `args = [{"a": 5}, 7]`
- **Output:** `12`

#### Example 2

- **Input:** `fn = function tax(price, taxRate) { return \`The cost of the ${this.item} is ${price * taxRate}\`; }`, `args = [{"item": "burger"}, 10, 1.1]`
- **Output:** `"The cost of the burger is 11"`
