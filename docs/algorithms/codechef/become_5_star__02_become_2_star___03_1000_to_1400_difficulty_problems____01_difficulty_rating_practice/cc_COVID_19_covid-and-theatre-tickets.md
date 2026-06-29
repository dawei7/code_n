# Covid and Theatre Tickets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COVID_19 |
| Difficulty Rating | 1077 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [COVID_19](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/COVID_19) |

---

## Problem Statement

Mr. Chef is the manager of the Code cinemas and after a long break, the theatres are now open to the public again. To compensate for the loss in revenue due to Covid-19, Mr. Chef wants to maximize the profits for every show from now on and at the same time follow the guidelines set the by government.
The guidelines are:

- If two people are seated in the same row, there must be at least one empty seat between them.
- If two people are seated in different rows, there must be at least one **completely empty row** between them. That is, if there are people seated in rows $i$ and $j$ where $i \lt j$, there must be some row $k$ such that $i \lt k \lt j$ and nobody is seated in row $k$.

Given the information about the number of rows and the number of seats in each row, find the maximum number of tickets Mr. Chef can sell.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing two space-separated integers $N, M$ — the number of rows and the number of seats in each row, respectively.

---

## Output Format

For each test case, output a single line containing one integer – the maximum number of tickets Mr. Chef can sell.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,M\leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
1 5
3 3
4 4
```

**Output**

```text
3
4
4
```

**Explanation**

**Test Case 1:** There is only one row with five seats. Mr. Chef can sell a maximum of 3 tickets for seat numbers 1, 3 and 5.

**Test Case 2:** There are three rows with three seats each. Mr. Chef can sell a maximum of 4 tickets, for seats at the start and end of row numbers 1 and 3.

**Test Case 3:** There are four rows with four seats each. Mr. Chef can sell a maximum of 4 tickets, for example by choosing the seats at the start and end of row numbers 1 and 4.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4 4
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COVID_19)

[Div1](https://www.codechef.com/START21A/problems/COVID_19)

[Div2](https://www.codechef.com/START21B/problems/COVID_19)

[Div3](https://www.codechef.com/START21C/problems/COVID_19)

**Setter:**  [Devendra Singh](https://www.codechef.com/users/devendra7700)

**Testers:**  [Lavish Gupta](https://www.codechef.com/users/lavish315), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

###
[](#difficulty-2)DIFFICULTY:

CAKEWALK

###
[](#prerequisites-3)PREREQUISITES:

None

###
[](#problem-4)PROBLEM:

There is a theatre with N rows and M seats in each row. We need to find the maximum number of seats that can be occupied with the following conditions:

-

No adjacent seats in the same row can be occupied

-

No two adjacent rows can be occupied

###
[](#explanation-5)EXPLANATION:

-

Clearly, the optimal way to allocate the seats would be to select the rows as row 1, row 3, \dots and in each row we select the seats as seat 1, seat 3, \dots

-

Then, total number of rows selected will be  \lfloor \frac{N+1}{2} \rfloor and the number of seats in each row would be  \lfloor \frac{M+1}{2} \rfloor.

-

Therefore, the total number of seats selected will be  \lfloor \frac{N+1}{2} \rfloor \cdot \lfloor \frac{M+1}{2} \rfloor.

###
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

###
[](#solution-7)SOLUTION:

Editorialist's solution
``#include <bits/stdc++.h>
using namespace std;

int main()
{
      int tests;
      cin >> tests;
      while (tests--)
      {
            int n, m;
            cin >> n >> m;

            int ans = ((n + 1) / 2) * ((m + 1) / 2);
            cout << ans << endl;
      }
      return 0;
}

``

Tester's solution
``// validating input
#include <bits/stdc++.h>
using namespace std;
#define ll long long

/*
------------------------Input Checker----------------------------------
*/

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

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

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

/*
------------------------Main code starts here----------------------------------
*/

const int MAX_T = 100;
const int MAX_N = 100;
const int MAX_Q = 100000;
const int MAX_val = 1000000000;
const int MAX_SUM_N = 100000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll p = 1000000007;
ll sum_nk = 0 ;

void solve()
{
    int m = readIntSp(1 , MAX_N) ;
    int n = readIntLn(1 , MAX_N) ;

    int ans = (m+1)/2 ;
    ans *= ((n+1)/2) ;

    int flag = (n%2 == 1) + (2*(m%2 == 1)) ;
    cerr << "flag = " << flag << endl ;
    cout << ans << endl ;
    return ;
}

signed main()
{
    //fast;
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
        solve() ;
    }

    assert(getchar() == -1);
    // assert(sum_n <= MAX_SUM_N);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    // cerr<<"Sum of lengths : " << sum_n << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr << "Sum of product : " << sum_nk << '\n' ;
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
