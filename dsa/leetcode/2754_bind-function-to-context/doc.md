# Bind Function to Context

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2754 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/bind-function-to-context/) |

## Problem Description

### Goal

Extend every JavaScript function with a method named `bindPolyfill`. Calling that method with one non-null object `obj` must return a new function whose later invocations always execute the original target with `obj` as its `this` context.

The returned function receives between zero and 100 arguments. Forward every argument in its original order and return the target function's result without alteration. Reads and writes through `this` must affect the supplied object itself.

Do not use the built-in `Function.bind`. A basic solution may use another invocation helper, while the follow-up asks for a solution that does not use built-in context-binding methods.

### Function Contract

Let $a$ be the length of `inputs`.

**Inputs**

- `fn`: The function on which `bindPolyfill` is called.
- `obj`: One non-null object that must become the target's `this` value.
- `inputs`: The argument array supplied when the returned function is invoked, with $0 \le a \le 100$.

The app-local adapter uses a serializable `behavior` name to construct representative target functions before exercising the same polyfill.

**Return value**

Return a function. When invoked with `inputs`, that function must call `fn` with `this === obj`, preserve argument order, and return exactly what `fn` returns.

### Examples

#### Example 1

- **Input:** `fn = function(multiplier) { return this.x * multiplier; }, obj = {"x":10}, inputs = [5]`
- **Output:** `50`
- **Explanation:** The bound context supplies `x = 10`, and the invocation forwards multiplier `5`.

#### Example 2

- **Input:** `fn = function() { return "My name is " + this.name; }, obj = {"name":"Kathy"}, inputs = []`
- **Output:** `"My name is Kathy"`
- **Explanation:** Binding must work even when the returned function receives no arguments.

#### Example 3

- **Input:** a target that increments `this.count`, with `obj = {"count":40}` and `inputs = [2]`
- **Output:** `42`
- **Explanation:** The target operates on the original context object, not on a copy.
