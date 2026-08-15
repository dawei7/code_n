### 1. Description

You are given two string arrays `creators` and `ids`, and an integer array `views`, all of length `n`. The $$i^{\text{th}}$$ video on a platform was created by $\text{creators}[i]$, has an id of $\text{ids}[i]$, and has $\text{views}[i]$ views.

The **popularity** of a creator is the **sum** of the number of views on **all** of the creator's videos. Find the creator with the **highest** popularity and the id of their **most** viewed video.

- If multiple creators have the highest popularity, find all of them.

- If multiple videos have the highest view count for a creator, find the lexicographically **smallest** id.

Note: It is possible for different videos to have the same `id`, meaning that `id`s do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount.

Return* *a **2D array** of **strings** `answer` where $\text{answer}[i] = [\text{creators}_{i}, \text{id}_{i}]$ means that $\text{creators}_{i}$ has the **highest** popularity and $\text{id}_{i}$ is the **id** of their most **popular** video. The answer can be returned in any order.

### 2. Function Contract

**Inputs**

- `creators`: Input parameter (`List[str]`).
- `ids`: Input parameter (`List[str]`).
- `views`: Input parameter (`List[int]`).

**Return value**

- Returns `List[List[str]]`.

### 3. Examples

#### Example 1

- **Input:** creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]

- **Output:** [["alice","one"],["bob","two"]]

- **Explanation:** The popularity of alice is 5 + 5 = 10.

The popularity of bob is 10.

The popularity of chris is 4.

alice and bob are the most popular creators.

For bob, the video with the highest view count is "two".

For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than "three", it is included in the answer.

#### Example 2

- **Input:** creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]

- **Output:** [["alice","b"]]

- **Explanation:** The videos with id "b" and "c" have the highest view count.

Since "b" is lexicographically smaller than "c", it is included in the answer.

### 4. Constraints

- $n = \text{creators.length} = \text{ids.length} = \text{views.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{creators}[i].length, \text{ids}[i].length \le 5$

- $\text{creators}[i]$ and $\text{ids}[i]$ consist only of lowercase English letters.

- $0 \le \text{views}[i] \le 10^{5}$
