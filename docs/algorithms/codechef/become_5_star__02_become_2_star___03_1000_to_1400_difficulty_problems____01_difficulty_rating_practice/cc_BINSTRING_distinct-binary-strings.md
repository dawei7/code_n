# Distinct Binary Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BINSTRING |
| Difficulty Rating | 1262 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [BINSTRING](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/BINSTRING) |

---

## Problem Statement

You are given a binary string $S$ of length $N$.

You have to perform the following operation **exactly** once:
- Select an index $i$ $(1 \le i \leq N)$ and delete $S_i$ from $S$. The remaining parts of $S$ are concatenated in the same order.

How many **distinct** binary strings of length $N-1$ can you get after applying this operation?

---

## Input Format

- The first line of input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follow.
- The first line of each test case contains $N$ - the length of the binary string $S$.
- The second line contains the binary string $S$.

---

## Output Format

For each test case, output the number of distinct binary strings that you can get after applying the operation exactly once.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- Sum of $N$ does not exceed $2 \cdot 10^5$ over all testcases.

---

## Examples

**Example 1**

**Input**

```text
3
3
100
4
1111
5
10110
```

**Output**

```text
2
1
4
```

**Explanation**

**Test Case 1:** We have $S = 100$. Now, we can get $00$ (on deleting $S_1$), $10$ (on deleting $S_2$) and $10$ (on deleting $S_3$). Therefore, we can get $2$ distinct strings.

**Test Case 2:** We have $S = 1111$. Now, we will always get $111$ irrespective of the index $i$ on which we apply the operation. Therefore, we can get $1$ distinct string.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
100
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
1111
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5
10110
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START27A/problems/BINSTRING)

[Contest Division 2](https://www.codechef.com/START27B/problems/BINSTRING)

[Contest Division 3](https://www.codechef.com/START27C/problems/BINSTRING)

[Contest Division 4](https://www.codechef.com/START27D/problems/BINSTRING)

Setter: [Satyam](https://www.codechef.com/users/satyam_343)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

There are no such pre-requisites for the problem. You need to be comfortable with loops and conditional statements to solve this problem.

#
[](#problem-4)PROBLEM:

You are given a binary string S of length N.

You have to perform the following operation **exactly** once:

- Select an index i (1 \le i \leq N) and delete S_i from S. The remaining parts of S are concatenated in the same order.

How many **distinct** binary strings of length N-1 can you get after applying this operation?

#
[](#quick-explanation-5)QUICK EXPLANATION:

- Let str_i represents the string obtained after deleting the i^{th} character from the string. Compare str_i and str_{i+1}. When are they same? When are they different? What if we consider str_i and str_j?

#
[](#explanation-6)EXPLANATION:

Let us use the notations as defined in the Quick Explanation and try to answer the questions that are asked there.

Consider a continuous block of 0s. If we remove any 0 from this continuous block, then the resulting strings will be equal.  The same holds for a continuous block of 1's. So, if S_i = S_{i+1}, then the resulting str_i will be equal to str_{i+1}.

This motivates us to consider the string as the blocks of 0s and 1s. Let us represent the string as S = O_1Z_1O_2Z_2...O_KZ_K, where Z_i represents a block of 0s and O_i represents a block of 1s. (It is possible that string starts with 0 or ends with 1, all these cases are equivalent, so the above representation is good enough for us).

We have seen that if we remove any 1 from O_i, the resulting strings will be equal. The only case to consider is, if we remove 1 from O_i in one case and from O_j in second case (i \neq j).

The first string will be: O_1Z_1...Z_{i-1}(O_i-1)Z_i...O_jZ_j...O_KZ_K

The second string will be: O_1Z_1...Z_{i-1}O_iZ_i...(O_j-1)Z_j...O_KZ_K

We can see that strings differ at the O_i block. So these both strings are different.

Therefore, total number of **distinct** strings that we can obtain is equal to the number of continuous blocks of 0s and 1s.

#
[](#time-complexity-7)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-8)SOLUTION:

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
        int n ;
        string str ;
        cin >> n >> str ;
        int ans = 1 ;
        for(int i = 1 ; i < n ; i++)
            if(str[i] != str[i-1])
                ans++ ;

        cout << ans << '\n' ;
    }

    return 0;
}

``

</details>
