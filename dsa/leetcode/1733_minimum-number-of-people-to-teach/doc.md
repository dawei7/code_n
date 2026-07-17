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

### Required Complexity

- **Time:** $O(S + C)$
- **Space:** $O(S + m)$

<details>
<summary>Approach</summary>

#### General

**Discard friendships that already communicate**

Convert each user's languages to a set. For every friendship, test whether the two sets intersect. If they do, that pair needs no teaching regardless of which language is eventually selected. If they do not, add both endpoints to one set of affected users. Friendship is not transitive, so each listed pair is tested directly rather than through graph connectivity.

**Only affected users can require teaching**

Every broken friendship has both endpoints in the affected set. Teaching the chosen language to each affected user who does not already know it is sufficient: afterward every broken pair shares that language, while previously working pairs remain able to communicate. A user outside this set belongs to no broken friendship and never needs to be taught.

**Keep the most common existing language**

Suppose there are $P$ affected users. If the chosen language is already known by $q$ of them, exactly $P-q$ users need lessons. Count all language occurrences among affected users and retain the largest count. Choosing that most common language minimizes $P-q`; if the affected set is empty, the answer is zero.

#### Complexity detail

Building all language sets costs $O(S)$ time and space. Testing a friendship can iterate through the smaller endpoint set, so all communication checks cost $O(C)$ time. Counting languages among affected users visits no more than the $S$ stored entries. The affected-user set needs $O(m)$ space, giving $O(S+C)$ time and $O(S+m)$ auxiliary space.

#### Alternatives and edge cases

- **Try every language against every affected user:** This is correct but can take $O(nm)$ membership checks even when most available languages never occur among affected users.
- **Teach per broken friendship:** Choosing lessons independently can teach the same user repeatedly or choose incompatible languages; the contract requires one global language.
- **Graph connected components:** Friendship is explicitly non-transitive, so connectivity does not determine whether a listed pair shares a language.
- **No broken friendships:** Return zero without choosing or teaching a language.
- **User in several broken pairs:** Add that user once and count one possible lesson.
- **Unaffected language expert:** A language known only by users outside broken pairs cannot reduce the lesson count.
- **Tied frequencies:** Any tied most-common language gives the same minimum.

</details>
