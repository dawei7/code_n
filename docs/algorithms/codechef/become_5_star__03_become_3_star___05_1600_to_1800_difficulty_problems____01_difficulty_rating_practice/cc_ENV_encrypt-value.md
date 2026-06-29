# Encrypt Value

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ENV |
| Difficulty Rating | 1633 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [ENV](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/ENV) |

---

## Problem Statement

You are given an array $A$ containing $N$ integers.

Consider the following process:
- Let $S = 0$ initially.
- For each $i$ from $1$ to $N$ **in order**, update $S$ to either $(S+A_i)$ or $(S\times A_i)$.
That is, either add $A_i$ to $S$ or multiply $S$ by $A_i$.

Before performing the process, you're allowed to freely rearrange the elements of $A$ as you like.
If you choose the rearrangement of $A$ and the sequence of operations optimally, what's the **maximum** possible value of $S$ that you can obtain?

This maximum value can be very large, so print it modulo $10^9 + 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - the elements of the array.

---

## Output Format

For each test case, output on a new line the maximum possible value of $S$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
4
4 2 5 2
3
1 2 1
```

**Output**

```text
80
4
```

**Explanation**

**Test case $1$:** Choose the rearrangement $A = [2, 2, 5, 4]$. Then,
- Add $A_1 = 2$ to $S$. Now, $S = 2$.
- Add $A_2 = 2$ to $S$. Now, $S = 4$.
- Multiply $S$ by $A_3 = 5$. Now, $S = 20$.
- Multiply $S$ by $A_4 = 4$. Now, $S = 80$.

This is the maximum value that can be obtained.

**Test case $2$:** Choose any rearrangement and sum up all the numbers to get $1+1+2 = 4$.
This is the maximum value that can be obtained.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 2 5 2
```

**Output for this case**

```text
80
```



#### Test case 2

**Input for this case**

```text
3
1 2 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ENV)

[Contest: Division 1](https://www.codechef.com/START131A/problems/ENV)

[Contest: Division 2](https://www.codechef.com/START131B/problems/ENV)

[Contest: Division 3](https://www.codechef.com/START131C/problems/ENV)

[Contest: Division 4](https://www.codechef.com/START131D/problems/ENV)

***Author:*** [kingmessi](https://www.codechef.com/users/kingmessi)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given an array A, which you can rearrange as you like.

Then, do the following process:

- Let S = 0.

- For each i from 1 to N, either add A_i to S or multiply A_i by S.

Find the maximum possible value of S if you act optimally.

# [](#explanation-5)EXPLANATION:

Since we’re dealing with positive integers, and our aim is to get as large a value as possible, intuitively multiplication seems a lot more powerful than addition.

First, note that if we have both additions and multiplications, it’s always optimal to do the additions first.

Proof

This should be fairly easy to see.

For any three integers S, x, y (where S\geq 0 and x, y \geq 1), we have

(S+x)\cdot y \geq S\cdot y + x

(Note that in the LHS we added x first then multiplied by y, while in the RHS we multiplied y first then added x. This is fine, since we’re allowed to reorder elements).

Essentially, performing the multiplication later allows for it to amplify the value of whatever was added too, in addition to the initial value.

So, we start out with a score of 0, add some values from A, and then multiply everything else.

The question now is, when do we add, and when do we multiply?

Suppose our current score is S, and we’re looking at A_i.

We can get either S + A_i or S\cdot A_i.

Analyzing these, you can see that:

- If S \geq 2 and A_i \geq 2, it’s better to multiply and obtain S\cdot A_i.

- Otherwise, it’s better to add and obtain S + A_i.

In particular, if A_i = 1, it’s always better to add rather than multiply.

So, we can start off by setting S to be the sum of ones in the array, since as we noted it’s better to start off with the additions.

Then, there are three possibilities:

- If S \geq 2, every other A_i is also \geq 2, so as per our conclusion above we can simply multiply them all with S.

The answer is thus the sum of the ones, multiplied by the product of everything else.

- If S = 0, there are no ones in the array.

In this case, we must start off by adding something to S, and then every other action will be a multiplication.

Notice that the order doesn’t really matter here: the final value is simply the product of all the elements in the array.

- If S = 1, we must add a single value to S (after which S will exceed 2), and then multiply everything else to it.

In the last case, we only need to decide which element to add to S, in order to maximize the final value.

It can be seen that it’s optimal to choose the smallest possible value (which in this case is the second smallest element of the array, since 1 is the smallest).

Proof

Again, this can be proved with simple algebra.

Let x \lt y.

Then,

- Adding x and multiplying y gets us (1+x)\cdot y = y + xy.

- Adding y and multiplying x gets us (1+y)\cdot x = x + xy.

Since x \lt y, clearly the first option is superior.

So, in the third case of S = 1, simply add the second-smallest element to S, and then multiply everything else.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``//Har Har Mahadev
#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp>
#define ll long long
#define int long long
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)
#define repin rep(i,0,n)
#define di(a) int a;cin>>a;
#define precise(i) cout<<fixed<<setprecision(i)
#define vi vector<int>
#define si set<int>
#define mii map<int,int>
#define take(a,n) for(int j=0;j<n;j++) cin>>a[j];
#define give(a,n) for(int j=0;j<n;j++) cout<<a[j]<<' ';
#define vpii vector<pair<int,int>>
#define sis string s;
#define sin string s;cin>>s;
#define db double
#define be(x) x.begin(),x.end()
#define pii pair<int,int>
#define pb push_back
#define pob pop_back
#define ff first
#define ss second
#define lb lower_bound
#define ub upper_bound
#define bpc(x) __builtin_popcountll(x)
#define btz(x) __builtin_ctz(x)
using namespace std;

using namespace __gnu_pbds;

typedef tree<int, null_type, less<int>, rb_tree_tag,tree_order_statistics_node_update> ordered_set;
typedef tree<pair<int, int>, null_type,less<pair<int, int> >, rb_tree_tag,tree_order_statistics_node_update> ordered_multiset;

const long long INF=1e18;
const long long M=1e9+7;
const long long MM=998244353;

int power( int N, int M){
    int power = N, sum = 1;
    if(N == 0) sum = 0;
    while(M > 0){if((M & 1) == 1){sum *= power;}
    power = power * power;M = M >> 1;}
    return sum;
}

int smn = 0;

void solve()
{
    int n;
    cin >> n;
    assert(n >= 1);
    assert(n <= 2e5);
    smn += n;
    vi a(n);
    take(a,n);
    sort(be(a));
    repin{
        assert(a[i] >= 1);
        assert(a[i] <= 1e9);
    }
    if(n == 1){
    	cout << a[0] << "\n";return;
    }
    if(a[0] > 1){
    	int pr = 1;
    	for(auto x : a){
    		pr *= x;
    		pr %= M;
    	}
    	pr += M;
    	pr %= M;
    	cout << pr << endl;
    	return;
    }
    if(a[1] > 1){
    	int pr = a[0]+a[1];
    	rep(i,2,n){
    		pr *= a[i];
    		pr %= M;
    	}
    	pr += M;
    	pr %= M;
    	cout << pr << endl;
    	return;
    }
    int sm = 0;
    for(auto x : a){
    	if(x == 1)sm++;
    	else break;
    }
    int pr = sm;
    for(auto x : a){
    	if(x > 1){
    		pr *= x;
    		pr %= M;
    	}
    }
    pr += M;
    pr %= M;
    cout << pr << endl;

}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    #ifdef NCR
        init();
    #endif
    #ifdef SIEVE
        sieve();
    #endif

    di(t)

    while(t--)
        solve();

    assert(smn >= 1);
    assert(smn <= 2e5);
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

#define IGNORE_CR

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
#ifdef IGNORE_CR
            if (c == '\r') {
                continue;
            }
#endif
            buffer.push_back((char) c);
        }
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            assert(!isspace(buffer[pos]));
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
    int tt = in.readInt(1, 1e3);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 2e5);
        in.readEoln();
        sn += n;
        auto a = in.readInts(n, 1, 1e9);
        in.readEoln();
        sort(a.begin(), a.end());
        long long ans = 1;
        const long long mod = 1e9 + 7;
        int cnt = 0;
        if (n >= 2 && a[0] == 1 && a[1] > 1) {
            a[1]++;
        }
        for (auto i : a) {
            if (i >= 2) {
                ans *= i;
                ans %= mod;
            } else if (i == 1) {
                cnt++;
            }
        }
        if (cnt > 0) {
            ans *= cnt;
            ans %= mod;
        }
        cout << ans << '\n';
    }
    assert(sn <= 2e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a.count(1) == 0 or n == 1:
        ans = 1
        for x in a:
            ans *= x
            ans %= mod
        print(ans)
    elif a.count(1) > 1:
        ans = a.count(1)
        for x in a:
            ans *= x
            ans %= mod
        print(ans)
    else:
        a.remove(1)
        mn = min(a)
        j = a.index(mn)
        ans = 1 + mn
        for k in range(n-1):
            if k == j: continue
            ans *= a[k]
            ans %= mod
        print(ans)
``

</details>
