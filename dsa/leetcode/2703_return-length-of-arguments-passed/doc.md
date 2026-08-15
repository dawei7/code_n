# Return Length of Arguments Passed

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2703 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/return-length-of-arguments-passed/) |

## Problem Description

### Goal

Implement a JavaScript function named `argumentsLength` that accepts any number of JSON-compatible arguments. Return how many separate arguments were supplied to that invocation, regardless of their types or values.

The distinction is based on call arity: an explicitly passed `null`, object, array, string, number, or boolean each counts as one argument. Their contents do not matter. Calling the function without arguments produces zero.

### Function Contract

**Inputs**

- `...args`: Between $0$ and $100$ arguments whose ordered collection is a valid JSON array.

**Return value**

Return the integer number of arguments passed to the function.

### Examples

#### Example 1

- **Input:** `argumentsLength(5)`
- **Output:** `1`
- **Explanation:** One number was passed.

#### Example 2

- **Input:** `argumentsLength({}, null, "3")`
- **Output:** `3`
- **Explanation:** The object, `null`, and string are three distinct arguments.

#### Example 3

- **Input:** `argumentsLength()`
- **Output:** `0`
- **Explanation:** The call contains no arguments.
