## Description

Build a new JavaScript object from two parallel arrays, `keysArr` and `valuesArr`. For every index $i$, the element `keysArr[i]` proposes the property whose value is `valuesArr[i]`.

Convert each proposed key by calling `String()`. When multiple input elements convert to the same property name, keep only the pair at the earliest index and ignore every later collision. The result must therefore preserve the first value associated with each converted key, including names that already have special meaning on ordinary JavaScript objects.

The two arrays always have equal length. Empty arrays produce an empty object.
