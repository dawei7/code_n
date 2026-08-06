## General
**Reuse the longest valid suffix**

Starting a fresh scan at every position repeats work. When a new rightmost character is appended, the previous window can become invalid for only one reason: that same character already occurs inside it. All other character relationships are unchanged.

Track the most recent position of every character in `last_seen`. For a right boundary `right` containing `char`, move `left` to `last_seen[char] + 1` only when that previous occurrence lies inside the current window. Then store `last_seen[char] = right` and compare `right - left + 1` with the best length seen so far.

**Stale occurrences must not move the window backward**

The safe update is `left = max(left, last_seen[char] + 1)`. In `abba`, the second `b` moves `left` past the first `b`. When the final `a` arrives, its old occurrence is already outside the window; assigning `left = last_seen[char] + 1` directly would move the boundary backward and incorrectly admit both `b` characters.

**One optimal window for every right boundary**

After the duplicate adjustment, `s[left:right + 1]` is the longest distinct-character substring ending at `right`. Any earlier start would include the conflicting previous occurrence, while any later start is shorter. Every possible answer has some right boundary, so taking the maximum of these boundary-optimal windows yields the global optimum.

For `s = "pwwkew"`:

| Right boundary | Character | Left boundary | Valid suffix | Best |
|---:|:---:|---:|---|---:|
| 0 | p | 0 | `p` | 1 |
| 1 | w | 0 | `pw` | 2 |
| 2 | w | 2 | `w` | 2 |
| 3 | k | 2 | `wk` | 2 |
| 4 | e | 2 | `wke` | 3 |
| 5 | w | 3 | `kew` | 3 |

## Complexity detail
Let $n$ be the length of `s`, and let $a$ be the number of characters in its alphabet. Each character is processed once as the right boundary, and `left` never moves backward, giving $O(n)$ time. The last-occurrence table stores at most $min(n, a)$ entries, so the auxiliary space is $O(\min(n, a))$.

## Alternatives and edge cases
- **Restart from every position:** can inspect the same region repeatedly and takes $O(n^2)$ time.
- **Sliding window with a set:** is also linear because characters enter and leave once, but advances `left` one position at a time instead of jumping.
- **Fixed position array:** can replace the hash table when the alphabet is known and small.
- **Empty string:** the loop performs no iterations, so the initialized best length of zero is returned.
- **Stale duplicate:** an occurrence before `left` must not move the window backward.
