# Lunchtime

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LTIME |
| Difficulty Rating | 352 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [LTIME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LTIME) |

---

## Problem Statement

Chef has his lunch only between $1$ pm and $4$ pm (both inclusive).

Given that the current time is $X$ pm, find out whether it is *lunchtime* for Chef.

---

## Input Format

- The first line of input will contain a single integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, containing one integer $X$.

---

## Output Format

For each test case, print in a single line $\texttt{YES}$ if it is lunchtime for Chef. Otherwise, print $\texttt{NO}$.

You may print each character of the string in either uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 12$
- $1 \leq X \leq 12$

---

## Examples

**Example 1**

**Input**

```text
3
1
7
3
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** Lunchtime is between $1$ pm and $4$ pm (both inclusive). Since $1$ pm lies within lunchtime, the answer is $\texttt{YES}$.

**Test case $2$:** Lunchtime is between $1$ pm and $4$ pm (both inclusive). Since $7$ pm lies outside lunchtime, the answer is $\texttt{NO}$.

**Test case $3$:** Lunchtime is between $1$ pm and $4$ pm (both inclusive). Since $3$ pm lies within lunchtime, the answer is $\texttt{YES}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
7
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME107A/problems/LTIME)

[Contest Division 2](https://www.codechef.com/LTIME107B/problems/LTIME)

[Contest Division 3](https://www.codechef.com/LTIME107C/problems/LTIME)

[Contest Division 4](https://www.codechef.com/LTIME107D/problems/LTIME)

**Setter:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has his lunch only between 1 pm and 4 pm (both inclusive).

Given that the current time is X pm, find out whether it is *lunchtime* for Chef.

#
[](#explanation-5)EXPLANATION:

We check whether X is greater or equal than 1 and less than or equal than 4.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    if(x>=1 && x<=4) cout<<"YES";
	    else cout<<"NO";
	    cout<<endl;
	}
	return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
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
ll n;
ll a[2001];
ll dp[2001];
void solve(){
	int x;x=readInt(1,12,'\n');
	if(1<=x && x<=4) cout << "YES\n";
	else cout << "NO\n";
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;t=readInt(1,12,'\n');while(t--) solve();
	readEOF();
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
        int x; cin >> x;
        cout << (x >= 1 && x <= 4 ? "YES\n" : "NO\n");
    }
}
``

</details>
