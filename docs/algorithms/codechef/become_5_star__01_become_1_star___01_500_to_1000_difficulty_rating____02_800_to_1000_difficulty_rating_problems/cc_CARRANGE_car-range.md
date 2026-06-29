# Car Range

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CARRANGE |
| Difficulty Rating | 938 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CARRANGE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CARRANGE) |

---

## Problem Statement

The *fuel economy* of a car is the distance which it can travel on one litre of fuel.

The base fuel economy (i.e, its fuel economy when there is only one person - the driver - in the car) of a certain car is $M$ kilometres per litre. It was also observed that every extra passenger in the car *decreases* the fuel economy by $1$ kilometre per litre.

$P$ people want to take this car for a journey. They know that the car currently has $V$ litres of fuel in its tank.

What is the **maximum** distance this car can travel under the given conditions, assuming that all $P$ people always stay in the car and no refuelling can be done?

**Note** that among the $P$ people is also a driver, i.e, there are exactly $P$ people in the car.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing three space-separated integers $P, M$, and $V$ - the number of people, base fuel economy, and amount of fuel present in the car, respectively.

---

## Output Format

For each test case, output a single line containing one integer - the maximum distance that the car can travel.

---

## Constraints

- $1 \leq T \leq 3 \cdot 10^4$
- $1 \leq P \leq 5$
- $6 \leq M \leq 56$
- $1 \leq V \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
5 10 20
1 6 10
4 6 1
```

**Output**

```text
120
60
3
```

**Explanation**

**Test Case $1$:**
There are $5$ people in the car, and its base fuel economy is $10$. Thus, its effective fuel economy is $10 - 4 = 6$, since there are $4$ people present other than the driver.
There are $20$ litres of fuel in the car, so the maximum distance that can be travelled is $6\cdot 20 = 120$.

**Test Case $2$:**
The effective fuel economy is $6$, and the maximum distance that can be travelled is $6\cdot 10 = 60$.

**Test Case $3$:**
The effective fuel economy is $3$, and the maximum distance that can be travelled is $3\cdot 1 = 3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 10 20
```

**Output for this case**

```text
120
```



#### Test case 2

**Input for this case**

```text
1 6 10
```

**Output for this case**

```text
60
```



#### Test case 3

**Input for this case**

```text
4 6 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/SDELP21A/problems/CARRANGE)

[Contest Division 2](https://www.codechef.com/SDELP21B/problems/CARRANGE)

[Contest Division 3](https://www.codechef.com/SDELP21C/problems/CARRANGE)

[Practice](https://www.codechef.com/problems/CARRANGE)

**Setter:** [Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p) and [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

The *fuel economy* of a car is the distance which it can travel on one litre of fuel.

The base fuel economy (i.e, its fuel economy when there is only one person - the driver - in the car) of a certain car is M kilometres per litre. It was also observed that every extra passenger in the car *decreases* the fuel economy by 1 kilometre per litre.

P people want to take this car for a journey. They know that the car currently has V litres of fuel in its tank.

What is the **maximum** distance this car can travel under the given conditions, assuming that all P people always stay in the car and no refuelling can be done?

**Note** that among the P people is also a driver, i.e, there are exactly P people in the car.

#
[](#quick-explanation-5)QUICK EXPLANATION

The fuel economy with P people is M-(P-1), since P-1 more passengers enter the car. For V liters, the car can cover distance V*(M-(P-1))

#
[](#explanation-6)EXPLANATION

Since the base economy is M when there’s one person (driver) in car, the fuel economy with P people would be equivalent to P-1 people joining the car, reducing the fuel economy of car from M to M - (P-1).

Hence, the fuel economy with P passengers is (M-(P-1)) kilometers per liter. There is V liters of fuel available, so the maximum distance the car can cover is V * (M-(P-1)).

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-8)SOLUTIONS

Tester's Solution 1
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 30000;
const int MAX_P = 5;
const int MAX_M = 56;
const int MAX_V = 100;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_len=0;

void solve()
{
    int p, m, v;
    p = readIntSp(1, MAX_P);
    m = readIntSp(MAX_P + 1, MAX_M);
    v = readIntLn(1, MAX_V);
    cout << v*(m - p + 1) << "\n";
}

signed main()
{
    fast;
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int t = readIntLn(1, MAX_T);

    for(int i=1;i<=t;i++)
    {
        solve();
    }

    assert(getchar() == -1);
}
``

Tester's Solution 2
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 30000;
const int MAX_P = 5;
const int MAX_M = 56;
const int MIN_M = 6;
const int MAX_V = 100;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

void solve()
{
    int p=readInt(1,MAX_P,' ');
    int m=readInt(MIN_M,MAX_M,' ');
    int v=readInt(1,MAX_V,'\n');
    int mileage=(m+1-p);
    int ans=mileage*v;
    cout<<ans<<'\n';
}

signed main()
{
    // fast;
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int t = readInt(1,MAX_T,'\n');

    for(int i=1;i<=t;i++)
    {
        solve();
    }

    assert(getchar() == -1);
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class CARRANGE{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int P = ni(), M = ni(), V = ni();
        pn(V*(M-P+1));
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new CARRANGE().run();
    }
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}

    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }

        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }

        String nextLine() throws Exception{
            String str = "";
            try{
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }
            return str;
        }
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
