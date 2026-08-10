## General

The set of reachable strings changes completely depending on whether `k` equals 1 or is at least 2. The solution separates those cases because they have different mathematical behavior.

**Case `k == 1`: only rotation is possible.** The only eligible character is the first one. Moving it to the end transforms

```text
s[0] s[1] ... s[n-1]
```

into

```text
s[1] ... s[n-1] s[0]
```

which is a one-position left rotation. Repeating the operation generates all $n$ cyclic rotations and nothing else. Relative circular order never changes, so arbitrary sorting is impossible.

The exact code begins with the original string as `ans`, then performs `len(s) - 1` rotations. Together with the original, that examines exactly $n$ rotation positions. After every rotation, `ans = min(ans, s)` keeps the lexicographically smallest string seen.

After $n$ rotations the original arrangement returns, so further moves only repeat the same cycle. This proves the enumeration is complete.

For `s = "cba"`, the rotations are `cba`, `bac`, and `acb`. Their lexicographic minimum is `acb`.

**Case `k >= 2`: every permutation is reachable.** Having at least the first two positions available breaks the fixed cyclic order. Rotating by repeatedly moving the first character to the end can place any neighboring circular pair into the first two positions. Choosing the second of those positions instead of the first changes their relative order. Combining such operations and rotations can realize adjacent transpositions, and adjacent transpositions generate every permutation.

Another constructive way to view the freedom is that the first two eligible characters provide a buffer: one character can be held back while the character before or after it is moved around the queue. Repeating this local reordering lets the process arrange characters in any desired order. Values of `k` greater than 2 include at least the same choices and therefore cannot reduce reachability.

If every permutation is reachable, the lexicographically smallest reachable string is simply the characters sorted in ascending order. Lexicographic comparison prioritizes the first differing position, so placing the smallest available character first, then the next smallest, and so on is globally minimal.

The code therefore returns `"".join(sorted(s))` for every `k > 1`.

**Why the case distinction is necessary.** Applying sorting for `k == 1` can return an unreachable string. For example, the sorted form of `cba` is `abc`, but its only rotations are `cba`, `bac`, and `acb`. Conversely, enumerating only rotations for `k >= 2` misses reachable non-rotation permutations.

For the rotation branch, it is helpful to view the string as labels written around a circle. Moving the first character to the end changes only where the linear reading begins; it never changes the clockwise order of the labels. Every possible reading start is reached once during $n$ moves. This circular-order invariant proves not only that all rotations are reachable, but also that no non-rotation can appear when `k == 1`.

**Lexicographic minimum handling.** Python string comparison is lexicographic and characters are lowercase English letters, so `min` and `sorted` use exactly the required ordering. Duplicate characters create duplicate rotations or equivalent permutations, but they do not affect the minimum.

The input string is immutable. In the rotation branch, each assignment creates a new string value rather than modifying a shared buffer.

## Complexity detail

Let $n=\lvert s\rvert$.

- **When `k == 1`:** The exact code constructs $n-1$ rotations using slicing and concatenation. Each construction and comparison can cost $O(n)$, so time is $O(n^2)$ and temporary space is $O(n)$.
- **When `k > 1`:** Comparison sorting costs $O(n\log n)$ time and $O(n)$ space for sorted characters and the returned string.

The overall worst-case exact bound is $O(n^2)$ time and $O(n)$ space. The manifest's $O(n)$ time does not match these Python operations. A linear-time minimum-rotation algorithm could improve the `k == 1` branch, while a fixed-alphabet counting sort could make the other branch linear.

## Alternatives and edge cases

- **Booth's minimum-rotation algorithm:** It finds the smallest cyclic rotation in $O(n)$ time, improving the `k == 1` case.
- **Counting sort for lowercase letters:** A 26-entry frequency array can construct the sorted `k > 1` result in $O(n)$ time.
- **Always sort:** Incorrect for `k == 1` because only rotations are reachable.
- **Always test rotations:** Incorrect for `k >= 2` because many non-rotation permutations are reachable.
- **One-character string:** Both branches return the same sole string; no move changes it.
- **`k` equals string length:** Any character can be moved directly, and the general permutation result applies.
- **Duplicate letters:** Several operations may lead to identical strings, but comparing them repeatedly does not alter correctness.
- **Already sorted with `k > 1`:** Sorting returns the input unchanged.
- **Already minimum among rotations:** The initial `ans = s` ensures the original is considered.
- **Exactly $n$ rotations:** The $n$-th returns to the original, so checking the original plus $n-1$ new rotations covers the cycle.
- **Lowercase contract:** Native character sorting matches lexicographic order without locale or case complications.
- **Input immutability:** The local variable `s` is rebound to new rotation strings; the caller's string cannot be mutated.
- **Manifest mismatch:** The exact repeated slicing branch must not be described as $O(n)$ merely because a more advanced minimum-rotation method exists.
