# Break the Stick

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BREAKSTICK |
| Difficulty Rating | 1026 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [BREAKSTICK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/BREAKSTICK) |

---

## Problem Statement

Chef has a stick of length $N$.

He can break the stick into $2$ or more parts such that the [parity](https://en.wikipedia.org/wiki/Parity_(mathematics)) of length of each part is same. For example, a stick of length $11$ can be broken into three sticks of lengths $\{3, 3, 5\}$ since each part is odd, but it cannot be broken into two sticks of lengths $\{5, 6\}$ since one is even and the other is odd.

Chef can then continue applying this operation on the smaller sticks he obtains, as many times as he likes.

Can Chef obtain a stick of length exactly $X$ by doing this?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of a single line of input, containing two space-separated integers $N, X$.

---

## Output Format

For each test case, output on a new line `YES` if Chef can obtain a stick of length exactly $X$, and `NO` otherwise.

Each letter of the output may be printed in either lowercase or uppercase. For example, the strings `YES`, `yEs`, and `Yes` will be considered identical.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \lt N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
6 1
3 2
4 3
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** Chef can initially break the stick into $3$ parts of length $2$ each. After that, Chef can pick any segment of length $2$ and break it into $2$ sticks of length $1$ each.

**Test case $2$:** Chef cannot obtain a stick of length $2$, since the only way to break a stick of length $3$ following the given conditions is into three parts of length $1$ each.

**Test case $3$:** Chef can break the stick into lengths $3$ and $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 3
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

[Contest Division 1](https://www.codechef.com/COOK142A/problems/BREAKSTICK)

[Contest Division 2](https://www.codechef.com/COOK142B/problems/BREAKSTICK)

[Contest Division 3](https://www.codechef.com/COOK142C/problems/BREAKSTICK)

[Contest Division 4](https://www.codechef.com/COOK142D/problems/BREAKSTICK)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

1026

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has a stick of length N.

He can break the stick into 2 or more parts such that the parity of length of each part is same. For example, a stick of length 11 can be broken into three sticks of lengths {3,3,5} since each part is odd, but it cannot be broken into two sticks of lengths {5,6} since one is even and the other is odd.

Chef can then continue applying this operation on the smaller sticks he obtains, as many times as he likes.

Can Chef obtain a stick of length exactly X by doing this?

#
[](#explanation-5)EXPLANATION:

There are two cases:

- When X is odd, we can always perform the operation regardless of N (by simply breaking N into X and a lot of 1's).

- When X is even, since all the parts must also be even, we need N to be even as well. When this is the case, we can also always perform the operation (by breaking N into X and a bunch of 2's).

Therefore the necessary and sufficient condition is X odd or N even.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
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
void solve()
{
    int n=readInt(1,1000000000,' ');
    int x=readInt(1,n-1,'\n');
    if(n%2==1 && x%2==0)
        cout<<"NO\n";
    else
        cout<<"YES\n";
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,1000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
const int N=2e6+1;
int main(){
	ios::sync_with_stdio(false);
	int t;cin >> t;
	while(t--){
		ll n,x;cin >> n >> x;
		if(n%2==0 || x%2==1) cout << "YES\n";
		else cout << "NO\n";
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
        int n, x; cin >> n >> x;
        cout << (x % 2 == 1 || n % 2 == 0 ? "YES\n" : "NO\n");
    }
}
``

</details>
