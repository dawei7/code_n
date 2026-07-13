# Design Browser History

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1472 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-browser-history](https://leetcode.com/problems/design-browser-history/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-browser-history/).

### Goal
Design browser history navigation with a current page, backward navigation, forward navigation, and visits to new pages that clear forward history.

### Function Contract
**Inputs**

- `homepage`: the initial browser page.
- `operations`: a list of operations after construction. Each operation is `[name, args]`, where `name` is `"visit"`, `"back"`, or `"forward"`.

**Return value**

A list containing `null` for each `visit` operation and the current URL returned by each `back` or `forward` operation.

### Examples
**Example 1**

- Input: `homepage = "leetcode.com", operations = [["visit",["google.com"]],["visit",["facebook.com"]],["back",[1]]]`
- Output: `[null,null,"google.com"]`

**Example 2**

- Input: `homepage = "leetcode.com", operations = [["visit",["a.com"]],["visit",["b.com"]],["back",[2]],["forward",[1]]]`
- Output: `[null,null,"leetcode.com","a.com"]`

**Example 3**

- Input: `homepage = "home.com", operations = [["visit",["x.com"]],["back",[1]],["visit",["y.com"]],["forward",[1]]]`
- Output: `[null,"home.com",null,"y.com"]`

---

## Solution
### Approach
Array history with a current index. Visiting truncates entries after the current index, appends the new URL, and updates the pointer; navigation clamps the pointer within valid bounds.

### Complexity Analysis
- **Time Complexity**: `O(1)` per `back` or `forward`; `visit` may be `O(f)` if truncating `f` forward entries.
- **Space Complexity**: `O(v)` for visited pages.

### Reference Implementations
<details>
<summary>python</summary>

```python
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[: self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


def solve(homepage, operations):
    browser = BrowserHistory(str(homepage))
    output = []
    for raw_operation in operations:
        if not isinstance(raw_operation, list) or not raw_operation:
            continue
        name = str(raw_operation[0])
        args = raw_operation[1] if len(raw_operation) > 1 and isinstance(raw_operation[1], list) else []
        if name == "visit":
            url = str(args[0]) if args else ""
            browser.visit(url)
            output.append(None)
        elif name == "back":
            steps = int(args[0]) if args else 0
            output.append(browser.back(max(0, steps)))
        elif name == "forward":
            steps = int(args[0]) if args else 0
            output.append(browser.forward(max(0, steps)))
    return output
```
</details>
