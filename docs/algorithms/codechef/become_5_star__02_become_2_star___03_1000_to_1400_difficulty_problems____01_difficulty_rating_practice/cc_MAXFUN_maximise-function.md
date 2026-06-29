# Maximise Function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXFUN |
| Difficulty Rating | 1301 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MAXFUN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MAXFUN) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$. Find the maximum value of the expression $|A_x-A_y| + |A_y-A_z| + |A_z-A_x|$ over all triples of pairwise distinct valid indices $(x, y, z)$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the maximum value of $|A_x-A_y| + |A_y-A_z| + |A_z-A_x|$.

### Constraints
- $1 \leq T \leq 5$
- $3 \leq N \leq 10^5$
- $|A_i| \leq 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $N \leq 500$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
3
2 7 5
3
3 3 3
5
2 2 2 2 5
```

**Output**

```text
10
0
6
```

**Explanation**

**Example case 1:** The value of the expression is always $10$. For example, let $x = 1$, $y = 2$ and $z = 3$, then it is $|2 - 7| + |7 - 5| + |5 - 2| = 5 + 2 + 3 = 10$.

**Example case 2:** Since all values in the sequence are the same, the value of the expression is always $0$.

**Example case 3:** One optimal solution is $x = 1$, $y=2$ and $z = 5$, which gives $|2 - 2| + |2 - 5| + |5 - 2| = 0 + 3 + 3 = 6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 7 5
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
3
3 3 3
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5
2 2 2 2 5
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXFUN)

[Div-1 Contest](https://www.codechef.com/FEB21A/problems/MAXFUN)

[Div-2 Contest](https://www.codechef.com/FEB21B/problems/MAXFUN)

[Div-3 Contest](https://www.codechef.com/FEB21C/problems/MAXFUN)

***Author:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Testers:*** [Felipe Mota ](https://www.codechef.com/users/fmota) and [Radoslav Dimitrov ](https://www.codechef.com/users/radoslav192)

***Editorialist:*** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Observations, Algebra

# PROBLEM:

Given a sequence A_1,A_2,…,A_N. Find the maximum value of the expression |A_x?A_y|+|A_y?A_z|+|A_z?A_x| over all triples of pairwise distinct valid indices (x,y,z).

# QUICK EXPLANATION

Find maximum and minimum element of the given sequence. Answer is always 2*(A_{max} - A_{min}).

# EXPLANATION

### Subtask 1

As N \le 500, Brute force solution should pass for subtask 1. Iterate over  all possible triplets, compute the value of the expression and take maximum of all.

Pseudocode
``ans = 0
for x in range(0, n):
	for y in range(x+1, n):
		for z in range(y+1, n):
			value = abs(A[x] - A[y]) + abs(A[y] - A[z]) + abs(A[z] - A[x])
			ans = max(ans, value)
print(ans)
``

Time Complexity: \mathcal{O}(N^3) for iterating over all triples.

Space Complexity: \mathcal{O}(1).

**Note**: the ans might **overflow int** in C++. Use long long int instead.

### Subtask 2

The above solution won’t pass for subtask 2 because N \le 10^5. The answer is always 2*(A_{max} - A_{min}). Lets prove!

Let the three chosen numbers be A_x, A_y, A_z such that A_x \le A_y \le A_z.

Here |A_x?A_y|=-(A_x-A_y) because A_x-A_y \le 0.

Similarly |A_y?A_z|=-(A_y-A_z)  and |A_z?A_x|=(A_z-A_x).

Now the expression is,

|A_x?A_y|+|A_y?A_z|+|A_z?A_x|

=-(A_x-A_y)-(A_y-A_z)+(A_z-A_x)

=A_y-A_x+A_z-A_y+A_z-A_x

=2*A_z - 2*A_x

=2*(A_z-A_x)

To maximize the expression 2*(A_z-A_x), A_z should be maximum possible and A_x should be minimum possible. Hence for maximum value of the expression,

A_z = A_{max} and A_x = A_{min}.

Similarly you can consider other cases and prove the same.

**Alternate(Geometrical) Approach**:

Think all N integers as 1D points on number line. Now if we take any three points A_x, A_y and A_z as shown in below figure

[

MAXFUN721×302 2.59 KB
](https://s3.amazonaws.com/discourseproduction/original/3X/7/d/7d3ecb9596f4dca7bceeba84e564c8391746096e.png)

See that clearly expression |A_x?A_y|+|A_y?A_z|+|A_z?A_x| = 2*|A_z-A_x|. Now to maximize, we should choose A_x = A_{min} and A_z = A_{max}.

Time Complexity: \mathcal{O}(N) for finding maximum and minimum element of the sequence.

Space Complexity: \mathcal{O}(1).

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

const int minv = -1e9, maxv = 1e9, maxt = 5, maxn[2] = {100000, 500};
vector<long long int> v;
void solve0(int n){
    sort(v.begin(), v.end());
    long long int ans = 2 * (v[n - 1] - v[0]);
    cout << ans << endl;
}
void solve1(int n){
    long long int ans = -1;
    for(int i = 0; i < n - 2; i++){
        for(int j = i + 1; j < n - 1; j++){
            for(int k = j + 1; k < n; k++){
                ans = max(ans, abs(v[i] - v[j]) + abs(v[j] - v[k]) + abs(v[k] - v[i]));
            }
        }
    }
    cout << ans << endl;
}
int main()
{
    int t; cin >> t;
    for(int i = 0; i < t; i++){
        v.clear();
        int n, x; cin >> n;
        for(int i = 0; i < n; i++){
            cin >> x;
            v.push_back(x);
        }
        if(n <= maxn[1]){
            solve1(n);
        }else{
            solve0(n);
        }
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
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t = readIntLn(1, 5);
	while(t--){
		int n = readIntLn(1, 100000);
		vector<int> a(n);
		for(int i = 0; i < n; i++){
			if(i != n - 1) a[i] = readIntSp(-1'000'000'000, 1'000'000'000);
			else a[i] = readIntLn(-1'000'000'000, 1'000'000'000);
		}
		sort(a.begin(), a.end());
		long long ans = 0;
		for(int i = 1; i + 1 < n; i++){
			ans = max(ans, (long long)(a[i] - a[0]) + (a.back() - a[i]) + a.back() - a[0]);
		}
		cout << ans << '\n';
	}
	return 0;
}

``

Editorialist's Solution
``/***************************************************

@author: vichitr
Compiled On: 06 Feb 2021

*****************************************************/
#include<bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int a[n];
    for(int i = 0; i < n; i++)
    	cin >> a[i];
    int minElement = a[0];
    int maxElement = a[0];
    for(int i = 1; i < n; i++){
    	minElement = min(minElement, a[i]);
    	maxElement = max(maxElement, a[i]);
    }
    long long int ans = 2LL * (maxElement - minElement);
    cout << ans <<'\n';
}

signed main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t = 1;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        solve();
    }
    return 0;
}
``

# VIDEO EDITORIAL:

</details>
