# Chef and Riffles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RIFFLES |
| Difficulty Rating | 2360 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [RIFFLES](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/RIFFLES) |

---

## Problem Statement

Let $f$ be a [permutation](https://en.wikipedia.org/wiki/Permutation) of length $N$, where $N$ is **even**. The *riffle* of $f$ is defined to be the permutation
$$g = (f(1), f(3), \ldots, f(N-1), f(2), f(4), \ldots, f(N))$$

You are given two integers $N$ and $K$. Output the resultant permutation when you riffle the identity permutation of length $N$, $K$ times.

The identity permutation of length $N$ is ${\sigma}_N = (1, 2, \ldots, N)$

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing two space-separated integers $N$ and $K$.

---

## Output Format

For each test case, output the answer permutation as $N$ space-separated integers in a new line.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 3 \cdot 10^5$
- $1 \leq K \leq 10^9$
- $N$ is even
- The sum of $N$ across test cases does not exceed $3 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
6 1
8 2
14 452
```

**Output**

```text
1 3 5 2 4 6
1 5 2 6 3 7 4 8
1 10 6 2 11 7 3 12 8 4 13 9 5 14
```

**Explanation**

**Test case $1$:** Performing the riffle on $\sigma_6 = (1, 2, 3, 4, 5, 6)$ once results in $(1, 3, 5, 2, 4, 6)$, by definition.

**Test case $2$:** The process goes as follows:
- Performing the riffle on $(1, 2, 3, 4, 5, 6, 7, 8)$ results in $(1, 3, 5, 7, 2, 4, 6, 8)$
- Performing the riffle on $(1, 3, 5, 7, 2, 4, 6, 8)$ results in $(1, 5, 2, 6, 3, 7, 4, 8)$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 1
```

**Output for this case**

```text
1 3 5 2 4 6
```



#### Test case 2

**Input for this case**

```text
8 2
```

**Output for this case**

```text
1 5 2 6 3 7 4 8
```



#### Test case 3

**Input for this case**

```text
14 452
```

**Output for this case**

```text
1 10 6 2 11 7 3 12 8 4 13 9 5 14
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JAN221A/problems/RIFFLES)

[Contest Division 2](https://www.codechef.com/JAN221B/problems/RIFFLES)

[Contest Division 3](https://www.codechef.com/JAN221C/problems/RIFFLES)

**Setter:** [Aryan Agarwala](https://www.codechef.com/users/aryanag_adm)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Venkata Nikhil Medam](https://www.codechef.com/users/nikhil_medam)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

[Permutation Cycles](https://en.wikipedia.org/wiki/Cyclic_permutation)

#
[](#problem-4)PROBLEM:

For a permutation f of length N (given N is **even**), a riffle is defined as the permutation g = (f(1), f(3), …, f(N-1), f(2), f(4), …, f(N)).

Given two numbers N and K, find the resultant permutation, when you riffle the identity permutation of length N, K times.

The identity permutation of length N is (1, 2, 3, …, N).

#
[](#quick-explanation-5)QUICK EXPLANATION:

- Define the riffle permutation g, such that after one riffle, f(i) \rightarrow f(g(i)).

- Decompose the identity permutation into disjoint cycles.

- For any cycle, an edge a \rightarrow b implies that the element at position a moves to position b in one riffle.

- For a cycle, if an element is present at position cycle[i] initially, then, after K riffles, its position would be cycle[(i + K) \% (cycle\_len)].

#
[](#explanation-6)EXPLANATION:

Observation

Let us look at some smaller values of N and apply riffles to the corresponding identity permutations.

N = 4

(1, 2, 3, 4) \rightarrow (1, 3, 2, 4) \rightarrow (1, 2, 3, 4)

We get after the identity permutation after 2 riffles.

N = 6

(1, 2, 3, 4, 5, 6) \rightarrow (1, 3, 5, 2, 4, 6) \rightarrow (1, 5, 4, 3, 2, 6) \rightarrow (1, 4, 2, 5, 3, 6) \rightarrow (1, 2, 3, 4, 5, 6)

We get after the identity permutation after 4 riffles.

After a certain number of riffles, we reach the identity permutation again.

Let us look at the journey of a particular element. After each riffle, we can determine its next position based on its current position. After a certain amount of riffles, the element reaches its initial position. Thus, each element moves in a cycle.

**Defining the riffle permutation:** We know that the riffle permutation is defined as g =  (f(1), f(3), …, f(N-1), f(2), f(4), …, f(N)). By observation, we can define this formally as:

- If i is odd (1 \leq i \leq N), g( (i+1)/2 ) = i.

- If i is even (1 \leq i \leq N), g( i/2 + N/2) = i.

We decompose the permutation into disjoint cycles and calculate the final position of each element in a particular cycle. An interesting thing to note is that, the number of riffles required to reach back to the identity permutation is nothing but the lcm of all the cycle lengths.

**Decomposing the permutation:** Iterate over all the elements, if the current element is not visited, we start a cycle from this element. Store all the elements of the current cycle, simultaneously marking them visited.

Let us assume a cycle of length m, as,  a_0 \rightarrow a_1 \rightarrow a_2 \rightarrow … \rightarrow a_{m-1} \rightarrow a_0

Suppose, we want to find the final position of the element currently at position a_i (0 \leq i < m) after K riffles. Since the cycle has length m, the element at position i moves to position a_{(i + K) \% m}.

Example

Let us take an example of the identity permutation of length 8, i.e., (1, 2, 3, 4, 5, 6, 7, 8). The riffle for this permutation would be (1, 3, 5, 7, 2, 4, 6, 8).

The disjoint cycles would be:

- 1 \rightarrow 1

- 2 \rightarrow 3 \rightarrow 5 \rightarrow 2

- 4 \rightarrow 7 \rightarrow 6 \rightarrow 4

- 8 \rightarrow 8

Now suppose an element is initially at position 2 (which is present at index 0 of second cycle). After 10 riffles, the element moves to (0+10) \% 3 = 1, the first index. Here, it refers to the third position.

Alternate solution using Binary Exponentiation

- Consider the permutation U =  (1, 3, 5, …, N-1, 2, 4, …, N).

- Applying a riffle to permutation f is just f composed with U.

- Therefore, applying K riffles is f composed with U^K.

- In this case, f is the identity permutation. Thus, we just want U^K.

- We can compose permutations in O(N) trivially.

- Permutation composition is associative, so we can use the binary exponentiation algorithm to find U^K in O(Nlog(N)).

See setter’s solution for implementation details.

#
[](#time-complexity-7)TIME COMPLEXITY:

The time complexity is O(N) per test case.

#
[](#solution-8)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//#include <sys/resource.h>
#define int long long
#define initrand mt19937 mt_rand(time(0));
#define rand mt_rand()
#define MOD 1000000007
#define INF 1000000000
#define mid(l, u) ((l+u)/2)
#define rchild(i) (i*2 + 2)
#define lchild(i) (i*2 + 1)
#define lz lazup(l, u, i);
#define ordered_set tree<pair<int, int>, null_type,less<pair<int, int>>, rb_tree_tag,tree_order_statistics_node_update>
using namespace std;
using namespace __gnu_pbds;
int n;
vector<int> unit;
vector<int> ans;
void riffle(vector<int> a, vector<int> &b){
    vector<int> x;
    for(int i = 0;i<n;i++){
        x.push_back(a[b[i]]);
    }
    b.clear();
    for(int i: x){
        b.push_back(i);
    }
}
void exp(int p){
    if(p==0) return;
    exp(p/2);
    riffle(ans, ans);
    if(p%2){
        riffle(unit, ans);
    }
}
signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin>>t;
    int sumn = 0;
    assert(1<=t && t<=100);
    while(t--){
        int k;
        cin>>n>>k;
        sumn += n;
        assert(1<=n && n<=3e5);
        assert(1<=sumn && sumn<=3e5);
        assert(1<=k && k<=1e9);
        assert(n%2 == 0);

        unit.clear();
        ans.clear();
        for(int i = 0;i<n/2;i++) unit.push_back(i*2);
        for(int i = n/2;i<n;i++) unit.push_back(1 + (i-n/2)*2);
        for(int i =0 ;i<n;i++) ans.push_back(i);
        exp(k);
        for(int i =0 ;i<n;i++) cout<<(ans[i]+1)<<" ";
        cout<<endl;
    }
}
``

Tester's Solution
``#include<bits/stdc++.h>
#pragma GCC optimize ("-O3")
using namespace std;
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long
#define double long double
const int N = 3e5 + 5;
int t, n, k, a[N];
int32_t main()
{
    IOS;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        map<int, int> nxt;
        map<int, bool> vis;
        for (int i = 1; i <= n; i++) {
            if (i % 2) {
                nxt[i] = (i + 1) / 2;
            }
            else {
                nxt[i] = (i + n) / 2;
            }
        }
        for (int i = 1; i <= n; i++) {
            if (vis[i]) {
                continue;
            }
            vector<int> cycle;
            int cur = i;
            while (nxt[cur] != i) {
                vis[cur] = true;
                cycle.push_back(cur);
                cur = nxt[cur];
            }
            vis[cur] = true;
            cycle.push_back(cur);
            int cycle_size = cycle.size();
            int rem = k % cycle_size;
            for (int j = 0; j < cycle_size; j++) {
                int val = cycle[j];
                int idx = cycle[(j + rem) % cycle_size];
                a[idx] = val;
            }
        }
        for (int i = 1; i <= n; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define sync {ios_base ::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);}
#define rep(n) for(int i = 0;i<n;i++)
#define rep1(a,b) for(int i = a;i<b;i++)
#define int long long int
#define mod 1000000007

int n, k;

void solve()
{
    cin>>n>>k;
    vector<int> next(n+1, 0);
    vector<int> ans(n+1, 0);
    vector<bool> vis(n+1, false);

    for (int i = 1; i <= n; i++) {
        if(i%2){
            next[i/2 + 1] = i;
        }
        else{
            next[i/2 + n/2] = i;
        }
    }

    for(int i = 1; i<=n; i++){
        if(!vis[i]){
            vector<int> cycle;
            int curr = i;
            vis[curr] = true;
            cycle.push_back(curr);
            while(next[curr] != i){
                curr = next[curr];
                vis[curr] = true;
                cycle.push_back(curr);
            }
            int cycle_len = cycle.size();
            for(int j = 0; j<cycle_len; j++){
                ans[cycle[j]] = cycle[(j+k)%cycle_len];
            }
        }
    }

    for(int i = 1; i<=n; i++){
        cout<<ans[i]<<' ';
    }
}

int32_t main()
{

    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    sync;
    int t = 1;
    cin>>t;
    while(t--){
        solve();
        cout<<"\n";
    }
    return 0;
}
``

</details>
