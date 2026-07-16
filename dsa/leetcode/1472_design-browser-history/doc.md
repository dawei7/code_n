# Design Browser History

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1472 |
| Difficulty | Medium |
| Topics | Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/design-browser-history/) |

## Problem Description
### Goal

Model the history of a browser with one active tab. The browser begins at a supplied homepage. It can visit a new URL from its current page, move backward by up to a requested number of history entries, or move forward by up to a requested number of entries.

Visiting a URL makes that page current and permanently clears every forward entry that was reachable from the former current page. Backward and forward requests are clamped by the history that actually exists: if fewer than `steps` pages are available in the requested direction, move as far as possible and return the URL reached. Implement these rules in the `BrowserHistory` class.

### Function Contract
**Platform interface**

- `BrowserHistory(homepage)` initializes the only history entry and makes `homepage` current.
- `visit(url)` moves to `url`, discards all forward history, and returns nothing.
- `back(steps)` moves at most `steps` entries toward the homepage and returns the current URL.
- `forward(steps)` moves at most `steps` entries toward the newest valid page and returns the current URL.

Both `homepage` and every `url` have length from $1$ through $20$ and contain only lowercase English letters and `.`. Each `steps` value lies in $[1,100]$, and there are at most $5000$ method calls.

**App-local adapter**

Let $q$ be the number of entries in `operations`, and let $v$ be the number of `visit` entries.

- `homepage`: the initial URL.
- `operations`: an ordered array of `[name, arguments]` entries using `"visit"`, `"back"`, or `"forward"`.
- Return one output per operation: `null` for `visit`, and the returned current URL for `back` or `forward`.

### Examples
**Example 1**

- Input: `homepage = "leetcode.com", operations = [["visit",["google.com"]],["visit",["facebook.com"]],["visit",["youtube.com"]],["back",[1]],["back",[1]],["forward",[1]],["visit",["linkedin.com"]],["forward",[2]],["back",[2]],["back",[7]]]`
- Output: `[null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]`
- Explanation: Visiting `linkedin.com` from `facebook.com` removes `youtube.com` from the forward path. The later forward request therefore remains at `linkedin.com`, and the final oversized backward request stops at the homepage.

**Example 2**

- Input: `homepage = "home.com", operations = [["visit",["a.com"]],["visit",["b.com"]],["back",[2]],["forward",[1]]]`
- Output: `[null,null,"home.com","a.com"]`
- Explanation: Moving backward or forward changes only the current position; it does not delete entries.

**Example 3**

- Input: `homepage = "home.com", operations = [["visit",["x.com"]],["back",[1]],["visit",["y.com"]],["forward",[100]]]`
- Output: `[null,"home.com",null,"y.com"]`
- Explanation: The visit from the homepage clears `x.com`, so no forward page remains.

### Required Complexity
- **Time:** $O(q)$
- **Space:** $O(v)$

<details>
<summary>Approach</summary>

#### General

**Representing the valid timeline**

Store visited URLs in an array `history`. Two indices describe its logical state:

- `current` identifies the page displayed now.
- `last` identifies the final entry that still belongs to valid history.

Only the prefix from index `0` through `last` is logically reachable. Array cells beyond `last` may contain stale URLs left from an older forward branch, but navigation never reads them. Initially, `history = [homepage]` and both indices are zero.

**Visiting without copying a history prefix**

A new visit belongs immediately after the current entry, so increment `current`. If that index already exists in the allocated array, overwrite it with the new URL; otherwise append the URL. Then assign `last = current`.

Resetting `last` is the logical deletion of all former forward history. No slice, loop, or physical removal is necessary. Suppose the active prefix was `[home, a, b, c]`, `current` moved back to `a`, and `d` is visited. Overwriting index two produces `[home, a, d, c]`, but setting `last = 2` makes `c` unreachable. A later visit may overwrite that stale cell as well.

**Clamping navigation with indices**

For `back(steps)`, set `current = max(0, current - steps)`. Index zero is the homepage and is the farthest legal backward destination. For `forward(steps)`, set `current = min(last, current + steps)`; `last`, rather than the physical array length, prevents traversal into a discarded branch. Return `history[current]` after either update.

**Why the representation implements browser semantics**

Maintain the invariant that `history[0:last + 1]` is exactly the valid history timeline and `current` identifies its active page. Construction establishes it with one page. A back or forward operation keeps the same valid prefix and clamps `current` to one of its indices, preserving the invariant.

On a visit, entries through the old `current` remain unchanged, the next logical entry becomes the new URL, and assigning `last` to that position excludes every old forward entry. The resulting valid prefix is therefore precisely the retained past followed by the new page, and `current == last` identifies it. By induction over all calls, every returned URL and every cleared branch matches the required behavior.

#### Complexity detail

Construction takes $O(1)$ time. Each `back` and `forward` call performs constant-time arithmetic, clamping, and indexing. Each `visit` performs one overwrite or an amortized $O(1)$ append, so all $q$ operations take $O(q)$ total time.

At most one stored array position is needed for the homepage plus each visit that extends the greatest allocated depth. This is $O(v)$ space. Stale cells beyond `last` do not change the bound and are reused by later visits.

#### Alternatives and edge cases

- **Two stacks:** Keep backward pages in one stack and forward pages in another. A visit pushes the old current page and clears the forward stack; navigation transfers one entry per step. This is intuitive, but a call costs $O(\texttt{steps})$ rather than constant time.
- **Doubly linked list:** Store pages as nodes with previous and next links. Navigation still walks one node per step, and a new visit detaches the forward chain. It supports the model directly but adds allocation and pointer overhead.
- **Slice the array on every visit:** Replacing history with `history[:current + 1]` before appending is correct, but copying a long retained prefix on repeated back/visit cycles can take $O(q^2)$ total time.
- **Physically delete every forward entry:** Popping the discarded suffix is semantically correct, yet its cost is proportional to the cleared branch. Logical deletion by changing `last` is sufficient.
- **Oversized backward request:** Clamp at index zero and return the homepage; never wrap around or raise an error.
- **Oversized forward request:** Clamp at `last`, which may be earlier than the physical final array cell after a branch was cleared.
- **Visit while already at the latest page:** Advance by one and append or reuse storage normally; there is no forward branch to preserve.
- **Repeated URLs:** History is positional. Visiting the same URL twice creates two distinct entries and navigation must traverse both.
- **Forward after a branch-changing visit:** It must remain on the newly visited page until another visit extends that new branch.

</details>
