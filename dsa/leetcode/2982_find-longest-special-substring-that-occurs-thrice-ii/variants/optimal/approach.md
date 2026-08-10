## General

**Reduce every candidate to a character and a length**

A special substring is entirely one repeated character. Instead of comparing arbitrary strings, a candidate can be represented as `(character, length)`. Its occurrences can exist only within maximal runs of that character.

Suppose one run has length $L$. A candidate of length $x$ fits at starting offsets zero through $L-x$, so that run contributes $L-x+1$ occurrences when $L\ge x$, and zero otherwise. Overlapping starts count separately.

The helper `check(x)` computes these totals. Pointer `i` begins a run, `j` advances to the first different character or the end, and the run contribution is `max(0, j - i - x + 1)`. Dictionary `cnt` adds contributions under the run’s character. At the end, `max(cnt.values()) >= 3` says whether at least one length-$x$ special string occurs three times.

**Why maximal runs form a complete accounting**

Every special occurrence is contained within exactly one maximal equal-character run; it cannot cross a boundary where the character changes. Within a run, the start-position formula counts it exactly once. Summing over all runs of the same character therefore gives the exact global occurrence count for that special string.

This includes two patterns that are easy to miss:

- one long run can supply several overlapping occurrences;
- several shorter runs of the same letter can combine to reach three occurrences.

For example, a run `"aaaa"` supplies three occurrences of `"aa"`. Separately, three isolated `'a'` runs supply three occurrences of the length-one string `"a"`.

**Why feasibility is monotone**

If length $x$ is feasible, choose its three occurrences. Shortening each occurrence by one character at the right produces three occurrences of the same repeated character with length $x-1$ and the same starting positions. Therefore every positive length below a feasible length is also feasible.

This monotonicity permits binary search over the answer. Search boundaries begin as `l = 0` and `r = n`. Zero is a sentinel representing “no nonempty candidate found yet.” The upper midpoint is calculated as `mid = (l + r + 1) >> 1`.

When `check(mid)` is true, `mid` and all smaller lengths are feasible, so `l` moves to `mid`. When false, `mid` and all larger lengths are impossible, so `r` moves to `mid - 1`. The upper midpoint ensures progress even when `r = l + 1`.

After convergence, `l` is the maximum feasible length. The return expression changes zero to `-1` because the problem requires a nonempty substring and uses `-1` when none occurs three times.

**Why the large input still avoids substring creation**

The string can contain 500,000 characters. Creating every candidate substring or using slicing inside nested loops would be far too expensive. `check` never creates a substring. It compares adjacent characters, measures run lengths through indices, and uses one integer count per encountered letter.

Each binary-search probe rereads the string, but there are only $O(\log N)$ probes. This gives a log-linear method rather than quadratic or cubic enumeration.


For fixed $x$, the run decomposition proves `check(x)` is true exactly when a length-$x$ special substring has at least three positional occurrences. The shortening argument proves these truth values are monotone over $x$. Standard binary-search reasoning then proves the final `l` is the largest true length. If no positive length is true, `l=0` and the required answer is `-1`.

No probabilistic hashing or string comparison is involved, so there are no collision concerns.

**The exact source is not the manifest’s linear method**

The manifest summary says the solution retains three longest values per letter in a single pass and lists $O(N)$ time. The exact Optimal source for this package is identical to version I’s binary-search implementation. It calls an $O(N)$ checker $O(\log N)$ times and therefore has actual time complexity $O(N\log N)$.

At $N=500{,}000$, this is materially different, even though it remains a practical and asymptotically efficient solution. The document follows the executable behavior rather than attributing a different editorial algorithm to it.

## Complexity detail

Let $N$ be the length of `s`. Each `check` call traverses all runs and, across those runs, advances over all $N$ characters once. It takes $O(N)$ time. Binary search uses $O(\log N)$ calls, so total time is $O(N\log N)$.

The dictionary has at most 26 entries because the alphabet is fixed. It is recreated for each check and released afterward. Auxiliary space is therefore $O(26)=O(1)$, plus constant pointer and binary-search state. No substring copies or arrays proportional to $N$ are created.

## Alternatives and edge cases

- **Three-longest-length method:** Updating three run-derived values per character gives the manifest’s $O(N)$ solution, but that is not what the exact source executes.
- **Frequency table by every length:** It can be linear with suffix accumulation but requires $O(26N)$ storage, which is substantial at the large constraint.
- **Enumerate all special starts and lengths:** A single long run has $\Theta(N^2)$ such substrings, making explicit enumeration too slow.
- **Ignore overlaps:** This would fail the central `"aaaa"` example because its three length-two occurrences overlap.
- **Combine different letters:** Occurrences count only when the substring contents are identical; dictionary keys keep letters separate.
- **Combine separated runs of one letter:** This is required and handled by adding to the same dictionary key.
- **All one repeated letter:** The maximum length occurring three times is $N-2$.
- **No qualifying character:** The zero sentinel becomes `-1`.
- **Manifest mismatch:** The correct bound for this file is $O(N\log N)$ time and $O(1)$ auxiliary space.
