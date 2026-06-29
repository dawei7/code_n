# Sardar and GCD

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DLTNODE |
| Difficulty Rating | 2190 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [DLTNODE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/DLTNODE) |

---

## Problem Statement

Sardar Khan has finally decided to attack Ramadhir - he will bomb one of Ramadhir's businesses in Wasseypur. Sardar Khan knows that Ramadhir has $N$ businesses (numbered $1$ to $N$) and that there are $N - 1$ roads connecting pairs of these businesses in such a way that all businesses are connected. Further, Sardar knows that each business has a specific value - the $i$-th business has value $A_i$.

When Sardar Khan destroys a business, he also destroys every road directly connected to it.
Formally, destroying business $v$ also destroys all existing roads of the form $(u, v)$.

Sardar thinks that the damage dealt to Ramadhir upon destroying business $v$ equals the sum of the [greatest common divisors](https://en.wikipedia.org/wiki/Greatest_common_divisor) of every remaining maximal connected set of businesses. More formally,
* Let the connected components of the graph obtained on deleting $v$ and edges incident to it be $C_1, C_2, \dots, C_k$.
* Define $\gcd(C_i)$ to be $\gcd(A_{i_1}, A_{i_2}, \dots, A_{i_r})$ where $C_i$ consists of vertices $i_1, i_2, \dots, i_r$.
* The damage caused by destroying $v$ is then $\sum_{i = 1}^k \gcd(C_i)$.

Sardar Khan wants to maximize the damage he deals. Can you find the maximum possible damage he can achieve, given that he destroys **exactly one** business?

If the process of computing damage is still unclear, please refer to sample test cases for an explained example.

---

## Input Format

- The first line of input contains an integer $T$, denoting the total number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$, denoting the number of businesses Ramadhir owns.
- Each of the next $N-1$ lines contains $2$ integers $a$ and $b$, denoting a road between businesses $a$ and $b$.
- Finally, the last line of each test case contains $N$ space-separated positive integers $A_1, A_2, \ldots, A_N$, where $A_i$ is the value of the $i$-th business.

---

## Output Format

- For each test case, output a single line containing one integer - the maximum possible damage that Sardar Khan can deal.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases will not exceed $5 \cdot 10^5$.
- It is guaranteed that the given roads connect every business.

---

## Examples

**Example 1**

**Input**

```text
1
5
1 2
1 3
3 4
3 5
4 6 8 12 15
```

**Output**

```text
29
```

**Explanation**

* If business $1$ is bombed, the remaining connected components are $\{(2), (3, 4, 5)\}$. This gives a damage of $\gcd(A_2) + \gcd(A_3, A_4, A_5) = 6 + 1 = 7$.
* If business $2$ is bombed, the remaining connected components are $\{(1, 3, 4, 5)\}$. This gives a damage of $\gcd(A_1, A_3, A_4, A_5) = 1$.
* If business $3$ is bombed, the remaining connected components are $\{(1, 2), (4), (5)\}$. This gives a damage of $\gcd(A_1, A_2) + \gcd(A_4) + \gcd(A_5) = 2 + 12 + 15 = 29$.
* If business $4$ is bombed, the remaining connected components are $\{(1, 2, 3, 5)\}$. This gives a damage of $\gcd(A_1, A_2, A_3, A_5) = 1$.
* If business $5$ is bombed, the remaining connected components are $\{(1, 2, 3, 4)\}$. This gives a damage of $\gcd(A_1, A_2, A_3, A_4) = 2$.

Clearly, bombing business $3$ gives the maximum possible damage, that being 29.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem statement](https://www.codechef.com/CSNS21B/problems/DLTNODE)

[Contest source](https://www.codechef.com/CSNS21B)

***Author, Editorialist :*** [Dhananjay Raghuwanshi](https://www.codechef.com/users/dhananjay_777)

***Tester :*** [Miten Shah](https://www.codechef.com/users/mtnshh)

#
[](#difficulty-1)DIFFICULTY:

Easy

#
[](#prerequisites-2)PREREQUISITES:

Tree Flattening, prefix sums, DFS and similar

#
[](#problem-3)PROBLEM:

Given a tree consisting of N nodes. Each node is given some value. We have to delete one node from the tree such that the sum of GCD of node values in all connected components formed after deleting that node is as maximum as possible.

#
[](#explanation-4)EXPLANATION:

- One way is to delete each node one by one and check answer for each node and select maximum answer from them. But doing this lamely obviously will give TLE. So we will use tree flattening and prefix sum technique to do above task more optimally.

- First root the tree let at node 1 then flatten the tree by using tree flattening technique and along with it also store in and out time for each node and also store the GCD of each subtree and parent of each node by running a simple DFS from node 1. Now lastly precompute the GCD from both forward and backward side of the array obtained from tree flattening . Now we can easily calculate for each node the possible sum of GCD of node values in each connected component after removing that node, and can output maximum of them.

####
[](#how-to-find-answer-for-a-particular-node-x-5)How to find answer for a particular node x

- To find answer for a node x, first let’s see what happens by deleting the node x. If we delete node x, then the total number of connected components formed will be Number of children of node x +1.

- Also for each child of node x we already have calculated the GCD of node values of all the node in subtree of it’s child as earlier we have precomputed GCD of each subtree. Now the part left is the part formed after removing the whole subtree of node x from the tree.

- To calculate GCD of all nodes values in this part we will make use of in and out time of node x and of  prefix and suffix arrays of GCD’s we have earlier calculated.

- So this part is equal to the GCD(forward[in[x]-1],backward[out[x]+1]), the array forward[i] (prefix array) stores GCD of all the nodes from index 1 to i of the array obtained from tree flattening and backward[j] (suffix array) stores GCD of all the nodes from last index of array to index j of the array obtained from tree flattening.

- The answer for node x is equal to the sum all above parts we have calculated above.

#
[](#solution-6)SOLUTION :

c++ Solution
``  #include <bits/stdc++.h>
using namespace std;

#define int int long long
#define fr(i, n) for (int i = 0; i < n; i++)
#define fr1(i, n) for (int i = 1; i <= n; i++)
#define S second
#define F first
#define pb(n) push_back(n)
#define endl "\n"
vector<int> v[1000001];
int in[1000001] = {0};
int out[1000001] = {0};
int timer = 1, n, m, t, k, eq = 0;
int flatentree[1000001];
int parent[1000001];
int gcd_subtree[1000001];
int value[1000001];
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    else
        return (gcd(b, a % b));
}

int dfs(int x, int p)
{
    parent[x] = p;
    flatentree[timer] = x;
    in[x] = timer++;
    gcd_subtree[x] = value[x];
    for (auto child : v[x])
    {
        if (child != p)
        {
            gcd_subtree[x] = gcd(dfs(child, x), gcd_subtree[x]);
        }
    }
    flatentree[timer] = x;
    out[x] = timer++;
    return (gcd_subtree[x]);
}

signed main()
{
    cin >> t;
    while (t--)
    {
        timer = 1;
        cin >> n;
        fr(i, n + 1)
        {
            v[i].clear();
        }

        fr1(i, n - 1)
        {
            int a, b;
            cin >> a >> b;
            v[a].pb(b);
            v[b].pb(a);
        }
        fr1(i, n)
        {
            cin >> value[i];
        }
        dfs(1, -1);
        int si = 2 * n;
        int forward[si + 1], backward[si + 1];
        forward[1] = backward[si] = value[1];
        for (int i = 2; i <= si; i++)
        {
            forward[i] = gcd(forward[i - 1], value[flatentree[i]]);
        }
        for (int i = si - 1; i >= 1; i--)
        {
            backward[i] = gcd(backward[i + 1], value[flatentree[i]]);
        }
        int ans = 1;
        int temp;
        fr1(i, n)
        {
            vector<int> children;
            for (auto child : v[i])
            {
                if (child != parent[i])
                {
                    children.pb(gcd_subtree[child]);
                }
            }
            if (children.size() != 0)
            {
                temp = 0;
                for (auto j : children)
                {
                    temp += j;
                }
                int temp1;
                if (i != 1)
                {
                    temp1 = gcd(forward[in[i] - 1], backward[out[i] + 1]);
                    ans = max(ans, temp + temp1);
                }
                else
                {
                    ans = max(ans, temp);
                }
            }
            else
            {
                temp = gcd(forward[in[i] - 1], backward[out[i] + 1]);
                ans = max(ans, temp);
            }
        }
        cout << ans << endl;
    }
}
``

C++ Tester's solution
``// created by mtnshh

#include<bits/stdc++.h>
#include<sys/resource.h>
using namespace std;
#define ll long long int
#define pb push_back
#define rb pop_back
#define ti tuple<int, int, int>
#define pii pair<int, int>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define mp make_pair
#define mt make_tuple

#define rep(i,a,b) for(ll i=a;i<b;i++)
#define repb(i,a,b) for(ll i=a;i>=b;i--)

#define err() cout<<"--------------------------"<<endl;
#define errA(A) for(auto i:A)   cout<<i<<" ";cout<<endl;
#define err1(a) cout<<#a<<" "<<a<<endl
#define err2(a,b) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<endl
#define err3(a,b,c) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<" "<<#c<<" "<<c<<endl
#define err4(a,b,c,d) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<" "<<#c<<" "<<c<<" "<<#d<<" "<<d<<endl

#define all(A)  A.begin(),A.end()
#define allr(A)    A.rbegin(),A.rend()
#define ft first
#define sd second

#define V vector<ll>
#define S set<ll>
#define VV vector<V>
#define Vpll vector<pll>

// #define endl "\n"

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        // char g = getc(fp);
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
            // cerr << x << " " << l << " " << r << endl;
            assert(l<=x && x<=r);
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
        // char g=getc(fp);
        assert(g != -1);
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

const int max_q = 1e3;
const int max_n = 1e5;
const int max_sum_n = 1e6;
const int max_ai = 1e9;

const ll N = 100005;
const ll INF = 1e12;

V adj[N];
ll A[N];

ll in[N], out[N], cnt = 0, pref[N], suff[N], ans = 0, ord[N];

void dfs1(ll n, ll p){
    in[n] = cnt;
    ord[cnt] = n;
    cnt += 1;
    for(auto i: adj[n]){
        if(i == p)  continue;
        dfs1(i, n);
    }
    out[n] = cnt - 1;
}

ll dfs2(ll n, ll p){
    ll sum = 0, gcd = A[n];
    for(auto i: adj[n]){
        if(i == p)  continue;
        ll q = dfs2(i, n);
        gcd = __gcd(gcd, q);
        sum += q;
    }
    sum += __gcd(pref[in[n]-1], suff[out[n]+1]);
    ans = max(ans, sum);
    return gcd;
}

void solve(ll n){
    rep(i,0,n+1)    adj[i].clear();
    rep(i,0,n-1){
        ll u = readIntSp(1, n), v = readIntLn(1, n);
        adj[u].pb(v);
        adj[v].pb(u);
    }
    rep(i,1,n+1)    A[i] = (i != n) ? readIntSp(1, max_ai) : readIntLn(1, max_ai);
    cnt = 1;
    dfs1(1, 0);
    pref[0] = 0;
    suff[n+1] = 0;
    rep(i,1,n+1){
        pref[i] = __gcd(pref[i-1], A[ord[i]]);
    }
    repb(i,n,1){
        suff[i] = __gcd(suff[i+1], A[ord[i]]);
    }
    ans = 0;
    dfs2(1, 0);
    cout << ans << endl;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ll q = readIntLn(1, max_q);
    ll sum_n = 0;
    rlimit R;
    getrlimit(RLIMIT_STACK, &R);
    R.rlim_cur = R.rlim_max;
    setrlimit(RLIMIT_STACK, &R);
    while(q--){
        ll n = readIntLn(2, max_n);
        solve(n);
        sum_n += n;
    }
    assert(sum_n <= max_sum_n);
    assert(getchar()==-1);
}
``

</details>
