# Infinite Method Object

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2690 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/infinite-method-object/) |

## Problem Description

### Goal

Create an object that behaves as though it has a method for every possible string property name. Accessing any property must yield a callable function, and invoking that function must return the exact property name that was accessed.

The property does not need to have been declared in advance. Names may be empty, ordinary identifiers, or strings containing punctuation and other characters that require bracket notation. For example, calling `obj.abc123()` returns `"abc123"`, while `obj[".-qw73n|^2It"]()` returns that exact punctuation-heavy name.

### Function Contract

**Inputs**

- `method`: In the app-local adapter, the string property name to access and invoke. Its length is from 0 through 1000.

**Return value**

The native `createInfiniteObject()` returns an object whose every string property resolves to a zero-argument function returning that property name. The app-local `solve(method)` returns the result of one such access and call.

### Examples

#### Example 1

- **Input:** `method = "abc123"`
- **Output:** `"abc123"`

#### Example 2

- **Input:** `method = ".-qw73n|^2It"`
- **Output:** `".-qw73n|^2It"`

#### Example 3

- **Input:** `method = ""`
- **Output:** `""`
