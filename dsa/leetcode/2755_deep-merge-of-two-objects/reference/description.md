## Description

Given two arbitrary JSON values `obj1` and `obj2`, construct their deep merge. Each input may be `null`, a boolean, a number, a string, an array, or an object.

When both current values are plain objects, include every key appearing in either one. A key found in only one input retains that input's value. For a shared key, recursively merge its two associated values.

When both current values are arrays, apply the same rule with array indices as keys. The result therefore has the length of the longer array: shared positions merge recursively, while a position present in only one array remains unchanged.

For every other pair—including primitives, `null`, or an array paired with an object—the second value replaces the first. Both inputs are valid outputs of `JSON.parse`, and each serialized input has length from 1 through $5 \cdot 10^5$.
