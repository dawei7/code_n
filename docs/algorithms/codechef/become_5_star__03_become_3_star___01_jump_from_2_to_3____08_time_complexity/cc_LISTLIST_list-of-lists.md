# List of Lists

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LISTLIST |
| Difficulty Rating | 1567 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [LISTLIST](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/LISTLIST) |

---

## Problem Statement

You are given a positive integer $N$ and an array $A$ of size $N$. There are $N$ lists $L_1, L_2 \ldots L_N$. Initially, $L_i = [A_i]$.

You can perform the following operation any number of times as long as there are at least $2$ lists:

- Select $2$ (non-empty) lists $L_i$ and $L_j$ ($i \neq j$)
- Append $L_j$ to $L_i$ and remove the list $L_j$. Note that this means $L_j$ cannot be chosen in any future operation.

Find the minimum number of operations required to obtain a set of lists that satisfies the following conditions:

- The first element and last element of each list are equal.
- The first element of all the lists is the same.

Print $-1$ if it is not possible to achieve this via any sequence of operations.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer: the minimum number of operations required to obtain an array of lists that satisfies the given conditions.

Print $-1$ if it is impossible to achieve such an array of lists.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq N$
- Sum of $N$ over all test cases doesn't exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1
1
2
1 2
3
1 1 2
```

**Output**

```text
0
-1
2
```

**Explanation**

**Test case $1$:** There is only one list $[1]$, and it trivially satisfies the condition so no operations are required.

**Test case $2$:** There are only $2$ ways to do an operation - either take list $[1]$ and append it to list $[2]$ or take list $[2]$ and append it to list $[1]$. In both cases, it is not possible to satisfy both given conditions at the same time. Hence, the answer is $-1$.

**Test case $3$:** Here is one possible order of operations:
- Select the $3$rd list $[2]$ and append it to the $1$st list $[1]$.
- Then, select the $2$nd list $[1]$ and append it to the $1$st list $[1, 2]$.

Finally, we are left with the single list $[1, 2, 1]$ which satisfies the given conditions. It can be verified that it is impossible to do this using less than $2$ operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
3
1 1 2
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

[Contest Division 1](https://www.codechef.com/DEC21A/problems/LISTLIST)

[Contest Division 2](https://www.codechef.com/DEC21B/problems/LISTLIST)

[Contest Division 3](https://www.codechef.com/DEC21C/problems/LISTLIST)

[Practice](https://www.codechef.com/problems/LISTLIST)

**Setter:** [Nishant Shah](https://www.codechef.com/users/nishant_adm)

**Tester:** [Lavish Gupta](https://www.codechef.com/users/lavish315)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

You are given a positive integer N and an array A of size N. There are N lists L_1, L_2 \ldots L_N. Initially, L_i = [A_i].

You can perform the following operation any number of times as long as there are at least 2 lists:

- Select 2 (non-empty) lists L_i and L_j (i \neq j)

- Append L_j to L_i and remove the list L_j. Note that this means L_j cannot be chosen in any future operation.

Find the minimum number of operations required to obtain a set of lists that satisfies the following conditions:

- The first element and last element of each list are equal.

- The first element of all the lists is the same.

Print -1 if it is not possible to achieve this via any sequence of operations.

#
[](#quick-explanation-5)QUICK EXPLANATION

- If all elements are the same, no operations are needed.

- If all elements are different, it is not possible to satisfy the above conditions.

- Otherwise, after applying an optimal set of operations, all but one list consist of the same element x, and in the one list, only the first and last elements are x.

#
[](#explanation-6)EXPLANATION

First of all, let’s consider base cases.

###
[](#if-all-elements-are-the-same-7)If all elements are the same

All N lists have same the first and last elements, and the first element of each list is the same, so no operations are required.

###
[](#all-elements-are-different-8)All elements are different

Since there’s no pair of equal elements, the first and the last element of any list with at least 2 elements cannot be the same. So, to satisfy the first condition, all lists must have one element only. But that violates the second condition.

Hence, if all elements are different, and N \gt 1, it is impossible to satisfy both conditions at the same time.

###
[](#general-case-9)General case

In the general case, there always exists a solution. Since all elements are not distinct, we can always join all elements into a single list such that the first and last elements are the same. Hence, an answer is always possible in this case. We just need to find minimum number of operations.

**Observation**: We can see that initially, there are N lists, and after each operation, the number of lists reduces by 1. Hence, minimizing the number of operations is the same as maximizing the number of lists.

Based on the above observation, we need to maximize the number of lists, while satisfying the above conditions.

**Observation 2**: After an optimal set of operations, there’s exactly one list with more than one operation.

**Proof:** Let’s assume after all operations, there are two lists with more than one element. Let’s assume the first and last element of both lists is x.

The lists might look something like `x,a,b,c,x` and `x,d,e,f,g,x`. Instead, we can add all non-border elements of the second list into the first list, and the border elements can form two lists of length 1, increasing the number of lists. `x,a,b,c,d,e,f,g,x`, `x` and `x`, reducing the number of operation by 1.

Hence, all lists except the first must have only one element. They must also consist of values same as the first and last elements of the first list. Let’s assume x appears f times in the list. Two occurrences of x are used in the first list. We can form f-2 list with length 1. The total number of lists became f-1. The number of operations required becomes N - (f-1)

Hence, we can try all x, compute its frequency, and compute the minimum value of N-(f-1) over all candidates.

#
[](#time-complexity-10)TIME COMPLEXITY

The time complexity is O(N*log(N)) per test case due to sorting or frequency map operations.

#
[](#solutions-11)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int getRand(int l, int r)
{
    uniform_int_distribution<int> uid(l, r);
    return uid(rng);
}

#define int long long
#define pb push_back
#define S second
#define F first
#define f(i,n) for(int i=0;i<n;i++)
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define vi vector<int>
#define pii pair<int,int>
#define all(x) x.begin(),x.end()
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define precise(x) fixed << setprecision(x)

const int MOD = 1e9+7;

int mod_pow(int a,int b,int M = MOD)
{
    if(a == 0) return 0;
    b %= (M - 1);  //M must be prime here

    int res = 1;

    while(b > 0)
    {
        if(b&1) res=(res*a)%M;
        a=(a*a)%M;
        b>>=1;
    }

    return res;
}

void solve()
{
   int n;
   cin >> n;

   int a[n];
   f(i,n) cin >> a[i];

   map<int,int> mp;
   f(i,n) mp[a[i]]++;

   if(mp.size() == 1) cout << 0 << '\n';
   else if(mp.size() == n) cout << -1 << '\n';
   else
   {
       int mx = 0;
       for(auto x : mp) mx = max(mx , x.S);
       cout << n - (mx - 1) << '\n';
   }
}

signed main()
{
    fast;

    int t = 1;

    cin >> t;

    while(t--)

    solve();
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
const int MAX_N = 200000;
const int MAX_SUM_LEN = 200000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

void solve()
{
    int n = readIntLn(1 , MAX_N);
    sum_len += n ;
    max_n = max(max_n , n) ;

    int arr[n] ;
    for(int i = 0 ; i < n-1 ; i++)
        arr[i] = readIntSp(1 , n) ;
    arr[n-1] = readIntLn(1 , n) ;

    int maxi = 0 ;
    map<int , int> m ;
    for(int i = 0 ; i < n ; i++)
    {
        m[arr[i]]++ ;
        maxi = max(maxi , m[arr[i]]) ;
    }
    if(n == 1)
    {
        cout << 0 << endl ;
        return ;
    }

    if(maxi == 1)
        cout << -1 << endl ;
    else
    {
        if(maxi == n)
            cout << 0 << endl ;
        else
            cout << n-maxi+1 << endl ;
    }
    return ;

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("inputf.txt", "r" , stdin);
    freopen("outputf.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;
    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(sum_len <= MAX_SUM_LEN) ;
    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class LISTLIST{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        int[] A = new int[N];
        for(int i = 0; i< N; i++)A[i] = ni();
        Arrays.sort(A);
        int ans = N+2;
        for(int i = 0, ii = 0; i< N; i = ii){
            while(ii< N && A[i] == A[ii])ii++;  //Finding the largest block [i, ii) containing same element A[i]
            if(ii-i > 1)
                ans = Math.min(ans, N-(ii-i-1));
            if(ii-i == N)ans = 0;
        }
        if(ans == N+2)ans = -1;
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
        new LISTLIST().run();
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
