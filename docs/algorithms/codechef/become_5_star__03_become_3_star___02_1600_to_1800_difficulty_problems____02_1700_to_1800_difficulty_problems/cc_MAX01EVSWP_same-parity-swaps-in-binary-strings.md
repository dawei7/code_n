# Same Parity Swaps in Binary Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAX01EVSWP |
| Difficulty Rating | 1747 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MAX01EVSWP](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MAX01EVSWP) |

---

## Problem Statement

You are given a binary string $S$ of length $N$ (i.e. every character of $S$ is either $0$ or $1$).

You can perform the following operation on $S$:
- select any two indices $i, j$ of the same parity, i.e. either both $i, j$ are odd or both $i, j$ are even
- swap $S_i$ and $S_j$

For example, in the string $1110$, we can swap the second and the fourth characters to get $1011$. However, we can never obtain $1101$ from $1110$ by performing such swaps.

Find the maximum possible number of occurrences of the string $01$ as a [substring](https://en.wikipedia.org/wiki/Substring) of $S$ after performing the above operation any number of times (it is also allowed to not perform any operation).

For example, the string $1110$ has no occurrence of the string $01$ as a substring, whereas we can swap the second and fourth characters to obtain $1{\color{red}{01}}1$ which has exactly one occurrence of $01$ (colored red).

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of testcases. The description of the $T$ testcases follow.
- Each testcase consists of two lines.
- The first line contains a single integer $N$, the length of the string $S$.
- The second line contains a binary string of length $N$.

---

## Output Format

- For each testcase, print in a single line, an integer — the answer as per the problem statement.

---

## Constraints

- $1 \leq T \leq 4000$
- $1 \leq |S| \leq 10^5$
- The sum of $|S|$ over all testcases doesn't exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5
00100
5
01010
5
10001
```

**Output**

```text
1
2
2
```

**Explanation**

**Test case $1$:** The only strings that can be obtained by performing the given operations are $\{10000, 00100, 00001\}$. Of these the two strings $0{\color{red}{01}}00$ and $000{\color{red}{01}}$ contain exactly one occurrence of $01$.

**Test case $2$:** The given string $S$ cannot be changed by performing the given operation and contains $2$ occurrences of the string $01$, i.e. ${\color{red}01}{\color{blue}01}0$.

**Test case $3$:** The only strings that can be obtained by performing the given operations are $\{00101, 10001, 10100\}$. The string $0{\color{red}{01}}{\color{blue}{01}}$ contains two occurrences of $01$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
00100
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5
01010
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
10001
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

[Contest Division 1](https://www.codechef.com/MARCH222A/problems/MAX01EVSWP)

[Contest Division 2](https://www.codechef.com/MARCH222B/problems/MAX01EVSWP)

[Contest Division 3](https://www.codechef.com/MARCH222C/problems/MAX01EVSWP)

[Contest Division 4](https://www.codechef.com/MARCH222D/problems/MAX01EVSWP)

Setter: [ Srikkanth R](https://www.codechef.com/users/srikkanth_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given a binary string S of length N (i.e. every character of S is either 0 or 1).

You can perform the following operation on S:

- select any two indices i, j of the same parity, i.e. either both i, j are odd or both i, j are even

- swap S_i and S_j

For example, in the string 1110, we can swap the second and the fourth characters to get 1011. However, we can never obtain 1101 from 1110 by performing such swaps.

Find the maximum possible number of occurrences of the string 01 as a [substring](https://en.wikipedia.org/wiki/Substring) of S after performing the above operation any number of times (it is also allowed to not perform any operation).

For example, the string 1110 has no occurrence of the string 01 as a substring, whereas we can swap the second and fourth characters to obtain 1{\color{red}{01}}1 which has exactly one occurrence of 01 (colored red).

#
[](#explanation-5)EXPLANATION:

We will use 1-based indexing in the discussion of this problem.

Realizing the operation on S.

Because we can swap any two indices that are of same parity, we can rearrange the characters that occurs at odd indices in whichever way we want. Similarly, we can  rearrange the characters occurring at even indices in whichever way we want.

Can we categorize the substring 01 in some groups to make our problem easier?

Let us look at the index from which a substring starts. That index can either be even, or it can be odd. Let us try to find out the maximum number of substrings that starts at odd -index, and maximum number of substrings that starts at even-index.

Also, note that if a substring 01 starts at index i, then we cannot have this substring starting at index i+1 (as the (i+1)^{th} character would be 1)

What is the maximum number of subtring 01 that can start at an odd-index.

First of all, let us try to find out the maximum number of substring 01 that can start at an odd-index in any arbitrary string S.

Let N denotes the length of string S. If N is even, i.e. N = 2 \cdot K for some K \gt 0, then there are K odd indices, and each odd index is followed by an even index. So in this case, we can have at most K occurrences of 01 that starts at an odd-index in S. This happens when S is of form 01010101. If N is odd, i.e. N = 2 \cdot K + 1 for some K \gt 0, then there are K+1 odd indices. However, the last odd index is not followed by an even index, hence we can have at most K occurrences of 01 that starts at an odd-index in S.

**But how to get the answer when we are given a fixed string S?**

Note that for a substring 01 to start at an odd-index, 0 must occur at the odd index, followed by 1 at the even index. Let oddCnt_0 denotes the number of 0s that occurs at odd-indices in string S. Similarly, we have oddCnt_1, evenCnt_0 and evenCnt_1.

So the maximum number of 01 that can start at odd-index is val_1 = min(oddCnt_0, evenCnt_1). We can do so greedily by having val_1 zeroes at the starting odd-indices, and val_1 ones at the starting even-indices.

What are the remaining number of even-indices from which the substring can start?

As discussed earlier, N can either be 2 \cdot K or 2 \cdot K + 1 for some K \gt 0. In both the cases, we have total K even indices. We have already used val_1 even indices, and that leaves us with K - val_1 even indices.

If N = 2\cdot K, then the last even index is not followed by an odd-index. In other words, we cannot have our substring 01 to start at that index. This leaves us K - val_1 - 1 valid even indices if K - val_1 \gt 0. In simpler terms, we have valid = max(0, K - val_1 - 1) valid even indices.

If N = 2 \cdot K + 1, then we have valid = K - val_1 valid even indices.

What is the maximum number of subtring 01 that can start at an even-index.

Similar to what we discussed in the odd case, we need 0s at even indices, and 1s at odd indices. So the maximum possible number of subtrings will be val_2 = min(oddCnt_1, evenCnt_0). However, this is constrained by the number of valid even indices.

So the final answer in this case will be min(valid, val_2).

The final answer

So we have got the answers for odd and even indices. We can directly add them to get our final answer. Hence, ans = val_1 + min(valid, val_2) is our final answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
#define pll pair<ll ,ll>
#define pub push_back
using namespace std ;

void solve()
{
    ll n ;
    cin >> n ;
    string str ;
    cin >> str ;

    ll cnt[2][2] ;
    for(int i = 0 ; i < 2 ; i++)
        for(int j = 0 ; j < 2 ; j++)
            cnt[i][j] = 0 ;

    for(int i = 0 ; i < n ; i++)
    {
        cnt[(i+1)%2][str[i] - '0']++ ;
    }

    ll len = n/2 ;
    ll val1 = min(cnt[1][0] , cnt[0][1]) ;
    ll ans = val1 ;

    if(n%2 == 0)
    {
        ans += max((ll)0 , min(len - val1 - 1, min(cnt[0][0] , cnt[1][1]))) ;
    }
    else
        ans += min(len - val1, min(cnt[0][0] , cnt[1][1])) ;

    cout << ans << endl ;
    return ;

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t ;
    cin >> t ;
    while(t--)
    {
        solve() ;
    }

    return 0;
}
``

</details>
