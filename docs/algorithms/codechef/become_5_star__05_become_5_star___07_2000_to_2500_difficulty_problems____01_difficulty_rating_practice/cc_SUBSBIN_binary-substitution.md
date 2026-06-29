# Binary Substitution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSBIN |
| Difficulty Rating | 2161 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SUBSBIN](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SUBSBIN) |

---

## Problem Statement

Chef has binary string $S$ of length $N$.

Chef can perform the following operation on the string:
- Choose a contiguous subarray $S_L, S_{L + 1}, \ldots , S_R$ such that the count of set bits in the subarray is **equal** to the count of unset bits in the subarray.
- Replace the chosen subarray with either a set bit or an unset bit.

Chef wants to reduce the string to **minimum** possible length using **minimum** number of given operations. Help Chef by telling him the **minimum** length and also the operations required to obtain that. If there are multiple ways to obtain the answer, print any.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains a single integer $N$, denoting the length of the binary string.
- The second line of each test case contains a binary string $S$.

---

## Output Format

For each test case, output $K+1$ lines:
- The first line should contain two space-separated integers $M$ and $K$, denoting the **minimum** length that can be obtained and the **minimum** number of operations required to obtain it respectively.
- Then, $K$ lines follow, where the $i^{th}$ line denotes the $i^{th}$ operation:
    - Each operation is denoted using three space separated integers $L$, $R$, and $B$.
The integers $L$ and $R$ denote the chosen substring such that $(1\le L\lt R \le |S|)$ and the substring $S[L, R]$ has equal count of set and unset bits. Note that, $|S|$ denotes the length of the current string.
The integer $B$ denotes the bit with which the substring is replaced.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
4
1100
1
1
5
11000
```

**Output**

```text
1 1
1 4 0
1 0
1 2
1 4 1
1 2 1
```

**Explanation**

**Test case $1$:** We can reduce the string to a string of length $1$. We require only $1$ operation to do so:
- Choose $L = 1, R = 4,$ and $B = 0$. We chose the substring $S[1,4]$ which contains $2$ set bits and $2$ unset bits. We can replace the chosen substring with bit $0$.

**Test case $2$:** The given string is of length $1$. Thus, we cannot reduce it any further.

**Test case $3$:** We can reduce the string to a string of length $1$. We require $2$ operations to do so:
- Operation $1$: Choose $L = 1, R = 4,$ and $B = 1$. We chose the substring $S[1,4]$ which contains $2$ set bits and $2$ unset bits. We can replace the chosen substring with bit $1$. Thus, the string after this operation is $S = 10$.
- Operation $2$: Choose $L = 1, R = 2,$ and $B = 1$. We chose the substring $S[1,2]$ which contains $1$ set bit and $1$ unset bit. We can replace the chosen substring with bit $1$. Thus, the string after this operation is $S = 1$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUBSBIN)

[Contest: Division 1](https://www.codechef.com/START56A/problems/SUBSBIN)

[Contest: Division 2](https://www.codechef.com/START56B/problems/SUBSBIN)

[Contest: Division 3](https://www.codechef.com/START56C/problems/SUBSBIN)

[Contest: Division 4](https://www.codechef.com/START56D/problems/SUBSBIN)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1950

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a binary string S, in one move you can choose any substring of S that has an equal number of zeros and ones, and replace it with a single 0 or 1.

Find the minimum length of the final string, and a sequence of moves that achieves this.

#
[](#explanation-5)EXPLANATION

First, let’s get one edge case out of the way: if S consists of only a single character, no moves can be made on it so the minimum length is just N.

In any other case, you can bring the length down to 1.

A proof of this also gives us a construction.

Let d denote the difference between the number of ones and the number of zeros in the string.

- If d = 0, the string has an equal number of zeros and ones, so just replace the entire string with a single character.

- Otherwise, suppose d \gt 0 (the d \lt 0 case can be handled similarly). This means there are d more ones then zeros.

-
S has at least one 1 and one 0 (since the case when it doesn’t was taken care of right at the start).

- In particular, it has at least one substring that is either \texttt{10} or \texttt{01}.

- Replace this substring with a \texttt{0} (if d \lt 0, replace it with \texttt{1} instead).

Notice that doing this operation reduces d by 1 (since we effectively just deleted a \texttt{1} from the string and did nothing else), while also ensuring that the string still has both 1's and 0's. So, this can be repeated till we reach d = 0, at which point the entire string is replaced.

The small limit on N allows for each operation to be done in \mathcal{O}(N), giving us a \mathcal{O}(N^2) solution. However, it also possible (and not very hard) to implement this in \mathcal{O}(N).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N^2) or \mathcal{O}(N) per test case, depending on implementation.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("inp3.in", "r", stdin);
    //freopen("out3.txt", "w", stdout);
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        int c[2] = {0, 0};
        for(int i = 0; i < s.size(); i++) c[s[i] - '0']++;
        if(c[0] && c[1]) {
            cout << "1 " << max(c[0], c[1]) - min(c[0], c[1]) + 1 << "\n";
            while(c[0] != c[1]) {
                string now = "";
                int flag = 1;
                for(int i = 0; i < s.size(); i++) {
                    if(s[i] != s[i + 1] && flag) {
                        flag = 0;
                        cout << i + 1 << " " << i + 2 << " ";
                        if(c[0] > c[1]) cout << "1\n", c[1]++, now += '1';
                        else cout << "0\n", c[0]++, now += '0';
                        i++;
                    } else now += s[i];
                }
                s = now;
            }
            cout << "1 " << s.size() << " 0\n";
        } else cout << s.size() << " 0\n";
    }
}
``

Tester (utkarsh_25dec)'s code (C++)
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
    int n=readInt(1,1000,'\n');
    string s=readString(n,n,'\n');
    for(int i=0;i<n;i++)
        assert(s[i]=='0' || s[i]=='1');
    int cnt0=0,cnt1=0;
    for(int i=0;i<n;i++)
    {
        if(s[i]=='0')
            cnt0++;
        else
            cnt1++;
    }
    if(min(cnt0,cnt1)==0)
    {
        cout<<n<<' '<<0<<'\n';
        return;
    }
    cout<<1<<' '<<(abs(cnt0-cnt1)+1)<<'\n';
    int substitute=0;
    if(cnt1<cnt0)
        substitute=1;
    for(int x=1;x<=abs(cnt0-cnt1);x++)
    {
        int l=0;
        string tmp="";
        for(int i=0;i<n;i++)
        {
            if(s[i]!=s[i+1])
            {
                l=i;
                break;
            }
        }
        cout<<l+1<<' '<<l+2<<' '<<substitute<<'\n';
        for(int i=0;i<l;i++)
            tmp+=s[i];
        tmp+=('0'+substitute);
        for(int i=l+2;i<s.length();i++)
            tmp+=s[i];
        s=tmp;
    }
    cout<<1<<' '<<s.length()<<' '<<substitute<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,100,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester (rivalq)'s code (C++)
``// Jai Shree Ram

#include<bits/stdc++.h>
using namespace std;

#define rep(i,a,n)     for(int i=a;i<n;i++)
#define ll             long long
#define int            long long
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define endl           "\n"
#define x              first
#define y              second
#define gcd(a,b)       __gcd(a,b)
#define mem1(a)        memset(a,-1,sizeof(a))
#define mem0(a)        memset(a,0,sizeof(a))
#define sz(a)          (int)a.size()
#define pii            pair<int,int>
#define hell           1000000007
#define elasped_time   1.0 * clock() / CLOCKS_PER_SEC

template<typename T1,typename T2>istream& operator>>(istream& in,pair<T1,T2> &a){in>>a.x>>a.y;return in;}
template<typename T1,typename T2>ostream& operator<<(ostream& out,pair<T1,T2> a){out<<a.x<<" "<<a.y;return out;}
template<typename T,typename T1>T maxs(T &a,T1 b){if(b>a)a=b;return a;}
template<typename T,typename T1>T mins(T &a,T1 b){if(b<a)a=b;return a;}

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

const int maxn=2000005;
int p[maxn];
int sz[maxn];
void clear(int n=maxn){
    rep(i,0,maxn)p[i]=i,sz[i]=1;
}
int root(int x){
   while(x!=p[x]){
       p[x]=p[p[x]];
       x=p[x];
   }
   return x;
}
void merge(int x,int y){
    int p1=root(x);
    int p2=root(y);
    if(p1==p2)return;
    if(sz[p1]>=sz[p2]){
        p[p2]=p1;
        sz[p1]+=sz[p2];
    }
    else{
        p[p1]=p2;
        sz[p2]+=sz[p1];
    }
}

int solve(){
		int n = readIntLn(1,1000);

                string s = readStringLn(n,n);
                for(auto i:s)assert(i >= '0' and i <= '1');
                int c0 = count(all(s),'0');
                int c1 = n - c0;
                if(c0 == n or c1 == n){
                        cout << n << " " << 0 << endl;
                        return 0;
                }
                int op = abs(c0 - c1) + 1;
                vector<array<int,3>> ops;
                for(int i = 1; i < op; i++){
                        int j = 1;
                        while(s[j] == s[j - 1])j++;
                        char c = (c0 < c1)?'0':'1';
                        ops.push_back({j,j + 1,c});
                        string t = s.substr(0,j - 1) + c + s.substr(j + 1);
                        s = t;
                }
                ops.push_back({1,(int)s.length(),'0'});
                cout << 1 << " " << ops.size() << endl;
                for(auto i:ops){
                        cout << i[0] << " " << i[1] << " " << char(i[2]) << endl;
                }

 return 0;
}
signed main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout)`;
    #ifdef SIEVE
    sieve();
    #endif
    #ifdef NCR
    init();
    #endif
    int t = readIntLn(1,100);
    while(t--){
        solve();
    }
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    if s.count('0') == n or s.count('1') == n:
        print(n, 0)
        continue

    dif = s.count('0') - s.count('1')
    print(1, abs(dif) + 1)
    while dif != 0:
        n = len(s)
        for i in range(n):
            if s[i] != s[i+1]:
                which = '0'
                if dif > 0:
                    which = '1'
                s = s[0:i] + which + s[i+2:]
                print(i+1, i+2, which)
                break
        dif = s.count('0') - s.count('1')
    n = len(s)
    print(1, n, 1)
``

</details>
