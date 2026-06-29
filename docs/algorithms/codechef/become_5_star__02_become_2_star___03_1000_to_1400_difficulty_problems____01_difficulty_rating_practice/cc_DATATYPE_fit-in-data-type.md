# Fit in Data Type

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DATATYPE |
| Difficulty Rating | 1133 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [DATATYPE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/DATATYPE) |

---

## Problem Statement

Chef wants to store some important numerical data on his personal computer. He is using a new data type that can store values only from $0$ till $N$ both inclusive. If this data type receives a value greater than $N$ then it is cyclically converted to fit into the range $0$ to $N$.
For example:
- Value $N+1$ will be stored as $0$.
- Value $N+2$ will be stored as $1$.

and so on...

Given $X$, the value chef wants to store in this new data type. Determine what will be the actual value in memory after storing $X$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains a single line of input, two space separated integers $N, X$ - the maximum value a data type can store and the value Chef wants to store in the data type respectively.

---

## Output Format

For each testcase, output in a single line the value which will be actually stored in memory.

---

## Constraints

- $1 \leq T \leq 3000$
- $1 \leq N \leq 50$
- $0 \leq X \leq 50$

---

## Examples

**Example 1**

**Input**

```text
5
15 0
15 10
11 12
27 37
50 49
```

**Output**

```text
0
10
0
9
49
```

**Explanation**

**Test Case $1$**: The data type can store values from $0$ to $15$. If we try to put $0$ in this data type, then the stored value will be the same, that is $0$.

**Test Case $2$**: The data type can store values from $0$ to $15$. If we try to put $10$ in this data type, then the stored value will be the same, that is $10$.

**Test Case $3$**: The data type can store values from $0$ to $11$. If we try to put $12$ in this data type, then the stored value will cyclically come back to $0$. Hence the output is $0$.

**Test Case $4$**: The data type can store values from $0$ to $27$. If we try to put $37$ in this data type, then the stored value will cyclically convert to $9$. Hence the output is $9$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15 0
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
15 10
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
11 12
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
27 37
```

**Output for this case**

```text
9
```



#### Test case 5

**Input for this case**

```text
50 49
```

**Output for this case**

```text
49
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START25A/problems/DATATYPE)

[Contest Division 2](https://www.codechef.com/START25B/problems/DATATYPE)

[Contest Division 3](https://www.codechef.com/START25C/problems/DATATYPE)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is using a new data type that can store values only in the range 0 to N (both inclusive). If a value greater than N is received, it is cyclically converted to fit in the range 0 to N. Given X, determine what will be the actual value in memory after storing X in this new data type.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- The answer is X \% (N+1).

#
[](#explanation-6)EXPLANATION:

Brute Force

Simply translate the problem statement into error-free code. Since the values of N and X are very small, the solution passes within the time limit.

We keep a counter to store our current answer. Initialise this counter with -1. Run a loop from 0 to X (inclusive) and increment the counter in each iteration. Each time the counter hits the value N+1, reset its value to 0.

This approach has a time complexity of O(X) per testcase.

Optimised Approach

Observe that the value in this new data type always lies in the range 0 to N. All greater values are cyclically converted to this range. The new value of X is the remainder when X is divided by (N+1).

Thus, the answer is simply X \% (N+1). The complexity for this is O(1) per testcase.

#
[](#time-complexity-7)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-8)SOLUTION:

Setter's Solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int n,x;
    cin>>n>>x;
    cout<<(x%(n+1))<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin>>t;
    while(t--)
        solve();
}
``

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n, x;
	    cin>>n>>x;
	    int cnt = -1;
	    for(int i = 0; i<=x; i++){
	        cnt++;
	        if(cnt==n+1){
	            cnt = 0;
	        }
	    }
	    cout<<cnt<<endl;
	}
	return 0;
}
``

</details>
