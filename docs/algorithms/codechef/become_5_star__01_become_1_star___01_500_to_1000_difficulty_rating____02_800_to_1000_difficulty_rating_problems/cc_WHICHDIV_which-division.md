# Which Division

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WHICHDIV |
| Difficulty Rating | 867 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [WHICHDIV](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/WHICHDIV) |

---

## Problem Statement

Given the rating $R$ of a person, tell which division he belongs to. The rating range for each division are given below:

- Division $1$: $2000 \le$ Rating.
- Division $2$: $1600 \le$ Rating $\lt 2000$.
- Division $3$: Rating $\lt 1600$.

---

## Input Format

- The first line of the input contains $T$ - the number of test cases. Then the test cases follow.
- Each testcase contains a single line of input, which contains a single integer $R$.

---

## Output Format

For each test case, output on a single line the answer: $1$ if the person belongs to Division $1$, $2$ if the person belongs to Division $2$, and $3$ if the person belongs to Division $3$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1000 \leq R \leq 4500$

---

## Examples

**Example 1**

**Input**

```text
3
1500
4000
1900
```

**Output**

```text
3
1
2
```

**Explanation**

**Test case $1$:** Since the rating of the person lies in the range $[1000, 1600)$, he belongs to Division $3$.

**Test case $2$:** Since the rating of the person lies in the range $[2000, 4500]$, he belongs to Division $1$.

**Test case $3$:** Since the rating of the person lies in the range $[1600, 2000)$, he belongs to Division $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1500
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4000
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
1900
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WHICHDIV)

[Contest: Division 1](https://www.codechef.com/COOK132A/problems/WHICHDIV)

[Contest: Division 2](https://www.codechef.com/COOK132B/problems/WHICHDIV)

[Contest: Division 3](https://www.codechef.com/COOK132C/problems/WHICHDIV)

***Author:*** [Arjun Arul](https://www.codechef.com/users/arjunarul)

***Tester:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the rating R of a person, output which division he belongs to.

#
[](#explanation-5)EXPLANATION:

Simply do exactly as the problem asks - input R, check which of the 3 ranges it lies in, and print the corresponding division. The simplest implementation of this is to use if-else statements.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#solutions-7)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
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

using namespace std;

FILE *fp;
ofstream outfile;

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        // char g=getchar();
        char g = getc(fp);
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
        // char g=getchar();
        char g=getc(fp);
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

const int maxt = 1000, minr = 1000, maxr = 4500;
const string newln = "\n", space = " ";

int main()
{
    int t, r; cin >> t;
    while(t--){
        cin >> r;
        int ans = 1;
        if(r < 1600)ans = 3;
        else if(r < 2000)ans = 2;
        cout << ans << endl;
    }
}
``

Tester's Solution
``//By TheOneYouWant
#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0)

int main(){
	fastio;

	int tests;
	cin >> tests;

	while(tests--){
		int r;
		cin >> r;
		if(r >= 2000){
			cout << 1 << endl;
		}
		else if(r >= 1600){
			cout << 2 << endl;
		}
		else{
			cout << 3 << endl;
		}
	}

	return 0;
}
``

Editorialist's Solution
``for _ in range(int(input())):
    rating = int(input())
    if rating >= 2000:
        print(1)
    elif rating >= 1600:
        print(2)
    else:
        print(3)
``

</details>
