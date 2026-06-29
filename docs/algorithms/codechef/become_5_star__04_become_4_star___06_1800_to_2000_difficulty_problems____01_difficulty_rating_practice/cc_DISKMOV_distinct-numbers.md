# Distinct Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISKMOV |
| Difficulty Rating | 1912 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [DISKMOV](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/DISKMOV) |

---

## Problem Statement

Given an array $A$ consisting of $N$ **distinct** integers $(1 \le A_i \le 2 \cdot N)$, we have to perform $K$ moves.
We perform the following steps in one move:

- Select an integer $X$ such that $1 \le X \le 2 \cdot N$ and $X \ne A_i$ for all $i$ $(X$ is not equal to any element of the current array$)$.
- Append $X$ to $A$.
- The *score* of this move $= (\max_{1 \le i \le |A|} A_i) - X$.
Note that the *score* is calculated after appending $X$. Thus, $X$ can be the maximum element of the array as well.

For e.g. if $A = [3, 1, 5]$ and we append $X = 2$ to $A$, then, $A$ becomes $[3, 1, 5, 2]$ and the *score* of this move is $\max([3, 1, 5, 2]) - 2 = 5 - 2 = 3$.

Find the **maximum sum** of *scores* we can achieve after performing **exactly** $K$ moves.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains three space-separated integers $N$ and $K$ — the size of the array $A$ and the number of moves respectively.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the **maximum sum** of *scores* we can achieve after performing **exactly** $K$ moves.
It is guaranteed that it is always possible to perform $K$ moves under the given constraints.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \le K \le N$
- $1 \leq A_i \leq 2 \cdot N$
- All $A_i$ are distinct.
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3 1
1 3 6
2 2
1 2
3 2
1 2 5
```

**Output**

```text
4
1
3
```

**Explanation**

**Test Case 1:** We can perform the following move:
- Append $X = 2$. Score of this move $= \max([1, 3, 6, 2]) - 2 = 6 - 2 = 4$

Hence, the maximum total score is $4$.

**Test Case 2:** We can perform the following moves:
- Append $X = 4$. Score of this move $= \max([1, 2, 4]) - 4 = 4 - 4 = 0$
- Append $X = 3$. Score of this move $= \max([1, 2, 4, 3]) - 3 = 4 - 3 = 1$

Hence, the maximum total score is $0+1=1$.

**Test Case 3:** We can perform the following moves:
- Append $X = 4$. Score of this move $= \max([1, 2, 5, 4]) - 4 = 5 - 4 = 1$
- Append $X = 3$. Score of this move $= \max([1, 2, 5, 4, 3]) - 3 = 5 - 3 = 2$

Hence the maximum total score is $1+2=3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
1 3 6
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
2 2
1 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3 2
1 2 5
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

[Practice](https://www.codechef.com/problems/DISKMOV)

[Contest: Division 1](https://www.codechef.com/START60A/problems/DISKMOV)

[Contest: Division 2](https://www.codechef.com/START60B/problems/DISKMOV)

[Contest: Division 3](https://www.codechef.com/START60C/problems/DISKMOV)

[Contest: Division 4](https://www.codechef.com/START60D/problems/DISKMOV)

***Author:*** [Akshat Anil Jain](https://www.codechef.com/users/akshatjain18)

***Tester:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1912

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A containing N distinct integers ranging from 1 to 2N, perform the following operation exactly K times:

- Choose some 1 \leq x \leq 2N such that x \notin A, append x to A, and add \max(A) - x to your score

What is the maximum possible final score?

#
[](#explanation-5)EXPLANATION:

Let’s look at how the score changes when we add a new element x to A. There are two cases:

- If x \lt \max(A), then we get \max(A) - x added to the score

- Otherwise, we must have x = \max(A), in which case we add 0 to the score.

Ideally, we’d like as many operations of the first type as possible, since they’re profitable. Note that the score of the first operation is maximized when x is as small as possible and \max(A) is as large as possible.

This gives us a strategy. Let M denote the initial maximum of A, before any operations are done.

- Suppose we add K elements that do not change the maximum, i.e, they are all \lt M. Then, of course we choose the smallest K elements to insert.

- Suppose we add some element that does change the maximum.

- It’s optimal to add this element first so that all later operations have a higher score.

- It’s optimal to add as large a maximum as possible, so let’s just choose 2N to add in the first move

- The other K-1 elements then should be chosen to be as small as possible to maximize the score, so choose the K-1 smallest remaining elements

The answer is the maximum of both cases. Each one’s score can be computed in \mathcal{O}(N), giving us a linear time solution.

Note that we need to be able to quickly find the sum of the K smallest elements that are not in A. This can be done by maintaining a `mark` array that denotes which elements are already in A, then iterating across it from 1 to 2N and adding i to the sum if `mark[i] == 0`.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--) {
	    int n, k;
	    cin >> n >> k;
	    long long int ans1 = 0, ans2 = 0;
	    int a[n];
	    for(int i = 0; i < n; i++) cin >> a[i];
	    sort(a, a + n);
	    vector<int> missing;
	    int now = 0;
	    for(int i = 1; i <= 2*n; i++) {
	        if(a[now] == i) now++;
	        else missing.push_back(i);
	    }
	    for(int i = 0 ; i < k ; i++) ans1 += max(0, a[n - 1] - missing[i]);
	    for(int i = 0 ; i < k - 1 ; i++) ans2 += max(0, 2*n - missing[i]);
	    cout << max(ans1, ans2) << "\n";
	}
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mark = [0]*(2*n + 1)
    b = []
    for x in a:
        mark[x] = 1
    for i in range(1, 2*n+1):
        if mark[i] == 0:
            b.append(i)
    mx = max(a)
    ans = int(-10 ** 13)
    ans = max(ans, (k-1)*(2*n) - sum(b[0:k-1]))
    ans = max(ans, k*mx - sum(b[0:k]))
    print(ans)
``

</details>
