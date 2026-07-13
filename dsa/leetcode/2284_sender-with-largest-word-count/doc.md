# Sender With Largest Word Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2284 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sender-with-largest-word-count](https://leetcode.com/problems/sender-with-largest-word-count/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sender-with-largest-word-count/).

### Goal
Sum the number of words sent by each sender. Return the sender with the largest total, breaking ties by lexicographically larger name.

### Function Contract
**Inputs**

- `messages`: space-separated messages.
- `senders`: sender names at matching indices.

**Return value**

The winning sender's name.

### Examples
**Example 1**

- Input: `messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]`, `senders = ["Alice", "userTwo", "userThree", "Alice"]`
- Output: `"Alice"`

**Example 2**

- Input: `messages = ["How is leetcode for everyone", "Leetcode is useful for practice"]`, `senders = ["Bob", "Charlie"]`
- Output: `"Charlie"`

**Example 3**

- Input: `messages = ["one", "two three"]`, `senders = ["Zoe", "Amy"]`
- Output: `"Amy"`

---

## Solution
### Approach
Count words in each message and add them to a hash map keyed by sender. Select the pair with maximum `(word_count, sender_name)`, using ordinary lexicographic order for the second component.

### Complexity Analysis
- **Time Complexity**: `O(L)`, where `L` is the total message length
- **Space Complexity**: `O(s)`, where `s` is the number of senders

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
