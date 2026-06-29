# Highest Divisor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HDIVISR |
| Difficulty Rating | 860 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [HDIVISR](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/HDIVISR) |

---

## Problem Statement

You are given an integer $N$. Find the largest integer between $1$ and $10$ (inclusive) which divides $N$.

### Input
The first and only line of the input contains a single integer $N$.

### Output
Print a single line containing one integer ― the largest divisor of $N$ between $1$ and $10$.

### Constraints
- $2 \leq N \leq 1,000$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
91
```

**Output**

```text
7
```

**Explanation**

The divisors of $91$ are $1, 7, 13, 91$, out of which only $1$ and $7$ are in the range $[1, 10]$. Therefore, the answer is $\max(1, 7) = 7$.

**Example 2**

**Input**

```text
24
```

**Output**

```text
8
```

**Explanation**

The divisors of $24$ are $1, 2, 3, 4, 6, 8, 12, 24$, out of which $1, 2, 3, 4, 6, 8$ are in the range $[1, 10]$. Therefore, the answer is $\max(1, 2, 3, 4, 6, 8) = 8$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/HDIVISR)

[Div-1 Contest](https://www.codechef.com/FEB21A/problems/HDIVISR)

[Div-2 Contest](https://www.codechef.com/FEB21B/problems/HDIVISR)

[Div-3 Contest](https://www.codechef.com/FEB21C/problems/HDIVISR)

***Author:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Testers:*** [Felipe Mota ](https://www.codechef.com/users/fmota) and [Radoslav Dimitrov ](https://www.codechef.com/users/radoslav192)

***Editorialist:*** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Given an integer N. Find the largest integer between 1 and 10 (inclusive) which divides N.

# EXPLANATION

Our task is to find the largest integer between 1 and 10 which divides N. So iterate over all integers between 1 and 10 and check if they divide N. Finally take maximum integer out of them who divides N.

Other possible way is to iterate from 10 to 1 and print first integer who divides N as that would be largest integer between 1 to 10 dividing N.

Time Complexity: \mathcal{O}(1) as we run a loop for constant (10) times only.

Space Complexity: \mathcal{O}(1)  as no extra space is used.

# SOLUTIONS:

Setter's Solution
``# include<bits/stdc++.h>

using namespace std;

const int minv = 2, maxv = 1000;

int main()
{
    int n, ans = 1; cin >> n;
    for(int i = 10; i >= 1; i--){
        if(n % i == 0){
            ans = i; break;
        }
    }
    cout << ans << endl;
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
	int n = readIntLn(1, 1000);
	for(int i = 10; i >= 1; i--){
		if(n % i == 0){
			cout << i << '\n';
			return 0;
		}
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
    int n; cin>>n;
    for(int i=10;i>=1;i--){
        if(n%i == 0){
            cout<<i;
            break;
        }
    }
}

signed main()
{
    int t=1;
    // cin >>t;
    for(int i=1;i<=t;i++)
    {
        solve();
    }
    return 0;
}
``

# VIDEO EDITORIAL:

</details>
