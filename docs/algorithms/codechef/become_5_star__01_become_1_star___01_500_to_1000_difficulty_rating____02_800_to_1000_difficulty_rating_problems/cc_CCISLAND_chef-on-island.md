# Chef On Island

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CCISLAND |
| Difficulty Rating | 878 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CCISLAND](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CCISLAND) |

---

## Problem Statement

Suppose Chef is stuck on an island and currently he has $x$ units of food supply and $y$ units of water supply in total that he could collect from the island. He needs $x_r$ units of food supply and $y_r$ units of water supply per day at the minimal to have sufficient energy to build a boat from the woods and also to live for another day. Assuming it takes exactly $D$ days to build the boat and reach the shore, tell whether Chef has the sufficient amount of supplies to be able to reach the shore by building the boat?

### Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, five integers $x, y, x_r, y_r, D$.

### Output:
For each testcase, output in a single line answer "YES" if Chef can reach the shore by building the boat and "NO" if not (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 300$
- $1 \leq x, y \leq 100$
- $1 \leq x_r, y_r, D \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 1 1 1
4 2 1 3 1
4 2 4 2 2
```

**Output**

```text
YES
NO
NO
```

**Explanation**

**TestCase 1:** Chef's food supply will last for $\frac{4}{1} = 4$ days and water supply will last for $\frac{2}{1} = 2$ days, so in total he will be able to survive for $min(4, 2) = 2$ days and since required time to reach the shore is $1$ day, he will be able to reach there.

**TestCase 2:** Chef's food supply will last for $\frac{4}{1} = 4$ days and water supply will last for $\frac{2}{3} = 0.67$ days, so in total he will be able to survive for $min(4, 0.67) = 0.67$ days and since required time to reach the shore is $1$ day, he won't be able to reach there.

**TestCase 3:** Chef's food supply will last for $\frac{4}{4} = 1$ day and water supply will also last for $\frac{2}{2} = 1$ day, so in total he will be able to survive for $min(1, 1) = 1$ day and since required time to reach the shore is $2$ days, he won't be able to reach there.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 1 1 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 2 1 3 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 2 4 2 2
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice ](https://www.codechef.com/problems/CCISLAND)

[Contest: Division 3 ](https://www.codechef.com/START3C/problems/CCISLAND)

[Contest: Division 2 ](https://www.codechef.com/START3B/problems/CCISLAND)

[Contest: Division 1 ](https://www.codechef.com/START3A/problems/CCISLAND)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

None

# PROBLEM:

Given x units of food and y units of water. You need x_r units of food and y_r units of water per day to work. If it takes D days to finish the work, would you be able to finish it with given amount of food and water?

# EXPLANATION:

Just check the condition as specified in the statement. If it takes D days to finish the work, and x_r units of food and y_r units of water are needed per day. Hence total of D \cdot x_r units of food and D \cdot y_r units of water are needed. Check if they are less than or equal to available amount ie check if D \cdot x_r \leq x and D \cdot y_r \leq y.

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>

# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 300, minv = 1, maxv = 10, mintv = 1, maxtv = 100;
const string newln = "\n", space = " ";

int main()
{
    int t; cin >> t;
    while(t--){
        int x, y, xr, yr, d; cin >> x >> y >> xr >> yr >> d;
        string ans = (min(x / xr, y / yr) >= d ? "YeS" : "No");
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
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t = readIntLn(1, 300);
	while(t--){
		int x = readIntSp(1, 100);
		int y = readIntSp(1, 100);
		int xr = readIntSp(1, 10);
		int yr = readIntSp(1, 10);
		int d = readIntLn(1, 10);
		for(int i = 0; i < d && x >= 0 && y >= 0; i++)
			x -= xr, y -= yr;
		cout << (x >= 0 && y >= 0 ? "YES\n" : "NO\n");
	}
	return 0;
}
``

Editorialist's Solution
``/***************************************************

@author: vichitr
Compiled On: 23 Apr 2021

*****************************************************/
#include<bits/stdc++.h>
using namespace std;

void solve(){
    int x, y, xr, yr, d;
    cin >> x >> y >> xr >> yr >> d;
    if(xr * d <= x and yr * d <= y)
        cout <<"YES\n";
    else
        cout <<"NO\n";
}

signed main()
{
    int t = 1;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        solve();
    }
    return 0;
}
``

</details>
