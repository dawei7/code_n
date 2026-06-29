# Playlist

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SONGS |
| Difficulty Rating | 489 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SONGS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SONGS) |

---

## Problem Statement

Chef's playlist contains $3$ songs named $A, B$, and $C$, each of duration exactly $X$ minutes. Chef generally plays these $3$ songs in loop, i.e, $A \rightarrow B \rightarrow C \rightarrow A \rightarrow B \rightarrow C \rightarrow A \rightarrow \dots$

Chef went on a train journey of $N$ minutes and played his playlist on loop for the whole journey. How many times did he listen to the song $C$ **completely**?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of a single line of input, containing two space-separated integers $N, X$.

---

## Output Format

For each test case, output on a new line the number of times Chef listens to the song $C$ **completely**.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq X \leq 10$

---

## Examples

**Example 1**

**Input**

```text
5
6 1
5 1
11 2
5 8
100 9
```

**Output**

```text
2
1
1
0
3
```

**Explanation**

**Test case $1$:** Since each song is of duration $1$ minute and the journey is $6$ minutes long, Chef listens each of the songs $A, B, C$ twice.

**Test case $2$:** Since each song is of duration $1$ minute and the journey is $5$ minutes long, Chef listens the songs $A, B$ twice but $C$ only once.

**Test case $3$:** Since each song is of duration $2$ minutes and the journey is $11$ minutes long, Chef listens the songs $A, B$ twice but $C$ only once. Note that Chef is in the middle of listening to song $C$ for the second time when the journey ends, but it is not counted since he hasn't listened to it fully.

**Test case $4$:** Chef cannot hear any song since the journey is shorter than his song duration.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
11 2
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5 8
```

**Output for this case**

```text
0
```



#### Test case 5

**Input for this case**

```text
100 9
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

[Contest Division 1](https://www.codechef.com/COOK142A/problems/SONGS)

[Contest Division 2](https://www.codechef.com/COOK142B/problems/SONGS)

[Contest Division 3](https://www.codechef.com/COOK142C/problems/SONGS)

[Contest Division 4](https://www.codechef.com/COOK142D/problems/SONGS)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

489

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s playlist contains 3 songs named A,B, and C, each of duration exactly X minutes. Chef generally plays these 3 songs in loop, i.e, A \to B \to C \to A \to B \to C \to A \to \dots

Chef went on a train journey of N minutes and played his playlist on loop for the whole journey. How many times did he listen to the song C completely?

#
[](#explanation-5)EXPLANATION:

There are \lfloor N/X \rfloor whole songs that Chef listens to throughout the journey. Among those songs, we know that every 3 songs has 1 C, so the number of times Chef listens to C is \lfloor \lfloor N / X \rfloor / 3 \rfloor.

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
    int n=readInt(1,100,' ');
    int x=readInt(1,10,'\n');
    cout<<(n/(3*x))<<'\n';
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
ll a[N];
int main(){
	ios::sync_with_stdio(false);
	int t;cin >> t;
	while(t--){
		ll n,x;cin >> n >> x;
		cout << n/(3*x) << '\n';
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
        cout << n / x / 3 << '\n';
    }
}
``

</details>
