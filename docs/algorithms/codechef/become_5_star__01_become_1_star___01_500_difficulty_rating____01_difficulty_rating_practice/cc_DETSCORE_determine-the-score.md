# Determine the Score

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DETSCORE |
| Difficulty Rating | 267 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DETSCORE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DETSCORE) |

---

## Problem Statement

Chef appeared for a placement test.

There is a problem worth $X$ points. Chef finds out that the problem has exactly $10$ test cases. It is known that each test case is worth the same number of points.

Chef passes $N$ test cases among them. Determine the score Chef will get.

**NOTE:** See sample explanation for more clarity.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $N$, the total points for the problem and the number of test cases which pass for Chef's solution.

---

## Output Format

For each test case, output the points scored by Chef.

---

## Constraints

- $1 \leq T \leq 100$
- $10 \leq X \leq 200$
- $0 \leq N \leq 10$
- $X$ is a multiple of $10$.

---

## Examples

**Example 1**

**Input**

```text
4
10 3
100 10
130 4
70 0
```

**Output**

```text
3
100
52
0
```

**Explanation**

**Test Case $1$:** The problem is worth $10$ points and since there are $10$ test cases, each test case is worth $1$ point. Since Chef passes $3$ test cases, his score will be $1 \cdot 3 = 3$ points.

**Test Case $2$:** The problem is worth $100$ points and since there are $10$ test cases, each test case is worth $10$ points. Since Chef passes all the $10$ test cases, his score will be $10 \cdot 10 = 100$ points.

**Test Case $3$:** The problem is worth $130$ points and since there are $10$ test cases, each test case is worth $13$ points. Since Chef passes $4$ test cases, his score will be $13 \cdot 4 = 52$ points.

**Test Case $4$:** The problem is worth $70$ points and since there are $10$ test cases, each test case is worth $7$ points. Since Chef passes $0$ test cases, his score will be $7 \cdot 0 = 0$ points.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
100 10
```

**Output for this case**

```text
100
```



#### Test case 3

**Input for this case**

```text
130 4
```

**Output for this case**

```text
52
```



#### Test case 4

**Input for this case**

```text
70 0
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME109A/problems/DETSCORE)

[Contest Division 2](https://www.codechef.com/LTIME109B/problems/DETSCORE)

[Contest Division 3](https://www.codechef.com/LTIME109C/problems/DETSCORE)

[Contest Division 4](https://www.codechef.com/LTIME109D/problems/DETSCORE)

**Setter:** [utkarsh_adm](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

267

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef appears in a placement test and appears in a problem worth X points. The problem has 10 test cases. The Chef clears N test cases. We have to output Chef’s score for this problem

#
[](#explanation-5)EXPLANATION:

Note that X is the maximum possible score when all 10 test cases are cleared

Hint 1

What are the points per test case?

Hint 2

10 test cases are worth X points. So each test case is worth X/10 points. Note that we are told that X is a multiple of 10.

Hint 3

So now, given that Chef clears N test cases, what will Chef’s score be?

Hint 4

It is N * (X/10).

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
const int N=2e5+5;
int n;
ll a[N];
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;
	while(t--){
		int n,x;cin >> n >> x;
		cout << n/10*x << '\n';
	}
}
``

Editorialist's Solution
``t=int(input())
for _ in range(t):
    X,N = map(int,input().split())
    print((X//10)*N)
``

</details>
