## Description

Given two valid JSON values `o1` and `o2`, determine whether they are deeply equal.

Primitive values are deeply equal only when JavaScript's strict equality operator `===` considers them equal. Arrays must have the same length, contain corresponding elements in the same order, and have deeply equal values at every position. Objects must have exactly the same set of keys, regardless of key insertion order, and the values associated with each key must be deeply equal.

The values may be `null`, booleans, numbers, strings, arrays, or objects because both originate from `JSON.parse`. Arrays and ordinary objects are distinct JSON structures even when their enumerable property names and values look alike. Implement the comparison without using Lodash's `_.isEqual` function.
