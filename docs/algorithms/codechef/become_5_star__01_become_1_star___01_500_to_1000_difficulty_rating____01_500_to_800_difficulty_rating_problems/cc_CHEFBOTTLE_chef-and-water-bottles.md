# Chef and Water Bottles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFBOTTLE |
| Difficulty Rating | 662 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFBOTTLE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFBOTTLE) |

---

## Problem Statement

Chef has $N$ empty bottles where each bottle has a capacity of $X$ litres.
There is a water tank in Chefland having $K$ litres of water. Chef wants to fill the empty bottles using the water in the tank.

Assuming that Chef does not spill any water while filling the bottles, find out the **maximum** number of bottles Chef can fill completely.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $N, X,$ and $K$.

---

## Output Format

For each test case, output in a single line answer, the **maximum** number of bottles Chef can fill completely.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, X \leq 10^5$
- $0 \leq K \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5 2 8
10 5 4
3 1 4
```

**Output**

```text
4
0
3
```

**Explanation**

**Test Case $1$:** The amount of water in the tank is $8$ litres. The capacity of each bottle is $2$ litres. Hence, $4$ water bottles can be filled completely.

**Test Case $2$:** The amount of water in the tank is $4$ litres. The capacity of each bottle is $5$ litres. Hence, no water bottle can be filled completely.

**Test Case $3$:** The amount of water in the tank is $4$ litres. The capacity of each bottle is $1$ litre. Chef has $3$ bottles available. He can fill all these bottles completely using $3$ litres of water.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 8
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
10 5 4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 1 4
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

[Contest Division 1](https://www.codechef.com/START30A/problems/CHEFBOTTLE)

[Contest Division 2](https://www.codechef.com/START30B/problems/CHEFBOTTLE)

[Contest Division 3](https://www.codechef.com/START30C/problems/CHEFBOTTLE)

[Contest Division 4](https://www.codechef.com/START30D/problems/CHEFBOTTLE)

**Setter:** [Abhishek Aman](https://www.codechef.com/users/pertifiedcobra)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403), [ Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has N empty bottles where each bottle has a capacity of X litres.

There is a water tank in Chefland having K litres of water. Chef wants to fill the empty bottles using the water in the tank.

Assuming that Chef does not spill any water while filling the bottles, find out the **maximum** number of bottles Chef can fill completely.

#
[](#explanation-5)EXPLANATION:

We are given N empty bottles. Capacity of each bottle is X litres. Thus, with K litres of water Chef can fill exactly \lfloor \frac{K}{X}  \rfloor bottles completely. Following cases are possible:

-

\lfloor \frac{K}{X}  \rfloor \geq N :  This means we can fill all the N bottles completely.

-

\lfloor \frac{K}{X}  \rfloor \lt N :  This means we can only fill \lfloor \frac{K}{X}  \rfloor bottles completely.

Here, \lfloor N  \rfloor is floor(N) which represents the largest integer less than or equal to N.

Examples

-

N = 4, X = 4, K = 15;

\lfloor \frac{15}{4}  \rfloor = 3. Since 3 \lt 4, Chef can fill only 3 bottles completely.

-

N = 4, X = 4, K = 20;

\lfloor \frac{20}{4}  \rfloor = 5. Since 5 \gt 4, Chef can fill all the 4 bottles completely.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

signed main(){
    // freopen("CHEFBOTTLE_3.in","r",stdin);
    // freopen("CHEFBOTTLE_3(Slow Check).out","w",stdout);
    int t;cin>>t;
    while(t--){
    	int N,X,K;cin>>N>>X>>K;
        int ans=0;
        while(N>0){
            K=K-X;
            if(K<=0) break;
            ans++;N--;
        }
    	cout<<ans<<"\n";
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

/*
------------------------Input Checker----------------------------------
*/

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

/*
------------------------Main code starts here----------------------------------
*/

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)
#define pb push_back

int sum_n = 0, sum_m = 0;
int max_n = 0, max_m = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll mod = 1000000007;

void solve()
{

    int n = readIntSp(1,1e5);
    int x = readIntSp(1,1e5);
    int k = readIntLn(0,1e5);

    cout<<min(k/x,n)<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,100);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
   // assert(sum_n<=2e3);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n <<'\n';
    cerr<<"Maximum length : " << max_n <<'\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define inf INT_MAX
#define mod 998244353

void f() {
    int n, x, k;
    cin >> n >> x >> k;
    int ans = min(n, k / x);
    cout << ans << "\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
