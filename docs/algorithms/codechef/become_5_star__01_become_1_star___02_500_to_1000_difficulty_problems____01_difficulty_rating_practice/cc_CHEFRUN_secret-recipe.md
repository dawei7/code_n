# Secret Recipe

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFRUN |
| Difficulty Rating | 888 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CHEFRUN](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CHEFRUN) |

---

## Problem Statement

Chef and his competitor Kefa own two restaurants located at a straight road. The position of Chef's restaurant is $X_1$, the position of Kefa's restaurant is $X_2$.

Chef and Kefa found out at the same time that a bottle with a secret recipe is located on the road between their restaurants. The position of the bottle is $X_3$.

The cooks immediately started to run to the bottle. Chef runs with speed $V_1$, Kefa with speed $V_2$.

Your task is to figure out who reaches the bottle first and gets the secret recipe (of course, it is possible that both cooks reach the bottle at the same time).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains five space-separated integers $X_1$, $X_2$, $X_3$, $V_1$ and $V_2$.

### Output
For each test case, print a single line containing the string `"Chef"` if Chef reaches the bottle first, `"Kefa"` if Kefa reaches the bottle first or `"Draw"` if Chef and Kefa reach the bottle at the same time (without quotes).

### Constraints
- $1 \le T \le 10^5$
- $|X_1|, |X_2|, |X_3| \le 10^5$
- $X_1 \lt X_3 \lt X_2$
- $1 \le V_1 \le 10^5$
- $1 \le V_2 \le 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1 3 2 1 2
1 5 2 1 2
1 5 3 2 2
```

**Output**

```text
Kefa
Chef
Draw
```

**Explanation**

**Example case 1.** Chef and Kefa are on the same distance from the bottle, but Kefa has speed $2$, while Chef has speed $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3 2 1 2
```

**Output for this case**

```text
Kefa
```



#### Test case 2

**Input for this case**

```text
1 5 2 1 2
```

**Output for this case**

```text
Chef
```



#### Test case 3

**Input for this case**

```text
1 5 3 2 2
```

**Output for this case**

```text
Draw
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFRUN)

[Contest](https://www.codechef.com/COOK94A/problems/CHEFRUN)

**Author:** [Yuri Shilyaev](https://www.codechef.com/users/hloya_ygrt)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/deadwing97)

**Editorialist:** [Yury Shilyaev](https://www.codechef.com/users/hloya_ygrt)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Mechanics, numbers with floating point.

### PROBLEM:

Two players are standing on a straight line at coordinates X_1 and X_2. Their goal is located at coordinate X_3. The first player runs to the goal with speed V_1, the second with V_2. The task is to find, who will came to the goal faster.

### QUICK EXPLANATION:

Refresh that the time of route S with velocity v is equal to \frac{S}{v}.

### EXPLANATION:

By the formula above, we can find time for the first player t_1 = \frac{S_1}{V_1}, where S_1 = X_3 - X_1. The time for the second player would be t_2 = \frac{S_2}{V_2}, where S_2 = X_2 - X_3. We can already solve the problem by simply comparing t_1 and t_2, but how to determine a ‘Draw’?

As you know, we can’t say that two real numbers are equal in programming language, because of precision. The best way to get rid of floating point numbers is to multiply t_1 and t_2 by V_1 \cdot V_2. The ‘Draw’ happens, when t_1 \cdot V_2 = t_2 \cdot V_1.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here].

Tester’s solution can be found [here].

</details>
