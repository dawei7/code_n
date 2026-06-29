# Squirrel and chestnut

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SQUIRREL |
| Difficulty Rating | 1611 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [SQUIRREL](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/SQUIRREL) |

---

## Problem Statement

There are n squirrel(s) waiting below the feet of m chestnut tree(s). The first chestnut of the i-th tree will fall right after Ti second(s), and one more every Pi second(s) after that. The “big mama” of squirrels wants them to bring their nest no less than k chestnuts to avoid the big storm coming, as fast as possible! So they are discussing to wait below which trees to take enough chestnuts in the shortest time. Time to move to the positions is zero, and the squirrels move nowhere after that.

### Request
Calculate the shortest time (how many seconds more) the squirrels can take enough chestnuts.

### Input

- The first line contains an integer t, the number of test cases, for each:

- The first line contains the integers m,n,k, respectively.

- The second line contains the integers Ti  (i=1..m), respectively.

- The third line contains the integers Pi  (i=1..m), respectively.

***(Each integer on a same line is separated by at least one space character, there is no added line between test cases)***

### Output

For each test cases, output in a single line an integer which is the shortest time calculated.

---

## Constraints

- $0 \lt t \leq 20$
- $0 \lt m, n \leq 10,000$
- $0 \lt k \leq 10^7$
- $0 < T_i, P_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2
3 2 5
5 1 2
1 2 1
3 2 5
5 1 2
1 1 1
```

**Output**

```text
4
3
```

**Explanation**

**Test case $1$:** Two squirrels wait below trees $2$ and $3$.
- After $1$ second, a chestnut from tree $2$ falls. Total chestnuts the squirrels have is $1$.
- After $2$ seconds, a chestnut from tree $3$ falls. Total chestnuts the squirrels have is $2$.
- After $3$ seconds, two chestnuts fall from trees $2$ and $3$. Total chestnuts the squirrels have is $4$.
- After $4$ seconds, a chestnut from tree $3$ falls. Total chestnuts the squirrels have is $5$.

Total time to gather $5$ chestnuts is $4$ seconds.

**Test case $2$:** Two squirrels wait below trees $2$ and $3$.
- After $1$ second, a chestnut from tree $2$ falls. Total chestnuts the squirrels have is $1$.
- After $2$ seconds, two chestnuts fall from trees $2$ and $3$. Total chestnuts the squirrels have is $3$.
- After $3$ seconds, two chestnuts fall from trees $2$ and $3$. Total chestnuts the squirrels have is $5$.

Total time to gather $5$ chestnuts is $3$ seconds.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 5
5 1 2
1 2 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3 2 5
5 1 2
1 1 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

###
[](#problem-links-1)PROBLEM LINKS

[Practice](http://www.codechef.com/problems/SQUIRREL/)

[Contest](http://www.codechef.com/JUNE10/problems/SQUIRREL/)

###
[](#difficulty-2)DIFFICULTY

MEDIUM

###
[](#explanation-3)EXPLANATION

View solution [here](http://www.flickr.com/photos/directi/4690716421/) first.

But for a given t, we don’t really need O(m * n) dp to calculate maximum nuts the squirrels can get. For each tree, we simply calculate the number of nuts that will drop in time t. After that, we sort those numbers, and pick the first n highest numbers. So complexity becomes O( m + m*log(m) + n ).

</details>
