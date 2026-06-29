# IPC Trainers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IPCTRAIN |
| Difficulty Rating | 1500 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [IPCTRAIN](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/IPCTRAIN) |

---

## Problem Statement

During the Indian Programming Camp (IPC), there are **N** trainers. The camp runs for **D** days. Each day, there can be at most one lecture. The i-th trainer arrives on day **D**i and then stays till the end of the camp. He also wants to teach exactly **T**i lectures. For each lecture that a trainer was not able to teach, he will feel sad and his sadness level will be increased by **Si**.

You are the main organizer of the contest. You want to find minimum total sadness of the trainers.

### Input

The first line of the input contains an integer **T**, denoting the number of testcases.

For each test case, the first line contains two space separated integers, **N, D**.

The i-th of the next **N** lines will contain three space separated integers: **D**i**, **T**i**, **S**i** respectively.

### Output

For each test case, output a single integer corresponding to the minimum total sadness of the trainers achievable.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N, D** ≤ 105

- 1 ≤  **D**i**,  **T**i** ≤ D

- 1 ≤  **S**i** ≤ 105

### Subtasks

**Subtask #1 (40 points)**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N, D** ≤ 103

- 1 ≤  **D**i**,  **T**i** ≤ D

- 1 ≤  **S**i** ≤ 103

**Subtask #2 (60 points)**

- Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2 3
1 2 300
2 2 100
2 3
1 1 100
2 2 300
2 3
3 2 150
1 1 200
```

**Output**

```text
100
0
150
```

**Explanation**

**Example case 1**. Both the first and second trainer want to take exactly two lectures. The first trainer arrives on the 1st day and the second trainer arrives on the 2nd day. Consider a schedule where the first trainer takes the first two lectures, and the second trainer takes the last lecture on the day 3. This way the second trainer will take only one lecture but wanted to take two. Thus, his sadness will be 100. The first trainer took all the lectures that he wanted to take (ie. two lectures). Thus the total sadness is 100 + 0 = 100. You can check that no other way of assigning trainers to the days will give a better answer than this.

**Example case 2**. In this case, the trainers can all take all their ideal number of lectures.

**Example case 3**. In this case, the first trainer arrives on day 3 and wants to take two lectures. This is not possible as he can take at most one lecture on day 3 and the camp ends on day 3. The second trainer wants to take only one lecture which he can take on any one of the 1st or 2nd days. You can see that in one of the first or second days, no lecture will be held.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
1 2 300
2 2 100
```

**Output for this case**

```text
100
```



#### Test case 2

**Input for this case**

```text
2 3
1 1 100
2 2 300
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 3
3 2 150
1 1 200
```

**Output for this case**

```text
150
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/JULY17/problems/IPCTRAIN)

[Contest](https://www.codechef.com/problems/IPCTRAIN)

**Author:** [Admin2](https://www.codechef.com/users/admin2)

**Primary Tester:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### DIFFICULTY:

Easy

### PREREQUISITES:

Greedy,Heap

### PROBLEM:

You have an upcoming camp. There are N trainers. The camp runs for **D** days.Each day,there can be at most one lecture. The **ith** trainer arrives on day **Di** and then stays till the end of the camp. He also wants to teach exactly **Ti** lectures. For each lecture that a trainer was not able to teach,his sadness level will be increased by **Si.**

You are the main organizer of the contest. You want to find minimum total sadness of the trainers.

### EXPLANATION:

Let’s assign our trainers starting from the first day of the camp. At each day adding arriving trainers to our set of trainers.

Each day should be assigned to only **one** trainer, it’s obvious that we should assign the trainer with maximum sadness to this lecture, so our set (container) should be a heap sorting trainers by their sadness value. In fact we should know also the number of days each lecturer wants to serve in, so we take the lecturer with maximum sadness from our heap and decrease his demand by 1. In case he still has lectures he would like to do, we keep him in the heap, otherwise we just pop him out.

After finishing all days, some teachers may have some remaining lectures they wanted to teach but we couldn’t find such days for them. Let’s denote the number of lectures the **ith** trainer couldn’t teach by **remi**  So our answer would be :

answer = \sum_{i=1}^{i=N} rem_i  * S_i

### AUTHOR’S AND TESTER’S SOLUTIONS:

**AUTHOR’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Setter/IPCTRAIN.cpp)

**TESTER’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Tester/IPCTRAIN.cpp)

**EDITORIALIST’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Editorialist/IPCTRAIN.cpp)

</details>
