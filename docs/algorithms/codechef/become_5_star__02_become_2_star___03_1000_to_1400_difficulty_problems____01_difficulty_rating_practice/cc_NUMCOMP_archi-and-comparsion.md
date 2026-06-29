# Archi and Comparsion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NUMCOMP |
| Difficulty Rating | 1320 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [NUMCOMP](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/NUMCOMP) |

---

## Problem Statement

Danya gave integers $a$, $b$ and $n$ to Archi. Archi wants to compare $a^n$ and $b^n$. Help Archi with this task.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $a$, $b$ and $n$.

### Output
For each test case, print a single line containing one integer: $1$ if $a^n > b^n$, $2$ if $a^n < b^n$ or $0$ if $a^n = b^n$.

### Constraints
- $1 \le T \le 1,000$
- $|a|, |b| \le 10^9$
- $1 \le n \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
3 4 5
-3 2 4
```

**Output**

```text
2
1
```

**Explanation**

**Example case 1:** $a^n = 243$ and $b^n = 1024$.

**Example case 2:** $a^n = 81$ and $b^n = 16$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
-3 2 4
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/COOK95A/problems/NUMCOMP)

[Div2](https://www.codechef.com/COOK95B/problems/NUMCOMP)

[Practice](https://www.codechef.com/problems/NUMCOMP)

**Setter-** [Igor Barenblat](https://www.codechef.com/users/barenuz)

**Tester-** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist-**  [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

Cakewalk

### PRE-REQUISITES:

Basic Maths of power and exponents, [if-else statements](https://www.geeksforgeeks.org/decision-making-c-c-else-nested-else/)

### PROBLEM:

Given a, b and n , we need to tell if {a}^{n}>{b}^{n} or not.

### QUICK EXPLANATION:

**Key to Success:** While its a cakewalk question, and everyone gets AC, edge is gained over others by implementing the **correct** solution **quickly.** A proper insight of conditions is the key to success here.

There are many ways to do the question. As I said, a good insight in condition helps. We simply make cases for-

- if a==b or (n is even AND abs(a)==abs(b))

- if n is even - we check if a is greater or b

- if n is odd, compare a and b and print corresponding answer.

Try making a solution using these if this question gave you a problem during contest!!

### EXPLANATION:

We will have a single section in this editorial, and will refer to tester [@mgch](/u/mgch)’s solution for reference.

**Full Solution-**

**"OMG SO MANY CONDITIONS. WTF?! A AND B CAN BE NEGATIVE AS WELL!!! HOLY COW INFINITE IF-ELSE WTFFFFFF RIP EVERYTHING RIP GGWP I M DEAD"**

If you are one of those who have similar problems, then this editorial is just for you. There are multiple ways to tackle this statement, but I will discuss tester’s approach here as I find it elegant

We will, this time, use Divide and conquer. Divide the cases into sub-cases until they are easy to conquer!! xD

Lets formalize our cases. I assume you know about absolute function ( abs() ) of C++. If not, check tab below.

Click to view

**If input is a positive number, return it. If input is a negative number, multiply it with -1 to make it positive and then return it. This is abs() function in simple words.**

**a. When will answer be 0?**

Simple. If A==B OR If (N is even and abs(A)==abs(B)). Only these cases are possible.

We hence get the following condition-

``If A==B OR (N is even AND abs(A)==abs(B) ):
     Print(0);
``

Good, we have done 33\% of the problem. But making cases more cases like, when will answer be 1 or when will it be 2 is tedious. What is a bugging thing right now? Oh yes! The signs are of A and B may not be same. Lets deal with it.

If N is even, then we dont care of signs. Thats a great case. We can easily frame this condition now-

``If N is EVEN:
   Print 1 if abs(a)>abs(b)
   Print 2 if abs(b)>abs(a)
``

Now, we are left with cases where N is odd. Signs will matter here, so lets deal with it now. In case you feel “Now we are left with cases where N is odd” a too sudden conclusion, the tab below is for you :).

Click to view

**Recall that we are using an if-else-if ladder. An else or else-if block (of statements) will not execute if condition of any of the if's above it are satisfied which leads to that if block being executed. Atmost one of the blocks get executed.**

**\implies if our second condition (N is even) didnt execute, then N is odd.**

Now, if N is odd, I said signs matter. Yes, they ‘matter’ a lot indeed :). Hence, ignore them! Nobody should matter so much xD. Our next condition is-

``If N is odd: //automatically implied
          Compare if A>B or B<A and print corresponding answer.
``

We are DONE with this question after this! :D. A question for you, why did we not care for signs here?

Any bonus content is in Chef Vijju’s Corner.

### SOLUTIONS:

It takes time for [@admin](/u/admin) to link solutions and get the links working. If they arent working for you, please open the tab below to check the codes.

[Setter](http://www.codechef.com/download/Solutions/COOK95/setter/NUMCOMP.cpp)

Click to view
``#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define files(name) name!=""?freopen(name".in","r",stdin),freopen(name".out","w",stdout):0
#define all(a) a.begin(),a.end()
#define len(a) (int)(a.size())
#define elif else if
#define mp make_pair
#define pb push_back
#define fir first
#define sec second

using namespace std;
#define int long long

typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long double ld;
typedef long long ll;

const int arr=2e5+10;
const int ar=2e3+10;
const ld pi=acos(-1);
const ld eps=1e-10;
const ll md=1e9+7;

///---program start---///

void solve()
{
    int a,b,n;
    cin>>a>>b>>n;
    if (n%2==0){
        int ans=0;
        a=abs(a);
        b=abs(b);
        if (a>b){
            ans=1;
        }
        elif (a<b){
            ans=2;
        }
        else{
            ans=0;
        }
        cout<<ans<<"\n";
    }
    else{
        pii cur1={a<0?-1:a==0?0:1,a};
        pii cur2={b<0?-1:b==0?0:1,a};
        if (cur1.fir>cur2.fir){
            cout<<1<<"\n";
        }
        elif (cur1.fir<cur2.fir){
            cout<<2<<"\n";
        }
        else{
            if (cur1.fir<0){
                if (abs(a)<abs(b)){
                    cout<<1<<"\n";
                }
                elif (abs(a)>abs(b)){
                    cout<<2<<"\n";
                }
                else{
                    cout<<0<<"\n";
                }
            }
            elif (cur1.fir==0){
                cout<<0<<"\n";
            }
            else{
                if (abs(a)<abs(b)){
                    cout<<3-1<<"\n";
                }
                elif (abs(a)>abs(b)){
                    cout<<3-2<<"\n";
                }
                else{
                    cout<<0<<"\n";
                }
            }
        }
    }
}

main()
{
    #ifdef I_love_Maria_Ivanova
        files("barik");
        freopen("debug.txt","w",stderr);
    #endif

    int test;
    cin>>test;
    while (test--){
        solve();
    }
}
``

[Tester](http://www.codechef.com/download/Solutions/COOK95/tester/NUMCOMP.cpp)

Click to view
``#include <bits/stdc++.h>

using namespace std;

const int MaxN = (int)4e5 + 10;
const int MOD = (int)1e9 + 7;
const int INF = (int)1e9;

void solve() {
	int a, b, n;
	scanf("%d%d%d", &a, &b, &n);
	if (a == b || (n % 2 == 0 && a + b == 0)) {
		printf("0\n");
		return;
	}
	if (n % 2 == 0) {
		printf("%d\n", 1 + (abs(b) > abs(a)));
		return;
	}
	if ((a < 0) != (b < 0)) {
		printf("%d\n", 1 + (a < 0));
		return;
	}
	printf("%d\n", 1 + (a < b));
}

int main() {
//	freopen("input.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	while (t --> 0) {
		solve();
	}
	return 0;
}
``

Editorialist’s solution will be put on demand.

Time Complexity=O(1) per test case.

### CHEF VIJJU’S CORNER

**1. Why not care for signs if N is odd?**

Click to view

**Say signs are not same. A simple comparison will tell which number is positive (as a positive number is always greater!) and hence no need to consider sign here. Say signs are same, again we handle this case by checking which of the two is greater.**

**2. Why we dont care to calculate {a}^{n} and {b}^{n}**

Click to view

**Exponents are same!! Hence, a larger number raised to power n is always greater than smaller number raised to power n!!**

**3.Test Case Bank-**

Click to view

**Official Input-** [https://pastebin.com/WV5EcPHJ](https://pastebin.com/WV5EcPHJ)

**Official Output-** [https://pastebin.com/v5p8udFy](https://pastebin.com/v5p8udFy)

**4. Related Problems-**

-
[B. High School: Become Human](https://codeforces.com/contest/987/problem/B) - A tougher version of this problem

</details>
