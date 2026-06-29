# Equal by XORing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQBYXOR |
| Difficulty Rating | 1507 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [EQBYXOR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/EQBYXOR) |

---

## Problem Statement

JJ has three integers $A$, $B$, and $N$. He can apply the following operation on $A$:
- Select an integer $X$ such that $1 \le X \lt N$ and set $A := A \oplus X$. (Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).)

JJ wants to make $A$ **equal** to $B$.
Determine the **minimum** number of operations required to do so. Print $-1$ if it is not possible.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $A$, $B$, and $N$ — the parameters mentioned in the statement.

---

## Output Format

For each test case, output the minimum number of operations required to make $A$ equal to $B$. Output $-1$ if it is not possible to do so.

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq A, B \lt 2^{30}$
- $1 \leq N \le 2^{30}$

---

## Examples

**Example 1**

**Input**

```text
3
5 5 2
3 7 8
8 11 1
```

**Output**

```text
0
1
-1
```

**Explanation**

- **Test Case $1$:** $A$ is already equal to $B$. Hence we do not need to perform any operation.
- **Test Case $2$:** We can perform the operation with $X = 4$ which is $\lt 8$. Therefore $A = 3 \oplus 4 = 7$. Thus, only one operation is required.
- **Test Case $3$:** We can show that it is not possible to make $A$ equal to $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 7 8
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
8 11 1
```

**Output for this case**

```text
-1
```



**Example 2**

**Input**

```text
2
24 27 3
4 5 1000
```

**Output**

```text
2
1
```

**Explanation**

Note that the above sample case belongs to subtask $2$.

- **Test Case 1:** We can first perform the operation with $X = 1$ which is $\lt 3$. Therefore $A = 24 \oplus 1 = 25$. Then we can perform the operation with $X = 2$ which is $\lt 3$. Therefore $A = 25 \oplus 2 = 27$. Therefore we can make $A$ equal to $B$ in $2$ operations. It can be shown that it is not possible to do this in less than $2$ operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
24 27 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 5 1000
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME109A/problems/EQBYXOR)

[Contest Division 2](https://www.codechef.com/LTIME109B/problems/EQBYXOR)

[Contest Division 3](https://www.codechef.com/LTIME109C/problems/EQBYXOR)

[Contest Division 4](https://www.codechef.com/LTIME109D/problems/EQBYXOR)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevan_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

1507

#
[](#prerequisites-3)PREREQUISITES:

XOR

#
[](#problem-4)PROBLEM:

JJ has three integers A, B, and N. He can apply the following operation on A:

- Select an integer X such that 1 \le X \lt N and set A := A \oplus X. (Here, \oplus denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).)

JJ wants to make A **equal** to B.

Determine the **minimum** number of operations required to do so. Print -1 if it is not possible.

#
[](#explanation-5)EXPLANATION:

Let X = A \oplus B, and for the sake of editorialist’s sanity we decrease N by 1. We now want to achieve X from XOR-ing as few elements no greater than N as possible.

There are 4 cases:

-
X = 0. Answer is 0.

-
X \le N. Answer is 1.

-
\lfloor \log_2(X) \rfloor = \lfloor \log_2(N) \rfloor . Answer is 2. This semantically means the largest bit of X is equal to the largest bit of N, which means we can construct X by 2^{\lfloor \log_2(X) \rfloor} with some other value less than 2^{\lfloor \log_2(X) \rfloor}.

- Otherwise. Answer is -1. This happens in the case where the largest bit of X is larger to the largest bit of N, which means we cannot create this largest bit by any means.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Setter's Solution
``#ifdef WTSH
    #include <wtsh.h>
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
                cerr << l << ' ' << r << ' ' << x << '\n';
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
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
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

void solve()
{
    int a = readIntSp(0, (1 << 30) - 1);
    int b = readIntSp(0, (1 << 30) - 1);
    int n = readIntLn(1, (1 << 30));
    int z = a ^ b;
    if(z == 0)
        cout << 0 << endl;
    else if(z < n)
        cout << 1 << endl;
    else
    {
        int msb = -1;
        for(int i = 30; i >= 0; i--)
        {
            if(z >> i & 1)
            {
                msb = i;
                break;
            }
        }
        if((1 << msb) < n)
            cout << 2 << endl;
        else
            cout << -1 << endl;
    }
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1000);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    readEOF();
    return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
const int N=2e5+5;
int n;
ll a[N];
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;
	while(t--){
		ll a,b,n;cin >> a >> b >> n;
		ll z=1;
		while(z<n) z*=2;
		if((a^b)==0) cout << "0\n";
		else if((a^b)<n) cout << "1\n";
		else if((a^b)<z) cout << "2\n";
		else cout << "-1\n";
	}
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int a, b, n; cin >> a >> b >> n; --n;
        int x = a ^ b;
        if (x == 0) {
            cout << "0\n";
        } else if (x <= n) {
            cout << "1\n";
        } else if (n != 0 && __lg(x) == __lg(n)) {
            cout << "2\n";
        } else {
            cout << "-1\n";
        }
    }
}
``

</details>
