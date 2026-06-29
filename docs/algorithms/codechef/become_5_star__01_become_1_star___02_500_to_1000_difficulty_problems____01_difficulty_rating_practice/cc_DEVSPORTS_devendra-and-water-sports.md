# Devendra and Water Sports

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DEVSPORTS |
| Difficulty Rating | 859 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [DEVSPORTS](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/DEVSPORTS) |

---

## Problem Statement

Recently, Devendra went to Goa with his friends. Devendra is well known for not following a budget.

He had Rs. $Z$ at the start of the trip and has already spent Rs. $Y$ on the trip. There are three kinds of water sports one can enjoy, with prices Rs. $A$, $B$, and $C$. He wants to try each sport at least once.

If he can try all of them at least once output `YES`, otherwise output `NO`.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing five space-separated integers $Z, Y, A, B, C$.

---

## Output Format

For each test case, print a single line containing the answer to that test case — `YES` if Devendra can try each ride at least once, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1\leq T\leq 10$
- $10^4 \leq Z \leq 10^5$
- $0 \leq Y \leq Z$
- $100 \leq A,B,C \leq 5000$

---

## Examples

**Example 1**

**Input**

```text
3
25000 22000 1000 1500 700
10000 7000 100 300 500
15000 5000 2000 5000 3000
```

**Output**

```text
NO
YES
YES
```

**Explanation**

**Test Case 1:** After spending Rs. $22000$ on the trip already, Devendra is left with Rs. $3000$. The water sports cost a total of $1000+1500+700 = 3200$. So, he does not have enough money left to try all the watersports.

**Test Case 2:** After spending Rs. $10000$ on the trip, he is left with Rs. $3000$. The water sports cost a total of $100+300+500 = 900$. So, he has enough money to try all the watersports.

**Test Case 3:** After spending Rs. $5000$ on the trip, he is left with Rs. $10000$. The water sports cost a total of $2000+5000+3000 = 10000$. So, he still has enough money left to try all the watersports.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
25000 22000 1000 1500 700
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
10000 7000 100 300 500
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
15000 5000 2000 5000 3000
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DEVSPORTS)

[Div1](https://www.codechef.com/START21A/problems/DEVSPORTS)

[Div2](https://www.codechef.com/START21B/problems/DEVSPORTS)

[Div3](https://www.codechef.com/START21C/problems/DEVSPORTS)

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

Devandra is on a trip  and initially had Z rupees at the start of the trip and already has spent Y rupees from it. He wants to try three kinds of sports which have costs A, B and C rupees. If Devandra can try all the sports atleast once, we need to output YES, else we need to output NO.

###
[](#explanation-5)EXPLANATION:

-

Initially Devandra has Z rupees. Out of that, Y rupees has already been spent. Now, the current amount  he has will be Z-Y rupees.

-

The minimum cost to try all the sports will be A+B+C rupees.

-

Therefore, if Z-Y \geq A+B+C, we output YES, else we output NO.

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
            int z, y, a, b, c;
            cin >> z >> y >> a >> b >> c;

            if (z - y >= a + b + c)
            {
                  cout << "YES" << endl;
            }
            else
            {
                  cout << "NO" << endl;
            }
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

const int MAX_T = 10;
const int MAX_N = 100000;
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
    int z = readIntSp(10000 , 100000) ;
    int y = readIntSp(0 , z) ;

    int a = readIntSp(100 , 5000) ;
    int b = readIntSp(100 , 5000) ;
    int c = readIntLn(100 , 5000) ;

    int s = y+a+b+c ;
    cerr << z-s << endl ;

    if(z-s >= 0)
        cout << "YES\n" ;
    else
        cout << "NO\n" ;
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
