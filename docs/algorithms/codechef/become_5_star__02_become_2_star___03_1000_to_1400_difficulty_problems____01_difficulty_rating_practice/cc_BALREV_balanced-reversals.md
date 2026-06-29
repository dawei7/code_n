# Balanced Reversals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BALREV |
| Difficulty Rating | 1165 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [BALREV](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/BALREV) |

---

## Problem Statement

Chef is given a binary string $A$ of length $N$. He can perform the following operation on $A$ any number of times:
- Choose $L$ and $R$ $(1 \leq L \leq R \leq N)$, such that, in the [substring](https://en.wikipedia.org/wiki/Substring) $A[L,R]$, the number of $1$s is **equal** to the number of $0$s and **reverse** the substring $A[L,R]$.

Find the lexicographically **smallest** string that Chef can obtain after performing the above operation **any** (possibly zero) number of times on $A$.

String $X$ is lexicographically smaller than string $Y$, if either of the following satisfies:
- $X$ is a prefix of $Y$ and $X \neq Y$.
- There exists an index $i$ such that $X_i \lt Y_i$ and $X_j = Y_j, \forall j$ such that $1 \leq j \lt i$.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow. Each test case contains two lines.
- The first line contains the integer $N$, the length of the binary string.
- The second line contains the binary string $A$.

---

## Output Format

For each test case, print the lexicographically **smallest** binary string that can be obtained after performing the operation **any** (possibly zero) number of times.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5
01100
4
0000
```

**Output**

```text
00011
0000
```

**Explanation**

**Test Case $1$:** Chef can choose $L = 2$ and $R=5$. The chosen substring, $A[2,5] = 1100$. On reversing this, we get $0011$. Thus, the final string is $A = 00011$.  Note that this is the lexicographically smallest string possible.

**Test Case $2$:** Since the string is already lexicographically minimum, Chef does not need to apply any operation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
01100
```

**Output for this case**

```text
00011
```



#### Test case 2

**Input for this case**

```text
4
0000
```

**Output for this case**

```text
0000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START30A/problems/BALREV)

[Contest Division 2](https://www.codechef.com/START30B/problems/BALREV)

[Contest Division 3](https://www.codechef.com/START30C/problems/BALREV)

[Contest Division 4](https://www.codechef.com/START30D/problems/BALREV)

Setter: [ Saritesh](https://www.codechef.com/users/saritesh)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

[Inversions](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))

#
[](#problem-4)PROBLEM:

Chef is given a binary string A of length N. He can perform the following operation on A any number of times:

- Choose L and R (1 \leq L \leq R \leq N), such that, in the [substring](https://en.wikipedia.org/wiki/Substring) A[L,R], the number of $1$s is **equal** to the number of $0$s and **reverse** the substring A[L,R].

Find the lexicographically **smallest** string that Chef can obtain after performing the above operation **any** (possibly zero) number of times on A.

String X is lexicographically smaller than string Y, if either of the following satisfies:

-
X is a prefix of Y and X \neq Y.

- There exists an index i such that X_i \lt Y_i and X_j = Y_j, \forall j such that 1 \leq j \lt i.

#
[](#explanation-5)EXPLANATION:

The first intuition when we read the problem is, can we sort the string? If Yes, we have got our answer, as the sorted string is the lexicographically smallest possible string that we can get.

Let’s see if we can sort the string. Let there be an index i such that S_i = 1 and S_{i+1} = 0. If there is no such index i, then we have already sorted our string. Otherwise, the substring S_iS_{i+1} is a valid substring, and we can reverse it, making it 01. We can repeat this process as long as we can find such index i, and hence finally ending up with a sorted string.

But how to prove that the above process will eventually terminate?

We will prove this by using the number of inversions. It is recommended to first understand the concept of [inversions](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)).

Note that when we perform the above operation, the number of inversions decreases by 1. Because the initial number of inversions is finite, and the final number of inversions will be greater than or equal to 0, we can perform the above operation only finite number of times, eventually reaching a state where we cannot find a valid index i. In other words, the number of inversions will become 0, and hence we will end up getting our sorted string.

#
[](#time-complexity-6)TIME COMPLEXITY:

We need to sort the given string - O(N \cdot \log{N}) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#define ll long long
#define fo(i , n) for(ll i = 0 ; i < n ; i++)
#include<bits/stdc++.h>
using namespace std ;

void solve()
{
    ll n ;
    cin >> n ;
    string a ;
    cin >> a ;

    sort(a.begin() , a.end()) ;
    cout << a << endl ;
    return ;
}

int main()
{

    ll t = 1 ;
    cin >> t ;
    while(t--)
    {
        solve() ;
    }

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";

    return 0;
}
``

</details>
