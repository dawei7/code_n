## General

**A window is invalid only after its second equal-adjacent boundary**

A substring is semi-repetitive when it contains at most one index where consecutive digits are equal. Rather than count digit frequencies, the algorithm counts these special adjacent boundaries.

For each right endpoint `i`, the comparison `s[i] == s[i - 1]` tells whether the newly included boundary contributes one repeated pair. Python Booleans behave as integers in arithmetic, so adding the comparison increments `cnt` by one when equal and by zero otherwise.

The sliding window is `s[j:i + 1]`. The invariant after shrinking is that `cnt` equals the number of equal-adjacent pairs fully inside this window and is at most one.

**Why pairs, not runs, must be counted**

String `"111"` has two equal adjacent pairs: the boundary between the first two characters and the boundary between the last two. Although it is one run of repeated digit, it violates the “at most one adjacent pair” condition.

Counting every boundary comparison handles this correctly. As the right endpoint enters the third `'1'`, `cnt` becomes two, forcing the left boundary forward.

**Extend the right endpoint once**

The loop begins at `i=1` because index zero has no preceding character. Before processing `i`, the prior window ending at `i-1` is valid.

Adding `s[i]` creates exactly one new internal boundary, between `i-1` and `i`. No older adjacency changes. Therefore the one Boolean addition updates `cnt` completely.

If `cnt <= 1`, the expanded window remains valid and no shrinking is necessary.

**Shrink until the oldest extra pair is removed**

When `cnt > 1`, the code advances `j` inside a while loop. Removing the character at old index `j` removes exactly one possible adjacency from the window: the boundary between `j` and `j+1`.

The statement:

`cnt -= s[j] == s[j + 1]`

subtracts one if that outgoing boundary was an equal pair. Then `j += 1` establishes the smaller window.

If the outgoing boundary was unequal, `cnt` stays above one and shrinking continues. Eventually the left endpoint passes the older equal boundary, decreasing `cnt`. Since the window before adding `i` had at most one repeated pair, adding one new boundary can raise the count only to two. Removing the old one restores the limit.

**Why the remaining window is longest for this right endpoint**

When a second repeated pair appears, any substring ending at `i` that starts at or before the older repeated pair contains both pairs and is invalid. The while loop moves `j` only far enough to exclude that older pair. Stopping earlier would be invalid; moving farther would make the window unnecessarily short.

Thus after shrinking, `s[j:i+1]` is the longest valid substring ending at `i`. Taking the maximum of `i - j + 1` across all right endpoints yields the global longest valid substring.

**Trace s equal to 52233**

The initial answer is one. At `i=1`, boundary `5-2` is unequal, so the window `"52"` has count zero.

At `i=2`, boundary `2-2` is equal, so count becomes one and `"522"` is valid.

At `i=3`, boundary `2-3` is unequal, so `"5223"` remains valid with length four.

At `i=4`, boundary `3-3` is equal and count becomes two. The loop advances `j` past boundary `5-2` without decreasing count, then past boundary `2-2`, which lowers count to one. The new window is `"233"`. The recorded maximum remains four.

**Trace all identical digits**

For `"1111111"`, every new boundary is equal. Once a length-three window appears, count reaches two and `j` moves one step, removing the oldest equal boundary. The valid window returns to length two. This repeats, so the answer is two.

**Why every pointer moves only forward**

The right endpoint visits indices in increasing order. The left endpoint never moves backward. This monotonicity is what makes the method linear even though it contains a while loop.


The counter exactly tracks repeated boundaries in the current window because right extension adds its one new boundary and left contraction removes its one outgoing boundary. The while loop ends precisely when the window is semi-repetitive. It uses the smallest possible left endpoint for each right endpoint, so the window is the longest valid one ending there. Every substring has some right endpoint, and the maximum over these per-endpoint optima is therefore the longest semi-repetitive substring.

## Complexity detail

Let $n$ be the string length. The right pointer advances $n-1$ times. The left pointer `j` advances at most $n-1$ times over the entire run, because it never retreats. Each comparison and update is constant time, so total time is $O(n)$ rather than $O(n^2)$.

The algorithm stores `ans`, `n`, `cnt`, `j`, `i`, and a few temporary Boolean values. It creates no substring copies, so auxiliary space is $O(1)$.

The input string is read-only. Window boundaries are represented by integer indices.

## Alternatives and edge cases

- **Enumerate every substring:** Checking all $O(n^2)$ substrings repeats work and can become $O(n^3)$ with rescanning.
- **Store positions of repeated pairs:** Keeping only the most recent pair boundary can yield another linear formulation, but the counter window is direct.
- **Count repeated runs:** Incorrect because a run of length three contributes two adjacent equal pairs.
- **Length one:** `ans` starts at one, and the loop is empty, so the answer is one.
- **No equal neighbors:** The whole string stays in the window and the answer is $n$.
- **Exactly one equal pair:** The whole string is still valid.
- **All digits equal:** No valid window can exceed length two when $n\ge2$.
- **Pairs at both ends:** The window must exclude one of them; shrinking removes the older pair for the current right endpoint.
- **Overlapping pairs:** `"111"` contributes two and is correctly reduced to length two.
- **Boolean arithmetic:** In Python, `True` is one and `False` is zero, making the compact counter updates exact.
