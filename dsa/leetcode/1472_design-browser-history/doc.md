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
