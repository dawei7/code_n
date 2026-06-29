# Unique xor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UNIQUEK |
| Difficulty Rating | 1955 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [UNIQUEK](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/UNIQUEK) |

---

## Problem Statement

Given a binary string $S$ of length $N$ and an integer $K$.
An operation on the string is defined as:

- Select two indices $i$ and $j$ $(i \neq j)$ such that  $i \ \% K$  is equal to $j \ \% K$;
- Set both $S_i$ and $S_j$ as $S_i\oplus S_j$, where $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

Determine the **minimum** number of operations required to obtain a string such that either all characters of the string are $0$ or all characters of the string are $1$.

Under the given constraints, it can be proven that the answer always exists.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two integer $N$ the length of the string and an integer $K$ separated by space.
    - The second line contains a binary string $S$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of operations required to obtain a string such that either all character of the string are $0$ or all characters of the string are $1$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $1 \leq K$ and $2K \leq N$
- $0 \leq S_i \leq 1$
- The sum of $N$ over all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
2 1
00
2 1
10
4 2
1100
```

**Output**

```text
0
1
2
```

**Explanation**

**Test case $1$:** Since the string already contains all zeros, we do not need to apply any operation.

**Test case $2$:** The given string is $S = 10$.
- Select $i = 1$ and $j = 2$ (since $i \ \% K = j \ \% K = 0$) and set $S_1$ and $S_2$ as $S_1\oplus S_2$ = $1$.

The string formed will be $11$ where all characters are $1$. The minimum number of operations required is $1$.

**Test case $3$:** The given string is $S = 1100$.
- Select $i = 1$ and $j = 3$ and set $S_1$ and $S_3$ as $S_1\oplus S_3$ = $1$. The string formed will be $1110$.
- Select $i = 2$ and $j = 4$ and set $S_2$ and $S_4$ as $S_2\oplus S_4$ = $1$. The string formed will be $1111$ where all characters are $1$.

The minimum number of operations required is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
00
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2 1
10
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4 2
1100
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/UNIQUEK)

[Contest: Division 1](https://www.codechef.com/START103A/problems/UNIQUEK)

[Contest: Division 2](https://www.codechef.com/START103B/problems/UNIQUEK)

[Contest: Division 3](https://www.codechef.com/START103C/problems/UNIQUEK)

[Contest: Division 4](https://www.codechef.com/START103D/problems/UNIQUEK)

***Author:*** [danishiitp_24](https://www.codechef.com/users/danishiitp_24)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given a binary string S and an integer K.

The following operation can be performed:

- Pick two indices i and j such that |i - j| is a multiple of K, and replace *both* S_i and S_j with S_i \oplus S_j

Find the minimum number of operations required to make all the characters of S the same.

# [](#explanation-5)EXPLANATION:

First, note that the condition that we can only choose indices with the same remainder modulo K essentially breaks the given string up into K smaller strings (one for each remainder) such that we can operate on any two elements of each string (in other words, each smaller string technically has K = 1).

Further, the condition 2K \leq N means that each smaller string has length at least 2.

We can either make all the characters of S, or we can make them all 1.

Let’s try both options, and take the minimum of them.

To do this, all that remains is to solve the problem for K = 1: that is, find the minimum number of moves to make a string all zeros (or all ones) when S_i and S_j can be replaced by S_i\oplus S_j for any two distinct indices i and j.

Making everything 0

Consider a string S, all of whose characters we want to make zero.

Note that:

- Operating on two zeros leaves them both unchanged.

- Operating on two ones makes them both into 0.

- Operating on a zero and a one turns them both into 1.

Clearly, we should do the second operation type as much as possible since that’s our only way of turning a 1 into a 0.

In particular, if there are an even number of ones, all of them can be turned into zeros by operating on them pairwise; requiring \frac{x}{2} operations for x ones.

If there are an odd number of ones, one will be left behind.

To get rid of it, we use the third operation on a 0 and a 1, after which we now have two ones and can turn both into zero.

So, if there are x ones in the string,

- If x is even, we need \frac{x}{2} moves.

- If x is odd, we need \left\lfloor \frac{x}{2} \right\rfloor + 2 moves.

Making everything 1

From the potential moves in the previous section, we see that the only way to turn a 0 into a 1 is to operate on a 0 and a 1, which turns a single 0 into a 1.

So, if there are x zeros, we need x moves to do so.

However, there’s one catch here: if there are no ones to begin with, we can’t perform this move!

If there are no ones, it’s impossible to make everything into 1; so we assign it a cost of \infty (in practice, some large number) instead.

Now we know the costs of turning each smaller string into all zeros or all ones.

Sum up the costs for zeros and ones; and print the minimum of them.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int k;
        cin>>k;
        string s;
        cin>>s;
        map< int,pair<int,int> > mp;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='1')
            mp[i%k].first++;
            else mp[i%k].second++;
        }
        bool canone=true;
        int ans1=0,ans0=0;
        for(auto i:mp){
            if(i.second.first==0)
            canone=false;
            int one=i.second.first;
            int zero=i.second.second;
            ans0+=one/2;
            if(one%2)
            ans0+=2;
            ans1+=zero;

        }

        int ans=INT_MAX;
        if(canone)
        ans=min(ans1,ans0);
        else ans=ans0;
        cout<<ans;
        cout<<"\n";
    }
	return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18
#define f first
#define s second

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

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

    auto readInts(int n, int minv, int maxv) {
        assert(n >= 0);
        vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = readInt(minv, maxv);
            if (i+1 < n) readSpace();
        }
        return v;
    }

    auto readLongs(int n, long long minv, long long maxv) {
        assert(n >= 0);
        vector<long long> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = readLong(minv, maxv);
            if (i+1 < n) readSpace();
        }
        return v;
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

input_checker inp;
int n, k;
int sum_n = 0;

void Solve()
{
    n = inp.readInt(1, (int)1e5); inp.readSpace();
    sum_n += n;
    k = inp.readInt(1, (n + 1) / 2); inp.readEoln();

    string s = inp.readString(n, n, "01");
    inp.readEoln();

    //convert all to 0, this takes ones / 2 or ones / 2 + 2
    //convert all to 1, this takes number of zeroes

    int ans = 0;
    for (auto x : s) if (x == '0') ans++;

    int tot = 0;

    for (int i = 0; i < k; i++){
        int cnt = 0;
        for (int j = i; j < n; j += k){
            if (s[j] == '1') cnt++;
        }

        if (cnt % 2 == 0) tot += cnt / 2;
        else tot += (cnt / 2) + 2;

        if (cnt == 0) ans = INF;
    }

    ans = min(ans, tot);

    cout << ans << "\n";
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;

    t = inp.readInt(1, (int)1e5);
    inp.readEoln();
   // cin >> t;
    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }

    inp.readEof();

    assert(sum_n <= (int)(1e6));

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ansz, anso = 0, 0

    for i in range(k):
        ones, zeros = 0, 0
        for j in range(i, n, k):
            ones += s[j] == '1'
            zeros += s[j] == '0'
        # convert to zeros
        ansz += ones//2
        if ones % 2 == 1: ansz += 2

        # convert to ones
        if ones == 0: anso += 10**9
        else: anso += zeros
    print(min(ansz, anso))
``

</details>
