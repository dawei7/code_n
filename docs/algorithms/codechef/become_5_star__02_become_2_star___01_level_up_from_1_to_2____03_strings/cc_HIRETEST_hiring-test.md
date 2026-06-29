# Hiring Test

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HIRETEST |
| Difficulty Rating | 1260 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [HIRETEST](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/HIRETEST) |

---

## Problem Statement

A company conducted a coding test to hire candidates. $N$ candidates appeared for the test, and each of them faced $M$ problems. Each problem was either unsolved by a candidate (denoted by 'U'), solved partially (denoted by 'P'), or solved completely (denoted by 'F').

To pass the test, each candidate needs to either solve $X$ or more problems completely, or solve $(X-1)$ problems completely, and $Y$ or more problems partially.

Given the above specifications as input, print a line containing $N$ integers. The $i^{th}$ integer should be $1$ if the $i^{th}$ candidate has passed the test, else it should be $0$.

###Input:

- The first line of the input contains an integer $T$, denoting the number of test cases.
- The first line of each test case contains two space-separated integers, $N$ and $M$, denoting the number of candidates who appeared for the test, and the number of problems in the test, respectively.
- The second line of each test case contains two space-separated integers, $X$ and $Y$, as described above, respectively.
- The next $N$ lines contain $M$ characters each. The $j^{th}$ character of the $i^{th}$ line denotes the result of the $i^{th}$ candidate in the $j^{th}$ problem. 'F' denotes that the problem was solved completely, 'P' denotes partial solve, and 'U' denotes that the problem was not solved by the candidate.

###Output:

For each test case, print a single line containing $N$ integers. The $i^{th}$  integer denotes the result of the $i^{th}$ candidate. $1$ denotes that the candidate passed the test, while $0$ denotes that he/she failed the test.

###Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $2 \le M \le 100$
- $1 \le X, Y \le M$
- $1 \le (X-1)+Y \le M$

---

## Examples

**Example 1**

**Input**

```text
3
4 5
3 2
FUFFP
PFPFU
UPFFU
PPPFP
3 4
1 3
PUPP
UUUU
UFUU
1 3
2 2
PPP
```

**Output**

```text
1100
101
0
```

**Explanation**

- **Sample Test 1:** There are $4$ candidates and $5$ problems. Each candidate needs to solve $3$ or more problems completely, or $2$ problems completely and $2$ or more problems partially. Only the first and the second candidates satisfy this.

- **Sample Test 2:** The candidates need to either solve at least one problem completely, or they need to solve three or more problems partially. Only candidates $1$ and $3$ satisfy this.

- **Sample Test 3:** The candidate needs to either solve two or more problems completely, or solve at least one problems completely and two problems partially. The candidate does not satisfy this.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice ](https://www.codechef.com/problems/HIRETEST)

[Contest: Division 3 ](https://www.codechef.com/START3C/problems/HIRETEST)

[Contest: Division 2 ](https://www.codechef.com/START3B/problems/HIRETEST)

[Contest: Division 1 ](https://www.codechef.com/START3A/problems/HIRETEST)

**Author:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

None

# PROBLEM:

Given N candidates appeared for the test, and each of them faced M problems. Each problem was either unsolved by a candidate (denoted by ‘U’), solved partially (denoted by ‘P’), or solved completely (denoted by ‘F’).

To pass the test, each candidate needs to either solve X or more problems completely, or solve (X?1) problems completely, and Y or more problems partially. Check if given candidates passed the test or not.

# QUICK EXPLANATION:

Just check the conditions as specified in the problem.

# EXPLANATION:

For a candidate, lets denote the count of problems solved completely by C_F, solved partially by C_P. Now check if (C_F \geq X) or (C_F \geq X-1 and C_P \geq Y).

# TIME COMPLEXITY:

O(N * M) if there are N candidates and M problems as we need to iterate through each candidate and find the count of problems solved full, solved partial.

# SOLUTIONS:

Setter's Solution
``//created by Whiplash99
import java.io.*;
import java.util.*;
class A
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int i,N;

        int T=Integer.parseInt(br.readLine().trim());
        StringBuilder sb=new StringBuilder();

        while (T-->0)
        {
            String[] s=br.readLine().trim().split(" ");
            N=Integer.parseInt(s[0]);
            int M=Integer.parseInt(s[1]);

            s=br.readLine().trim().split(" ");
            int X=Integer.parseInt(s[0]);
            int Y=Integer.parseInt(s[1]);

            for(i=0;i<N;i++)
            {
                char[] ch=br.readLine().trim().toCharArray();
                int full=0,partial=0;

                for(char c:ch)
                {
                    if(c=='F') full++;
                    else if(c=='P') partial++;
                }

                if(full>=X||(full==X-1&&partial>=Y)) sb.append(1);
                else sb.append(0);
            }

            sb.append("\n");
        }
        System.out.println(sb);
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
	int t = readIntLn(1, 100);
	while(t--){
		int n = readIntSp(1, 100);
		int m = readIntLn(1, 100);
		int x = readIntSp(1, m);
		int y = readIntLn(1, m);
		assert((x - 1) + y <= m);
		for(int i = 0; i < n; i++){
			string s = readStringLn(m, m);
			for(auto & c : s)
				assert(c == 'U' || c == 'P' || c == 'F');
			int f = count(s.begin(), s.end(), 'F');
			int p = count(s.begin(), s.end(), 'P');
			int has = 0;
			if(f >= x) has = 1;
			else if(f == x - 1 && p >= y) has = 1;
			cout << has;
		}
		cout << '\n';
	}
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
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    int x, y; cin >> x >> y;
    for(int i=0;i<n;i++){
        int p = 0, f = 0;
        string c; cin >> c;
        for(char j: c){
            if(j == 'P')
                p++;
            if(j == 'F')
                f++;
        }
        if(f >= x or (f == x - 1 and p >= y))
            cout <<"1";
        else
            cout <<"0";
    }
    cout << '\n';
}

signed main()
{
    int t=1;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        solve();
    }
    return 0;
}
``

</details>
