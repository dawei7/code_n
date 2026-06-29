# N Queens Puzzle Solved !

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EUREKA |
| Difficulty Rating | 1109 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [EUREKA](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EUREKA) |

---

## Problem Statement

Chef, being a Chess fan, was thrilled after he read the following news:

[Michael Simkin, a postdoctoral fellow at Harvard University’s Center of Mathematical Sciences and Applications proved that for a large value of $N$, there are approximately $(0.143 \cdot N)^N$ configurations in which $N$ queens can be placed on a $N \times N$ chessboard so that none attack each other.](https://www.quantamagazine.org/mathematician-answers-chess-problem-about-attacking-queens-20210921/)

Although the formula is valid for large $N$, Chef is interested in finding the value of function $f(N)$ = $(0.143 \cdot N)^N$ for a given small value of $N$. Since Chef is busy understanding the [proof](https://arxiv.org/abs/2107.13460) of the formula, please help him calculate this value.

Print the answer rounded to the nearest integer. That is, if the actual value of $f(N)$ is $x$,
- Print $\lfloor x\rfloor$ if $x - \lfloor x\rfloor \lt 0.5$
- Otherwise, print $\lfloor x\rfloor + 1$

where $\lfloor x\rfloor$ denotes the [floor](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of $x$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing one integer $N$.

---

## Output Format

For each test case, output in a single line the value of $f(N)$ rounded to the nearest integer.

---

## Constraints

- $1 \leq T \leq 12$
- $4 \leq N \leq 15$

---

## Examples

**Example 1**

**Input**

```text
2
4
10
```

**Output**

```text
0
36
```

**Explanation**

**Test case $1$:** $f(N) = (0.143 \cdot 4)^4 = 0.107$, which when rounded to nearest integer gives $0$.

**Test case $2$:** $f(N) = (0.143 \cdot 10)^{10} = 35.7569$, which when rounded to nearest integer gives $36$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
10
```

**Output for this case**

```text
36
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/FEB221A/problems/EUREKA)

[Contest Division 2](https://www.codechef.com/FEB221B/problems/EUREKA)

[Contest Division 3](https://www.codechef.com/FEB221C/problems/EUREKA)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Print the value of f(N) = (0.143 \cdot N)^N rounded to the nearest integer. That is, if the actual value of f(N) is x,

- Print ?x? if, x - ?x? < 0.5

- Otherwise, print ?x?+1

#
[](#explanation-5)EXPLANATION:

In this problem, we just need to implement the problem statement. The focus is on our ability to translate the problem statement into functioning error-free code.

Calculating f(N)

We can calculate f(N) either by running a loop N times or by using the power function from the library. Since the value of N is very small, it would take constant time to calculate f(N) using either way.

Round off to nearest integer

f(N) can be rounded to nearest integer either by checking the value of f(N) - ?f(N)? or using the round function. It would take constant time to do this.

Most languages have power and round functions available. In languages like C++, we need to take special care of the floating point number.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
# define ld long double

int main()
{
    int t; cin >> t;
    int n;
    while(t--){
        cin >> n;
        ld ans = 1, mul = (ld)0.143 * n;
        for(int i = 1; i <= n; i++){
            ans *= mul;
        }
        cout << round(ans) << endl;
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--) {
		int n;
		cin >> n;
		cout << (int)(pow(0.143*n, n) + 0.5) << "\n";
	}
	return 0;
}
``

Editorialist's Solution
``testcases = int(input())
for testcase_idx in range(testcases):
	n = int(input())
	x = 0.143 * n
	res = x ** n
	ans = round(res)
	print(ans)
``

</details>
