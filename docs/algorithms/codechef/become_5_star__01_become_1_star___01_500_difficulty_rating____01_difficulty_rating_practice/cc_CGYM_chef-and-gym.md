# Chef and Gym

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CGYM |
| Difficulty Rating | 496 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CGYM](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CGYM) |

---

## Problem Statement

Chef has decided to join a Gym in ChefLand and if possible, also hire a personal trainer at the gym. The monthly cost of the gym is $X$ and personal training will cost him an additional $Y$ per month. Chef's total budget per month is only $Z$. Print `1` if Chef can only join the gym, `2` if he can also have a personal trainer, and `0` if he can't even join the gym.

**Note** that if Chef wants to hire a personal trainer, he *must* join the gym — he cannot hire the trainer without joining the gym.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing three space-separated integers $X, Y, Z$.

---

## Output Format

For each test case, output in a single line `2` if Chef can go to the gym and have a trainer, `1` if Chef can only go to the gym, `0` if he can't even go to the gym.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X,Y,Z \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 2 3
10 12 13
23 1 22
23 1 63
```

**Output**

```text
2
1
0
2
```

**Explanation**

**Test case $1$:** Since the total cost of Chef getting a gym membership and a trainer is $1+2 = 3$ which is equal to his budget of $3$, Chef can get both a gym membership and a trainer.

**Test case $2$:** Since the total cost of Chef getting a gym membership and a trainer is $10+12 = 22$ which is greater than his budget of $13$, he can't get both a gym membership and a trainer. However, the cost of the gym membership is $10$ which is less than his budget of $13$, so Chef can get only a gym membership.

**Test case $3$:** Since the cost of Chef getting a gym membership is $23$ which is greater than his budget of $22$, Chef can't even get the gym membership.

**Test case $4$:** The same costs as the previous test, but this time Chef has enough money to afford both the membership and a personal trainer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
10 12 13
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
23 1 22
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
23 1 63
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CGYM)

[Div-4 Contest](https://www.codechef.com/COOK141D/problems/CGYM)

***Author:*** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

#
[](#difficulty-2)DIFFICULTY:

496

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has decided to join a Gym in ChefLand and if possible, also hire a personal trainer at the gym. The monthly cost of the gym is X and personal training will cost him an additional Y per month. Chef’s total budget per month is only Z. Print `1` if Chef can only join the gym, `2` if he can also have a personal trainer, and `0` if he can’t even join the gym.

**Note** that if Chef wants to hire a personal trainer, he *must* join the gym — he cannot hire the trainer without joining the gym.

#
[](#explanation-5)EXPLANATION:

Simple Casework:

``if(X + Y <= Z)cout << 2 << endl;
else if(X <= Z)cout << 1 << endl;
else cout << 0 << endl;
``

</details>
