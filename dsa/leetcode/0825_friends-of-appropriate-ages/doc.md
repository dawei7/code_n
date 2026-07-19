# Friends Of Appropriate Ages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 825 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/friends-of-appropriate-ages/) |

## Problem Description

### Goal

There are $n$ people on a social-media website, and `ages[i]` is the age of person $i$. For two different people $x$ and $y$, person $x$ will not send a friend request to person $y$ when any one of these conditions holds:

- $\operatorname{age}(y) \le \frac{1}{2}\operatorname{age}(x) + 7$;
- $\operatorname{age}(y) > \operatorname{age}(x)$; or
- $\operatorname{age}(y) > 100$ while $\operatorname{age}(x) < 100$.

If none of the conditions holds, $x$ sends a friend request to $y$. Requests are directed: a request from $x$ to $y$ does not imply one from $y$ to $x$. Nobody sends a request to themself, even when several people have the same age. Return the total number of friend requests made among all ordered pairs of people.

### Function Contract

**Inputs**

- `ages`: an array of $n$ integers, where $1 \le n \le 2 \cdot 10^4$ and $1 \le \texttt{ages}[i] \le 120$
- Let $A=120$ be the largest possible age.

**Return value**

- The total number of directed friend requests permitted by the three age conditions, excluding self-requests

### Examples

**Example 1**

- Input: `ages = [16, 16]`
- Output: `2`
- Explanation: Each person may send one request to the other person of age `16`.

**Example 2**

- Input: `ages = [16, 17, 18]`
- Output: `2`
- Explanation: The permitted requests are from age `17` to age `16` and from age `18` to age `17`.

**Example 3**

- Input: `ages = [20, 30, 100, 110, 120]`
- Output: `3`
- Explanation: The permitted requests are `110 -> 100`, `120 -> 110`, and `120 -> 100`.
