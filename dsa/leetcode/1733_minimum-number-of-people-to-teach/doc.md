# Minimum Number of People to Teach

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1733 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-people-to-teach/) |

## Problem Description

### Goal

A social network has $m$ users and $n$ possible languages, numbered from $1$ through $n$. `languages[i]` lists the distinct languages known by user $i + 1$. Two friends can communicate when their language sets have at least one value in common.

Each pair in `friendships` identifies two users who are directly friends; friendship is not transitive. Choose exactly one language and teach that language to any selected users so that every listed friendship can communicate. Return the minimum number of users who need to be taught. Users who already know the chosen language do not need another lesson.

### Function Contract

**Inputs**

- `n`: the number of available languages, with $2 \le n \le 500$.
- `languages`: a length-$m$ list in which `languages[i]` contains the distinct language identifiers known by user $i + 1$, with $1 \le m \le 500$.
- `friendships`: between $1$ and $500$ unique pairs `[u,v]`, where $1 \le u < v \le m$.

Let

$$
S = \sum_{i=1}^{m} \lvert L_i \rvert
$$

be the total number of known-language entries, and let

$$
C = \sum_{(u,v) \in \texttt{friendships}} \min(\lvert L_u \rvert,\lvert L_v \rvert)
$$

bound the work needed to test the friendship pairs.

**Return value**

- Return the fewest distinct users that must learn one common chosen language so every listed friendship can communicate.

### Examples

**Example 1**

- Input: `n = 2`, `languages = [[1],[2],[1,2]]`, `friendships = [[1,2],[1,3],[2,3]]`
- Output: `1`
- Explanation: Teach language `2` to user `1`, or language `1` to user `2`.

**Example 2**

- Input: `n = 3`, `languages = [[2],[1,3],[1,2],[3]]`, `friendships = [[1,4],[1,2],[3,4],[2,3]]`
- Output: `2`
- Explanation: Teaching language `3` to users `1` and `3` makes every pair communicable.

**Example 3**

- Input: `n = 3`, `languages = [[1,2],[2,3],[1,3]]`, `friendships = [[1,2],[2,3]]`
- Output: `0`
- Explanation: Both listed friendship pairs already share a language.
