# Final Population

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POPULATION |
| Difficulty Rating | 358 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [POPULATION](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/POPULATION) |

---

## Problem Statement

There were initially $X$ million people in a town, out of which $Y$ million people left the town and $Z$ million people immigrated to this town.

Determine the final population of town in millions.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case consists of three integers $X$, $Y$ and $Z$.

---

## Output Format

For each test case, output the final population of the town in millions.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y, Z \leq 10$
- $Y \leq X$

---

## Examples

**Example 1**

**Input**

```text
4
3 1 2
2 2 2
4 1 8
10 1 10
```

**Output**

```text
4
2
11
19
```

**Explanation**

**Test case $1$:** The initial population of the town was $3$ million, out of which $1$ million people left and $2$ million people entered the town. So, final population $= 3 - 1 + 2 = 4$ million.

**Test case $2$:** The initial population of the town was $2$ million, out of which $2$ million left and $2$ million immigrated. The final population is thus $2+2-2 = 2$ million.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1 2
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
2 2 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 1 8
```

**Output for this case**

```text
11
```



#### Test case 4

**Input for this case**

```text
10 1 10
```

**Output for this case**

```text
19
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/POPULATION)

[Contest: Division 1](https://www.codechef.com/START51A/problems/POPULATION)

[Contest: Division 2](https://www.codechef.com/START51B/problems/POPULATION)

[Contest: Division 3](https://www.codechef.com/START51C/problems/POPULATION)

[Contest: Division 4](https://www.codechef.com/START51D/problems/POPULATION)

***Author:*** [Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

***Testers:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Venkata Nikhil Medam](https://www.codechef.com/users/nikhil_medam)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

358

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

X million people live in a town. Of them, Y million leave and Z million enter. How many people are in the town now?

#
[](#explanation-5)EXPLANATION:

There were initially X million people in the town. After Y million leave, there were X -  Y million people in it. After Z million entered, there are X - Y + Z million people in it. Thus, the solution is to print X - Y + Z.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Tester (C++)
``// Tester: Nikhil_Medam
#include <bits/stdc++.h>
using namespace std;
#define endl "\n"

int t, x, y, z;
int32_t main() {
    cin >> t;
    while(t--) {
        cin >> x >> y >> z;
        cout << x - y + z << endl;
    }
	return 0;
}

``

Editorialist (Python)
``for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(x - y + z)
``

</details>
