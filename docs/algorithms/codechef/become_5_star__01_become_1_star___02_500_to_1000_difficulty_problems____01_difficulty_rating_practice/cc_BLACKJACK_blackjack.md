# Blackjack

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BLACKJACK |
| Difficulty Rating | 681 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [BLACKJACK](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BLACKJACK) |

---

## Problem Statement

Chef is playing a variant of Blackjack, where $3$ numbers are drawn and each number lies between $1$ and $10$ (with both $1$ and $10$ inclusive). Chef wins the game when the sum of these $3$ numbers is exactly $21$.

Given the first two numbers $A$ and $B$, that have been drawn by Chef, what should be $3$-rd number that should be drawn by the Chef in order to win the game?

Note that it is possible that Chef cannot win the game, no matter what is the $3$-rd number. In such cases, report $-1$ as the answer.

---

## Input Format

- The first line will contain an integer $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $A$ and $B$ - the first and second number drawn by the Chef.

---

## Output Format

For each testcase, output the $3$-rd number that should be drawn by the Chef in order to win the game. Output $-1$ if it is not possible for the Chef to win the game.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A, B \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
1 10
1 5
4 9
```

**Output**

```text
10
-1
8
```

**Explanation**

**Test case $1$**: The first two numbers are $1$ and $10$. If the third number will be $10$, the resulting sum will be $1 + 10 + 10 = 21$. So Chef will win the game if the third number is $10$.

**Test case $2$**: The first two numbers are $1$ and $5$. There is no number between $1$ and $10$, that can make the resulting sum $21$. Hence, the answer will be $-1$ in this test case.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
1 5
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
4 9
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START27A/problems/BLACKJACK)

[Contest Division 2](https://www.codechef.com/START27B/problems/BLACKJACK)

[Contest Division 3](https://www.codechef.com/START27C/problems/BLACKJACK)

[Contest Division 4](https://www.codechef.com/START27D/problems/BLACKJACK)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish315)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is playing a variant of Blackjack, where 3 numbers are drawn and each number lies between 1 and 10 (with both 1 and 10 inclusive). Chef wins the game when the sum of these 3 numbers is exactly 21.

Given the first two numbers A and B, that have been drawn by Chef, what should be 3-rd number that should be drawn by the Chef in order to win the game?

Note that it is possible that Chef cannot win the game, no matter what is the 3-rd number. In such cases, report -1 as the answer.

#
[](#explanation-5)EXPLANATION:

Let us represent the 3-rd number that should be drawn by Chef by C. The following condition needs to be satisfied: A+B+C = 21.

This can be rewritten as C = 21 - (A+B). However, note that the 3-rd number can only lie between 1 and 10 (inclusive).

Hence, after getting the above value of C, we need to check if the resulting C is between 1 and 10. If Yes, we have got our answer as C, otherwise the answer is -1.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

int main()
{
    ll t;
    cin >> t ;
    while(t--)
    {
         ll a , b ;
        cin >> a >> b ;
        ll ans = (21 - (a+b)) ;

        if(ans >= 1 && ans <= 10)
            cout << ans << '\n' ;
        else
            cout << -1 << '\n' ;
    }

    return 0;
}
``

</details>
