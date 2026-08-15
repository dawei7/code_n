# To Be Or Not To Be

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2704 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/to-be-or-not-to-be/) |

## Problem Description

### Goal

Implement a JavaScript function `expect` that receives any value `val` and returns an assertion object with two methods. Each method receives another value and compares it with the captured original value using JavaScript strict equality.

Calling `toBe(other)` must return `true` when `val === other`; otherwise it must throw an `Error` whose message is exactly `"Not Equal"`. Calling `notToBe(other)` applies the opposite assertion: it returns `true` when `val !== other` and throws an `Error` with the exact message `"Equal"` when the values are strictly equal.

### Function Contract

**Inputs**

- `val`: Any value accepted by the JavaScript challenge runtime. The returned methods retain this value through a closure.
- `other`: The comparison value supplied later to either `toBe` or `notToBe`.

**Return value**

Return an object exposing callable methods `toBe` and `notToBe`. A satisfied assertion returns `true`; a failed assertion throws the required `Error` rather than returning `false`.

### Examples

#### Example 1

- **Input:** `expect(5).toBe(5)`
- **Output:** `true`
- **Explanation:** The two numbers are strictly equal.

#### Example 2

- **Input:** `expect(5).toBe(null)`
- **Output:** throws `Error("Not Equal")`
- **Explanation:** A number and `null` are not strictly equal.

#### Example 3

- **Input:** `expect(5).notToBe(null)`
- **Output:** `true`
- **Explanation:** Strict inequality satisfies the negative assertion.
