# Matchsticks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MSTICK |
| Difficulty Rating | 1714 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MSTICK](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MSTICK) |

---

## Problem Statement

Chef Ceil has some matchsticks in his kitchen.

**Detail of matchsticks:**

There are $N$ matchsticks in total. They are numbered from to $0$ to $N-1$ inclusive. The $i^{th}$ matchstick takes $b_{i}$ time to burn when lighted at one end, and it burns at a uniform rate.

If lighted at both ends simultaneously, the matchstick will take only half of the original time to burn down.

**Arrangement:**

He ties rear end of the all the matchsticks together at one point and the front end is kept free. The matchstick numbered $i$ is adjacent to matchstick numbered $i+1$ for all $0 \leq i \leq N-2$.

*Bodies of matchsticks do not touch each other, except at the rear end.*

**Task:**

There are $Q$ queries, in each query we ask:
If he lights the free end of all matchsticks numbered between $L$ and $R$ inclusive, what will be the time needed for all matchsticks to get completely burnt?

### Input
- First line of input contains a single integer $N$.
- The next line contains $N$ space separated integers, the $i^{th}$ of which is $b_i$
- The next line contains a single integer $Q$
- The next $Q$ lines each contain two space separated integers - $L$ and $R$. The $i^{th}$ line represents the $i^{th}$ query.

### Output
For each query, print the answer on a new line.

### Constraints:
- $1 \leq N \leq 10^{5}$
- $1 \leq b_{i} \leq 10^{8}$
- $1 \leq Q \leq 10^{5}$
- $0 \leq L \leq R \leq N-1$

---

## Examples

**Example 1**

**Input**

```text
1
5
1
0 0
```

**Output**

```text
5.0
```

**Example 2**

**Input**

```text
2
3 5
1
0 1
```

**Output**

```text
4.0
```

**Example 3**

**Input**

```text
18
3 4 2 1 5 7 9 7 10 5 12 3 1 1 2 1 3 2
1
4 10
```

**Output**

```text
9.0
```

**Explanation**

**Test Case 3:** , in the figure above, yellow colored matches are lighted by a lighter simultaneously.

The numbers indicate the time required to burn that matchstick (if lighted at one end).

Now the first lighted matchstick will completely burn in $5$ seconds. Then it will light up all the rest matches from the rear end.

Some matches will have fire at both ends and thus after $5$ seconds, they will start burning with twice the original rate.

Thus time taken for matches to burn completely will be :
(from left to right):  $8.0$, $9.0$, $7.0$, $6.0$, $5.0$, $6.0$, $7.0$, $6.0$, $7.5$, $5.0$, $8.5$, $8.0$, $6.0$, $6.0$, $7.0$, $6.0$, $8.0$, $7.0$.
So, the answer will be $9.0$ (the maximum among these).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/MSTICK)

[Contest](http://www.codechef.com/MAY13/problems/MSTICK)

### DIFFICULTY

SIMPLE

### PREREQUISITES

[Range Minimum Query](http://en.wikipedia.org/wiki/Range_Minimum_Query), Simple Math

### PROBLEM

You are given **N** matchsticks arranged in a straight line, with their **rear** **ends** touching each other. You are also given the rate of burn for every matchstick (possibly same) in number of seconds it takes to burn it out. If a matchstick is lit from both ends, it burns out **twice** as fast - taking **half** as much time.

Answer several queries of the following type efficiently

All the matchsticks in the range **L** to **R**, inclusive are lit from their front ends simultaneously. Find how much time it takes for **all** the matchsticks to burn out.

### QUICK EXPLANATION

For each query, the operation performed plays out in the following way

- All the matchsticks in the range **L** to **R** are lit from their front ends.

- The matchstick that burns **quickest** in the range **L** to **R** burns out and **ignites** all the other matchsticks on their **rear** ends.

- The matchticks in the range **L** to **R** now burn out **twice** as fast.

-
**All** the other matchsticks burn out at their **original** rate.

We can find the time taken in all the steps above using only the following pieces of information for the segment **L** to **R**

- Quickest rate of burning for a match in the range **L** to **R**.

- Slowest rate of burning for all matches in the range **L** to **R**.

- Slowest rate of burning for all matches outside the range **L** to **R**.

### EXPLANATION

For a given range **L** to **R**

- Let **m** denote the minimum time taken by some matchstick in the range **L** to **R** to burn out

- Let **M** denote the largest time taken by some matchstick in the range **L** to **R** to burn out

- Let **M**’ denote the largest time taken by some matchstick outside the range **L** to **R** to burn out

The time taken by each of the steps in the scenario described above is as follows

- The matchstick that burns quickest, burns out

- Takes time **m**

- The following things happen in parallel

- The matchsticks in the range **L** to **R** now burn out twice as fast

- Takes time **(M - m) / 2**

- The matchsticks outside the range

- Takes time **M’**

Thus, the time taken for all the matches to burn out completely is

`
m + max( (M-m)/2 , M' )
`

It remains to find efficiently the **minimum** time some matchstick will take in a range, and the **maximum** time some matchstick will take in a **range**.

Such queries can be answered in **O(N log N)** time by using [segment trees](http://en.wikipedia.org/wiki/Segment_tree). Refer to [this](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=lowestCommonAncestor) topcoder tutorial for a wonderful writeup with code samples on how to get about writing a segment tree. The topcoder tutorial also describes a **O(N sqrt(N))** approach as well which will also work within the time limits for this problem.

**Two segment trees must be constructed**. One to answer queries of the type “**minimum in a range**”, that returns the time it takes for the fastest burning matchstick to burn out. Another to answer queries of the type “**maximum in a range**” to find **M** and **M**’ as defined above. Note that **M**’ will itself be the maxmimum of two ranges, **1 to L-1** and **R+1 to N** respectively.

A lot of solutions were stuck in the caveat that it is required to **always** print the answer in a **single** decimal place. Note how the answer will either be **integer**, or contain a single decimal digit (**5**). In case the answer is **integer**, it is required to print a trailing decimal followed by **0**.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/May/Setter/MSTICK.cpp).

### TESTER’S SOLUTION

Approach - finds range min query in time O(rootN) - [solution](http://www.codechef.com/download/Solutions/2013/May/Tester/MSTICK-rootN.cpp).

Approach - finds range min query using segment trees in O(logN) - [solution](http://www.codechef.com/download/Solutions/2013/May/Tester/MSTICK-logN.cpp).

</details>
