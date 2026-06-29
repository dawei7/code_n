# Flip the Prefix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFIXFLIP |
| Difficulty Rating | 1758 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PREFIXFLIP](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PREFIXFLIP) |

---

## Problem Statement

You are given a **binary** string $S$ of length $N$ and an integer $K$. You can perform the following operation on the string:
- Select a *prefix* of the string $S$ and flip all the characters of the prefix. A flip corresponds to changing $0$ to $1$ and vice-versa.

Find the **minimum** number of operations required to obtain a substring of length $K$ such that all characters of the substring are $1$.

Note:
- A prefix is obtained by deleting some (possibly zero) characters from the end of the string.
- A substring is obtained by deleting some (possibly zero) characters from the beginning of the string and some (possibly zero) characters from the end of the string.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of the string and the length length of substring containing all $1$s we want to achieve.
    - The next line contains the binary string $S$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of operations required to obtain a substring of length $K$ such that all characters of the substring are $1$.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq K \le N \leq 3\cdot 10^5$
- $S$ consists of $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3 3
000
4 2
0110
5 3
10101
```

**Output**

```text
1
0
2
```

**Explanation**

**Test case $1$:** We need to obtain a substring containing three $1$s. Using one operation, we can select the prefix $S[1,3]$ and flip all the characters in the prefix. Thus, the string becomes $111$.

**Test case $2$:** The string already contains a substring having two $1$s. Thus, we do not need any operation.

**Test case $3$:** We need to obtain a substring containing three $1$s. We can do so using $2$ operations:
- Operation $1$: Select the prefix $S[1, 4]$ and flip all characters in the prefix. Thus, the string becomes $01011$.
- Operation $2$: Select the prefix $S[1, 3]$ and flip all characters in the prefix. Thus, the string becomes $10111$.

Thus, we have a substring $S[3,5]$ of length $3$ where all characters of the substring are $1$. It can be shown that we cannot obtain such substring using less than $2$ operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
000
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 2
0110
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5 3
10101
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

[Practice](https://www.codechef.com/problems/PREFIXFLIP)

[Contest: Division 1](https://www.codechef.com/START71A/problems/PREFIXFLIP)

[Contest: Division 2](https://www.codechef.com/START71B/problems/PREFIXFLIP)

[Contest: Division 3](https://www.codechef.com/START71C/problems/PREFIXFLIP)

[Contest: Division 4](https://www.codechef.com/START71D/problems/PREFIXFLIP)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1758

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a binary string S, in one move you can flip (i.e, convert 0\to 1 and 1\to 0) some prefix of S.

Find the minimum number of flips to make S contain a substring of K ones.

#
[](#explanation-5)EXPLANATION:

Let’s fix a substring of length K and see how many moves we need to make it contain only ones.

Suppose the substring is A = A_LA_{L+1}\ldots A_R. Then,

- If A_i = 0, we need to flip a prefix that includes i an *odd* number of times.

- If A_i = 1, we need to flip a prefix that includes i an *even* number of times.

This should give you a greedy solution:

- If A_R = 1, then ignore it. Otherwise, flip the prefix [1, R].

- Then, repeat this with A_{R-1}, A_{R-2}, \ldots, A_L in order.

Analyzing this process, you’ll note that the number of flips is in fact determined exactly by the number of positions L \leq i \lt R such that A_i \neq A_{i+1}; in particular, if there are x such positions, then:

- If A_R = 0 then we need x+1 flips.

- If A_R = 1 then we need x flips.

Intuitively, we’re breaking the substring into contiguous ‘blocks’ of zeros and ones; after which each flip turns exactly one block into a block of ones.

This allows us to solve a single substring in \mathcal{O}(K). Repeating this for every substring will take \mathcal{O}(NK), which is too slow.

To improve this solution, notice that the answer for a substring is determined by exactly two things: the value of x (i.e, the number of adjacent pairs of unequal characters), and what the last character is.

So, suppose we know x for the substring starting at L. We can easily obtain it for the substring starting at L+1, since the only pairs that need to be looked at are (L, L+1) and (R, R+1) (here, R = L+K-1).

This allows us to move from one substring to the next in \mathcal{O}(1), giving us a solution in \mathcal{O}(N) overall.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdlib>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <cassert>
#define int long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;

const int N=500023;
bool vis[N];
vector <int> adj[N];
long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        if(g=='-'){
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g && g<='9'){
            x*=10;
            x+=g-'0';
            if(cnt==0){
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd){
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
        char g=getchar();
        assert(g!=-1);
        if(g==endd){
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt && cnt<=r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}

void solve()
{
    int n = readIntSp(1, 300000);
    int k = readIntLn(1, n);
    string s = readStringLn(1, n);
    int ans = n;
    int cnt = 0;
    for(int i = 0; i<k-1; i++){
        if(s[i] != s[i+1]){
            cnt++;
        }
    }
    if(s[k-1] == '0'){
        ans = min(ans, cnt + 1);
    }
    else{
        ans = min(ans, cnt);
    }
    for(int i = k-1; i<n-1; i++){
        if(s[i] != s[i+1]){
            cnt++;
        }
        if(s[i-k+1] != s[i-k+2]){
            cnt--;
        }
        if(s[i+1] == '0'){
            ans = min(ans, cnt + 1);
        }
        else{
            ans = min(ans, cnt);
        }
    }
    if(s[n-1] == '0'){
        ans = min(ans, cnt + 1);
    }
    else{
        ans = min(ans, cnt);
    }
    cout << ans;
}
int32_t main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,2000,'\n');
    while(T--){
        solve();
        cout<<'\n';
    }
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n, k = map(int, input().split())
	s = input()
	ans = n
	blocks = 1
	for i in range(1, k):
		blocks += s[i] != s[i-1]
	if s[k-1] == '1': ans = blocks-1
	else: ans = blocks
	for i in range(k, n):
		blocks += s[i] != s[i-1]
		blocks -= s[i-k] != s[i-k+1]
		if s[i] == '1': ans = min(ans, blocks-1)
		else: ans = min(ans, blocks)
	print(ans)
``

</details>
