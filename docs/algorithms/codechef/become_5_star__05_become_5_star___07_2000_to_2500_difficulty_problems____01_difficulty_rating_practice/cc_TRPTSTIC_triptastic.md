# TripTastic

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRPTSTIC |
| Difficulty Rating | 2095 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [TRPTSTIC](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TRPTSTIC) |

---

## Problem Statement

A school wants to plan a trip for a group of $K$ students and **one** mentor.
A hotel is booked for their stay, where the rooms are formatted in form of a matrix $A$ with $N$ rows and $M$ columns. There are a total of $N\times M$ rooms where the room $(i, j)$ has a capacity of $A_{(i,j)}$ people.

The *distance* between the rooms $(i_1, j_1)$ and $(i_2, j_2)$ is given by $\max( |i_1-i_2| , |j_1-j_2| )$, where $|X|$ denotes the absolute value of $X$.

To ensure that the trip goes smoothly, the rooms should be booked in a way such that the *distance* between the mentor's room and the farthest room of a student is **minimal**.
Note that the mentor and students can stay in the **same** room.

Your task is to find the **minimal distance** between the mentor's room and the farthest room of a student.
In case the total capacity of the hotel is less than $K+1$, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
    - The first line of each test case contains three space-separated integers $N, M,$ and $K$ — the number of rows, columns, and students, respectively.
    - The next $N$ lines contain $M$ space-separated integers each, denoting the capacity of each room.

---

## Output Format

For each test case, output on a new line, the **minimal** distance between the mentor's room and the farthest room of a student.

In case the total capacity of the hotel is less than $K+1$, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N, M \leq 10^{6}$
- $1 \leq K \leq 10^{9}$
- $0 \leq A_{(i,j)} \leq 10^{5}$
- The sum of $N\cdot M$ over all test cases won't exceed $10^{6}$.

---

## Examples

**Example 1**

**Input**

```text
4
1 7 5
2 1 0 1 3 0 1
2 4 3
1 0 4 0
0 2 0 3
2 2 7
1 0
4 1
3 2 3
0 2
1 0
1 0
```

**Output**

```text
3
0
-1
1
```

**Explanation**

**Test case $1$:** Mentor can stay in room $(1, 2)$, two students in room $(1, 1)$, one student in room $(1, 4)$ and two students in room $(1, 5)$.
The farthest room of a student would be $(1, 5)$ with distance $3$.
We can show that in no other arrangement, we can achieve a distance less than $3$.

**Test case $2$:** Mentor and all $3$ students can stay in room $(1, 3)$. Thus, the distance is $0$.

**Test case $3$:** The hotel does not have enough capacity.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 7 5
2 1 0 1 3 0 1
2 4 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
1 0 4 0
0 2 0 3
2 2 7
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
1 0
4 1
3 2 3
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
0 2
1 0
1 0
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

[Practice](https://www.codechef.com/problems/TRPTSTIC)

[Contest: Division 1](https://www.codechef.com/START85A/problems/TRPTSTIC)

[Contest: Division 2](https://www.codechef.com/START85B/problems/TRPTSTIC)

[Contest: Division 3](https://www.codechef.com/START85C/problems/TRPTSTIC)

[Contest: Division 4](https://www.codechef.com/START85D/problems/TRPTSTIC)

***Authors:*** [d_k_7386](https://www.codechef.com/users/d_k_7386)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2095

#
[](#prerequisites-3)PREREQUISITES:

Binary search, [2D prefix sums](https://usaco.guide/silver/more-prefix-sums?lang=cpp#2d-prefix-sums)

#
[](#problem-4)PROBLEM:

K students and one mentor want to stay in a hotel that has N\times M rooms, arranged in N rows and M columns.

The room at the intersection of the i-th row and j-th column can accommodate A_{i, j} people; and the mentor can stay in the same room as a student.

The distance between two rooms (x_1, y_1) and (x_2, y_2) is \max(|x_1-x_2|, |y_1-y_2|).

Find the minimum possible possible distance between the mentor’s room and the farthest student’s room.

#
[](#explanation-5)EXPLANATION:

First, if the sum of all A_{i, j} is \leq K, then it’s impossible to accommodate K+1 people in the hotel, so the answer is -1.

Otherwise, a valid answer always exists.

Suppose we fix which room the mentor is staying in, say (x, y).

Note that this is only possible when A_{x, y} \neq 0.

Suppose we also fix the maximum allowed distance D between the mentor and a student.

Notice that with these two constraints, the set of cells where students are allowed to stay forms a rectangular subgrid of A, specifically,

- We want all cells (i, j) such that \max(|x-i|, |y-j|) \leq D. This means |x-i|\leq D and |y-j|\leq D.

- From the definition of absolute value, this means

- -D \leq x-i \leq D

-
-D\leq y-j \leq D.

- Rearrange this to

- x-D \leq i \leq x+D

-
y-D\leq j \leq y+D.

This gives us a range of i and j, forming the rectangle [x-D, x+D]\times [y-D, y+D].

In particular, if K+1 people can be fit into this rectangle, then it’s possible for the maximum distance to be *at most* D.

Checking whether K+1 people fit into this rectangle is simple to do in \mathcal{O}(1) after some precomputation.

Notice that we only want the sum of all values in the specified rectangle. This is doable with 2D prefix sums: a tutorial can be found [here](https://usaco.guide/silver/more-prefix-sums?lang=cpp#2d-prefix-sums).

We are now able to quickly check, for a fixed (x, y) and D, whether a maximum distance of \leq D is possible.

However, there are N\times M possible cells (x, y) and upto \max(N, M) values of D for each of them, so going through them all would still be too slow.

However, notice that if we’re able to achieve a maximum distance of \leq D, then of course we can achieve a maximum distance of \leq D+1.

So, we only need to find the *smallest* D such that there exists *some* cell (x, y) which satisfies the condition.

This is exactly what binary search does!

That gives us the following solution:

- Binary search on the value of D, from 0 to \max(N, M).

- For a fixed value of D, go through all cells (x, y) such that A_{x, y}\neq 0, and check whether any of them allow for a maximum distance of \leq D, using 2D prefix sums as discussed above.

For a fixed value of D, this takes \mathcal{O}(NM) time.

Since we’re applying binary search, we check only \mathcal{O}(\log\max(N, M)) values of D, for a solution that’s \mathcal{O}(NM\log\max(N, M)).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(NM\log\max(N, M)) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#define ll long long int
#include<bits/stdc++.h>
#define loop(i,a,b) for(ll i=a;i<b;++i)
#define rloop(i,a,b) for(ll i=a;i>=b;i--)
#define in(a,n) for(ll i=0;i<n;++i) cin>>a[i];
#define pb push_back
#define mk make_pair
#define all(v) v.begin(),v.end()
#define dis(v) for(auto i:v)cout<<i<<" ";cout<<endl;
#define display(arr,n) for(int i=0; i<n; i++)cout<<arr[i]<<" ";cout<<endl;
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);srand(time(NULL));
#define l(a) a.length()
#define s(a) (ll)a.size()
#define fr first
#define sc second
#define mod 1000000007
#define endl '\n'
#define yes cout<<"Yes"<<endl;
#define no cout<<"No"<<endl;
using namespace std;
#define debug(x) cerr << #x<<" "; _print(x); cerr << endl;
void _print(ll t) {cerr << t;}
void _print(int t) {cerr << t;}
void _print(string t) {cerr << t;}
void _print(char t) {cerr << t;}
void _print(double t) {cerr << t;}
template <class T, class V> void _print(pair <T, V> p);
template <class T> void _print(vector <T> v);
template <class T> void _print(set <T> v);
template <class T, class V> void _print(map <T, V> v);
template <class T> void _print(multiset <T> v);
template <class T, class V> void _print(pair <T, V> p) {cerr << "{"; _print(p.fr); cerr << ","; _print(p.sc); cerr << "}";}
template <class T> void _print(vector <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(set <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(multiset <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T, class V> void _print(map <T, V> v) {cerr << "[ "; for (auto i : v) {_print(i); cerr << " ";} cerr << "]";}

ll add(ll x,ll y)  {ll ans = x+y; return (ans>=mod ? ans - mod : ans);}
ll sub(ll x,ll y)  {ll ans = x-y; return (ans<0 ? ans + mod : ans);}
ll mul(ll x,ll y)  {ll ans = x*y; return (ans>=mod ? ans % mod : ans);}

void solve(){
    ll n,m,k;   cin>>n>>m>>k;
    vector<vector<ll>> v(n,vector<ll>(m));
    loop(i,0,n) loop(j,0,m) cin>>v[i][j];
    vector<vector<ll>> vec = v;
    loop(i,1,n) v[i][0]+=v[i-1][0];
    loop(j,1,m) v[0][j]+=v[0][j-1];
    loop(i,1,n) loop(j,1,m) v[i][j]+=v[i-1][j]+v[i][j-1]-v[i-1][j-1];
    ll ans = INT_MAX;
    loop(i,0,n){
        loop(j,0,m){
            if(!vec[i][j])  continue;
            ll l = 0,r = max(n,m);
            while(l<=r){
                ll mid = (l+r)/2;
                ll x = min(n-1,i+mid),y = min(m-1,j+mid);
                ll sum = v[x][y];
                if(i-mid>0) sum-=v[i-mid-1][y];
                if(j-mid>0) sum-=v[x][j-mid-1];
                if(i-mid>0 && j-mid > 0)    sum+=v[i-mid-1][j-mid-1];
                if(sum>=k+1)    r = mid-1,ans = min(ans,mid);
                else l = mid+1;
            }
        }
    }
    if(ans == INT_MAX)  ans = -1;
    cout<<ans<<endl;
}

int main()
{
    fast
    int t; cin>>t;

    while(t--) solve();
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    int snm = 0;
    while (tt--) {
        int n = in.readInt(1, 1e6);
        in.readSpace();
        int m = in.readInt(1, 1e6);
        in.readSpace();
        int k = in.readInt(1, 1e9);
        in.readEoln();
        snm += n * m;
        vector<vector<int>> a(n);
        for (int i = 0; i < n; i++) {
            a[i] = in.readInts(m, 0, 1e5);
            in.readEoln();
        }
        {
            long long s = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    s += a[i][j];
                }
            }
            if (s < k + 1) {
                cout << -1 << '\n';
                continue;
            }
        }
        vector<vector<long long>> b(n + 1, vector<long long>(m + 1));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                b[i + 1][j + 1] = b[i + 1][j] + b[i][j + 1] - b[i][j] + a[i][j];
            }
        }
        int low = -1, high = n + m;
        while (high - low > 1) {
            int mid = (high + low) >> 1;
            int ok = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (a[i][j]) {
                        int i0 = min(i + mid + 1, n);
                        int j0 = min(j + mid + 1, m);
                        int i1 = max(i - mid, 0);
                        int j1 = max(j - mid, 0);
                        if (b[i0][j0] - b[i0][j1] - b[i1][j0] + b[i1][j1] > k) {
                            ok = 1;
                        }
                    }
                }
            }
            if (ok) {
                high = mid;
            } else {
                low = mid;
            }
        }
        cout << high << '\n';
    }
    assert(snm <= 1e6);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n, m, k = map(int, input().split())
	grid = [ [0 for i in range(m+1) ] ]
	for i in range(1, n+1): grid.append([0] + list(map(int, input().split())))

	pref = [ [0 for i in range(m+1)] for j in range(n+1)]
	for i in range(1, n+1):
		for j in range(1, m+1):
			pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + grid[i][j]
	if pref[n][m] <= k:
		print(-1)
		continue

	def getsum(l1, r1, l2, r2):
		return pref[l2][r2] - pref[l1-1][r2] - pref[l2][r1-1] + pref[l1-1][r1-1]

	lo, hi = -1, n+m+1
	while lo+1 < hi:
		mid = (lo + hi)//2
		mxsum = 0
		for i in range(1, n+1):
			for j in range(1, m+1):
				if grid[i][j] == 0: continue
				l1 = max(1, i-mid)
				l2 = min(n, i+mid)
				r1 = max(1, j-mid)
				r2 = min(m, j+mid)
				mxsum = max(mxsum, getsum(l1, r1, l2, r2))
		if mxsum <= k: lo = mid
		else: hi = mid
	print(hi)
``

</details>
