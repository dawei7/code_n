## General
Every candidate has the same fixed length, ten. Slide a window from start index `0` through `len(s) - 10`, and track two states:

- `seen` contains sequences encountered at least once.
- `repeated` contains sequences encountered at least twice.

On a first occurrence, insert the window into `seen`. On every later occurrence, insert it into `repeated`. Because the second collection is a set, a sequence appearing three or more times still contributes only one output value.

Overlapping windows count independently. In `"AAAAAAAAAAAAA"`, the ten-character sequence beginning at indices `0`, `1`, `2`, and `3` is the same, so `"AAAAAAAAAA"` is reported once.

Since ten is a problem constant, extracting and hashing a ten-character substring is constant work in asymptotic terms. A lower-level implementation can avoid substring allocation by encoding `A`, `C`, `G`, and `T` as two-bit digits. Then a 20-bit rolling value represents the window: shift left by two, add the next character, and mask away bits older than ten positions.

Before each window is processed, `seen` contains exactly the earlier windows and `repeated` contains exactly those earlier sequences already observed at least twice. A new sequence enters `seen` but not `repeated`, preserving both meanings. An already-seen sequence has now occurred at least twice and is added to `repeated`; set semantics prevent duplicate output. Therefore every returned sequence has at least two occurrences, and every sequence with at least two occurrences enters `repeated` at its second one.

## Complexity detail
There are $n - 9$ windows when $n \ge 10$, hence $O(n)$ windows. With the fixed length ten, substring hashing is expected $O(1)$ per window, for expected $O(n)$ time. The sets can hold $O(n)$ distinct windows and use $O(n)$ space. The rolling two-bit variant has the same bounds with smaller constant-sized keys.

## Alternatives and edge cases
- A two-bit rolling encoding avoids allocating substring keys but adds bit-manipulation complexity.
- A frequency map works, though counts above two store information the output does not need.
- Comparing every pair of windows is quadratic.
- Inputs shorter than ten have no candidate windows and return an empty list.
- Exactly one occurrence does not qualify; overlapping and non-overlapping repetitions both do.
- Output order is unrestricted, so converting the repeated set to a list is valid.
