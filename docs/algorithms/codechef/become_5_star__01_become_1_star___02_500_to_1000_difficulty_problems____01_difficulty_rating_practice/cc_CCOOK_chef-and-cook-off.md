# Chef and Cook-Off

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CCOOK |
| Difficulty Rating | 961 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CCOOK](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CCOOK) |

---

## Problem Statement

Chef has obtained the results of a past Cook-Off. He wants to estimate the skill level of each contestant. The contestants can be classified [with high probability](https://en.wikipedia.org/wiki/With_high_probability) (w.h.p.) based on the number of solved problems:

- A contestant that solved exactly 0 problems is a beginner.

- A contestant that solved exactly 1 problem is a junior developer.

- A contestant that solved exactly 2 problems is a middle developer.

- A contestant that solved exactly 3 problems is a senior developer.

- A contestant that solved exactly 4 problems is a hacker.

- A contestant that solved all five problems is [Jeff Dean](https://www.quora.com/What-are-all-the-Jeff-Dean-facts).

Please help Chef to identify the programming level of each participant.

### Input

- The first line of the input contains a single integer **N** denoting the number of competitors.

- **N** lines follow. The **i**-th of these lines contains five space-separated integers **Ai, 1, Ai, 2, Ai, 3, Ai, 4, Ai, 5**. The **j**-th of these integers (1 ≤ **j** ≤ 5) is 1 if the **i**-th contestant solved the **j**-th problem and 0 otherwise.

### Output

For each participant, print a single line containing one string denoting Chef's classification of that contestant — one of the strings "Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean" (without quotes).

### Constraints

- 1 ≤ **N** ≤ 5000

- 0 ≤ **Ai, j** ≤ 1 for each valid **i**, **j**

---

## Examples

**Example 1**

**Input**

```text
7
0 0 0 0 0
0 1 0 1 0
0 0 1 0 0
1 1 1 1 1
0 1 1 1 0
0 1 1 1 1
1 1 1 1 0
```

**Output**

```text
Beginner
Middle Developer
Junior Developer
Jeff Dean
Senior Developer
Hacker
Hacker
```

**Explanation**

The first contestant has no solved problems, therefore he is a beginner. The second contestant solved 2 problems (the second and fourth problem), therefore he has the skills of a middle developer. The third contestant solved 1 problem, therefore he's at the expected level of a junior developer. The fourth contestant solved 5 problems — we can guess it was Jeff Dean. The fifth contestant solved 3 problems, so he is a senior developer. And the last two contestants should be hackers because they solved exactly 4 problems each.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0 0 0 0
```

**Output for this case**

```text
Beginner
```



#### Test case 2

**Input for this case**

```text
0 1 0 1 0
```

**Output for this case**

```text
Middle Developer
```



#### Test case 3

**Input for this case**

```text
0 0 1 0 0
```

**Output for this case**

```text
Junior Developer
```



#### Test case 4

**Input for this case**

```text
1 1 1 1 1
```

**Output for this case**

```text
Jeff Dean
```



#### Test case 5

**Input for this case**

```text
0 1 1 1 0
```

**Output for this case**

```text
Senior Developer
```



#### Test case 6

**Input for this case**

```text
0 1 1 1 1
```

**Output for this case**

```text
Hacker
```



#### Test case 7

**Input for this case**

```text
1 1 1 1 0
```

**Output for this case**

```text
Hacker
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](https://www.codechef.com/problems/CCOOK)

[Contest](https://www.codechef.com/COOK91/problems/CCOOK)

## Setter: [Misha Chorniy](https://www.codechef.com/users/mgch)

## Tester: [Ke Bi](https://www.codechef.com/users/wwwwodddd)

## Editorialist: [Rashad Mammadov](https://www.codechef.com/users/mamedov)

# Difficulty:

CAKEWALK

# Prerequisites:

Loops, Conditional statements

# Problem:

You are given the results of each contestant for 5 problems, either 1 or 0 - which means the contestant has solved it or not correspondingly, and wants you to find his/her level(“Beginner”, “Junior Developer”, “Middle Developer”,“Senior Developer”,“Hacker”, or [Jeff Dean](https://www.quora.com/What-are-all-the-Jeff-Dean-facts)).

# Explanation:

It is just a straight-forward problem. The solution is to sum the results for each row and output the corresponding skill given in the problem statement using " if " conditions. Preferably you may use " switch - case " to make your code seem elegant.

# Time Complexity:

O(N)

# Space Complexity:

O(N) or O(1)

</details>
