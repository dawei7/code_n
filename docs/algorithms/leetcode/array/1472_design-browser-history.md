# Design Browser History

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1472 |
| Difficulty | Medium |
| Topics | Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream |
| Official Link | [design-browser-history](https://leetcode.com/problems/design-browser-history/) |

## Problem Description & Examples
### Goal
Design browser history navigation with a current page, backward navigation, forward navigation, and visits to new pages that clear forward history.

### Function Contract
**Inputs**

- Constructor input: `homepage`.
- `visit(url)`: move to a new page and erase forward history.
- `back(steps)`: move back up to `steps` entries.
- `forward(steps)`: move forward up to `steps` entries.

**Return value**

The data structure mutates over time; `back` and `forward` return the current URL after moving.

### Examples
**Example 1**

- Input: `BrowserHistory("leetcode.com"); visit("google.com"); visit("facebook.com"); back(1)`
- Output: `"google.com"`

**Example 2**

- Input: `BrowserHistory("leetcode.com"); visit("a.com"); visit("b.com"); back(2); forward(1)`
- Output: `"a.com"`

**Example 3**

- Input: `BrowserHistory("home.com"); visit("x.com"); back(1); visit("y.com"); forward(1)`
- Output: `"y.com"`

---

## Underlying Base Algorithm(s)
Array history with a current index. Visiting truncates entries after the current index, appends the new URL, and updates the pointer; navigation clamps the pointer within valid bounds.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` per `back` or `forward`; `visit` may be `O(f)` if truncating `f` forward entries.
- **Space Complexity**: `O(v)` for visited pages.
