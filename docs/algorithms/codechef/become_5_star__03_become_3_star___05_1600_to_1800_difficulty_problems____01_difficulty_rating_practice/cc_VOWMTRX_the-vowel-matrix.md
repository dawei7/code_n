# The Vowel Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VOWMTRX |
| Difficulty Rating | 1694 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [VOWMTRX](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/VOWMTRX) |

---

## Problem Statement

Welcome to The Mega City!

Neo finds himself in a high-stakes situation. He has a string $S$ of length $N$ and his task is to crack the string using the *vowel matrix*.
The vowel matrix is a unique cryptographic scheme where the string is sliced into multiple pieces, such that, each piece contains **exactly** $K$ vowels.

Determine the number of ways you can slice the string $S$ using *vowel matrix* scheme. Since the number can be huge, print it modulo $10^9+7$.

Note:
- The characters `a`, `e`, `i`, `o`, and `u` are considered vowels in lowercase english alphabets.
- It is **guaranteed** that $S$ contains at least one vowel and the number of vowels in $S$ is a multiple of $K$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$, the length of string and the number of vowels required in each piece of string.
    - The second line contains the string $S$, consisting of lowercase english letters.

---

## Output Format

For each test case, output on a single line, the number of ways you can slice the string $S$ using *vowel matrix* scheme. Since the number can be huge, print it modulo $10^9+7$.

---

## Constraints

- $1 \leq T \leq 10^{4}$
- $1 \leq N \leq 10^{6}$
- $1 \leq K \leq N$
- The sum of $N$ over all test cases won't exceed $10^{6}$.
- It is guaranteed that the number of vowels in $S$ is a multiple of $K$.

---

## Examples

**Example 1**

**Input**

```text
2 
3 1
neo
10 2
babylonian
```

**Output**

```text
1
2
```

**Explanation**

**Test case $1$:** There is only one possible way to slice the string such that all pieces have $1$ vowel each:
- `ne` $|$ `o`.

**Test case $2$:** There are two possible ways to slice the string such that all pieces have $2$ vowels each:
- `babylo` $|$ `nian`
- `babylon` $|$ `ian`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
neo
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
10 2
babylonian
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

[Practice](https://www.codechef.com/problems/CS2023_STK)

[Contest: Division 1](https://www.codechef.com/START94A/problems/CS2023_STK)

[Contest: Division 2](https://www.codechef.com/START94B/problems/CS2023_STK)

[Contest: Division 3](https://www.codechef.com/START94C/problems/CS2023_STK)

[Contest: Division 4](https://www.codechef.com/START94D/problems/CS2023_STK)

***Author:*** [starc15](https://www.codechef.com/users/starc15)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics

#
[](#problem-4)PROBLEM:

Given a string S of length N, find the number of ways of partitioning it into substrings such that each resulting substring has exactly k vowels.

#
[](#explanation-5)EXPLANATION:

Let \text{pos}_i denote the position of the i-th vowel in string S.

Let’s look at how we can partition S into substrings containing exactly k vowels.

- The first k vowels must be in the same substring; and this substring cannot include the (k+1)-th vowel.

So, the first ‘cut’ must be made after \text{pos}_k, but before \text{pos}_{k+1}.

There are \text{pos}_{k+1} - \text{pos}_k such choices.

- The next consecutive k vowels must be in the same substring.

By the same reasoning as above, the second cut must thus be made after \text{pos}_{2k}, but before \text{pos}_{2k+1}.

There are \text{pos}_{2k+1} - \text{pos}_{2k} choices here.

- More generally, it’s easy to see that for the i-th cut, there are \text{pos}_{ik+1} - \text{pos}_{ik} choices.

Finally, note that each cut is independent of the others.

So, the total number of ways is just the product of all these numbers.

In particular, if the string has x\cdot k vowels, we need exactly x-1 cuts to separate them.

So, the answer will be

\left( \text{pos}_{k+1} - \text{pos}_k \right) \cdot \left( \text{pos}_{2k+1} - \text{pos}_{2k} \right) \cdot \ldots \cdot \left( \text{pos}_{(x-1)k+1} - \text{pos}_{(x-1)k} \right)

The \text{pos}_i values can be computed by just iterating across the string, so this algorithm takes \mathcal{O}(N) time.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define ll long long int
const ll M=1e9+7;

int main() {
    ll t; cin>>t;
    map<char,ll>vow={{'a',1},{'e',1},{'i',1},{'o',1},{'u',1}};
    while(t--){
        ll n,k; cin>>n>>k;
        string s; cin>>s;
        ll ans=1;
        ll prev=-1;
        ll ct=0;
        for (int i = 0; i < n; ++i)
        {
            if(vow[s[i]]){
                if(ct==0){
                    if(prev!=-1){
                        ans=(ans*(i-prev))%M;
                    }
                }
                ct++;
                if(ct==k){
                    ct=0;
                    prev=i;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
``

Tester's code (C++)
``/*...................................................................*
 *............___..................___.....____...______......___....*
 *.../|....../...\........./|...../...\...|.............|..../...\...*
 *../.|...../.....\......./.|....|.....|..|.............|.../........*
 *....|....|.......|...../..|....|.....|..|............/...|.........*
 *....|....|.......|..../...|.....\___/...|___......../....|..___....*
 *....|....|.......|.../....|...../...\.......\....../.....|./...\...*
 *....|....|.......|../_____|__..|.....|.......|..../......|/.....\..*
 *....|.....\...../.........|....|.....|.......|.../........\...../..*
 *..__|__....\___/..........|.....\___/...\___/.../..........\___/...*
 *...................................................................*
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF 1000000000000000000
#define MOD 1000000007

void solve(int tc)
{
    int n,k;
    cin >> n >> k;
    string s;
    cin >> s;
    vector<int> idx;
    for(int i=0;i<n;i++)
    {
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
            idx.push_back(i);
    }
    int ans = 1;
    for(int i=k;i<idx.size();i+=k)
        ans = (ans*(idx[i]-idx[i-1]))%MOD;
    cout << ans << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc=1;
    cin >> tc;
    for(int ttc=1;ttc<=tc;ttc++)
        solve(ttc);
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans, vowels, curlen = 1, 0, 0
    for c in input():
        if c in 'aeiou':
            if vowels%k == 0 and vowels > 0:
                ans *= curlen
                ans %= mod
            curlen = 1
            vowels += 1
        else:
            curlen += 1
    print(ans)
``

</details>
