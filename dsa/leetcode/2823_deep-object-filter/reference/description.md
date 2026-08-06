## Description

Given a JSON object or array `obj` and a Boolean predicate `fn`, filter the structure at every nesting level.

Apply `fn` to primitive leaf values. Remove every leaf for which the predicate returns `false`. After filtering descendants, also remove any object or array that has become empty. Arrays must be compacted so retained elements remain in their original relative order without holes; retained object properties keep their original keys.

If no value remains anywhere in the root object or array, return `undefined`.
