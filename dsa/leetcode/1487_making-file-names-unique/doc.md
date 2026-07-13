# Making File Names Unique

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1487 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [making-file-names-unique](https://leetcode.com/problems/making-file-names-unique/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/making-file-names-unique/).

### Goal
Assign folder names in order. If a requested name already exists, append the smallest positive suffix `(k)` that makes it unique.

### Function Contract
**Inputs**

- `names`: requested folder names.

**Return value**

The assigned unique names in order.

### Examples
**Example 1**

- Input: `names = [\"pes\",\"fifa\",\"gta\",\"pes(2019)\"]`
- Output: `[\"pes\",\"fifa\",\"gta\",\"pes(2019)\"]`

**Example 2**

- Input: `names = [\"gta\",\"gta(1)\",\"gta\",\"avalon\"]`
- Output: `[\"gta\",\"gta(1)\",\"gta(2)\",\"avalon\"]`

**Example 3**

- Input: `names = [\"onepiece\",\"onepiece(1)\",\"onepiece\"]`
- Output: `[\"onepiece\",\"onepiece(1)\",\"onepiece(2)\"]`

---

## Solution
### Approach
Hash map of next suffixes. Store every assigned name and the next suffix to try for each base, advancing until a free candidate is found.

### Complexity Analysis
- **Time Complexity**: Amortized `O(n)` assigned names, since each tried suffix is advanced once.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(names):
    if not isinstance(names, list):
        names = [names]
    used = {}
    result = []
    for name in names:
        name = str(name)
        if name not in used:
            used[name] = 1
            result.append(name)
            continue
        suffix = used[name]
        while f"{name}({suffix})" in used:
            suffix += 1
        used[name] = suffix + 1
        unique = f"{name}({suffix})"
        used[unique] = 1
        result.append(unique)
    return result
```
</details>
