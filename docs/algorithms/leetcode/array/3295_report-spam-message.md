# Report Spam Message

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3295 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [report-spam-message](https://leetcode.com/problems/report-spam-message/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem utilizes a **Hash Set** for efficient membership testing. By converting the `bannedWords` list into a set, we reduce the lookup time for each word in the message from $O(M)$ to $O(1)$ on average. We then iterate through the message, counting how many words exist in the set, and terminate early once the count reaches two.

---

## Complexity Analysis
- **Time Complexity**: $O(N + M)$, where $N$ is the number of words in the message and $M$ is the number of words in the banned list. We iterate through the banned list once to build the set and through the message once to check for matches.
- **Space Complexity**: $O(M)$, required to store the unique banned words in a hash set.
