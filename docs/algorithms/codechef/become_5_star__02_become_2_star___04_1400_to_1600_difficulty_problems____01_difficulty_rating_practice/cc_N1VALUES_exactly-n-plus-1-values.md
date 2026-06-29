# Exactly N plus 1 Values

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | N1VALUES |
| Difficulty Rating | 1495 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [N1VALUES](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/N1VALUES) |

---

## Problem Statement

You are given a positive integer $N$. You have to print exactly $N + 1$ positive integers
satisfying the following conditions:

- Exactly one value should appear twice, all the remaining values should appear only once.
- Sum of all these values should be equal to $2^N$.

You have to print the values in non-decreasing order. If there are multiple solutions, you can print any of them.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

---

## Output Format

For each test case, print a single line containing $N + 1$ positive integers in non-decreasing order that satisfy the given conditions. If there are multiple solutions, you may print any of them.

---

## Constraints

- $1 \le T \le 60$
- $1 \le N \le 60$

---

## Examples

**Example 1**

**Input**

```text
2
3
4
```

**Output**

```text
1 2 2 3
1 2 3 3 7
```

**Explanation**

**Test Case $1$:** $2$ is repeated twice and the remaining elements occurred only once and the sum of all the elements is equal to $8$, which is $2^3$.

**Test Case $2$:** $3$ is repeated twice and the remaining elements occurred only once and the sum of all the elements is equal to $16$, which is $2^4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
1 2 2 3
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
1 2 3 3 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/N1VALUES)

[Contest: Division 1](https://www.codechef.com/LTIME101A/problems/N1VALUES)

[Contest: Division 2](https://www.codechef.com/LTIME101B/problems/N1VALUES)

[Contest: Division 3](https://www.codechef.com/LTIME101C/problems/N1VALUES)

***Author:*** [Sandeep V](https://www.codechef.com/users/dazlersan1)

***Tester:*** [Radostin Chonev](https://www.codechef.com/users/ronniechonev)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N, find N+1 positive integers whose sum is 2^N and exactly one of them appears twice, while the others appear once.

#
[](#quick-explanation-5)QUICK EXPLANATION:

One possible solution is 1, 1, 2, 4, \dots, 2^{N-1}.

#
[](#explanation-6)EXPLANATION:

Trying to find the answers on paper for small N should lead to the following observations:

- The only solution for N = 1 is [1, 1].

- The only solution for N = 2 is [1, 1, 2].

- One possible solution for N = 3 is [1, 1, 2, 4]

\vdots

From here, it is easy to observe that the array [1, 1, 2, 4, \dots, 2^{N-1}] always works as a solution.

Proof

2^i < 2^{i+1} for i\geq 0, so the only repeated number in our set is 1.

Further,

1 + 1 + 2 + 4 + \dots + 2^{N-1} \\ = 1 + (1 + 2 + 4 + \dots + 2^{N-1}) \\ = 1 + (2^N - 1) = 2^N

as required.

#
[](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(N)

#
[](#code-8)CODE:

Setter (Python)
``t=int(input())
for _ in range(t):
    n=int(input())
    print(1,end=" ")
    for i in range(n):
        print(2**i,end=" ")
    print()
``

Tester (C++)
``#include<bits/stdc++.h>
using namespace std ;

int n ;

void input ( ) {
    cin >> n ;
}

void solve ( ) {
    cout << "1 " ;
    for ( int i = 0 ; i < n ; ++ i ) {
        cout << ( 1LL << i ) << " \n"[ i == n - 1 ] ;
    }
}

int main ( ) {
    ios_base :: sync_with_stdio ( false ) ;
    cin.tie ( NULL ) ;
    int t ;
    t = 1 ;
    /// scanf ( "%d" , &t ) ;
    cin >> t ;
    while ( t -- ) {
        input ( ) ;
        solve ( ) ;
    }
    return 0 ;
}
``

Editorialist (Python)
``import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print('1 ' + ' '.join(str(2**i) for i in range(n)))
``

</details>
