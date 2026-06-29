# A Subtask Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBTASK |
| Difficulty Rating | 1217 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [SUBTASK](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/SUBTASK) |

---

## Problem Statement

Chef recently solved his first problem on CodeChef. The problem he solved has $N$ test cases. He gets a score for his submission according to the following rules:

1) If Chef’s code passes all the $N$ test cases, he gets $100$ points.

2) If Chef’s code does not pass all the test cases, but passes all the **first** $M\;(M \lt N)$ test cases, he gets $K\;(K \lt 100)$ points.

3) If the conditions $1$ and $2$ are not satisfied, Chef does not get any points (i.e his score remains at $0$ points).

You are given a binary array $A_1, A_2, \dots, A_N$ of length $N$, where $A_i = 1$ denotes Chef's code passed the $i^{th}$ test case, $A_i = 0$ denotes otherwise. You are also given the two integers $M, K$. Can you find how many points does Chef get?

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case contains three space-separated integers $N, M, K$.
- The second line contains $N$ space-separated integer $A_1, A_2,\dots, A_N$.

---

## Output Format

For each testcase, output in a single line the score of Chef.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 100$
- $1 \leq M \lt N$
- $1 \leq K \lt 100$
- $0 \leq A_i \leq 1$

---

## Examples

**Example 1**

**Input**

```text
4
4 2 50
1 0 1 1
3 2 50
1 1 0
4 2 50
1 1 1 1
5 3 30
1 1 0 1 1
```

**Output**

```text
0
50
100
0
```

**Explanation**

**Test case $1$**: Chef's code neither passes all $4$ test cases nor passes the first $2$ test cases. Hence he does not get any points.

**Test case $2$**: Chef's code does not pass all $3$ test cases, but passes the first $2$ test cases. Hence he gets $50$ points.

**Test case $3$**: Chef's code passes all the $4$ test cases. Hence he gets $100$ points.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 50
1 0 1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 2 50
1 1 0
```

**Output for this case**

```text
50
```



#### Test case 3

**Input for this case**

```text
4 2 50
1 1 1 1
```

**Output for this case**

```text
100
```



#### Test case 4

**Input for this case**

```text
5 3 30
1 1 0 1 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUBTASK)

[Div1](https://www.codechef.com/START15A/problems/SUBTASK)

[Div2](https://www.codechef.com/START15B/problems/SUBTASK)

[Div3](https://www.codechef.com/START15C/problems/SUBTASK)

**Setter:**  [ Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:**  [ Samarth Gupta](https://www.codechef.com/users/samarth2017)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

##
[](#difficulty-2)DIFFICULTY:

CAKEWALK

##
[](#prerequisites-3)PREREQUISITES:

None

##
[](#problem-4)PROBLEM:

We are given an array A of length N describing the status of chef’s solution for some problem where A_i =1  denotes that the i^{th} testcase has passed and A_i = 0 denotes that the i^{th} testcase has failed. If the chef’s code passes all  testcases, he will get 100 points, or else if the first M \lt N testcases have passed, he will get K \lt 100 points. If both these conditions fail, he will get 0 points. We need to find the score of chef for that particular problem.

##
[](#explanation-5)EXPLANATION:

-

We can solve the problem simply by simulation of the conditions in the problem statement.

-

Let us iterate over i from 1 to N and check the A_i values.

-

If A_i = 1 for all 1 \leq i \leq N, the score is 100.

-

If A_i = 1 for all 1 \leq i \leq M but A_i =0 for some  i \geq M, the score is K.

-

If A_i =0 for some i \leq M, the score is 0.

##
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each testcase.

##
[](#solution-7)SOLUTION:

Editorialist's solution
``
#include <bits/stdc++.h>
using namespace std;

int main()
{
     int tests;
     cin >> tests;
     while (tests--)
     {
          int n, m, k;
          cin >> n >> m >> k;
          vector<int> a(n);

          for (int i = 0; i < n; i++)
               cin >> a[i];

          bool first_m_passed = true;
          bool all_passed = true;

          for (int i = 0; i < n; i++)
          {
               if (i < m && a[i] == 0)
               {
                    all_passed = first_m_passed = false;
               }
               else if (a[i] == 0)
               {
                    all_passed = false;
               }
          }

          if (all_passed)
               cout << 100 << endl;
          else if (first_m_passed)
               cout << k << endl;
          else
               cout << 0 << endl;
     }
}

``

Setter's solution
``
#include<bits/stdc++.h>
using namespace std;

void solve() {
  int n, p, x; cin >> n >> p >> x;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] == 0) break;
    if (i == p - 1) ans = x;
    if (i == n - 1) ans = 100;
  }
  cout << ans << '\n';
}

signed main() {
  ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t = 1;
  cin >> t;
  for (int i = 1; i <= t; i++) solve();
  return 0;
}

``

Tester's solution
``#include <bits/stdc++.h>
using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

int main() {
	// your code goes here
	int t = readIntLn(1, 100);
	int sum = 0;
	while(t--){
	    int n = readIntSp(2, 100);
	    int m = readIntSp(1, n - 1);
	    int k = readIntLn(1, 99);
	    vector<int> vec(n);
	    for(int i = 0 ;i < n ; i++){
	        if(i == n - 1)
	            vec[i] = readIntLn(0, 1);
	        else
	            vec[i] = readIntSp(0, 1);
	    }
	    int cnt = 0;
	    for(int i = 0; i < n ; i++)
	        cnt += vec[i];
	    if(cnt == n)
	        cout << "100\n";
	    else{
	        int i;
	        for(i = 0; i < n ; i++)
	            if(vec[i] == 0)
	                break;
	        if(i < m)
	            cout << "0\n";
	        else
	            cout << k << '\n';
	    }
	}
    readEOF();
	return 0;
}

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
