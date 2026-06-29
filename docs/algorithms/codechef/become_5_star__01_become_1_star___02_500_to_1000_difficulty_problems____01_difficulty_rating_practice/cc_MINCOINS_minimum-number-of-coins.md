# Minimum number of coins

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINCOINS |
| Difficulty Rating | 711 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MINCOINS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINCOINS) |

---

## Problem Statement

Chef has infinite coins in denominations of rupees $5$ and rupees $10$.

Find the **minimum** number of coins Chef needs, to pay **exactly** $X$ rupees. If it is impossible to pay $X$ rupees in denominations of rupees $5$ and $10$ only, print $-1$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single integer $X$.

---

## Output Format

For each test case, print a single integer - the **minimum** number of coins Chef needs, to pay **exactly** $X$ rupees. If it is impossible to pay $X$ rupees in denominations of rupees $5$ and $10$ only, print $-1$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
50
15
8
```

**Output**

```text
5
2
-1
```

**Explanation**

**Test Case $1$:** Chef would require at least $5$ coins to pay $50$ rupees. All these coins would be of rupees $10$.

**Test Case $2$:** Chef would require at least $2$ coins to pay $15$ rupees. Out of these, $1$ coin would be of rupees $10$ and $1$ coin would be of rupees $5$.

**Test Case $3$:** Chef cannot pay exactly $8$ rupees in denominations of rupees $5$ and $10$ only.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
50
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
15
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
8
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME106A/problems/MINCOINS)

[Contest Division 2](https://www.codechef.com/LTIME106B/problems/MINCOINS)

[Contest Division 3](https://www.codechef.com/LTIME106C/problems/MINCOINS)

[Contest Division 4](https://www.codechef.com/LTIME106D/problems/MINCOINS)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has infinite coins in denominations of rupees 5 and rupees 10.

Find the **minimum** number of coins Chef needs, to pay **exactly** X rupees. If it is impossible to pay X rupees in denominations of rupees 5 and 10 only, print ?1.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- If X is divisible by 10, minimum coins required are \frac{X}{10}

- If X is divisible by 5 and not by 10, minimum coins required are \lfloor \frac{X}{10} \rfloor + 1

- If X is not divisible by 5 it is impossible to pay exactly X rupees, therefore output -1

#
[](#explanation-6)EXPLANATION:

Given that Chef has infinite coins in denominations of rupees 5 and rupees 10.

Chef needs to pay **exactly** X rupees using above denominations.

Suppose Chef selects A coins of 5 and B coins of 10 to pay exactly X rupees. The equation that will follow is 5 \cdot A + 10 \cdot B = X.

The above equation can also be written as A + 2 \cdot B =  \frac{X}{5}  .

**Observation 1**

Chef can pay exactly X rupees only if X is divisible by 5 because A + 2 \cdot B will always be a positive **integer**. If X is not divisible by 5, output -1

**Observation 2**

In order to **minimize** the number of coins used, we needs to maximize the value of B (number of 10 rupees coins used) and minimize the value of A (number of 5 rupees coins used). Following cases are possible

X is divisible by 10

Maximum 10 rupees coins used  = B_{max} = \frac{X}{10}

Minimum 5 rupees coins used = A_{min} = 0

Total minimum coins used = B_{max} + A_{min}  = \frac{X}{10}

X is divisible by 5 but not divisible by 10

Maximum 10 rupees coins used = B_{max} = \lfloor \frac{X}{10} \rfloor

Minimum 5 rupees coins used   = A_{min} = 1

Total minimum coins used  = B_{max} + A_{min} = \lfloor \frac{X}{10} \rfloor + 1

X is not divisible by 5

Not possible to pay exactly X rupees (**Observation 1**), therefore output -1

\lfloor N  \rfloor is floor(N) which represents the largest integer less than or equal to N.

Examples

-

X = 20; (1^{st} case is followed)

B_{max} = \frac{20}{10}; A_{min} = 0; B_{max} + A_{min} = \frac{20}{10} = 2

-

X = 15; (2^{nd} case is followed)

B_{max} =  \lfloor \frac{15}{10} \rfloor; A_{min} = 1; B_{max} + A_{min}  = \lfloor \frac{15}{10} \rfloor + 1 = 2

-

X = 97; (3^{rd} case is followed)

Not possible to pay exactly 97 rupees, therefore output -1

#
[](#time-complexity-7)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-8)SOLUTION:

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
    int x=readInt(1,1000,'\n');
    if(x%5!=0)
        cout<<-1<<'\n';
    else
        cout<<(x+5)/10<<'\n';
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
    //cin>>T;
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution
`` #include <bits/stdc++.h>
using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true) {
        char g = getchar();
        if (g == '-') {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9') {
            x *= 10;
            x += g - '0';
            if (cnt == 0) {
                fi = g - '0';
            }
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if (g == endd) {
            assert(cnt > 0);
            if (is_neg) {
                x = -x;
            }
            assert(l <= x && x <= r);
            return x;
        }
        else {
            assert(false);
        }
    }
}
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  int t;
  t = readInt(1, 1000, '\n');
  while(t--){
    int x;
    x = readInt(1, 1000, '\n');
    if(x % 5){
      cout<<-1<<"\n";
    }else{
      cout<<((x / 5) + 1) / 2<<"\n";
    }
  }
  return 0;
}
``

Editorialist's Solution
``/*prakhar_87*/
#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define inf INT_MAX
#define mod 998244353

void f() {
    int x; cin >> x;
    if (x % 5 != 0) cout << "-1\n";
    else {
        if (x % 10 == 0) cout << x / 10 << "\n";
        else if (x % 5 == 0) cout << (x / 10) + 1 << "\n";
    }
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
