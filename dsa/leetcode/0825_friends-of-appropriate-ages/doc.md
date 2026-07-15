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

### Required Complexity

- **Time:** $O(n + A)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Collapse people into age frequencies**

Only the sender's and recipient's ages affect a request, and every age lies between `1` and `120`. Count how many people have each age. Then build a prefix array $P(t)$ equal to the number of people whose age is at most $t$. This replaces work over individual recipient pairs with constant-time counts of whole age intervals.

**Translate the rejection rules into one eligible interval**

For a sender of integer age $x$, a recipient must satisfy

$$
\left\lfloor \frac{x}{2} + 7 \right\rfloor < y \le x.
$$

The number of people in that interval is `P[x] - P[x // 2 + 7]`. The upper bound $y \le x$ also makes the third rejection condition automatic: it is impossible to have $y>100$ and $x<100$ after enforcing $y \le x$. When $x \le 14$, the lower cutoff reaches or exceeds $x$, so no recipient age is valid.

**Exclude self-requests while retaining equal-age requests**

For each sender age $x>14$ with frequency $c_x$, the prefix difference counts all eligible people, including the sender themself. Subtract one eligible person per sender and add

$$
c_x\left(P(x)-P\!\left(\left\lfloor x/2+7 \right\rfloor\right)-1\right)
$$

to the answer. This multiplication counts each directed pair separately. Every accepted pair lies in exactly its sender-age group and satisfies the derived interval, while every pair counted by that interval violates none of the rejection rules; removing one per sender excludes precisely the forbidden self-pairs.

#### Complexity detail

Let $n$ be the number of people and $A=120$ the age-domain size. Counting the input takes $O(n)$ time. Building the prefix counts and evaluating each possible sender age takes $O(A)$ time, for $O(n+A)$ total. The frequency and prefix arrays each contain $A+1$ entries, so the auxiliary space is $O(A)$.

#### Alternatives and edge cases

- **Sort plus a sliding window:** Sorting the ages and maintaining the valid recipient range takes $O(n \log n)$ time and $O(n)$ space in Python, but it works even when the age domain is not small.
- **Binary search per sender:** After sorting, two boundary searches can count eligible recipients for every person in $O(n \log n)$ time; duplicate and self-request adjustments require care.
- **Enumerate every ordered pair:** Directly applying all three rules is simple and correct but takes $O(n^2)$ time at the maximum population.
- **Ages at most `14`:** No request is possible because the strict lower threshold is not below the sender's age.
- **Duplicate ages:** Distinct people of the same eligible age may request one another; subtract only each sender's own occurrence.
- **Directed counting:** A valid request in one direction does not automatically contribute the reverse request.
- **The `100` boundary:** The explicit cross-100 rule is preserved by the contract, although $y \le x$ already rejects every case with $y>100$ and $x<100$.

</details>
