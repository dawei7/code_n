## Description

Given a JSON object or array, return an immutable view of the same data. Reading properties, traversing nested containers, enumerating keys, and using non-mutating behavior must continue to work. Any attempted alteration must instead throw the exact required string literal; it must not throw an `Error` object and must not change the original JSON value.

Assigning or otherwise modifying a property of an object throws `"Error Modifying: key"`. Modifying an array index throws `"Error Modifying Index: index"`. Calling any mutating array method—`pop`, `push`, `shift`, `unshift`, `splice`, `sort`, or `reverse`—throws `"Error Calling Method: methodName"`. Nested objects and arrays require the same protection as the root.
