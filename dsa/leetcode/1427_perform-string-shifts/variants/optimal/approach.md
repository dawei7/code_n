## General
**Combine shifts algebraically.** Represent a right shift as a positive amount and a left shift as a negative amount. Sum those signed amounts across all operations. Cyclic rotations compose by adding their offsets, so only the final net value matters even though the operations are presented sequentially.

**Apply one normalized rotation.** Reduce the net right shift modulo $n$. If the result is zero, return `s` unchanged. Otherwise, split before the last `net` characters and concatenate the suffix before the prefix.

**Why composition is equivalent.** Each operation changes every character's cyclic index by its signed amount. Adding all changes gives the same final index as applying them one at a time, and modulo reduction preserves that cyclic destination. The single rotation therefore produces exactly the sequential result.

## Complexity detail
Reading the $q$ operations takes $O(q)$ time, and constructing the rotated string copies $O(n)$ characters, for $O(n+q)$ total time. The returned string uses $O(n)$ space.

## Alternatives and edge cases
- **Execute each operation directly:** Slice and concatenate after every shift. It is correct but repeatedly copies the string and takes $O(nq)$ time.
- **Shift one character at a time:** Repeating unit rotations for every amount can take $O(n\sum a_i)$ time.
- **Opposite directions:** Signed amounts naturally cancel.
- **Amount at least n:** Reduce only the final total modulo $n$; individual large amounts need no special case.
- **Net zero:** Return the original ordering.
- **Single character:** Every rotation produces the same string.
- **Direction sign:** Direction `0` is left and must subtract; direction `1` is right and must add.
