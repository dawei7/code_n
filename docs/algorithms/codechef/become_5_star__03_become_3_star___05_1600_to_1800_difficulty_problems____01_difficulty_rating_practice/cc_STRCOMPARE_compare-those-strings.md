# Compare those strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRCOMPARE |
| Difficulty Rating | 1756 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [STRCOMPARE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/STRCOMPARE) |

---

## Problem Statement

Chef has two strings $A$ and $B$ consisting of lowercase alphabets, each of length $N$. Help Chef in finding the number of indices $i$ $(1 \leq i \leq N)$ such that $A[i \dots N] \lt B[i \dots N]$.

- $S[i \dots N]$ denotes the suffix of string $S$ starting at index $i$, i.e. $S_iS_{i+1}$ $\dots$ $S_{N}$.
- String $S \lt$ String $T$ denotes that $S$ is lexicographically smaller than $T$. If two strings $S$ and $T$ have the same length $N$, we say that $S$ is lexicographically smaller than $T$ if there exists an index $i(1 \le i \le N)$ such that $S_1 = T_1,$ $S_2 = T_2, \ldots, S_{i-1} = T_{i-1}$ and $S_i \lt T_i$. For example, "$abc$" is lexicographically smaller than "$acd$", "$abe$", but not smaller than "$abc$", "$aac$".

---

## Input Format

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains $N$, denoting the length of the strings $A$ and $B$.
- The second line of each test case contains the string $A$.
- The third line of each test case contains the string $B$.

---

## Output Format

For each test case, print a single line containing one integer -  the number of indices $i$ such that $A[i \dots N] \lt B[i\dots N]$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^6$
- The sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
2
2
ab
bb
3
aaa
aab
```

**Output**

```text
1
3
```

**Explanation**

**Test Case $1$**:
- For $i = 1$, $A[1 \dots 2] = $ "$ab$", $B[1 \dots 2] = $ "$bb$" and lexicographically, "$ab$" $\lt$ "$bb$".
- For $i = 2$, $A[2 \dots 2] =$ "$b$", $B[2 \dots 2] = $ "$b$" and lexicographically, "$b$" $=$ "$b$".

**Test Case $2$**: For each $i \in \{1 , 2, 3\}$, $A[i \dots 3] \lt B[i \dots 3]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
ab
bb
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
aaa
aab
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

[Contest Division 1](https://www.codechef.com/START18A/problems/STRCOMPARE)

[Contest Division 2](https://www.codechef.com/START18B/problems/STRCOMPARE)

[Contest Division 3](https://www.codechef.com/START18C/problems/STRCOMPARE)

[Practice](https://www.codechef.com/problems/STRCOMPARE)

**Setter:** [Manan Bordia](https://www.codechef.com/users/mananbordia) and [Lavish Gupta](https://www.codechef.com/users/lavish315)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Given two strings A and B of length N each. Find the number of indices i such that A[i\ldots N] \lt B[i \ldots N].

#
[](#quick-explanation-5)QUICK EXPLANATION

- If A_i \lt B_i, then index i is good. If A_i \gt B_i, then index is not good.

- If A_i = B_i, then index i is good if and only if index i+1 is good.

#
[](#explanation-6)EXPLANATION

Let’s call an index i good if A[i\ldots N] \lt B[i \ldots N] holds.

Let us solve this problem for the easier cases first. Whenever we have A_i \neq B_i, we can immediately decide for index i whether it is good or not.

What happens when A_i = B_i? We’d need to compare A_{i+1} and B_{i+1} and so on, to find the first position p where A_p \neq B_p. All indices from i to p are decided by whether A_p \lt B_p is true or not.

We can see that if A_i = B_i, then index i is good only if index i+1 is good. Let’s compute this from right to left. Maintain whether index i+1 is good or not. First check if A_i \neq B_i. If yes, check if index is good or not by comparing A_i and B_i.

Maintain a count of good indices.

``nextGood = false # Whether index i+1 is good or not
count = 0
for i in N-1 to 0:
    if A[i] == B[i]:
        if nextGood: count++
    else:
        if A[i] < B[i]:
            count++
            nextGood = true
        else:
            nextGood = false

print count
``

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(N) per test case.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
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
        assert('a'<=g and g<='z');
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

const int MAX_T = 100000;
const int MAX_LEN = 1000000;
const int MAX_SUM_LEN = 1000000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_len = 0;
int max_n = 0;
int max_k = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

int n,k;
string s;

void solve()
{

    n = readIntLn(1, MAX_LEN);
    string a = readStringLn(1, MAX_LEN);
    string b = readStringLn(1, MAX_LEN);

    sum_len += n;

    assert(a.length()==n && b.length()==n);
    for(int i = 0 ; i < n ; i++)
    {
        int val_a = a[i] - 'a' ;
        int val_b = b[i] - 'a' ;
        assert(val_a >= 0 && val_a < 26) ;
        assert(val_b >= 0 && val_b < 26) ;
    }

    int ans = 0;

    if(a == b)
    {
        cout << ans << '\n' ;
        return ;
    }

    for(int i = 0 ; i < n ; i++)
    {
        int flag = 0 ;
        for(int j = i ; j < n ; j++)
        {
            if(a[j] < b[j])
            {
                ans += (j-i+1) ;
                i = j ;
                break ;
            }
            if(a[j] > b[j])
            {
                i = j ;
                break ;
            }
            if(j == n-1)
                flag = 1 ;
        }
        if(flag)
            break ;
    }

    cout<<ans<<'\n';
}

signed main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    // fast;

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(sum_len <= MAX_SUM_LEN);
    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    // cerr<<"maxN : " << max_n << '\n';
    // cerr<<"maxK : " << max_k << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Tester's Solution
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
        assert('a'<=g and g<='z');
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

const int MAX_T = 100000;
const int MAX_LEN = 1e6;
const int MAX_SUM_LEN = 1e6;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_len = 0;
int max_n = 0;
int max_k = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

int n,k;
string s;

void solve()
{

    n = readIntLn(1, 1e6);
    string a = readStringLn(1, MAX_LEN);
    string b = readStringLn(1, MAX_LEN);

    sum_len += n;

    assert(a.length()==n && b.length()==n);

    int ans = 0;

    int f=0;
    for(int i=n-1; i>=0; i--){
        if(a[i]<b[i]){
            if(!f) f=1;
        }
        else if(a[i]>b[i]){
            if(f) f=0;
        }

        ans+=f;
    }

    cout<<ans<<'\n';

}

signed main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(sum_len <= MAX_SUM_LEN);
    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    // cerr<<"maxN : " << max_n << '\n';
    // cerr<<"maxK : " << max_k << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class STRCOMPARE{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        String A = n(), B = n();
        int ans = 0;
        boolean small = false;
        for(int i = N-1; i>= 0; i--){
            if(A.charAt(i) < B.charAt(i)){
                ans++;
                small = true;
            }else if(A.charAt(i) == B.charAt(i)){
                if(small)
                    ans++;
            }else small = false;
        }
        pn(ans);
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
        new STRCOMPARE().run();
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
