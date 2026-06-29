# Remove Element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMELEM |
| Difficulty Rating | 1415 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [REMELEM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/REMELEM) |

---

## Problem Statement

You are given an array $A = [A_1, A_2, \ldots, A_N]$ consisting of $N$ positive integers.

You are also given a constant $K$, using which you can perform the following operation on $A$:
- Choose two distinct indices $i$ and $j$ such that $A_i + A_j \le K$, and remove either $A_i$ or $A_j$ from $A$.

Is it possible to obtain an array consisting of only one element using several (possibly, zero) such operations?

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, print `"YES"` if it is possible to obtain an array consisting of only one element using the given operation, otherwise print `"NO"`.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, K \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1 3
1
3 3
2 2 2
4 7
1 4 3 5
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** The length of the array is already $1$.

**Test case $2$:** There is no way to delete an element from the given array.

**Test case $3$:** One possible sequence of operations is:

- Choose $i = 1, j = 4$ and remove $A_j = 5$. Hence the array becomes $[1, 4, 3]$.
- Choose $i = 2, j = 3$ and remove $A_i = 4$. Hence the array becomes $[1, 3]$.
- Choose $i = 1, j = 2$ and remove $A_i = 1$. Hence the array becomes $[3]$, which is of length $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3
1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 3
2 2 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 7
1 4 3 5
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/SDELP21A/problems/REMELEM)

[Contest Division 2](https://www.codechef.com/SDELP21B/problems/REMELEM)

[Contest Division 3](https://www.codechef.com/SDELP21C/problems/REMELEM)

[Practice](https://www.codechef.com/problems/REMELEM)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p) and [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Given an array A containing N integers and a constant integer K, you are allowed to perform the following operation on A.

- Choose two distinct indices i and j such that A_i + A_j \leq K, and remove either A_i or A_j from A

Determine if we can obtain an array containing only one element using the above operation.

#
[](#quick-explanation-5)QUICK EXPLANATION

- It is possible only when the sum of minimum and maximum element of A does not exceed K.

- If the above condition is true, we can select indices of minimum and maximum of the current array, and delete maximum at each step.

#
[](#explanation-6)EXPLANATION

**Observation 1:** It is optimal to choose index of minimum element in each operation

**Proof:** Assume we choose indices i and j for current operation, and the index of minimum element is k. WLOG assume A_k \leq A_i \leq A_j. Since we have A_i + A_j \leq K, we also have A_k \leq A_i, so A_k+A_j \leq A_i+A_j \leq K. We can see that by choosing pair (k, j), we are still able to perform the operation.

Now, we know that one of the chosen elements in each operation shall be the minimum of the given array. Let’s call it min.

The largest element x which can be removed from array must satisfy x + min \leq K, which means x \leq K-min.

So if the array contains an element y \gt K-min, it is impossible to include y in any operation. So there would be at least 2 elements left at the end.

Hence, if the sum of minimum and maximum elements exceed K, then it is not possible to obtain an array containing only one element.

###
[](#if-you-wish-to-generate-the-actual-operations-7)If you wish to generate the actual operations

**Observation 2:** It is optimal to delete the larger element at each operation.

**Proof: ** Let’s assume we delete the minimum at some operation. Then for the next operation, the minimum chosen would be larger, possibly restricting us to including the maximum element.

For example, consider A = [2,4,6,7] and K = 9. If we choose pair (2, 7) and delete 2, we can no longer remove any element from [4,6,7].

#
[](#time-complexity-8)TIME COMPLEXITY

The time complexity is O(N) or O(N*log(N)) per test case.

#
[](#solutions-9)SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

void solve() {
  int n, k; cin >> n >> k;
  int mx = 0, mn = 1e9;
  for (int i = 0; i < n; i++) {
    int x; cin >> x;
    mn = min(mn, x);
    mx = max(mx, x);
  }
  cout << ((n == 1 || mx + mn <= k) ? "YES" : "NO") << '\n';
}

signed main() {
  int t = 1;
  cin >> t;
  while (t--) solve();
  return 0;
}
``

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

const int MAX_T = 1000;
const int MAX_N = 100000;
const int MAX_K = 1000000000;
const int MAX_A = 1000000000;
const int MAX_SUM_LEN = 500000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define mt make_tuple
#define ll long long
const ll LIM = 1000000000;
#define pll pair<ll ,ll>
#define tll tuple<ll, ll, ll>

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

void solve() {
    int n, k;
    n = readIntSp(1, MAX_N);
    k = readIntLn(1, MAX_K);
    sum_len += n;
    assert(sum_len <= MAX_SUM_LEN);
    int a[n];
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(1, MAX_A);
    a[n - 1] = readIntLn(1, MAX_A);
    sort(a, a + n);
    if(n == 1 || a[n - 1] + a[0] <= k) cout << "YES\n";
    else cout << "NO\n";
}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("inputf.txt", "r" , stdin);
    freopen("outputf.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;
    t = readIntLn(1, MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
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

const int MAX_T = 1000;
const int MAX_N = 100000;
const int MAX_SUM_LEN = 500000;
const int MAX_Ai = 1000000000;
const int MAX_K = 1000000000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

void solve()
{
    int n=readInt(1,MAX_N,' ');
    int k=readInt(1,MAX_Ai,'\n');
    vector <int> v;
    for(int i=1;i<=n;i++)
    {
        int c;
        if(i!=n)
            c=readInt(1,MAX_Ai,' ');
        else
            c=readInt(1,MAX_Ai,'\n');
        v.push_back(c);
    }
    if(n==1)
    {
        cout<<"YES\n";
        return;
    }
    sort(v.begin(),v.end());
    if((v[0]+v[n-1])<=k)
        cout<<"YES\n";
    else
        cout<<"NO\n";
}

signed main()
{
    fast;
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
class REMELEM{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), K = ni();
        int[] A = new int[N];
        for(int i = 0; i< N; i++)A[i] = ni();
        Arrays.sort(A);
        if(N == 1 || A[0]+A[N-1] <= K)pn("YES");
        else pn("NO");
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
        new REMELEM().run();
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
