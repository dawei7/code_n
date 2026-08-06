## Description

Given two deeply nested JavaScript objects or arrays, `obj1` and `obj2`, construct a new object describing only the values that differ at keys present in both inputs. Both inputs are values that could be produced by `JSON.parse`.

When the two values at a shared key are different primitive values, or when one is an array and the other is an object, store the leaf difference as `[valueFromObj1, valueFromObj2]`. When both values are arrays or both are objects, compare them recursively and retain only descendants that contain a difference.

Keys found in only one input are ignored. Array indices act as keys, so elements beyond the shorter array are likewise omitted. Object property order does not affect the result.
