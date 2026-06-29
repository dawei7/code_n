# Maximum Size

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RISK |
| Difficulty Rating | 2113 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [RISK](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/RISK) |

---

## Problem Statement

Chef is playing an easier variation of the board game ‘Risk’ with his friend Mike. There is an $N * M$ grid, depicting the world map. Each cell of the grid is either $1$ or $0$ where $1$ denotes that there is land on this cell, while $0$ denotes water.

In a turn, a player can capture an uncaptured cell that has land, and keep capturing neighbouring cells that share a side with it if they are on land. A cell once captured by a player can't be captured again by another player. The game continues till no uncaptured cell has land. Each player wants to be in control of as many cells of land as possible in total when the game finishes. Find the maximum number of cells of land that Chef can capture if he plays second, and both players play optimally.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains $N + 1$ lines of input.
- First line will contain $2$ space separated integers $N$ and $M$ denoting the size of the grid.
- Each of the next $N$ lines contains a binary string of length $M$ depicting the map.

###Output:
For each testcase, output in a single line answer to the problem.

###Constraints
- $1 \leq N, M \leq 10^5$
- Each character in the grid is either $0$ or $1$
- There's atleast $1$ land on the grid
- Sum of $N * M$ over all testcases is almost $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
4 4
1001
0110
0110
1001
2 2
11
11
3 3
100
010
001
```

**Output**

```text
2
0
1
```

**Explanation**

In **test case 1**, if both players play optimally, it takes $5$ steps to finish the game:

**Step 1:** First Mike chooses the cells $\{(2, 2), (2, 3), (3, 2), (3, 3)\}$ adding $4$ to his score.

**Step 2:** Second Chef chooses the cell $\{(1, 1)\}$ adding $1$ to his score.

**Step 3:** Next Mike chooses the cell $\{(1, 4)\}$ adding $1$ to his score.

**Step 4:** Next Chef chooses the cell $\{(4, 1)\}$ adding $1$ to his score.

**Step 5:** Finally, Mike chooses the cell $\{(4, 4)\}$ adding $1$ to his score.

Hence total score of Chef is $1 + 1 = 2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 4
1001
0110
0110
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1001
2 2
11
11
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 3
100
010
001
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice ](https://www.codechef.com/problems/RISK)

[Contest: Division 3 ](https://www.codechef.com/START3C/problems/RISK)

[Contest: Division 2 ](https://www.codechef.com/START3B/problems/RISK)

[Contest: Division 1 ](https://www.codechef.com/START3A/problems/RISK)

**Author:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

EASY

# PREREQUISITES:

DFS, BFS, Connected Components

# PROBLEM:

Given a binary grid. 1 shows land and 0 shows water.

In a turn, a player can capture an uncaptured cell that has land, and keep capturing neighboring cells sharing a side if they are also land. The game continues till no uncaptured cell has land and each player wants to capture as big size of land as possible in total when the game finishes. Find the maximum size of land that Chef can capture (in number of cells) if he plays second, and both players play optimally.

# QUICK EXPLANATION:

Run BFS or DFS and find sizes of all connected components with all ones. Sort the sizes array in decreasing order. Finally find the sum of alternate elements starting from index 1.

# EXPLANATION:

In each turn, one player can start capturing a cell with value 1 and he will keep capturing until he keeps finding 1. So basically, the player captures one whole connected component in one turn.

As both players play optimally, first player will always try to get bigger components, similarly the second player. Hence largest component will be captured by first player, second largest by second player, third largest by first player again, fourth largest by second player again and so on.

Hence we can find the sizes of all connected components with all ones. And sort the size array in decreasing order. Then find sum of alternate elements starting with index 1. (Assuming 0-based indexing).  This will give us the total sum, second player can achieve.

# TIME COMPLEXITY:

O(n \cdot m \cdot \log{(n \cdot m)}) per test case

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
#define pb push_back
#define ll long long int
#define pii pair<int, int>

using namespace std;

const int maxn = 1e5;
const int maxm = 1e5;
const int maxtnm = 1e6;
int del[][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
int main()
{

    int t, tot = 0; cin >> t;
    while(t--){
        int n, m; cin >> n >> m; tot += n * m;
        vector<string> v; v.clear();
        bool visit[n][m];
        string s;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                visit[i][j] = false;
            }
            cin >> s;
        	v.pb(s);
        }
        int queue[n * m], now = 0, end = 0;
        int comp = 0, cnt = 0;
        vector<int> arr; arr.clear();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(visit[i][j] || !(v[i][j] - '0'))continue;
                comp++; cnt = 0;
                queue[end++] = m * i + j; visit[i][j] = true;
                while(now < end){
                    cnt++;
                    int u = queue[now];
                    int nj = u % m, ni = u / m;
                    for(int k = 0; k < 4; k++){
                        int ui = ni + del[k][0], uj = nj + del[k][1];
                        if(ui >= n || uj >= m || ui < 0 || uj < 0)continue;
                        if(visit[ui][uj] || !(v[ui][uj] - '0'))continue;
                        queue[end++] = m * ui + uj; visit[ui][uj] = true;
                    }
                    ++now;
                }
                arr.pb(cnt);
            }
        }
        sort(arr.begin(), arr.end(), greater<int>());
        assert(arr.size());
        int ans = 0;
        for(int i = 1; i < arr.size(); i += 2){
            ans += arr[i];
        }
        cout << ans << endl;
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
template<typename T = int> vector<T> create(size_t n){ return vector<T>(n); }
template<typename T, typename... Args> auto create(size_t n, Args... args){ return vector<decltype(create<T>(args...))>(n, create<T>(args...)); }
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
long long TEN(int p){ long long r = 1; while(p--) r *= 10; return r; }
struct union_find {
    vector<int> parent;
    int n;
    union_find(int n) : n(n) { clear(); }
    inline void clear(){ parent.assign(n, -1); }
    inline int find(int u){ return (parent[u] < 0) ? u : parent[u] = find(parent[u]); }
    inline bool same(int u, int v){ return find(u) == find(v); }
    inline bool join(int u, int v){
        u = find(u);
        v = find(v);
        if (u != v){
            if (parent[u] > parent[v])
                swap(u, v);
            parent[u] += parent[v];
            parent[v] = u;
        }
        return u != v;
    }
    inline int size(int u){ return -parent[find(u)]; }
};
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t = readIntLn(1, 100000); // ????
	int sum_nm = 0;
	while(t--){
		int n = readIntSp(1, TEN(5)), m = readIntLn(1, TEN(5));
		sum_nm += n * m;
		int q1 = 0;
		vector<string> grid(n);
		for(int i = 0; i < n; i++){
			grid[i] = readStringLn(m, m);
			for(auto & c : grid[i])
				assert(c == '0' || c == '1');
			q1 += count(grid[i].begin(), grid[i].end(), '1');
		}
		assert(q1 > 0);
		union_find uf(n * m);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				for(int di : {0, 1})
					for(int dj : {0, 1})
						if(abs(di) + abs(dj) == 1){
							int ni = i + di, nj = j + dj;
							if(ni >= 0 && ni < n && nj >= 0 && nj < m){
								if(grid[i][j] == grid[ni][nj]){
									uf.join(i * m + j, ni * m + nj);
								}
							}
						}
		vector<int> szs;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(grid[i][j] == '1' && uf.find(i * m + j) == i * m + j){
					szs.push_back(uf.size(i * m + j));
				}
		sort(szs.rbegin(), szs.rend());
		int ans = 0;
		for(int i = 1; i < szs.size(); i += 2)
			ans += szs[i];
		cout << ans << '\n';
	}
	assert(sum_nm <= TEN(6));
	assert(getchar() == -1);
	return 0;
}
``

Editorialist's Solution
``/***************************************************

@author: vichitr
Compiled On: 23 Apr 2021

*****************************************************/
#include<bits/stdc++.h>
#define MAX 9223372036854775807
#define endl "\n"
#define ll long long
#define int long long
// #define double long double
#define pb push_back
#define pf pop_front
#define mp make_pair
#define ip pair<int, int>
#define F first
#define S second

#define loop(i,n) for(int i=0;i<n;i++)
#define loops(i,s,n) for(int i=s;i<=n;i++)
#define fast ios::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL)
using namespace std;

// #include <ext/pb_ds/assoc_container.hpp> // Common file
// #include <ext/pb_ds/tree_policy.hpp>     // Including tree_order_statistics_node_updat
// using namespace __gnu_pbds;
// typedef tree<ip, null_type, less_equal<ip>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

// order_of_key (k) : Number of items strictly smaller than k .
// find_by_order(k) : K-th element in a set (counting from zero).

const ll MOD = 1e9+7;
const ll SZ = 107;
const ll N = 1e6+7;
const ll M = 1e4+7;

int n, m, c;

void dfs(int x, int y, vector<string> &g, vector<vector<bool>> &vis){
    if(x < 0 or x >= n or y < 0 or y >= m or vis[x][y] or g[x][y] == '0')
        return;
    vis[x][y] = 1;
    c++;
    dfs(x-1, y, g, vis);
    dfs(x+1, y, g, vis);
    dfs(x, y-1, g, vis);
    dfs(x, y+1, g, vis);
}

void solve(){
    cin>>n>>m;
    vector<string> g(n);
    vector<vector<bool>> vis(n, vector<bool>(m, 0));
    loop(i, n) cin >> g[i];
    vector<int> comps;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!vis[i][j]){
                c = 0;
                dfs(i, j, g, vis);
                comps.pb(c);
            }
        }
    }
    sort(comps.begin(), comps.end());
    reverse(comps.begin(), comps.end());
    int ans = 0;
    for(int i=1;i<comps.size(); i+=2)
        ans += comps[i];
    cout << ans << '\n';
}

signed main()
{
    // fast;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t=1;
    cin >>t;
    for(int i=1;i<=t;i++)
    {
        // cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

``

</details>
