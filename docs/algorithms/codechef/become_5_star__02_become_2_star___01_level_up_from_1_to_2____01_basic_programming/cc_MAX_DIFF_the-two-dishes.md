# The Two Dishes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAX_DIFF |
| Difficulty Rating | 1254 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [MAX_DIFF](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MAX_DIFF) |

---

## Problem Statement

Chef prepared two dishes yesterday. Chef had assigned the $\textbf{tastiness}$ $T_1$ and $T_2$ to the first and to the second dish respectively. The tastiness of the dishes can be any $\textbf{integer}$ between $0$ and $N$ (both inclusive).

Unfortunately, Chef has forgotten the values of $T_1$ and $T_2$ that he had assigned to the dishes. However, he remembers the sum of the tastiness of both the dishes - denoted by $S$.

Chef wonders, what can be the maximum possible absolute difference between the tastiness of the two dishes. Can you help the Chef in finding the maximum absolute difference?

It is guaranteed that at least one pair $\{T_1, T_2\}$ exist such that $T_1 + T_2 = S, 0 \leq T_1, T_2 \leq N$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of the $T$ testcases follows.
- The first and only line of each test case contains two space-separated integers $N$, $S$, denoting the maximum tastiness and the sum of tastiness of the two dishes, respectively.

---

## Output Format

For each testcase, output a single line containing the maximum absolute difference between the tastiness of the two dishes.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq S \leq 2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3 1
4 4
2 3
```

**Output**

```text
1
4
1
```

**Explanation**

**Test Case $1$:** The possible pairs of $\{T_1, T_2\}$ are $\{0, 1\}$ and $\{1, 0\}$. Difference in both the cases is $1$, hence the maximum possible absolute difference is $1$.

**Test Case $2$:** The possible pairs of $\{T_1, T_2\}$ are $\{0, 4\}$, $\{1, 3\}$, $\{2, 2\}$, $\{3, 1\}$ and $\{4, 0\}$. The maximum possible absolute difference is $4$.

**Test Case $3$:** The possible pairs of $\{T_1, T_2\}$ are $\{1, 2\}$ and $\{2, 1\}$. Difference in both the cases is $1$, and hence the maximum possible absolute difference is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 4
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
2 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START11A/problems/MAX_DIFF)

[Contest Division 2](https://www.codechef.com/START11B/problems/MAX_DIFF)

[Contest Division 3](https://www.codechef.com/START11C/problems/MAX_DIFF)

[Practice](https://www.codechef.com/problems/MAX_DIFF)

**Setter:** [Lavish Gupta](https://www.codechef.com/users/lavish315)

**Tester:** [Samarth Gupta](https://www.codechef.com/users/samarth2017)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

Basic Math

#
[](#problem-4)PROBLEM

Given two integers N and S, Find maximum possible value of |T_1 - T_2| if 0 \leq T_1, T_2 \leq N and T_1+T_2 = S

It is guaranteed that for N and S in input, there exists at least one pair (T_1, T_2) such that 0 \leq T_1, T_2 \leq N and T_1+T_2 = S

#
[](#quick-explanation-5)QUICK EXPLANATION

- If S \leq N, we can choose pair T_1 = 0 and T_2 = S to obtain absolute difference S, which is maximum possible.

- If N \leq S \leq 2*N, we can choose pair T_1 = N and T_2 = S-N to obtain absolute difference 2*N-S

- There cannot be a case with S \gt 2*N as that requires at least one of T_1 and T_2 to be \gt N which is not allowed. Similarly for S \lt 0.

#
[](#explanation-6)EXPLANATION

I’d explain two thought processes here.

###
[](#thought-process-1-7)Thought Process 1

Let’s assume we only require 0 \lt T_1, T_2 and T_1 + T_2 = S. (Upper bound N is ignored). It is easy to see that if we choose T_1 = 0 and T_2 = S, we obtain maximum possible absolute difference. Increasing T_1 only decreases T_2 which reduces absolute difference. So we achieve absolute difference S.

In our problem, T_1,T_2 \leq N stops us from choosing above, as it may happen that T_2 = S \gt N. So we have to reduce T_2 by at least S-N. Let’s do that. T_1 = S-N and T_2 = N is the pair we get, and we don’t need to do any more changes, as reducing T_2 now only reduces absolute difference. So, we obtain an absolute difference 2*N-S.

###
[](#thought-process-2-8)Thought Process 2

In most min-max problems, it is always good to check out boundary points. We can prove that the absolute difference is maximized only when at least one of T_1 and T_2 are on end-points (0 or N).

Based on the above, we can try all pairs where T_1 is either 0 or N (There are only two such pairs). If a valid pair is formed, then take the maximum of absolute difference among valid pairs.

###
[](#tip-9)Tip

The required answer is min(S, 2*N-S). The proof is left as an exercise.

#
[](#time-complexity-10)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-11)SOLUTIONS

Setter's Solution
``#define ll long long
#define rep(i , n) for(ll i = 0 ; i < n ; i++)
#include<bits/stdc++.h>

ll max(ll a , ll b){if(a > b) return a ; return b ;}
ll min(ll a , ll b){if(a < b) return a ; return b ;}

using namespace std ;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    ll t ;
    cin >> t ;
    //t = 1 ;

    while(t--)
    {
        ll sum , max_marks ;
        cin >> max_marks >> sum ;

        if(sum <= max_marks)
        {
            cout << sum << endl ;
            continue ;
        }
        cout << (2*max_marks - sum) << endl ;
    }

    return 0;
}
``

Tester's Solution
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
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    t = readIntLn(1, 1000);
    int sum = 0;
    while(t--){
        int n = readIntSp(1, 1e5);
        int s = readIntLn(1, 2e5);
        assert(0 <= s && s <= 2*n);
        int t1, t2;
        t2 = s;
        t2 = min(t2, n);
        t1 = s - t2;
        cout << abs(t2 - t1) << '\n';
    }
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MAX_DIFF{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), S = ni();
        int d1 = 0, d2 = S;
        if(d2 > N){
            int d = d2-N;
            d1 += d;
            d2 -= d;
        }
        pn(d2-d1);
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
        new MAX_DIFF().run();
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
