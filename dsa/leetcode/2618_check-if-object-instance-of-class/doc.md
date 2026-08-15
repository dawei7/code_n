# Check if Object Instance of Class

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2618 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-object-instance-of-class/) |

## Problem Description

### Goal

Implement a JavaScript function that decides whether a supplied value should be considered an instance of a supplied class or one of its superclasses. For this problem, membership means that the value can access methods defined by that class through JavaScript's prototype chain.

Both arguments may have any type, including `null` or `undefined`. Primitive values receive their usual JavaScript object-wrapper behavior: for example, the number `5` is considered an instance of `Number` because its method lookup uses `Number.prototype`, even though the expression `5 instanceof Number` evaluates to `false`.

Return `true` exactly when the class's prototype occurs in the value's method-lookup chain; otherwise return `false`.

### Function Contract

**Inputs**

- `obj`: Any JavaScript value whose prototype ancestry is to be inspected.
- `classFunction`: Any JavaScript value proposed as the class or constructor. A non-function value cannot supply a valid class relationship.

Let $h$ denote the number of prototype links examined after primitives are boxed with their standard wrapper objects.

**Return value**

Return a boolean indicating whether `obj` has access to methods from `classFunction.prototype` through its prototype chain.

### Examples

#### Example 1

- **Input:** `checkIfInstanceOf(new Date(), Date)`
- **Output:** `true`
- **Explanation:** A value constructed by `Date` inherits from `Date.prototype`.

#### Example 2

- **Input:** `class Animal {}; class Dog extends Animal {}; checkIfInstanceOf(new Dog(), Animal)`
- **Output:** `true`
- **Explanation:** A `Dog` instance's prototype chain includes `Animal.prototype`.

#### Example 3

- **Input:** `checkIfInstanceOf(Date, Date)`
- **Output:** `false`
- **Explanation:** The `Date` constructor is a function object, not an object inheriting from `Date.prototype`.

#### Example 4

- **Input:** `checkIfInstanceOf(5, Number)`
- **Output:** `true`
- **Explanation:** Method access boxes the primitive number, exposing `Number.prototype`.
