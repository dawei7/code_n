# Mex Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEX_ARRAY |
| Difficulty Rating | 1965 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [MEX_ARRAY](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/MEX_ARRAY) |

---

## Problem Statement

Given an array $A$ containing $N$ non-negative integers, you have to create a new array $B$ that is formed in the following way:

While $A$ is not empty:

1. Choose an integer $k$ ($1 \leq k \leq |A|$).
Here, $|A|$ denotes the current length of $A$.
2. Choose $k$ elements of $A$.
3. Append the MEX of these chosen elements to the end of array $B$, and erase them from the array $A$.

That is, in each move you pick a non-empty subsequence of $A$, append its MEX to $B$, and delete the subsequence from $A$.

Find the **lexicographically maximum** array $B$ that can be formed via this process.

**Notes:**
- An array $X$ is lexicographically greater than an array $Y$ if:
    - In the first position where $X$ and $Y$ differ, $X_i \gt Y_i$; or
    - $|X| > |Y|$ and $Y$ is a prefix of $X$.
- The MEX of a set of non-negative integers is the minimal non-negative integer that is not in the set.
For example, $\text{MEX}(\{1, 2, 3, 2\}) = 0$ and $\text{MEX}(\{0, 1, 2, 5, 4\}) = 3$.

---

## Input Format

- The first line of the input contains a single integer $T$ — the number of test cases. The description of test cases follows.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array $A$.
    - The second line of each test case contains $N$ space-separated non-negative integers $A_1, A_2, \ldots, A_N$, where $A_i$ is the $i$-th integer from the array $A$.

---

## Output Format

For each test case, print two lines.
- The first line should contain a single integer $M$ — the length of the lexicographically maximum array $B$ you can create.
- The second line should contain $M$ space-separated integers, denoting the elements of the array $B$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
- $ 0 \leq A_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
3
5
0 1 2 2 3
1
1
2 
0 0
```

**Output**

```text
2
4 0
1
0
2
1 1
```

**Explanation**

**Test case $1$:** Perform two moves as follows:
- First, choose the subsequence $\{0, 1, 2, 3\}$ from $A$, with a MEX of $4$.
Now, $B = [4]$ and $A = [2]$.
- Next, choose the only remaining subsequence $\{2\}$, with a MEX of $0$.
Now, $B = [4, 0]$ and $A$ is empty.

It can be seen that no larger array $B$ is possible.

**Test case $2$:** $A = [1]$, and our only choice is to have $B = [0]$.

**Test case $3$:** Choose the subsequence $\{0\}$ twice, each with a MEX of $1$, to obtain $B = [1, 1]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MEX_ARRAY)

[Contest: Division 1](https://www.codechef.com/START96A/problems/MEX_ARRAY)

[Contest: Division 2](https://www.codechef.com/START96B/problems/MEX_ARRAY)

[Contest: Division 3](https://www.codechef.com/START96C/problems/MEX_ARRAY)

[Contest: Division 4](https://www.codechef.com/START96D/problems/MEX_ARRAY)

***Author:*** [sho358](https://www.codechef.com/users/sho358)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1965

# [](#prerequisites-3)PREREQUISITES:

Frequency arrays

# [](#problem-4)PROBLEM:

You have an array A, and an initially empty array B.

You can perform the following operation:

- Pick a non-empty subsequence of A.

- Append the mex of this subsequence to B.

- Delete the subsequence from A.

Find the lexicographically maximum possible value of B.

# [](#explanation-5)EXPLANATION:

Lexicographic minimization/maximization problems often require us to make greedy choices; and this one is no different.

In order to obtain the lexicographically largest array, the first step is to extract the maximum possible mex we can.

That is, find the largest possible integer k such that all of 0, 1, 2, \ldots, k exist in the array; giving us a mex of k+1.

It’s easy to see that this process can just be repeated:

While the array has at least one element, find the largest possible mex; and delete one instance of every element less than this mex.

We only need to implement this to run quickly enough.

That can be done with the help of a frequency array.

Let \text{freq}[x] be the number of times x occurs in A.

Then, in each step we can do the following:

- Iterate k starting from 0. Stop when \text{freq}[k] = 0.

k is the largest mex we can obtain.

- If k \gt 0, reduce \text{freq}[x] by 1 for every 0 \leq x \lt k, to simulate deleting the subsequence \{0, 1, 2, \ldots, k-1\} from the array.

- Otherwise, k = 0; meaning that 0 is no longer present in the array.

This means all further mexes will only be 0.

So, if there are m elements remaining in the array, append 0 to B, m times; then break out since we’ve processed everything we can.

The complexity of this is in fact \mathcal{O}(N):

- Building the frequency array takes \mathcal{O}(N) time, obviously.

- Whenever we find a mex of k \gt 0, we iterated k+1 times (and deleted k elements) to do so.

This means the total sum of non-zero mexes we obtain cannot exceed N; meaning the total number of iterations is also \mathcal{O}(N).

- When k = 0, we append a bunch of elements to B and immediately broke out; obviously this is linear time as well.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h> //Andrei Alexandru a.k.a Sho
using ll=long long;
using ld=long double;
int const INF=1000000005;
ll const LINF=1000000000000000005;
ll const mod=1e9+7;
ld const PI=3.14159265359;
ll const NMAX=3e6+5;
ld const eps=0.0000001;
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define endl '\n'
#define CODE_START  ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
ll n,a[200005],cnt[200005],pref[200005];
void testcase(){
cin>>n;
for(ll i=1;i<=n;i++)
{
    cin>>a[i];
    cnt[a[i]]++;
}
pref[0]=cnt[0];
for(ll i=1;i<=n;i++)
{
    pref[i]=min(cnt[i],pref[i-1]);
}
vector<ll>v;
ll sum=0;
for(ll i=n;i>=0;i--){
    while(pref[i]-sum>=1){
        sum++;
        v.pb(i+1);
    }
    cnt[i]-=sum;
}
for(ll i=1;i<=n;i++)
{
    while(cnt[i]){
        v.pb(0);
        cnt[i]--;
    }
}
cout<<v.size()<<endl;
for(auto it : v){
    cout<<it<<' ';
}
cout<<endl;
for(ll i=0;i<=n;i++)
{
    cnt[i]=0;
    pref[i]=0;
}
}
int32_t main(){
CODE_START;
#ifdef LOCAL
freopen("input.in", "r", stdin);
#endif
ll t=1;
cin>>t;
while(t--){
    testcase();
}
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

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
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
    int tt = in.readInt(1, 100);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        cerr << tt << endl;
        int n = in.readInt(1, 2e5);
        in.readEoln();
        sn += n;
        cerr << tt << endl;
        auto a = in.readInts(n, 0, n);
        in.readEoln();
        vector<int> c(n + 1);
        for (int i = 0; i < n; i++) {
            c[a[i]]++;
        }
        vector<int> b;
        while (c[0] > 0) {
            b.emplace_back(0);
            for (int i = 0; i <= n; i++) {
                if (c[i] == 0) {
                    break;
                }
                c[i]--;
                b.back()++;
            }
        }
        for (int i = 1; i <= n; i++) {
            while (c[i] > 0) {
                c[i]--;
                b.emplace_back(0);
            }
        }
        int m = (int) b.size();
        cout << m << '\n';
        for (int i = 0; i < m; i++) {
            cout << b[i] << " \n"[i == m - 1];
        }
    }
    assert(sn <= (int) 2e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0]*(n+2)
    for x in a:
        freq[x] += 1
    ans = []
    for i in range(n):
        mex = 0
        while True:
            if freq[mex] == 0: break
            mex += 1
        if mex > 0:
            ans.append(mex)
            for x in range(mex): freq[x] -= 1
        else:
            for x in range(sum(freq)): ans.append(0)
            break
    print(len(ans))
    print(*ans)
``

</details>
