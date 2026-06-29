# Search for 404

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CS2023_404 |
| Difficulty Rating | 2296 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CS2023_404](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CS2023_404) |

---

## Problem Statement

Om has a string $S$ consisting of characters $*$, $4$, and $0$ only.
- The character $*$ can be replaced by either $4$ or $0$.

Om wants to count the total number of [subsequences](https://en.wikipedia.org/wiki/Subsequence) of $404$ present in all the possible strings generated after replacing $*$.
As the number can be huge, you must output the number modulo $10^{9}+7$.

For example, if the given string is $S =$ $4*4*$, the possible strings after replacing $*$ are:
- $4040$: Only one subsequence of $404$ is present, that is $S_1S_2S_3$.
- $4044$: Two subsequences of $404$ are present, that are $S_1S_2S_3$ and $S_1S_2S_4$.
- $4440$: No subsequence of $404$ is present.
- $4444$: No subsequence of $404$ is present.

Thus, total number of $404$ subsequences present in all possible generated strings is $3$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — size of the given string.
    - The second line has a string $S$ of size $N$.

---

## Output Format

For each test case, output the total number of subsequences of $404$ present in all the possible strings generated after replacing $*$.
As the number can be huge, you must output the number modulo $10^{9}+7$.

---

## Constraints

- $1 \leq T \leq 10^{5}$
- $1 \leq N \leq 10^{5}$
- $S$ consists of $*, 4,$ and $0$ only.
- The sum of $N$ over all test cases won't exceed $10^{6}$.

---

## Examples

**Example 1**

**Input**

```text
2
4
4*04
4
4*4*
```

**Output**

```text
4
3
```

**Explanation**

**Test case $1$:** All possible generated strings of $4*04$ are:
- $4004$: Two subsequences of $404$ are present, that are $S_1S_2S_4$ and $S_1S_3S_4$.
- $4404$: Two subsequences of $404$ are present, that are $S_1S_3S_4$ and $S_2S_3S_4$.

Thus, the total number of $404$ subsequences present in all possible generated strings is $4$.

**Test case $2$:** Already explained in problem statement.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4*04
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4
4*4*
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

[Practice](https://www.codechef.com/problems/CS2023_404)

[Contest: Division 1](https://www.codechef.com/START94A/problems/CS2023_404)

[Contest: Division 2](https://www.codechef.com/START94B/problems/CS2023_404)

[Contest: Division 3](https://www.codechef.com/START94C/problems/CS2023_404)

[Contest: Division 4](https://www.codechef.com/START94D/problems/CS2023_404)

***Author:*** [himanshu154](https://www.codechef.com/users/himanshu154)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Math or dynamic programming

#
[](#problem-4)PROBLEM:

You’re given a string S containing the characters `4, 0, *` only.

Each `*` can be replaced with either `0` or `4`.

Find the number of times `404` appears as a subsequence of S, across all possible replacements.

#
[](#explanation-5)EXPLANATION:

There are two different ways to solve this problem: either somewhat directly using math, or using dynamic programming.

Solution 1 (Math)

Let’s start with a slow solution first.

Instead of fixing a way of replacing the `*`s and counting the number of `404` subsequences, let’s instead fix a `404` subsequence and figure out the number of replacements it occurs in.

So, suppose we fix indices i \lt j \lt k to form the `404` subsequence. Then,

- Each of S_i and S_k should be either `4` or `*`.

Further, if they’re `*`, their replacement is unique (since we want them to be `4`).

- Similarly, S_j should be either `0` or `*`, and if it is `*` its replacement is unique.

- If the above conditions are satisfied, then any `*` that’s not at positions i, j, k can be freely replaced by either `0` or `4`.

So, if there are m such indices, the count is 2^m.

Doing this for each (i, j, k) triplet gives us a solution in \mathcal{O}(N^3).

To optimize this, let’s try to only fix the position of j, i.e, where the `0` in the `404` subsequence will be.

For this, we can choose any position such that S_j is either `0` or `*`.

Let the remaining number of `*`s be m.

Once `0` is fixed, let’s try to fix i and k, i.e, the `4`s.

There are four options here:

-
**Case 1:** We can choose a `4` before j and a `4` after j.

For any such choice, the number of valid replacements is 2^{m}.

The number of such choices equals the number of `4`s before j, multiplied by the number of `4`s after j.

-
**Case 2:** We can choose a `4` before j and a `*` after j; and replace the `*` with `4`.

The number of valid replacements is now 2^{m-1}, since we used up one `*`.

The number of such choices equals the number of `4`s before j, multiplied by the number of `*`s after j.

-
**Case 3:** Choose a `*` before j and a `4` after j.

This is symmetric to case 2, just with ‘before’ and ‘after’ swapped.

-
**Case 4:** Choose a `*` before j and a `*` after j.

Here, there are 2^{m-2} valid replacements.

Notice that each case can be calculated in \mathcal{O}(1) time if we know the number of `4`s before/after index j, and the number of `*`s before/after index j.

These counts are easy to find quickly: for example, you can precompute them using prefix or suffix sums; maintain them as you iterate; or even binary search on a list of positions.

In particular, each index can be processed in \mathcal{O}(1) or \mathcal{O}(\log N) time, which is fast enough.

Solution 2 (Dynamic programming)

Let \text{dp}[i][404] denote the number of occurrences of `404` as a subsequence of the first i characters, across all replacements of `*` in them.

Similarly define \text{dp}[i][40] and \text{dp}[i][4].

Then, we have the following transitions for each 1 \leq i \leq N.

- First, for each x \in  \{4, 40, 404\}, set \text{dp}[i][x] = \text{dp}[i-1][x].

This is because existing instances of each subsequence will continue to exist.

Now, let’s look at new instances of each one we can create using the i-th character.

- If S_i is `4`, then:

- Add 2^m to \text{dp}[i][4], where m is the number of `*` before index i.

This is because the `4` at this index will contribute one occurrence for every possible replacement so far, and there are 2^m such replacements.

- Add \text{dp}[i-1][40] to \text{dp}[i][404].

This is because we can create a new instance of `404` from a previously existing instance of `40`.

- If S_i is `0`, add \text{dp}[i-1][4] to \text{dp}[i][40].

This is because we can create a new instance of `40` from an already existing instance of `4`.

- If S_i is `*`, perform both transitions.

Note that in this case, you should initially set \text{dp}[i][x] = 2\cdot \text{dp}[i-1][x]; once for each replacement.

The final answer is \text{dp}[N][404].

For ease of implementation, the states can be renamed into \text{dp}[i][0], \text{dp}[i][1], \text{dp}[i][2] corresponding to 4, 40, 404 respectively.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Author's code (C++ - Math)
``#include <bits/stdc++.h>
using namespace std;
#define int long long int
#define vi vector<int>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define all(a) a.begin(),a.end()
#define endl "\n"

int mod=1e9+7;
int _pow(int a,int p=mod-2){
	if(p<0) return 0;
	int res=1;
	while(p>0){
		if(p&1) res=(res*a)%mod;
		p=p>>1; a=(a*a)%mod;
	}
	return res;
}
void solve(){
	int n;
    cin>>n;
	string str;
	cin>>str;
 	int ls=0,l4=0,l0=0;
	int rs=0,r4=0,r0=0;
	rep(i,0,n){
		rs+=str[i]=='*';
		r4+=str[i]=='4';
		r0+=str[i]=='0';
	}
	int ans=0;
	rep(i,0,n){
		rs-=(str[i]=='*');
		r4-=(str[i]=='4');
		r0-=(str[i]=='0');

		if(str[i]=='0' || str[i]=='*'){
			//4 0 4
			ans+=(l4*r4)%mod*_pow(2,rs+ls);
			ans%=mod;

			//4 0 *
			ans+=(l4*rs)%mod*_pow(2,rs+ls-1);
			ans%=mod;

			//* 0 4
			ans+=(ls*r4)%mod*_pow(2,rs+ls-1);
			ans%=mod;

			//* 0 *
			ans+=(ls*rs)%mod*_pow(2,rs+ls-2);
			ans%=mod;
		}
		ls+=str[i]=='*';
		l4+=str[i]=='4';
		l0+=str[i]=='0';
	}
	cout<<ans<<endl;
}
int32_t main() {
    auto begin = std::chrono::high_resolution_clock::now();
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	#ifndef ONLINE_JUDGE
	freopen("D:/Desktop/Test_CPP/CS2023_404/CS2023_404_0.in", "r", stdin);
	freopen("D:/Desktop/Test_CPP/CS2023_404/CS2023_404_0.out", "w", stdout);
	#endif

    int t=1;
	cin>>t;
	while(t--)
        solve();

	auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-6 << "ms\n";
	return 0;
}
``

Tester's code (C++ - Math)
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

int power(int a,int b)
{
    if(b==0)
        return 1;
    else
    {
        int x=power(a,b/2);
        int y=(x*x)%MOD;
        if(b%2)
            y=(y*a)%MOD;
        return y;
    }
}

void solve(int tc)
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    int a=0,b=0,c=0,star=0;
    for(int i=0;i<n;i++)
    {
        if(s[i]=='4')
        {
            c=(c+b)%MOD;
            a=(a+power(2,star))%MOD;
        }
        else if(s[i]=='0')
        {
            b=(b+a)%MOD;
        }
        else
        {
            c=(2*c+b)%MOD;
            b=(2*b+a)%MOD;
            a=(2*a+power(2,star))%MOD;
            star++;
        }
    }
    cout << c << '\n';
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

Editorialist's code (Python - Math)
``mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    s = input()
    pref_fours, suf_fours = 0, s.count('4')
    pref_free, suf_free = 0, s.count('*')

    ans = 0
    for c in s:
        if c == '4':
            pref_fours += 1
            suf_fours -= 1
        else:
            if c == '*': suf_free -= 1

            ans += pref_fours * suf_fours * pow(2, pref_free + suf_free, mod)
            if pref_free + suf_free > 0:
                ans += pref_free * suf_fours * pow(2, pref_free + suf_free - 1, mod)
                ans += pref_fours * suf_free * pow(2, pref_free + suf_free - 1, mod)
                if pref_free + suf_free > 1:
                    ans += pref_free * suf_free * pow(2, pref_free + suf_free - 2, mod)
            ans %= mod

            if c == '*': pref_free += 1
    print(ans)
``

Editorialist's code (Python - DP)
``mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    s = input()
    dp = [ [0, 0, 0] for _ in range(n+1)]
    pw = 1
    for i in range(n):
        if s[i] == '0':
            dp[i+1][0] = dp[i][0]
            dp[i+1][2] = dp[i][2]

            dp[i+1][1] = (dp[i][1] + dp[i][0])%mod
        elif s[i] == '4':
            dp[i+1][1] = dp[i][1]

            dp[i+1][2] = (dp[i][2] + dp[i][1])%mod
            dp[i+1][0] = (dp[i][0] + pw)%mod
        else:
            # Place a 0 here
            dp[i+1][0] = dp[i][0]
            dp[i+1][2] = dp[i][2]
            dp[i+1][1] = (dp[i][1] + dp[i][0])%mod

            # Place a 4 here
            dp[i+1][1] = (dp[i+1][1] + dp[i][1]) % mod
            dp[i+1][2] = (dp[i+1][2] + dp[i][2] + dp[i][1])%mod
            dp[i+1][0] = (dp[i+1][0] + dp[i][0] + pw) % mod

            pw = (2 * pw) % mod
    print(dp[n][2])
``

</details>
