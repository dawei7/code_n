# Cutting Pizza

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CUTPIZ |
| Difficulty Rating | 1446 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CUTPIZ](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CUTPIZ) |

---

## Problem Statement

Vasya has ordered a pizza delivery. The pizza can be considered a perfect circle. There were $n$ premade cuts in the pizza when it was delivered. Each cut is a straight segment connecting the center of the pizza with its boundary.

Let $O$ be the center of the pizza, $P_i$ be the endpoint of the $i$-th cut lying on the boundary, and $R$ be the point of the boundary straight to the right of $O$. Then the counterclockwise-measured angle $\angle ROP_i$ is equal to $a_i$ degrees, where $a_i$ is an integer between $0$ and $359$. Note that angles between $0$ and $180$ angles correspond to $P_i$ in the top half of the pizza, while angles between $180$ and $360$ angles correspond to the bottom half.

Vasya may cut his pizza a few more times, and the new cuts still have to be straight segments starting at the center. He wants to make the pizza separated into several equal slices, with each slice being a circular sector with no cuts inside of it. How many new cuts Vasya will have to make?

### Input:

The first line of input contains $T$ , i.e number of test cases per file.

The first line of each test case contains a single integer $n-$  the numbers of premade cuts ($2 \leq n \leq 360$).

The second lines contains $n$ integers $a_1, \ldots, a_n-$ angles of the cuts $1, \ldots, n$ respectively ($0 \leq a_1 < \ldots, a_{n - 1} < 360$).

### Output:
Print a single integer$-$ the smallest number of additional cuts Vasya has to make so that the pizza is divided into several equal slices.

### Constraints
- $1  \leq T  \leq 36$
- $2 \leq n \leq 360$
- $0 \leq a_1 < \ldots, a_{n - 1} < 360$

---

## Examples

**Example 1**

**Input**

```text
3
4 
0 90 180 270
2
90 210
2
0 1
```

**Output**

```text
0
1
358
```

**Explanation**

In the first sample the pizza is already cut into four equal slices.

In the second sample the pizza will be cut into three equal slices after making one extra cut at $330$ degrees.

In the third sample Vasya will have to cut his pizza into $360$ pieces of $1$ degree angle each.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
0 90 180 270
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
90 210
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2
0 1
```

**Output for this case**

```text
358
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Cutting Pizza Practice Problem in 1400 to 1600 difficulty problems](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CUTPIZ)

### [](#problem-statement-1)Problem Statement:

In this problem, Vasya wants to divide his pizza, which already has some premade cuts at specific angles, into **equal slices**. The task is to determine how many additional cuts he needs to make to achieve this.

Each test case consists of:

- The number of premade cuts `n`.

- A list of `n` angles representing the positions of these cuts, measured counterclockwise from a fixed reference point (`0` degrees).

We are tasked with finding out how many **additional cuts** (if any) are required to divide the pizza into slices of equal angular sizes.

### [](#approach-2)Approach:

- The pizza is a circle with a total angle of `360` degrees. If the pizza is divided into `k` equal slices, then the angle between each adjacent cut should be `360/k` degrees.

- If the existing cuts divide the pizza into a set of angles, we can check if it’s possible to partition these angles into equal slices.

- The number of equal slices will be determined by the greatest common divisor (GCD) of the angular gaps between consecutive cuts.

- We compute the differences between consecutive angles (considering the circular nature of the pizza), and the GCD of these differences tells us the smallest slice size.

- If the GCD of the gaps between existing cuts is `g`, the pizza can be divided into `360 / g` slices.

- If `360 / g` is greater than `n`, we need to add `360 / g - n` cuts to make the number of slices equal.

**Steps:**

- **Calculate Gaps**: Calculate the angular gaps between consecutive cuts. Don’t forget that the last cut wraps around back to the first cut.

- **Compute GCD**: Compute the GCD of all the angular gaps.

- **Determine Needed Cuts**: The number of slices the pizza will be divided into is `360 / GCD(gaps)`. If this number of slices is more than the number of premade cuts, we need to add cuts to make the slices equal.

- **Output the Number of Additional Cuts**: The result is the difference between the desired number of slices and the number of premade cuts.

### [](#complexity-3)Complexity:

- **Time Complexity:** For each test case, computing the gaps and the GCD of the gaps takes `O(n)` time, where `n` is the number of cuts.

- **Space Complexity:** We use an additional array to store the gaps between cuts, which requires `O(n)` space per test case.

</details>
