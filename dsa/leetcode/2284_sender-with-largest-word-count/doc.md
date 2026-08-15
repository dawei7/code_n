# Sender With Largest Word Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2284 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/sender-with-largest-word-count/) |

## Problem Description

### Goal

A chat log contains $n$ messages. `messages[i]` was written by `senders[i]`,
and the same sender may appear at several indices. Each message contains one or
more words separated by single spaces, without leading or trailing spaces. A
sender's word count is the total number of words across all of that sender's
messages.

Return the sender with the greatest total word count. If several senders share
that maximum, choose the lexicographically largest name. Comparison is
case-sensitive: uppercase letters precede lowercase letters, and names such as
`"Alice"` and `"alice"` identify different senders.

### Function Contract

**Inputs**

- `messages`: An array of $n$ valid space-separated messages.
- `senders`: An array of $n$ sender names aligned with `messages`.

Here, $1 \le n \le 10^4$, each message has length at most 100, and each sender
name has length at most 10. Let $L$ be the total number of characters across
all messages.

**Return value**

The name with the largest accumulated word count, resolving a tie in favor of
the lexicographically largest sender.

### Examples

#### Example 1

- **Input:** `messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]`, `senders = ["Alice", "userTwo", "userThree", "Alice"]`
- **Output:** `"Alice"`

#### Example 2

- **Input:** `messages = ["How is leetcode for everyone", "Leetcode is useful for practice"]`, `senders = ["Bob", "Charlie"]`
- **Output:** `"Charlie"`

#### Example 3

- **Input:** `messages = ["a", "b"]`, `senders = ["Alice", "alice"]`
- **Output:** `"alice"`
