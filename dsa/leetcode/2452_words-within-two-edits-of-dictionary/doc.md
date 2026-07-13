# Words Within Two Edits of Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2452 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [words-within-two-edits-of-dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/words-within-two-edits-of-dictionary/).

### Goal
Given a list of query words and a dictionary of reference words, identify which query words can be transformed into at least one dictionary word by changing at most two characters. All words in both lists have the same length.

### Function Contract
**Inputs**

- `queries`: A list of strings representing the words to check.
- `dictionary`: A list of strings representing the reference vocabulary.

**Return value**

- A list of strings containing all words from `queries` that satisfy the "two-edit" condition.

### Examples
**Example 1**

- Input: `queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]`
- Output: `["word","note","wood"]`

**Example 2**

- Input: `queries = ["yes"], dictionary = ["not"]`
- Output: `[]`

**Example 3**

- Input: `queries = ["ac","ab"], dictionary = ["ac","ab"]`
- Output: `["ac","ab"]`

---

## Solution
### Approach
The problem is solved using a brute-force comparison approach. Since the constraints on word length and list sizes are relatively small (typically $N, M \le 100$ and length $L \le 100$), we can iterate through each query word and compare it against every dictionary word. For each pair, we count the number of differing characters. If the count is $\le 2$, the query word is valid.

### Complexity Analysis
- **Time Complexity**: $O(Q \cdot D \cdot L)$, where $Q$ is the number of queries, $D$ is the number of dictionary words, and $L$ is the length of the words.
- **Space Complexity**: $O(R \cdot L)$, where $R$ is the number of resulting words, to store the output list.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(queries: List[str], dictionary: List[str]) -> List[str]:
    """
    Determines which query words are within two edits of any word in the dictionary.
    """
    result = []

    for query in queries:
        is_valid = False
        for word in dictionary:
            # Count differences between query and dictionary word
            diff_count = 0
            for i in range(len(query)):
                if query[i] != word[i]:
                    diff_count += 1

                # Optimization: break early if edits exceed 2
                if diff_count > 2:
                    break

            if diff_count <= 2:
                is_valid = True
                break

        if is_valid:
            result.append(query)

    return result
```
</details>
