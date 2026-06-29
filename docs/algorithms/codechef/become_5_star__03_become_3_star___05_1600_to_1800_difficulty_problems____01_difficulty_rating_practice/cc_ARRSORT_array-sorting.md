# Array sorting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRSORT |
| Difficulty Rating | 1681 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [ARRSORT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/ARRSORT) |

---

## Problem Statement

You are given an **unsorted** permutation $P$ of size $N$. An operation is defined as:

- Swap $P_i$ and $P_{i+K}$ for any $i$ in the range $[1,N-K]$.

Find the **maximum** value of $K$, such that, the permutation $P$ can be **sorted** by applying any finite number of operations.

Note that, a permutation of size $N$ contains all integers from $1$ to $N$ **exactly** once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$, the size of permutation.
    - The next line contains $N$ integers describing the permutation $P$.
- It is guaranteed that the given permutation is **not sorted**.

---

## Output Format

For each test case, output on a new line the **maximum** possible value of $K$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
4 2 3 1
5
1 4 3 2 5
2
2 1
```

**Output**

```text
3
2
1
```

**Explanation**

- **Test Case $1$:** Permutation can be sorted by swapping $P_1$ and $P_4$. So, the maximum possible value of $K$ is $3$. It can be shown that we cannot sort the permutation for any $K\gt 3$.

- **Test Case $2$:** Swapping $P_2$ and $P_4$ will sort the permutation. So, the maximum possible value of $K$ is $2$. It can be shown that we cannot sort the permutation for any $K\gt 2$.

- **Test Case $3$:** Swapping $P_1$ and $P_2$ will sort the permutation. So, the maximum possible value of $K$ is $1$. It can be shown that we cannot sort the permutation for any $K\gt 1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 2 3 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
1 4 3 2 5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
2 1
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

[Contest Division 1](https://www.codechef.com/START46A/problems/ARRSORT)

[Contest Division 2](https://www.codechef.com/START46B/problems/ARRSORT)

[Contest Division 3](https://www.codechef.com/START46C/problems/ARRSORT)

[Contest Division 4](https://www.codechef.com/START46D/problems/ARRSORT)

[Practice](https://www.codechef.com/problems/ARRSORT)

**Setter:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

**Editorialist:** [Mithil Shah](https://www.codechef.com/users/mithilshah23)

#
[](#difficulty-2)DIFFICULTY

1681

#
[](#prerequisites-3)PREREQUISITES

Basic Math

#
[](#problem-4)PROBLEM

You are given an unsorted permutation P of size N. An operation is defined as:

Swap P_i and P_{i+K} for any i in the range [1,N?K].

Find the maximum value of K, such that, the permutation P can be sorted by applying any finite number of operations.

#
[](#explanation-5)EXPLANATION

###
[](#observation-6)Observation:

Assume P_i is not in i^{th} position where 1 \le i \le N, to move P_i to i^{th} position, K should be such that it is a factor of the displacement i.e. |P_i - i|.

Proof

We can say that we would need to move P_i in one direction only, as moving in the other direction would cancel out the previous one. Let us say that we take x moves to move P_i to i^{th} position.  In order for this to be possible, x \times K =|P_i - i|. Hence x = |P_i - i|/K where x is a natural number. This implies K divides |P_i - i| or in other words, K is a factor of |P_i - i|.

For example, in [5,2,3,4,1], we need to move 5 from 1^{st} position to 5^{th} position, this can be done by setting K=4 or K=2 or K=1.

Let us calculate all such displacement for which P_i is not in it’s sorted position.

Now, to calculate the maximum value of K that can make the array sorted, we need to find K such that for all P_i not in i^{th} position, we can send it to i^{th} position by performing finite operations.

Hence, K must be a factor of all such displacement and should be maximum. So, we need to find maximum common factor or greatest common divisor of all such displacements. Therefore, the answer would be the gcd of all such displacements.

To calculate this, we will iterate over all N integers, calculate the gcd of abs(P_i-i) where 1 \le i \le N. This would be the required answer.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(N) per testcase.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
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

ll sum_n = 0, sum_m = 0;
int max_n = 0, max_m = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll mod = 998244353;

using ii = pair<ll,ll>;

void solve(){
    int n = readIntLn(2,1e5);
    sum_n+=n;

    int p[n];
    rep(i,n){
        if(i<n-1) p[i] = readIntSp(1,n);
        else p[i] = readIntLn(1,n);
    }

    int g = 0;
    rep(i,n){
        g = __gcd(g, abs((p[i]-1)-i));
    }

    sort(p,p+n);
    rep(i,n) assert(p[i]=i+1);

    if(g==0) g=-1;
    cout<<g<<'\n';
}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,1e5);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_n<=1e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n<<'\n';
    //cerr<<"Maximum answer : " << max_n <<'\n';
    // // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution
``import math
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pos = [0]*(n+1)
	for i in range(n):
		pos[a[i]] = i+1
	ans = 0
	for i in range(1, n+1):
		ans = math.gcd(ans, i - pos[i])
	print(ans)
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define vi vector<int>
#define rep(i, n) for (int i = 0; i < n; i++)
#define endl '\n'
#define fastio                    \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
void tosolve()
{
    int n;
    cin>>n;
    int p[n+1];
    for(int i=1;i<=n;i++) cin>>p[i];
    int ans=0; //this will store gcd value
    for(int i=1;i<=n;i++)
    {
        ans=__gcd(ans,abs(p[i]-i));
    }
    cout<<ans<<endl;
}

int32_t main()
{
    fastio;
    int t;
    cin>>t;
    while(t--)
    {
        tosolve();
    }
    return 0;
}
``

Feel free to share your approach. Suggestions are welcomed.

</details>
