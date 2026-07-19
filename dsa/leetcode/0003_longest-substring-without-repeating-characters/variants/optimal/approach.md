## General
**Reuse the longest valid suffix**

Starting a fresh scan at every position repeats work. When a new rightmost character is appended, the previous window can become invalid for only one reason: that same character already occurs inside it. All other character relationships are unchanged.

Track the most recent index of every character. For a right endpoint `r` containing `c`, move the left boundary to `last[c] + 1` only when that previous occurrence lies inside the current window. Then record the new index and compare the window length with the best seen so far.

**Stale occurrences must not move the window backward**

The safe update is `left = max(left, last[c] + 1)`. In `abba`, the second `b` moves `left` past the first `b`. When the final `a` arrives, its old occurrence is already outside the window; assigning `left = last['a'] + 1` directly would move the boundary backward and incorrectly admit both `b` characters.

**One optimal window for every endpoint**

After the duplicate adjustment, `s[left:r+1]` is the longest distinct-character substring ending at `r`. Any earlier start would include the conflicting previous occurrence, while any later start is shorter. Every possible answer has some right endpoint, so taking the maximum of these endpoint-optimal windows yields the global optimum.

For `s = "pwwkew"`:

| Right endpoint | Character | Left boundary | Valid suffix | Best |
|---:|:---:|---:|---|---:|
| 0 | p | 0 | `p` | 1 |
| 1 | w | 0 | `pw` | 2 |
| 2 | w | 2 | `w` | 2 |
| 3 | k | 2 | `wk` | 2 |
| 4 | e | 2 | `wke` | 3 |
| 5 | w | 3 | `kew` | 3 |

## Complexity detail
Each character is processed once as a right endpoint, and the left boundary never moves backward, giving $O(n)$ time. The last-occurrence table stores at most the smaller of `n` and the alphabet size `a`, so space is $O(\min(n, a))$.

## Alternatives and edge cases
- **Restart from every index:** can inspect the same region repeatedly and takes $O(n^2)$ time.
- **Sliding window with a set:** is also linear because characters enter and leave once, but advances the left boundary one position at a time instead of jumping.
- **Fixed index array:** can replace the hash table for a known small alphabet.
- The empty string returns zero. Repeated characters outside the active window must be ignored as stale.
