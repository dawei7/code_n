# Permutation GCD

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMGCD |
| Difficulty Rating | 1328 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [PERMGCD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/PERMGCD) |

---

## Problem Statement

Chef is interested in the sum of [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor)s of all prefixes of a permutation of the integers $\{1, 2, \ldots, N\}$.

Formally, for a permutation $P = [P_1, P_2, \ldots, P_N]$ of $\{1, 2, \ldots, N\}$, let us define a function $F_i = \gcd(A_1, A_2, A_3, \ldots, A_i)$. Chef is interested in the value of $F_1 + F_2 + \ldots + F_N$.

Now, Chef wants to find a permutation of $\{1, 2, \ldots, N\}$ which has the given sum equal to $X$. Please help Chef find one such permutation. In case there is no such permutation, print $-1$. In case of multiple answers, any of them will be accepted.

A permutation of $\{1, 2, \ldots, N\}$ is a sequence of numbers from $1$ to $N$ in which each number occurs exactly once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space separated integers $N$ and $X$ denoting the length of required permutation and the required sum of GCDs of all prefixes respectively.

---

## Output Format

- If there is a valid permutation that satisfies the required condition, then:
    - In a single line, output $N$ space-separated integers denoting the required permutation permutation.
- If there is no permutation, print $-1$ in a single line.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 1000$
- $1 \leq X \leq 2\cdot N - 1$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
1 1
2 1
4 6
3 5
```

**Output**

```text
1
-1
2 4 3 1
3 2 1
```

**Explanation**

**Test case $1$:** The only possible permutation has a sum of $1$, as required.

**Test case $2$:** The two permutations of length $2$ are:
- $[1, 2]$ with a value of $1 + 1 = 2$
- $[2, 1]$ with a value of $2 + 1 = 3$

None of them have a sum of $X = 1$, so we output $-1$.

**Test case $3$:** For $P = [2, 4, 3, 1]$, we have:
- $F_1 = 2$
- $F_2 = \gcd(2, 4) = 2$
- $F_3 = \gcd(2, 4, 3) = 1$
- $F_4 = \gcd(2, 4, 3, 1) = 1$

The sum of these values is $6$, as required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 1
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
4 6
```

**Output for this case**

```text
2 4 3 1
```



#### Test case 4

**Input for this case**

```text
3 5
```

**Output for this case**

```text
3 2 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START50)

[Practice](https://www.codechef.com/problems/PERMGCD)

**Setter:** [tejas_adm](https://www.codechef.com/users/tejas_adm)

**Testers:** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec), [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1328

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Find a permutation of [1, N], so that the sum of prefix-GCDs is exactly X.

#
[](#explanation-5)EXPLANATION:

GCD of positive numbers is always \ge 1. So the sum of N of the prefix-GCDs is going to be \ge N. So, if X < N, there is no answer, and hence output -1.

For all other cases, we can construct a permutation. We see from the input constraints that X is guaranteed to be \le 2*N - 1. So, we can place a suitable element at the first, and then a 1, and the rest in any order. In such a case, the GCD of all prefixes except the very first is 1. So, the first element has to be X-(N-1). So the permutation is [X-(N-1), 1, 2, 3, \dots, N], taking care that the first element isn’t repeated twice.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int T, n, x;

int main() {

	cin>>T;

	while(T--)
	{
	    cin>>n>>x;
	    if(x<n)
	    {
	        cout<<-1<<"\n";
	        continue;
	    }
	    x -= (n-1);
	    cout<<x<<" ";
	    for(int i=1;i<=n;i++)
	    {
	        if(i==x)
	            continue;
	        cout<<i<<" ";
	    }
	    cout<<"\n";
	}

	return 0;
}
``

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, x;
        cin >> n >> x;
        if(x < n) {
            cout << "-1\n";
            continue;
        }
        int now = 1, done = x - n + 1;
        cout << done << " ";
        for(int i = 1; i < n; i++) {
            if(now == done) now++;
            cout << now << " ";
            now++;
        }
        cout << "\n";
    }
}

``

Tester's Solution
``for _ in range(int(input())):
	n, k = map(int, input().split())
	if k < n:
		print(-1)
	else:
		print(k-n+1, *range(1, k-n+1), *range(k-n+2, n+1))
``

</details>
