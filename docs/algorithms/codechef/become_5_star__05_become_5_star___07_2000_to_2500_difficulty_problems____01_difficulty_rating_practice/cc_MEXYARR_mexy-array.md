# Mexy Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEXYARR |
| Difficulty Rating | 2190 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MEXYARR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MEXYARR) |

---

## Problem Statement

You are given an array $B$ containing $N$ integers, each of which is either $-1$ or a non-negative integer. Construct **any** integer array $A$ of length $N$ such that:
- $0 \leq A_i \leq 10^9$ for every $1 \leq i \leq N$
- If $B_i \geq 0$, $A$ must satisfy $mex(A_1, A_2, \ldots, A_i) = B_i$
- Otherwise, $B_i = -1$, which means there is no constraint on $mex(A_1, A_2, \ldots, A_i)$

If there does not exist any array satisfying the constraints, print $-1$ instead.

**Note:** The mex of a set of non-negative integers is the smallest non-negative integer that does not belong to it. For example, $mex(1, 2, 3) = 0, mex(0, 2, 4, 1) = 3,$ and $mex(0, 0, 0) = 1$.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- The first line of each testcase contains a single integer $N$.
- The second line of each testcase contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

---

## Output Format

For each testcase, output the required answer on a new line: $-1$ if no valid array exists, or $N$ space-separated integers denoting the elements of **any** valid array $A$. The elements of $A$ must satisfy $0 \leq A_i \leq 10^9$.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $-1 \leq B_i \leq 10^5$
- The sum of $N$ across all testcases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
7
0 -1 2 -1 5 -1 -1
3
2 -1 -1
```

**Output**

```text
1 3 0 4 2 6 5
-1
```

**Explanation**

**Test case $1$:** We have $A = [1, 3, 0, 4, 2, 6, 5]$. Let $C_i = mex(A_1, A_2, \ldots, A_i)$. Then, it can be seen that $C = [0, 0, 2, 2, 5, 5, 7]$, which matches $B$ at all positions where $B_i \geq 0$.

**Test case $2$:** It can be shown that no array $A$ exists that satisfies the given constraints.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
0 -1 2 -1 5 -1 -1
```

**Output for this case**

```text
1 3 0 4 2 6 5
```



#### Test case 2

**Input for this case**

```text
3
2 -1 -1
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START31A/problems/MEXYARR)

[Contest Division 2](https://www.codechef.com/START31B/problems/MEXYARR)

[Contest Division 3](https://www.codechef.com/START31C/problems/MEXYARR)

[Contest Division 4](https://www.codechef.com/START31D/problems/MEXYARR)

Setter: [ Manuj Nanthan](https://www.codechef.com/users/munch_01)

Tester: [ Aryan](https://www.codechef.com/users/aryanc403), [ Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array B containing N integers, each of which is either ?1 or a non-negative integer. Construct **any** integer array A of length N such that:

-
0?A_i?10^9 for every 1?i?N

- If B_i?0, A must satisfy mex(A_1,A_2,…,A_i)=B_i

- Otherwise, B_i=?1 , which means there is no constraint on  mex(A_1,A_2,…,A_i)

If there does not exist any array satisfying the constraints, print ?1 instead.

**Note:** The mex of a set of non-negative integers is the smallest non-negative integer that does not belong to it. For example,

mex(1,2,3)=0 , mex(0,2,4)=3  , mex(0,0,0)=1

#
[](#quick-explanation-5)Quick Explanation

Take two sets x and y. x contains integers coming in B_i as positive integers and y contains the remaining integers from 0 to N-1.

Construct greedily from B_1 to B_n.

If B_i is -1 , print the elements from y set. else If B_i is positive , print the previous element of set x.

In this way we can construct valid array.

Note that it won’t be possible to create array A if for any i we have B_i \geq (i+1) or for any i, there is a B_j such that 0 \leq j < i and B_j > B_i

#
[](#explanation-6)Explanation

There can be multiple ways to go about its implementation, one of which is discussed here.

First we check if for any i, if there exists any B_j such that 0 \leq j < i and B_j >B_i. If such B_j  exists then it won’t be possible to create array and we would return -1.

Now we would create two separate sets slots and elements where slots  represents the available slots of A that needs to be filled, while elements  represents the available elements that can be used to fill the slots.

Let’s talk about the way we will go about filling. We will first remove duplicates from array B, i.e say array B = \{-1,1,1,1,2\}, then we would change duplicates to -1, so B would become \{-1,1,-1,-1,2\}. This way we would have increasing order of positive numbers and -1s. Now we will loop through array and upon reaching a positive value, we would loop through all available slots in A in increasing order and fill elements from set elements till Mex(A_1,A_2.....A_i) becomes B_i. If for any case we do not have slots available to fill then also it won’t be possible to create array A and we would return -1.

#
[](#time-complexity-7)TIME COMPLEXITY:

In this algorithm, we iterate through the array and when we find any positive B_i, we loop through all the available slots available and remove them from set after filling it. Thus we are basically iterating the array twice and in second iteration of going through availble slots, we are accessing from a set that takes O(logN) time, thus total time complexity would be O(NlogN).

#
[](#solution-8)SOLUTION:

[Editorialist’s Solution](https://pastebin.com/qr9ZLxVt)

[Setter’s Solution](https://pastebin.com/u96px510)

[Tester-1’s Solution](https://pastebin.com/nge29wY8)

[Tester-2’s Solution](http://p.ip.fi/8XQL)

</details>
