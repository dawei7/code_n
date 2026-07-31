## General

Item types do not interact: a window violation for one type depends only on retained arrivals of that same type. For each type, maintain a deque containing the indices of its retained arrivals that still lie in the current $w$-day window.

Before deciding day $i$, remove deque entries at most $i-w$, because those days lie before the current window. If the current type's deque now contains fewer than $m$ indices, keep the arrival and append $i$. If it already contains $m$, retaining the current arrival would create $m+1$ occurrences, so discard it and leave the deque unchanged.

Keeping an allowed arrival is always optimal. Compared with the new arrival, every previously retained arrival expires no later from every future window. If some optimal plan discarded an earlier retained item to keep the current one instead, exchanging those choices preserves feasibility and cannot reduce future capacity. Thus the greedy plan retains as many arrivals as any feasible plan, and its discard count is minimum.

Discarded days are never appended, so they neither consume current capacity nor need later expiration handling.

## Complexity detail

Each retained day is appended once and removed once. All deque operations therefore total $O(n)$ expected time, including expected constant-time hash-map access for each item type. Across all deques, at most $n$ indices are stored, giving $O(n)$ space.

The benchmark defines its size as $n$, sets `w = m = n`, and uses one repeated type. Every arrival is retained, forcing a correct rescan strategy to inspect the complete preceding window on each day. The accepted deques remain linear while that alternative grows quadratically.

## Alternatives and edge cases

- **Rescan the current window:** Counting matching retained arrivals from scratch is correct but can take $O(nw)$ time.
- **Global count plus retained flags:** Expiring `arrivals[i - w]` only when that day was retained is another linear implementation, but it needs a parallel decision array.
- **Window length one:** Every window contains a single day, and $m\ge1$, so no discard is needed.
- **Limit equals window length:** No type can exceed the limit, so every arrival is retained.
- **Discarded expiration day:** A discarded item never entered the deque and must not decrement a later count.
- **Sparse repeated type:** Old retained indices may expire across a long gap; remove all stale indices before checking capacity.
- **Different types:** Their capacities are independent even when they share the same time window.
