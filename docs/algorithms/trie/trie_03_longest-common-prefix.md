# Longest Common Prefix (Trie Method)

| | |
|---|---|
| **ID** | `trie_03` |
| **Category** | trie |
| **Complexity (required)** | $O(N \times M)$ Time, $O(N \times M)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |

## Problem statement

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

*(Note: We already solved this in $O(N \times M)$ time with $O(1)$ space using Horizontal Scanning in `string_11`. This document demonstrates the Trie-based solution, which is often asked in interviews as a follow-up to test your Trie knowledge).*

**Input:** An array of strings `strs`.
**Output:** A string representing the longest common prefix.

## When to use it

- In an interview when the interviewer says: "Great, your $O(1)$ space horizontal scanning is perfect. Now, what if the array of strings is a massive streaming database that updates constantly, and we need to query the Longest Common Prefix dynamically without rescanning the whole array?"
- You answer: "We build a Trie!"

## Approach

**1. The "Single Child" Characteristic:**
What happens when you insert an array of strings into a Trie?
If all strings share a common prefix, like `"flower"`, `"flow"`, and `"flight"`, they all start with `"fl"`.
Look at the root of the Trie. It only has one child: `'f'`.
Look at the `'f'` node. It only has one child: `'l'`.
Look at the `'l'` node. It has TWO children! `'o'` and `'i'`!
The Longest Common Prefix mathematically corresponds to the single, unbranched path from the root of the Trie downwards!

**2. The Breaking Conditions:**
We insert every string into the Trie. Then, we start at the root and trace downwards.
We add characters to our result string as long as:
1. The current node has EXACTLY 1 child. (If it has 2 children, the strings diverged! Stop!)
2. The current node is NOT the end of a word! (If `"flow"` ends here, we cannot continue, even if the only child path continues to `"flower"`, because `"flow"` physically cannot have a prefix longer than itself!).

**3. The Trace Execution:**
We maintain our `current_node`. We check `len(current_node.children)`. If it is `1`, we grab that single child character, append it to our result, move our pointer down, and repeat!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for trie_03: Longest Common Prefix.

Walk the trie from the root. While the current node has
exactly one child and is not a word end, descend.
"""


def solve(words, n):
    if n == 0:
        return ""
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    out = []
    cur = root
    while len(children[cur]) == 1 and not is_end[cur]:
        ch, nxt = next(iter(children[cur].items()))
        out.append(ch)
        cur = nxt
    return "".join(out)
```

</details>

## Walk-through

`strs = ["flower", "flow", "flight"]`.

**Building the Trie:**
Root -> `'f'` -> `'l'`.
From `'l'`, branches into:
- `'o'` -> `'w'` (word end) -> `'e'` -> `'r'` (word end).
- `'i'` -> `'g'` -> `'h'` -> `'t'` (word end).

**Tracing for LCP:**
1. Start at `root`.
   - `len(children)` is 1 (`'f'`).
   - Not a word end.
   - Append `'f'`. `lcp = ["f"]`.
   - Move to `'f'`.
2. At `'f'`:
   - `len(children)` is 1 (`'l'`).
   - Not a word end.
   - Append `'l'`. `lcp = ["f", "l"]`.
   - Move to `'l'`.
3. At `'l'`:
   - `len(children)` is 2 (`'o'` and `'i'`).
   - `len(curr.children) > 1` triggers `break`!
4. Return `"".join(["f", "l"])`.

Output: `"fl"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \times M)$ | $O(N \times M)$ |
| **Average** | $O(N \times M)$ | $O(N \times M)$ |
| **Worst** | $O(N \times M)$ | $O(N \times M)$ |

Let N be the number of strings and M be the maximum length of a string.
Inserting all strings into the Trie requires processing every character, taking exactly $O(N \times M)$ time.
Tracing the path down takes at most $O(M)$ time.
Total Time complexity is $O(N \times M)$.
Space complexity is $O(N \times M)$ because we physically construct a massive Trie in memory holding every single character in the array (unlike the horizontal scanning approach which takes $O(1)$ space).

## Variants & optimizations

- **Dynamic Updates:** This approach is fundamentally worse than Horizontal Scanning for static arrays. However, if the array is dynamic (strings are being added and removed continuously), Horizontal Scanning requires an $O(N \times M)$ rescan every time! A Trie handles insertions in $O(M)$ time and deletions in $O(M)$ time, and updating the LCP takes $O(M)$ time. It is exponentially faster for dynamic datasets!

## Real-world applications

- **Routing Tables:** IP packet routing in computer networks uses specialized Tries (Radix Trees / Patricia Tries) to find the longest matching IP prefix subnet dynamically as new routers connect and disconnect from the global grid.

## Related algorithms in cOde(n)

- **[string_11 - Longest Common Prefix](../strings/string_11_longest-common-substring.md)** — The $O(1)$ space algorithm that you should actually use in standard technical interviews.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
