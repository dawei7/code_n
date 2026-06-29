# Monks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MONKS |
| Difficulty Rating | 1776 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MONKS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MONKS) |

---

## Problem Statement

There is a town with $N$ people and initially, the $i^{th}$ person has $A_i$ coins. However, some people of the town decide to become *monks*. If the $i^{th}$ person becomes a monk, then:
- He leaves the town thereby reducing the number of people in the town by $1$.
- He distributes $X$ $(0 \le X \le A_i)$ coins to the remaining people of the town (not necessarily equally). Note that each monk can freely choose his value of $X$, and different monks may choose different values of $X$.
- He takes the remaining $A_i - X$ coins with him.

For example, initially, if $A = [1, 3, 4, 5]$ and $4^{th}$ person decides to become a monk then he can leave the town and can give $2$ coins to the $1^{st}$ person, $1$ coin to the $2^{nd}$ person, no coins to the $3^{rd}$ person and take $2$ coins along with him while going. Now $A$ becomes $[3, 4, 4]$.

Determine the **minimum** number of people who have to become monks, so that in the end, everyone remaining in the town has an equal number of coins.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the number of people in the town.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the initial number of coins of everyone in the town.

---

## Output Format

For each test case, output the minimum number of people who have to become monks, so that in the end, everyone remaining in the town has an equal number of coins.

---

## Constraints

- $1 \le T \le 10^5$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
6 6 6 6
3
5 1 4
5
2 1 2 1 1
```

**Output**

```text
0
1
2
```

**Explanation**

**Test case $1$:** All the people already have an equal number of coins.

**Test case $2$:** The $2^{nd}$ person can become a monk and give his $1$ coin to the person with $4$ coins. After this, both the remaining people will have $5$ coins.

**Test case $3$:** One way of two people becoming monks is as follows:
- The $2^{nd}$ person becomes a monk, and takes his $1$ coin with him
- The $3^{rd}$ person becomes a monk, and gives one coin each to the $4^{th}$ and $5^{th}$ people

Everyone remaining in the town now has $2$ coins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
6 6 6 6
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3
5 1 4
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5
2 1 2 1 1
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

[Contest Division 1](https://www.codechef.com/START49A/problems/MONKS)

[Contest Division 2](https://www.codechef.com/START49B/problems/MONKS)

[Contest Division 3](https://www.codechef.com/START49C/problems/MONKS)

[Contest Division 4](https://www.codechef.com/START49D/problems/MONKS)

Setter: [ Jeevan Jyot Singh](https://www.codechef.com/users/jeevan_adm)

Tester: [ Jeevan Jyot Singh](https://www.codechef.com/users/jeevan_adm),[ Nishank Suresh](https://www.codechef.com/users/iceknight1093)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

1776

#
[](#prerequisites-3)PREREQUISITES:

[]

#
[](#problem-4)PROBLEM:

There is a town with N people and initially, the i^{th} person has A_i coins. However, some people of the town decide to become *monks*. If the i^{th} person becomes a monk, then:

- He leaves the town thereby reducing the number of people in the town by 1.

- He distributes X (0 \le X \le A_i) coins to the remaining people of the town (not necessarily equally). Note that each monk can freely choose his value of X, and different monks may choose different values of X.

- He takes the remaining A_i - X coins with him.

For example, initially, if A = [1, 3, 4, 5] and 4^{th} person decides to become a monk then he can leave the town and can give 2 coins to the 1^{st} person, 1 coin to the 2^{nd} person, no coins to the 3^{rd} person and take 2 coins along with him while going. Now A becomes [3, 4, 4].

Determine the **minimum** number of people who have to become monks, so that in the end, everyone remaining in the town has an equal number of coins.

#
[](#explanation-5)EXPLANATION:

Let B be the set of people who become monks and C be the set of people who do not become monks. For all the people in C to have an equal number of coins, it is sufficient and optimal to distribute coins from the people in B to the people in C so that all the people in C have as much coins as the maximum coins held initially by any person in C.

Let Max_C be the maximum coins held initially by any person in C, Size_C be the size of C, Sum_B be the sum of the coins held initially by all the people in B, and Sum_C be the sum of the coins held initially by all people in C. It is clear that we have Sum_B coins to distribute among people in C and the minimum number of coins required so that all the people in C have Max_C  coins is Max_C \times Size_C - Sum_C. So, this selection of B and C is possible if Sum_B \geq Max_C \times Size_C - Sum_C.

C is characterized by Max_C so we can go over all possible C by iterating over each A[i] = Max_C. This means that all elements of A having values higher that A[i] will fall into B. This iteration is very easy if A is sorted because Size_C can be found easily using the index i, Sum_C is the prefix sum till index i, Sum_B is suffix sum for index i+1, and Max_C is A[i].

We will pick the split (of B and C) which is valid (satisfies the condition) and has minimum Size_B or maximum Size_C as required in the question.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N log(N)) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const long long INF = 1e18;

const int N = 1e6 + 5;

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << "L: " << l << ", R: " << r << ", Value Found: " << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

int sumN = 0;

void solve()
{
    int n = readIntLn(1, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e9);
    sort(a.begin(), a.end());
    vector<int> pref = a;
    for(int i = 1; i < n; i++)
        pref[i] += pref[i - 1];
    for(int i = n - 1; i >= 0; i--)
    {
        int S = pref.back() - pref[i];
        int P = pref[i];
        if((i + 1) * a[i] - P <= S)
        {
            cout << n - (i + 1) << endl;
            return;
        }
    }
    assert(false);
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1e5);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    assert(sumN <= 2e5);
    readEOF();
    return 0;
}
``

Editorialist's Solution
``using namespace std;
#define ll long long

int main() {
	ll T;
	cin >> T;
	while(T--){
	    ll n;
	    cin >> n;
	    vector<ll>a(n);
	    ll sum=0;
	    for(ll i=0;i<n;i++){
	        cin >> a[i];
	        sum+=a[i];
	    }
	    sort(a.begin(),a.end());
	    if(a[n-1]==a[0]){
	        cout << 0 << endl;
	        continue;
	    }
	    ll curr=0;
	    ll ans=n;
	    for(ll i=0;i<n;i++){
	        curr+=a[i];
	        ll x=sum-curr;
	        if(x>=a[i]*(i+1)-curr)ans=min(ans,n-i-1);
	    }
	    cout << ans << endl;
	}
	return 0;
}
``

</details>
