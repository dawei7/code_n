# Lunchtime

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUNCHTIM |
| Difficulty Rating | 1773 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [LUNCHTIM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/LUNCHTIM) |

---

## Problem Statement

There are $N$ students standing in a canteen queue, numbered $1$ to $N$ from left to right. For each valid $i$, the $i$-th student has a height $h_i$.

Two students $i$ and $j$ can see each other if there are no taller students standing between them. Formally, students $i$ and $j$ ($i \lt j$) can see each other if for each integer $k$ ($i \lt k \lt j$), $h_k \le h_i, h_j$.

For each valid $i$, determine the number $c_i$ of students that have the same height as student $i$ and can be seen by student $i$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $h_1, h_2, \ldots, h_N$.

### Output
For each test case, print a single line containing $N$ space-separated integers $c_1, c_2, \ldots, c_N$.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le h_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

### Subtasks
**Subtask #1 (30 points):** the sum of $N$ over all test cases does not exceed $10^3$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
5
1 2 2 3 2
```

**Output**

```text
0 1 1 0 0
```

**Explanation**

**Example case 1:** Student $3$ can see students $2$ and $4$, but only student $2$ has the same height (height $2$). On the other hand, student $3$ cannot see student $5$ since student $4$ is taller and therefore blocking the view.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LUNCHTIM)

[Contest: Division 1](https://www.codechef.com/LTIME94A/problems/LUNCHTIM)

[Contest: Division 2](https://www.codechef.com/LTIME94B/problems/LUNCHTIM)

[Contest: Division 2](https://www.codechef.com/LTIME94C/problems/LUNCHTIM)

***Author:***  Nguyen Gia Bao

***Testers:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant), [Aryan](https://www.codechef.com/users/aryanc403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

# DIFFICULTY:

Easy

# PREREQUISITES:

Stack

# PROBLEM:

N students stand in a queue, the i-th of them has height h_i. Students i and j (i < j) can see each other if h_k \leq min(h_i, h_j) for every i < k < j. Find, for each i, how many students of the same height as student i are visible to him?

# QUICK EXPLANATION:

- Use a stack to find, for each i, the closest student to the left and the right of i who has height \geq h_i.

- With this information, a simple linear dynamic programming solution finds the answer, iterating once from the left and once from the right.

# EXPLANATION:

**Subtask 1**

The condition about when students i and j can see each other can be stated as max(h_{i+1}, \dotsc, h_{j-1}) \leq min(h_i, h_j).

In the case when h_i = h_j, this is the same as max(h_i, h_{i+1}, \dotsc, h_{j-1}, h_j) = h_i

This lets us  solve the first subtask by bruteforcing every possible pair of students in \mathcal{O}(n^2). Fix the index of the left student, say i. Let m be the maximum of the current range; initially, m = h_i.

Now, iterate j from i+1 to n. If h_i = h_j, and m = h_i, increase the answer for both students i and j by 1. Finally, update m by setting m = max(m, h_j).

**Subtask 2**

\mathcal{O}(n^2) is too slow for this subtask - we need something faster.

Fix some student i. Let’s see if we can find out how many students he sees to his left quickly (denoted by left[i]).

Let j < i be the largest index such that h_j \geq h_i (denote jump\_left[i] = j). Suppose we are able to find this fast for every index i. Does this give us a way to solve the problem faster than \mathcal{O}(n^2)? Yes!

There are two cases:

-
h_j > h_i.

Here, student i doesn’t see anyone with the same height to his left, i.e, left[i] = 0.

Proof

Let k < i with h_k = h_i.

If k < j < i, clearly student j blocks k and i from seeing each other.

If j < k < i, j was not the maximum index of a student who is at least as tall as i - a contradiction. So this case cannot happen.

-
h_j = h_i

Here, left[i] = 1 + left[j].

Proof

Let k < i with h_k = h_i.

Of course, we must also have k \leq j - because j < k < i would contradict j being maximal.

If i and k can see each other, then clearly j and k can also see each other, because max(h_k, h_{k+1}, \dotsc, h_j) \leq max(h_k, h_{k+1}, \dotsc, h_j, \dotsc, h_i).

So, i sees everyone who j can see - and in addition, sees j as well.

Hence, left[i] = left[j] + 1.

Note that we assumed a suitable j exists.

What if no such j exists?

If no such j exists, that also means that there cannot be a student with the same height as i, to the left of student i. So, the answer for student i only depends on those on his right, meaning we can simply ignore any i where this is the case.

When no such j exists, set jump\_left[i] = -1.

Putting this together, we have the following solution:

- Find jump\_left[i] for every i.

How?

This is a classic problem which can be solved with a stack.

Let S be an empty stack.

For each i from 1 to N, do the following:

While the stack is not empty:

- Let j = S.top(). If h_j \geq h_i, break.

- Else, pop j from S and continue.

If the stack is empty, jump\_left[i] = -1.

Else jump\_left[i] = S.top().

Push i onto S.

- Iterate i from 1 to N. if jump\_left[i] = -1 or h_{jump\_left[i]} > h_i, set left[i] = 0. Else, set left[i] = 1 + left[jump\_left[i]].

Repeat this procedure from the right to find jump\_right[i] and right[i] for every 1\leq i\leq N.

The final answer for i is then left[i] + right[i].

# TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>

# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

FILE *fp;
ofstream outfile;

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

const int minv = 1, maxv = 1e9, maxt = 10, MAX = 100010;
const string newln = "\n", space = " ";

int main()
{
    int q = readIntLn(1, 10);
    // int q; cin >> q;
    while(q--){
        int n = readIntLn(1, MAX);
        // int n; cin >> n;
        vector<pii> v; v.clear();
        int a[n + 2]; a[0] = a[n + 1] = 0;
        for(int i = 1; i <= n; i++){
            int x = (i == n ? readIntLn(minv, maxv) : readIntSp(minv, maxv));
            // int x; cin >> x;
            a[i] = x;
            v.pb(mp(x, i));
        }
        sort(v.begin(), v.end(), [](const pii& A, const pii& B) {
            return A.first > B.first;
        });
        set<int> s; s.clear();
        set<int>::iterator it;
        s.insert(0); s.insert(n + 1);
        int id[n + 2][2];
        for(int i = 0; i < n;){
            int j = i;
            while(j < n && v[j].first == v[i].first){
                s.insert(v[j].second);
                j++;
            }
            j = i;
            while(j < n && v[j].first == v[i].first){
                it = s.lower_bound(v[j].second);
                it--;
                if(a[*it] == v[j].first)id[v[j].second][0] = *it;
                else id[v[j].second][0] = 0;
                it++; it++;
                if(a[*it] == v[j].first)id[v[j].second][1] = *it;
                else id[v[j].second][1] = n + 1;
                j++;
            }
            i = j;
        }
        int ans[n + 2][2];
        for(int i = 0; i < 2; i++){
            ans[0][i] = ans[n + 1][i] = 0;
        }
        for(int i = 1; i <= n; i++){
            // cerr << id[i][0] << " " << id[i][1] << endl;
            ans[i][0] = a[i] == a[id[i][0]] ? 1 + ans[id[i][0]][0] : 0;
        }
        for(int i = n; i >= 1; i--){
            ans[i][1] = a[i] == a[id[i][1]] ? 1 + ans[id[i][1]][1] : 0;
        }
        for(int i = 1; i <= n; i++){
            cout << ans[i][0] + ans[i][1] << (i == n ? newln : space);
        }
    }
    assert(getchar()==-1);
}
``

Tester's Solution
``//By TheOneYouWant
#pragma GCC optimize ("-O2")
#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0)

int main(){
    fastio;

    int tests;
    cin>>tests;

    while(tests--){
        int n;
        cin>>n;

        int h[n+1];
        // number of left seen and right seen of same height
        int le[n+1] = {0}, ri[n+1] = {0};
        // closest larger values to left and right
        int big_left[n+1] = {0}, big_right[n+1] = {0};

        for(int i = 1; i <= n; i++){
            cin>>h[i];
            big_right[i] = n+1;
        }
        map<int, int> last; // last seen of height

        stack<pair<int,int>> s;
        // now we will find closest element to left which is larger
        // well known stack solution
        for(int i = 1; i <= n; i++){
            while(!s.empty() && s.top().first <= h[i]){
                s.pop();
            }
            if(!s.empty()){
                big_left[i] = s.top().second;
            }
            s.push(make_pair(h[i], i));
            if(last[h[i]] != 0 && big_left[i] < last[h[i]]){
                le[i] = le[last[h[i]]] + 1;
            }
            last[h[i]] = i;
        }

        while(!s.empty()) s.pop();
        last.clear();

        for(int i = n; i >= 1; i--){
            while(!s.empty() && s.top().first <= h[i]){
                s.pop();
            }
            if(!s.empty()){
                big_right[i] = s.top().second;
            }
            s.push(make_pair(h[i], i));
            if(last[h[i]] != 0 && big_right[i] > last[h[i]]){
                ri[i] = ri[last[h[i]]] + 1;
            }
            last[h[i]] = i;
        }

        for(int i = 1; i <= n; i++) cout<<le[i] + ri[i]<<" ";
        cout<<endl;

    }

    return 0;
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,mmx,avx,avx2")
using namespace std;
using ll = long long;

int main()
{
    ios::sync_with_stdio(0); cin.tie(0);
    mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

    int q; cin >> q;
    while (q--) {
        int n; cin >> n;
        vector<int> h(n);
        for (auto &x : h)
            cin >> x;
        stack<int> s;
        vector<int> left_jump(n), right_jump(n);
        for (int i = 0; i < n; ++i) {
            while (!s.empty()) {
                auto pos = s.top();
                if (h[pos] >= h[i]) break;
                s.pop();
            }
            if (!s.empty()) left_jump[i] = s.top();
            else left_jump[i] = -1;
            s.push(i);
        }
        while (!s.empty()) s.pop();
        for (int i = n-1; i >= 0; --i) {
            while (!s.empty()) {
                auto pos = s.top();
                if (h[pos] >= h[i]) break;
                s.pop();
            }
            if (!s.empty()) right_jump[i] = s.top();
            else right_jump[i] = -1;
            s.push(i);
        }
        vector<int> see_left(n), see_right(n);
        for (int i = 0; i < n; ++i) {
            if (left_jump[i] == -1 or h[i] != h[left_jump[i]]) continue;
            see_left[i] = 1 + see_left[left_jump[i]];
        }
        for (int i = n-1; i >= 0; --i) {
            if (right_jump[i] == -1 or h[i] != h[right_jump[i]]) continue;
            see_right[i] = 1 + see_right[right_jump[i]];
        }
        for (int i = 0; i < n; ++i) {
            cout << see_left[i] + see_right[i] << ' ';
        }
        cout << '\n';
    }
}
``

</details>
