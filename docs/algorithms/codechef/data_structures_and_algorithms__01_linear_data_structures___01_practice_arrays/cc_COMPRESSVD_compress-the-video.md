# Compress the Video

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COMPRESSVD |
| Difficulty Rating | 940 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [COMPRESSVD](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/COMPRESSVD) |

---

## Problem Statement

Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.

Chef's video has $N$ frames initially. The value of the $i^{th}$ frame is $A_i$. Chef can do the following type of operation **any** number of times:
- Choose an index $i$ $(1\le i \le N)$ such that the value of the $i^{th}$ frame is **equal** to the value of **either** of its neighbors and **remove** the $i^{th}$ frame.

Find the **minimum** number of frames Chef can achieve.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the number of frames initially.
- The second line contains $N$ space-separated integers, $A_1, A_2, \ldots, A_N$ - the values of the frames.

---

## Output Format

For each test case, output in a single line the **minimum** number of frames Chef can achieve.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^6$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
1
5
2
1 1
3
1 2 3
4
2 1 2 2
```

**Output**

```text
1
1
3
3
```

**Explanation**

**Test case $1$:** There is only one frame with value $5$. Since there are no neighbors, Chef won't remove any frame and the minimum number of frames Chef can achieve is $1$.

**Test case $2$:** There are two frames where both frames have value $1$. Chef can remove the first frame as the value of the first frame is equal to that of the second frame. The remaining frames have values $[1]$. The minimum number of frames Chef can achieve is $1$.

**Test case $3$:** There are $3$ frames. All frames have distinct values. Thus, the minimum number of frames Chef can achieve is $3$.

**Test case $4$:** Chef can remove the fourth frame as the value of the fourth frame is equal to that of the third frame. The remaining frames have values $[2, 1, 2]$. Thus, the minimum number of frames Chef can achieve is $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
5
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
4
2 1 2 2
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START39A/problems/COMPRESSVD)

[Contest Division 2](https://www.codechef.com/START39B/problems/COMPRESSVD)

[Contest Division 3](https://www.codechef.com/START39C/problems/COMPRESSVD)

[Contest Division 4](https://www.codechef.com/START39D/problems/COMPRESSVD)

Setter: [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

940

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.

Chef’s video has N frames initially. The value of the i^{th} frame is A_i. Chef decides to remove a frame only if its value is **equal** to the value of **either** of its neighbors.

Find the **minimum** number of frames Chef can achieve.

#
[](#explanation-5)EXPLANATION:

Basically in this problem we need to calculate the total number of substrings having same characters. Here the video is considered as a string with each frame as individual character.

Initially we start with n frames. On traversing the string whenever we find two adjacent frames as equal, we can decrement our frames by 1, since those two frames would belong to the same substring.

After traversing we would get the final answer as frames.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/nBUD)

[Setter’s Solution](http://p.ip.fi/hHKq)

[Tester1’s Solution](http://p.ip.fi/L4fY)

[Tester2’s Solution](http://p.ip.fi/bcjp)

</details>
