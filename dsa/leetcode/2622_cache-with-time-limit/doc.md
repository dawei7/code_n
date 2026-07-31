# Cache With Time Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2622 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/cache-with-time-limit/) |

## Problem Description

### Goal

Implement a JavaScript cache whose integer keys expire after individually assigned durations. Every stored key is associated with an integer value and a timer measured in milliseconds. Once its duration has elapsed, that key must no longer be accessible or included in the cache size.

The class exposes three operations. `set(key, value, duration)` stores the pair for the given duration and returns whether the same key was already present and unexpired. When replacing an active key, both its value and its expiration deadline must be reset. `get(key)` returns the active value or `-1` when the key is absent or expired. `count()` returns the number of currently unexpired keys.

Keys and values are between $0$ and $10^9$, durations are between $0$ and $1000$ milliseconds, and at most $100$ actions are performed.

### Function Contract

**Inputs**

- `key`: The integer cache key used by `set` or `get`.
- `value`: The integer value stored by `set`.
- `duration`: The number of milliseconds for which the new value remains active.

The local adapter receives parallel `actions`, `values`, and `timeDelays` arrays describing calls and their absolute execution times.

**Return value**

`set` returns whether an unexpired entry was replaced. `get` returns the active value or `-1`. `count` returns the number of active keys.

### Examples

**Example 1**

- Input: `set(1, 42, 100)` at $t=0$, `get(1)` and `count()` at $t=50$, then `get(1)` at $t=150$
- Output: `[false, 42, 1, -1]`
- Explanation: Key `1` is active through the first two queries and has expired before the final query.

**Example 2**

- Input: `set(1, 42, 50)` at $t=0$, then `set(1, 50, 100)` at $t=40$
- Output: `[false, true]`
- Explanation: The second call replaces an active key and establishes a new deadline at $t=140$.

**Example 3**

- Input: `set(7, 9, 0)`, followed immediately in the same turn by `get(7)`
- Output: `[false, 9]`
- Explanation: A zero-delay timer expires asynchronously; the entry exists until its timer callback executes.
