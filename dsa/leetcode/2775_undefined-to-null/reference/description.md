## Description

Given a deeply nested JavaScript object or array `obj`, replace every property or array element whose value is `undefined` with `null`, and return the resulting root value. The nesting may contain any mixture of objects and arrays.

All other values must remain unchanged, including values that are already `null`. This distinction matters when data is serialized: `JSON.stringify` handles `undefined` differently from `null`, so converting the former makes those positions explicit in JSON-compatible data.
