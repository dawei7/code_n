# Implement Router

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3508 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Design, Queue, Ordered Set |
| Official Link | [implement-router](https://leetcode.com/problems/implement-router/) |

## Problem Description & Examples
### Goal
Design a routing system that manages a collection of network paths. The system must support registering specific URL patterns (which may include wildcards) and resolving incoming request URLs to the most specific matching registered path. If multiple patterns match, the system should prioritize the longest or most specific match.

### Function Contract
**Inputs**

- `add_route(pattern: str, handler: str)`: Registers a URL pattern to a specific handler.
- `resolve(url: str) -> str`: Returns the handler associated with the best-matching pattern for the given URL, or an empty string if no match exists.

**Return value**

- `resolve` returns the `handler` string associated with the matched pattern.

### Examples
**Example 1**

- Input: `add_route("/api/v1/*", "v1_handler"), resolve("/api/v1/users")`
- Output: `"v1_handler"`

**Example 2**

- Input: `add_route("/static/*", "static_handler"), add_route("/static/images/*", "img_handler"), resolve("/static/images/logo.png")`
- Output: `"img_handler"`

**Example 3**

- Input: `add_route("/home", "home_handler"), resolve("/about")`
- Output: `""`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes a **Trie (Prefix Tree)** data structure. Each node in the Trie represents a segment of the URL path (split by '/'). Wildcards are handled by storing a special node type that matches any segment but carries a lower priority than exact matches during the traversal.

---

## Complexity Analysis
- **Time Complexity**: `O(L)` for both `add_route` and `resolve`, where `L` is the number of segments in the URL path.
- **Space Complexity**: `O(N * L)` where `N` is the number of registered routes and `L` is the average length of the routes.
