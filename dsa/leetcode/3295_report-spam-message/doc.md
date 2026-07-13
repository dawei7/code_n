# Report Spam Message

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3295 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [report-spam-message](https://leetcode.com/problems/report-spam-message/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/report-spam-message/).

### Goal
Determine if a given message should be classified as spam based on a provided list of banned words. A message is considered spam if it contains at least two distinct words that appear in the banned list.

### Function Contract
**Inputs**

- `message`: A list of strings representing the words in the message.
- `bannedWords`: A list of strings representing the vocabulary of forbidden words.

**Return value**

- `bool`: Returns `True` if the message contains at least two occurrences of words found in `bannedWords` (counting distinct occurrences), otherwise `False`.

### Examples
**Example 1**

- Input: `message = ["hello","world","leetcode"], bannedWords = ["world","hello"]`
- Output: `True`

**Example 2**

- Input: `message = ["hello","programming","fun"], bannedWords = ["world","leetcode"]`
- Output: `False`

**Example 3**

- Input: `message = ["a","b","c"], bannedWords = ["a","b"]`
- Output: `True`

---

## Solution
### Approach
The problem utilizes a **Hash Set** for efficient membership testing. By converting the `bannedWords` list into a set, we reduce the lookup time for each word in the message from $O(M)$ to $O(1)$ on average. We then iterate through the message, counting how many words exist in the set, and terminate early once the count reaches two.

### Complexity Analysis
- **Time Complexity**: $O(N + M)$, where $N$ is the number of words in the message and $M$ is the number of words in the banned list. We iterate through the banned list once to build the set and through the message once to check for matches.
- **Space Complexity**: $O(M)$, required to store the unique banned words in a hash set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(message: List[str], bannedWords: List[str]) -> bool:
    """
    Determines if a message is spam by checking if at least two words
    from the message exist in the bannedWords set.
    """
    banned_set = set(bannedWords)
    spam_count = 0

    for word in message:
        if word in banned_set:
            spam_count += 1
            # If we find at least two banned words, it's spam.
            if spam_count >= 2:
                return True

    return False
```
</details>
