## General
**Begin with the smallest possible string.** Fill all $n$ positions with `a`. This contributes value $n$, leaving `remaining = k - n` additional value to distribute. Each position can absorb at most 25 more before reaching `z`.

**Spend extra value from right to left.** At the last position, add as much as possible, up to 25, then continue toward the front until no value remains. Concentrating increases at later positions preserves smaller letters at every earlier position for as long as feasibility allows.

**Why the greedy placement is lexicographically minimal.** Suppose an alternative places some positive increase at an earlier position while a later position is not yet `z`. Moving one unit of value from the earlier character to the later one preserves the total sum and length but makes the first differing position smaller. Therefore no optimal string can have such a pair. The required form is consequently some `a` prefix, at most one partially increased character, and a suffix of `z` characters—exactly what right-to-left allocation produces.

## Complexity detail
Creating and joining the $n$ output characters takes $O(n)$ time. The allocation loop visits at most $n$ positions, so total time remains $O(n)$. The mutable character array used to build the required output occupies $O(n)$ space.

## Alternatives and edge cases
- **Direct quotient construction:** Divide `k - n` by 25 to determine the number of trailing `z` characters and the optional middle character, then assemble the same greedy form.
- **Left-to-right feasibility checks:** Try letters in order while reserving enough capacity for the suffix. This is correct, but recomputing suffix capacity by scanning remaining positions can cost $O(n^2)$.
- **Largest letters first at the front:** This satisfies the sum but produces a lexicographically large string.
- When $k=n$, every character is `a`.
- When $k=26n$, every character is `z`.
- A remainder divisible by 25 needs no partially increased middle character.
- For $n=1$, the answer is the single letter whose value is `k`.
- The output length itself imposes an $\Omega(n)$ time and space requirement for materializing the returned string.
