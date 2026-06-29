# Balanced Suffix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BALSUFF |
| Difficulty Rating | 2447 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [BALSUFF](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/BALSUFF) |

---

## Problem Statement

You're given a string $S$ of length $N$ and an integer $K$.

Let $C$ denote the **set** of all characters in $S$. The string $S$ is called *good* if, for **every** *suffix* of S:
- The difference between the frequencies of any two characters in $C$ does not exceed $K$.
In particular, if the set $C$ has a single element, the string $S$ is *good*.

Find whether there exists a rearrangement of $S$ which is *good*.
If multiple such rearrangements exist, print the **lexicographically smallest** rearrangement.
If no such rearrangement exists, print $-1$ instead.

Note that a suffix of a string is obtained by deleting some (possibly **zero**) characters from the beginning of the string. For example, the suffixes of $S = abca$ are $\{a, ca, bca, abca\}$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of the string and the positive integer as mentioned in the statement, respectively.
    - The next line consists of a string $S$ of length $N$ containing lowercase English alphabets only.

---

## Output Format

For each test case, output on a new line the lexicographically smallest *good* rearrangement of $S$.

If no such rearrangement exists, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq N$
- $S$ consists of lowercase english alphabets only.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3 1
aaa
4 2
baba
4 1
babb
7 2
abcbcac
```

**Output**

```text
aaa
aabb
-1
abcabcc
```

**Explanation**

**Test case $1$:** Since $C = \{a\}$, the string $S$ is *good*.

**Test case $2$:** The set $C = \{a, b\}$. Consider the rearrangement $aabb$. Let $f_a$ and $f_b$ denote the frequencies of $a$ and $b$ respectively:
- In suffix $b$, $f_b = 1$ and $f_a = 0$. Thus, $|f_b-f_a| = 1 \le K$.
- In suffix $bb$, $f_b = 2$ and $f_a = 0$. Thus, $|f_b-f_a| = 2 \le K$.
- In suffix $abb$, $f_b = 2$ and $f_a = 1$. Thus, $|f_b-f_a| = 1 \le K$.
- In suffix $aabb$, $f_b = 2$ and $f_a = 2$. Thus, $|f_b-f_a| = 0 \le K$.

Thus, the rearrangement $aabb$ is good. It is also the lexicographically smallest rearrangement possible of string $S$.

**Test case $3$:** It can be proven that there exists no rearrangement of $S$ which is *good*.

**Test case $4$:** The set $C = \{a, b, c\}$. Consider the rearrangement $abcabcc$. Let $f_a, f_b,$ and $f_c$ denote the frequencies of $a, b,$ and $c$ respectively:
- In suffix $c$, $f_a = 0, f_b = 0, $ and $f_c = 1$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $cc$, $f_a = 0, f_b = 0, $ and $f_c = 2$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $bcc$, $f_a = 0, f_b = 1, $ and $f_c = 2$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $abcc$, $f_a = 1, f_b = 1, $ and $f_c = 2$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $cabcc$, $f_a = 1, f_b = 1, $ and $f_c = 3$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $bcabcc$, $f_a = 1, f_b = 2, $ and $f_c = 3$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $abcabcc$, $f_a = 2, f_b = 2, $ and $f_c = 3$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.

Thus, the rearrangement $abcabcc$ is good. It is also the lexicographically smallest *good* rearrangement of string $S$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
aaa
```

**Output for this case**

```text
aaa
```



#### Test case 2

**Input for this case**

```text
4 2
baba
```

**Output for this case**

```text
aabb
```



#### Test case 3

**Input for this case**

```text
4 1
babb
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
7 2
abcbcac
```

**Output for this case**

```text
abcabcc
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BALSUFF)

[Contest: Division 1](https://www.codechef.com/START78A/problems/BALSUFF)

[Contest: Division 2](https://www.codechef.com/START78B/problems/BALSUFF)

[Contest: Division 3](https://www.codechef.com/START78C/problems/BALSUFF)

[Contest: Division 4](https://www.codechef.com/START78D/problems/BALSUFF)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Greedy algorithms

#
[](#problem-4)PROBLEM:

A string S is called good if, for every suffix T of S and characters c_1, c_2 that occur in S, the frequencies of c_1 in T and c_2 in T differ by at most K.

Given S, find its lexicographically smallest good rearrangement.

#
[](#explanation-5)EXPLANATION:

Let’s first figure out when exactly a string S has a good rearrangement.

We’ll call a suffix that satisfies the given condition *balanced*.

Let c_1 and c_2 be some two characters that occur in S, and f_{c_1} and f_{c_2} be their respective frequencies.

If S is to be good, clearly |f_{c_1} - f_{c_2}| \leq K must hold; otherwise the string itself is not balanced, no matter how we rearrange it.

In fact, this condition is also sufficient for S to have a good rearrangement, i.e, |f_{c_1}-f_{c_2}| \leq K for every pair of characters c_1, c_2 in S.

Proof

We can construct a good rearrangement greedily.

Suppose we have N characters, such that |f_{c_1}-f_{c_2}| \leq K for every pair of them.

Construct a string as follows:

- Let c be a character with maximum frequency. Place one occurrence of c, and decrement f_c by 1.

It’s easy to see that this preserves the condition |f_{c_1}-f_{c_2}| \leq K, and so we can place all N characters.

Further, the string we construct is good, since at each step the suffix we create is balanced.

Notice that instead of checking every difference, it’s enough to check if the maximum difference satisfies the condition.

That is, a string has a good rearrangement if and only if the difference between its maximum and minimum frequency characters is \leq K.

Now that we know how to check whether S has a good rearrangement, we need to figure out how to construct the lexicographically smallest one.

Constructing lexicographically smallest objects usually involves doing so greedily, and this task is no different.

For each i from 1 to N, let’s greedily try to place the characters \text{'a', 'b', 'c', \ldots, 'z'} in order. As soon as one of them can be placed, do so and go to the next index.

To check whether placing a certain character is possible, we need to check if the suffix of the string starting from i+1 has a good rearrangement or not.

However, we have a pretty simple condition for this: the difference between the maximum and minimum frequencies of the remaining characters should be \leq K.

We know which characters we’ve placed so far, so we also know the frequencies of the remaining characters.

So, we can check this condition in \mathcal{O}(\Sigma) by just directly computing the maximum and minimum frequency, where \Sigma is the alphabet size (here, \Sigma = 26).

For each position, we try (at most) 26 possibilities, and process each in \mathcal{O}(26).

So, our solution runs in \mathcal{O}(26^2 \cdot N), which is fast enough.

It’s possible but unnecessary to make it run in \mathcal{O}(26\cdot N) with some minor optimizations.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(26\cdot N) per test case.

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

bool check(unordered_map<int, int>& freq, int k){
    int max_freq = 0;
    int min_freq = 1e9;
    for(auto it: freq){
        max_freq = max(max_freq, it.second);
        min_freq = min(min_freq, it.second);
    }
    return (max_freq - min_freq) <= k;
}

string solution(string s, int k){
    string ans = "";
    unordered_map<int, int> freq;
    for(int i = 0; i < s.size(); i++){
        freq[s[i] - 'a']++;
    }
    if(!check(freq, k)){
        return "-1";
    }
    for(int i = 0; i<s.length(); i++){
        bool flag = false;
        for(int j = 0; j < 26; j++){
            if(freq.find(j)!=freq.end() && freq[j] > 0){
                freq[j]--;
                if(check(freq, k)){
                    ans += (char)(j + 'a');
                    flag = true;
                    break;
                }
                freq[j]++;
            }
        }
        if(!flag){
            return "-1";
        }
    }
    string t = s;
    sort(all(t));
    if(t == ans){
        cerr << 1 << endl;
    }
    return ans;
}

int sumN = 0;

void solve()
{
    int n = readInt(1, 100000, ' ');
    int k = readInt(1, n, '\n');
    sumN += n;
    string s = readStringLn(1, n);
    cout << solution(s, k) << '\n';
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
    }
    assert(getchar()==-1);
    cerr << sumN << '\n';
    assert(sumN <= 200000);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    int nextDelimiter() {
        int now = pos;
        while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
            now++;
        }
        return now;
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        int nxt = nextDelimiter();
        string res;
        while (pos < nxt) {
            res += buffer[pos];
            pos++;
        }
        // cerr << res << endl;
        return res;
    }

    string readString(int minl, int maxl, const string &pattern = "") {
        assert(minl <= maxl);
        string res = readOne();
        assert(minl <= (int) res.size());
        assert((int) res.size() <= maxl);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int minv, int maxv) {
        assert(minv <= maxv);
        int res = stoi(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    long long readLong(long long minv, long long maxv) {
        assert(minv <= maxv);
        long long res = stoll(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    input_checker in;
    int tt = in.readInt(1, 2000);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 1e5);
        in.readSpace();
        int k = in.readInt(1, n);
        in.readEoln();
        string s = in.readString(n, n, in.lower);
        in.readEoln();
        map<char, int> cnt;
        for (int i = 0; i < n; i++) {
            cnt[s[i]]++;
        }
        int mx = -1, mn = n + 1;
        for (auto p : cnt) {
            mx = max(mx, p.second);
            mn = min(mn, p.second);
        }
        if (mx - mn > k) {
            cout << -1 << '\n';
            continue;
        }
        string ans(n, '?');
        for (int i = 0; i < n; i++) {
            for (char c = 'a'; c <= 'z'; c++) {
                if (!cnt.count(c) || cnt[c] == 0) {
                    assert(c != 'z');
                    continue;
                }
                cnt[c]--;
                int ok = 1;
                for (auto p : cnt) {
                    if (p.first != c && abs(p.second - cnt[c]) > k) {
                        ok = 0;
                        break;
                    }
                }
                if (ok) {
                    ans[i] = c;
                    break;
                } else {
                    assert(c != 'z');
                    cnt[c]++;
                }
            }
        }
        cout << ans << '\n';
    }
    assert(sn <= 2e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n, k = map(int, input().split())
	freq = {}
	for c in input():
		if c in freq: freq[c] += 1
		else: freq[c] = 1
	if max(freq.values()) - min(freq.values()) > k:
		print(-1)
		continue
	ans = ''
	alpha = sorted(freq.keys())
	for i in range(n):
		for c in alpha:
			if freq[c] == 0: continue
			freq[c] -= 1
			if max(freq.values()) - min(freq.values()) <= k:
				ans += c
				break
			freq[c] += 1
	print(ans)
``

</details>
