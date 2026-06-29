# Boring String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BORSTR |
| Difficulty Rating | 1566 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [BORSTR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/BORSTR) |

---

## Problem Statement

A string is called *boring* if all the characters of the string are **same**.

You are given a string $S$ of length $N$, consisting of lowercase english alphabets. Find the length of the longest *boring* substring of $S$ which occurs **more than once**.

Note that if there is no *boring* substring which occurs more than once in $S$, the answer will be $0$.

A substring is obtained by deleting some (possibly zero) elements from the beginning of the string and some (possibly zero) elements from the end of the string.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$, denoting the length of string $S$.
    - The next contains string $S$.

---

## Output Format

For each test case, output on a new line, the length of the longest *boring* substring of $S$ which occurs **more than once**.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \lt N \leq 2\cdot 10^5$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.
- $S$ consists of lowercase english alphabets.

---

## Examples

**Example 1**

**Input**

```text
4
3
aaa
3
abc
5
bcaca
6
caabaa
```

**Output**

```text
2
0
1
2
```

**Explanation**

**Test case $1$:** The length of the longest *boring* substring that occurs more than once is $2$. The *boring* substring of length $2$ occurring more than once is `aa`.

**Test case $2$:** There is no *boring* substring which occurs more than once. Thus, the answer is $0$.

**Test case $3$:** The length of the longest *boring* substring that occurs more than once is $1$. Some *boring* substrings of length $1$ occurring more than once are `c` and `a`.

**Test case $4$:** The length of the longest *boring* substring that occurs more than once is $2$. The *boring* substring of length $2$ occurring more than once is `aa`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
aaa
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
abc
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5
bcaca
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
6
caabaa
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

[Practice](https://www.codechef.com/problems/BORSTR)

[Contest: Division 1](https://www.codechef.com/START68A/problems/BORSTR)

[Contest: Division 2](https://www.codechef.com/START68B/problems/BORSTR)

[Contest: Division 3](https://www.codechef.com/START68C/problems/BORSTR)

[Contest: Division 4](https://www.codechef.com/START68D/problems/BORSTR)

***Author:*** [inov_360](https://www.codechef.com/users/inov_360)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1566

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A string is called *boring* if all its characters are the same.

Given a string S, find the longest boring substring of S that appears more than once.

#
[](#explanation-5)EXPLANATION:

First, note that boring substrings corresponding to different characters are independent.

So, let’s fix a character, say c, and compute the longest boring substring consisting of c that appears more than once. We can then repeat this for every letter and take the maximum across all answers.

Solving this problem hinges on a single major observation:

Suppose S has a boring substring of length k. S then contains **two** boring substrings of length k-1: the first k-1 and the last k-1 characters of the substring.

So, let’s fix a character c and compute the longest boring substring of S consisting of c.

This is fairly easy to do in \mathcal{O}(N) by just iterating across the string and maintaining the current length of the boring substring: increase it by 1 when you encounter a c and reset it to zero otherwise.

Let this length we compute be k. Then,

- If there are two separate boring substrings of length k, the answer for c is k

- Otherwise, the answer for c is k-1.

All that remains is to check the first condition. This is fairly easy to do: for example, when computing k, keep a second variable that counts the number of occurrences of k and update it each time you update k.

The above approach is \mathcal{O}(26N), but it’s not hard (though also unnecessary) to optimize it to \mathcal{O}(N) by solving for all characters simultaneously.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ll long long
#define db double
#define el "\n"
#define ld long double
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)
#define all(ds) ds.begin(), ds.end()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef vector< long long > vi;
typedef pair<long long, long long> ii;
typedef priority_queue <ll> pq;
#define o_set tree<ll, null_type,less<ll>, rb_tree_tag,tree_order_statistics_node_update>

const ll mod = 1000000007;
const ll INF = (ll)1e18;
const ll MAXN = 1000006;

ll po(ll x, ll n){
    ll ans=1;
    while(n>0){ if(n&1) ans=(ans*x)%mod; x=(x*x)%mod; n/=2;}
    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T=1;
    cin >> T;
    while(T--){
        int n;
        cin>>n;

        string s;
        cin>>s;

        assert(s.length()==n);
        for(auto h:s){
            assert(h>='a' && h<='z');
        }

        vector<int>len(26, 0);
        vector<int>cnt(26, 0);

        int curr = 1;

        rep_a(i,1,n+1){
            if(s[i]!=s[i-1] || i==n+1){
                int id = (int)(s[i-1]-'a');
                if(curr>len[id]){
                    len[id]=curr;
                    cnt[id]=1;
                }
                else if(curr==len[id]){
                    cnt[id]++;
                }
                curr=1;
            }
            else curr++;
        }

        int mx = 0, id, ans;
        rep(i,26){
            if(len[i]>mx){
                mx = len[i];
                if(cnt[i]>1){
                    ans = len[i];
                }
                else{
                    ans = len[i]-1;
                    mx--;
                }
            }
        }

        cout<<ans<<el;

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>

using namespace std;

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
    input_checker in;
    int tt = in.readInt(1, 1000);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 2e5);
        in.readEoln();
        sn += n;
        string s = in.readString(n, n, in.lower);
        in.readEoln();
        vector<vector<int>> c(26);
        for (int i = 0, j = 0; i < n; i = j) {
            while (j < n && s[i] == s[j]) {
                j++;
            }
            c[s[i] - 'a'].emplace_back(j - i);
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            sort(c[i].rbegin(), c[i].rend());
            if (c[i].size() >= 1) {
                ans = max(ans, c[i][0] - 1);
            }
            if (c[i].size() >= 2) {
                ans = max(ans, c[i][1]);
            }
        }
        cout << ans << '\n';
    }
    assert(sn <= 5e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    mx = [[0, 0] for _ in range(26)]
    curch, curlen = s[0], 0
    for i in range(n):
        if s[i] == curch: curlen += 1
        if i == n-1 or s[i] != s[i+1]:
            pos = ord(curch) - ord('a')
            if curlen > mx[pos][0]:
                mx[pos] = [curlen, 0]
            if curlen == mx[pos][0]: mx[pos][1] += 1
            if i < n-1: curch, curlen = s[i+1], 0
    ans = 0
    for i in range(26):
        if mx[i][1] > 1: ans = max(ans, mx[i][0])
        else: ans = max(ans, mx[i][0] - 1)
    print(ans)
``

</details>
