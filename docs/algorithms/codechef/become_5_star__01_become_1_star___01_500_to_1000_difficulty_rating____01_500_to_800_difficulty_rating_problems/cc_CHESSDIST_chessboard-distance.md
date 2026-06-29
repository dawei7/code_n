# Chessboard Distance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHESSDIST |
| Difficulty Rating | 690 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHESSDIST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHESSDIST) |

---

## Problem Statement

The Chessboard Distance for any two points $(X_1, Y_1)$ and $(X_2, Y_2)$ on a Cartesian plane is defined as $max(|X_1 - X_2|, |Y_1 - Y_2|)$.

You are given two points $(X_1, Y_1)$ and $(X_2, Y_2)$. Output their Chessboard Distance.

Note that, $|P|$ denotes the absolute value of integer $P$. For example, $|-4| = 4$ and $|7| = 7$.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing $4$ space separated integers - $X_1, Y_1, X_2, Y_2$ - as defined in the problem statement.

---

## Output Format

For each test case, output in a single line the chessboard distance between $(X_1, Y_1)$ and $(X_2, Y_2)$

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X_1, Y_1, X_2, Y_2 \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2 4 5 1
5 5 5 3
1 4 3 3
```

**Output**

```text
3
2
2
```

**Explanation**

- In the first case, the distance between $(2, 4)$ and $(5, 1)$ is $max(|2- 5|, |4 - 1|) = max(|-3|, |3|) = 3$.

- In the second case, the distance between $(5, 5)$ and $(5, 3)$ is $max(|5- 5|, |5 - 3|) = max(|0|, |2|) = 2$.

- In the third case, the distance between $(1, 4)$ and $(3, 3)$ is $max(|1- 3|, |4 - 3|) = max(|-2|, |1|) = 2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 4 5 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5 5 5 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
1 4 3 3
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

[Contest Division 1](https://www.codechef.com/LTIME105A/problems/CHESSDIST)

[Contest Division 2](https://www.codechef.com/LTIME105B/problems/CHESSDIST)

[Contest Division 3](https://www.codechef.com/LTIME105C/problems/CHESSDIST)

[Contest Division 4](https://www.codechef.com/LTIME105D/problems/CHESSDIST)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

The Chessboard Distance for any two points (X_1,Y_1) and (X_2,Y_2) on a Cartesian plane is defined as max(|X_1?X2|,|Y1?Y2|).

You are given two points .(X_1,Y_1) and (X_2,Y_2) Output their Chessboard Distance.

#
[](#explanation-5)EXPLANATION:

Let’s say S_X is the absolute difference between the X coordinates while S_Y is the absolute difference between y coordinates i.e.

S_X = abs(X_1-X_2) \\
S_Y = abs(Y_1 - Y_2);

Our answer is the maximum of S_X and S_Y. Hence if S_X is greater print S_X otherwise print S_Y.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

#
[](#solutions-7)SOLUTIONS:

Setter
``
``

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
  int a,b,c,d;
  cin>>a>>b>>c>>d;

  cout<<max(abs(a-c),abs(b-d))<<"\n";
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
